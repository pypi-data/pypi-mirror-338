import cv2
import numpy as np
import csv
import os
from ultralytics import YOLO

def analyser_va_et_vient(
    video_path: str,
    output_video_path: str = None,
    recap_csv_path: str = None,
    moments_csv_path: str = None,
    color_plot: str = "bleu",
    confidence_threshold: float = 0.1,
    frame_retention_limit: int = 60,
    cooldown_frames: int = 30,
    direction_zone_width: int = 80,
    min_va_ratio: float = 0.3,
    min_retour_ratio: float = 0.2,
    model_path: str = "yolo11x.pt",
    display: bool = False,
    save: bool = True
):
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    if output_video_path is None:
        output_video_path = f"output_{base_name}.mp4"
    if recap_csv_path is None:
        recap_csv_path = f"recap_{base_name}.csv"
    if moments_csv_path is None:
        moments_csv_path = f"moments_{base_name}.csv"

    model = YOLO(model_path)

    cap = cv2.VideoCapture(video_path)
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = None
    if save:
        out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), int(fps), (width, height))

    next_plot_id = 0
    active_plots = {}
    plot_vav_counts = {}
    plot_vav_moments = {}
    plot_progress = {}
    plot_zones = {}
    frame_idx = 0
    vav_deja_valide_ce_frame = False

    last_positions = []
    last_box = None
    ball_missing_counter = 0
    ball_max_missing_frames = 15

    awaiting_new_start = False
    awaiting_frame_count = 0
    awaiting_position = None
    STABILISATION_THRESHOLD = 5
    STABILISATION_FRAMES = 5

    PLOT_COLORS = [
        ((255, 0, 0), (255, 0, 0)),
        ((0, 255, 0), (0, 255, 0)),
        ((0, 255, 255), (0, 255, 255)),
        ((255, 255, 0), (255, 255, 0)),
        ((255, 0, 255), (255, 0, 255))
    ]

    def same_plot(box1, box2, max_dist=40):
        cx1, cy1 = (box1[0] + box1[2]) // 2, (box1[1] + box1[3]) // 2
        cx2, cy2 = (box2[0] + box2[2]) // 2, (box2[1] + box2[3]) // 2
        return np.hypot(cx1 - cx2, cy1 - cy2) < max_dist

    def detect_and_track_plots(frame, color="bleu"):
        nonlocal active_plots, next_plot_id
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        detected_boxes = []
        color_ranges = {"bleu": ([90, 50, 50], [130, 255, 255])}
        lower = np.array(color_ranges[color][0])
        upper = np.array(color_ranges[color][1])
        mask = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 80:
                perimeter = cv2.arcLength(cnt, True)
                circularity = 4 * np.pi * (area / (perimeter ** 2)) if perimeter > 0 else 0
                if 0.6 < circularity < 1.3:
                    x, y, w, h = cv2.boundingRect(cnt)
                    detected_boxes.append((x, y, x + w, y + h))
        new_active_plots = {}
        matched_ids = set()
        for new_box in detected_boxes:
            matched = False
            for plot_id, (old_box, age) in active_plots.items():
                if plot_id not in matched_ids and same_plot(new_box, old_box):
                    new_active_plots[plot_id] = (new_box, 0)
                    matched_ids.add(plot_id)
                    matched = True
                    break
            if not matched:
                new_active_plots[next_plot_id] = (new_box, 0)
                next_plot_id += 1
        for plot_id, (box, age) in active_plots.items():
            if plot_id not in new_active_plots and age < frame_retention_limit:
                new_active_plots[plot_id] = (box, age + 1)
        active_plots = new_active_plots
        return frame

    def detect_ball_yolo(frame):
        results = model.predict(frame, conf=confidence_threshold, verbose=False)
        if results and results[0].boxes:
            for box in results[0].boxes:
                if int(box.cls[0]) == 32:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    center = ((x1 + x2) // 2, (y1 + y2) // 2)
                    return center, (x1, y1, x2, y2)
        return None, None

    def compute_direction_zone(ball_center, plot_center, width):
        dx, dy = plot_center[0] - ball_center[0], plot_center[1] - ball_center[1]
        distance = np.hypot(dx, dy)
        if distance == 0:
            return []
        ux, uy = dx / distance, dy / distance
        w = width // 2
        perp_x, perp_y = -uy, ux
        p1 = (int(ball_center[0] + perp_x * w), int(ball_center[1] + perp_y * w))
        p2 = (int(ball_center[0] - perp_x * w), int(ball_center[1] - perp_y * w))
        p3 = (int(plot_center[0] - perp_x * w), int(plot_center[1] - perp_y * w))
        p4 = (int(plot_center[0] + perp_x * w), int(plot_center[1] + perp_y * w))
        return [p1, p2, p3, p4], (ux, uy), distance

    def draw_static_zone_with_lines(frame, zone_pts, ux, uy, start_dist, plot_id, state_text, line_color, plot_center):
        border_color, fill_color = PLOT_COLORS[plot_id % len(PLOT_COLORS)]
        overlay = frame.copy()
        poly_pts = np.array(zone_pts, np.int32).reshape((-1, 1, 2))
        # cv2.fillPoly(overlay, [poly_pts], fill_color)
        # cv2.addWeighted(overlay, 0.25, frame, 0.75, 0, frame)
        # cv2.polylines(frame, [poly_pts], isClosed=True, color=border_color, thickness=2)

        ratio = min_va_ratio
        left_interp = (
            int(zone_pts[0][0] + ratio * (zone_pts[3][0] - zone_pts[0][0])),
            int(zone_pts[0][1] + ratio * (zone_pts[3][1] - zone_pts[0][1]))
        )
        right_interp = (
            int(zone_pts[1][0] + ratio * (zone_pts[2][0] - zone_pts[1][0])),
            int(zone_pts[1][1] + ratio * (zone_pts[2][1] - zone_pts[1][1]))
        )
        # cv2.line(frame, left_interp, right_interp, line_color, 2, lineType=cv2.LINE_AA)

        state_pos = (plot_center[0] - 40, plot_center[1] + 40)
        cv2.putText(frame, state_text, state_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, line_color, 2)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        vav_deja_valide_ce_frame = False
        detected_center, ball_box = detect_ball_yolo(frame)

        if detected_center:
            last_positions.append(detected_center)
            last_box = ball_box
            if len(last_positions) > 2:
                last_positions.pop(0)
            ball_missing_counter = 0
        else:
            ball_missing_counter += 1

        if ball_missing_counter == 0:
            ball_center = last_positions[-1]
        elif ball_missing_counter <= ball_max_missing_frames and len(last_positions) >= 2:
            dx = last_positions[-1][0] - last_positions[-2][0]
            dy = last_positions[-1][1] - last_positions[-2][1]
            predicted = (last_positions[-1][0] + dx, last_positions[-1][1] + dy)
            ball_center = tuple(map(int, predicted))
        else:
            ball_center = None

        frame = detect_and_track_plots(frame, color=color_plot)

        if awaiting_new_start and ball_center and awaiting_position is not None:
            dist = np.linalg.norm(np.array(ball_center) - np.array(awaiting_position))
            if dist < STABILISATION_THRESHOLD:
                awaiting_frame_count += 1
            else:
                awaiting_frame_count = 0
            awaiting_position = ball_center

            if awaiting_frame_count >= STABILISATION_FRAMES:
                for pid, (plot_box, _) in active_plots.items():
                    plot_center_tmp = ((plot_box[0] + plot_box[2]) // 2, (plot_box[1] + plot_box[3]) // 2)
                    new_zone_pts, (ux, uy), new_start_dist = compute_direction_zone(ball_center, plot_center_tmp, direction_zone_width)
                    plot_zones[pid] = {"pts": new_zone_pts, "ux": ux, "uy": uy, "start_dist": new_start_dist}
                    if pid in plot_progress:
                        plot_progress[pid]["start_dist"] = new_start_dist
                        plot_progress[pid]["min_dist"] = new_start_dist
                awaiting_new_start = False
                awaiting_frame_count = 0
                awaiting_position = None

        if ball_center and ball_box:
            x1, y1, x2, y2 = ball_box
            radius_ball = (ball_box[2] - ball_box[0]) * 0.3
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            for plot_id, (plot, age) in active_plots.items():
                x1p, y1p, x2p, y2p = plot
                plot_center = ((x1p + x2p) // 2, (y1p + y2p) // 2)
                cv2.rectangle(frame, (x1p, y1p), (x2p, y2p), (0, 255, 255), 2)
                dist = np.linalg.norm(np.array(plot_center) - np.array(ball_center))

                if plot_id not in plot_zones:
                    zone_pts, (ux, uy), start_dist = compute_direction_zone(ball_center, plot_center, direction_zone_width)
                    plot_zones[plot_id] = {"pts": zone_pts, "ux": ux, "uy": uy, "start_dist": start_dist}
                    plot_progress[plot_id] = {"start_dist": start_dist, "min_dist": start_dist, "va_reached": False, "last_validated_frame": -100}
                    plot_vav_counts[plot_id] = 0
                    plot_vav_moments[plot_id] = []

                zone = plot_zones[plot_id]
                progress = plot_progress[plot_id]

                if not progress["va_reached"]:
                    state_text = "En attente VA"
                    line_color = (0, 0, 255)
                elif progress["va_reached"] and frame_idx - progress["last_validated_frame"] < cooldown_frames:
                    state_text = "VA validé"
                    line_color = (0, 255, 0)
                else:
                    state_text = "En attente RETOUR"
                    line_color = (255, 140, 0)

                if vav_deja_valide_ce_frame and frame_idx == progress["last_validated_frame"]:
                    state_text = "RETOUR validé"
                    line_color = (128, 0, 128)

                draw_static_zone_with_lines(frame, zone["pts"], zone["ux"], zone["uy"], zone["start_dist"], plot_id, state_text, line_color, plot_center)

                adjusted_dist = dist - radius_ball
                progress["min_dist"] = min(progress["min_dist"], adjusted_dist)
                if not progress["va_reached"] and (progress["start_dist"] - adjusted_dist) >= min_va_ratio * progress["start_dist"]:
                    progress["va_reached"] = True
                elif progress["va_reached"] and (adjusted_dist - progress["min_dist"]) >= min_retour_ratio * progress["start_dist"]:
                    if not vav_deja_valide_ce_frame and frame_idx - progress["last_validated_frame"] >= cooldown_frames:
                        plot_vav_counts[plot_id] += 1
                        plot_vav_moments[plot_id].append(frame_idx)
                        vav_deja_valide_ce_frame = True
                        progress["last_validated_frame"] = frame_idx
                        progress["va_reached"] = False
                        progress["start_dist"] = dist
                        progress["min_dist"] = dist
                        awaiting_new_start = True
                        awaiting_position = ball_center
                        awaiting_frame_count = 0

                cv2.putText(frame, f"Plot {plot_id} | {int(dist)}px", (plot_center[0] - 40, plot_center[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        total_vavs = sum(plot_vav_counts.values())
        cv2.putText(frame, f"Total Va-et-vient: {total_vavs}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        if display:
            cv2.imshow("Analyse en temps réel", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        if save:
            out.write(frame)
        frame_idx += 1
    cap.release()
    if save:
        out.release()
    cv2.destroyAllWindows()

    with open(recap_csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID Plot", "Nb Va-et-vient"])
        for plot_id, count in plot_vav_counts.items():
            writer.writerow([plot_id, count])
        writer.writerow(["TOTAL", sum(plot_vav_counts.values())])

    with open(moments_csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID Plot", "Instant Frame"])
        for plot_id, frames in plot_vav_moments.items():
            for instant in frames:
                writer.writerow([plot_id, instant])

    print("✅ Traitement terminé avec succès.")
