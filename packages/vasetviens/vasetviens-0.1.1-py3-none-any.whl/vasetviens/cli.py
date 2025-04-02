import argparse
from .core import analyser_va_et_vient

def main():
    parser = argparse.ArgumentParser(description="Analyse de va-et-vient autour de plots dans une vidéo de foot")
    parser.add_argument("video_path", help="Chemin vers la vidéo d'entrée")
    parser.add_argument("--display", action="store_true", help="Afficher le traitement en temps réel")
    parser.add_argument("--save", action="store_true", help="Enregistrer la vidéo de sortie")
    parser.add_argument("--cooldown_frames", type=int, default=30, help="Cooldown entre deux détections pour le même plot")
    parser.add_argument("--frame_retention_limit", type=int, default=60, help="Durée de conservation des plots")
    parser.add_argument("--direction_zone_width", type=int, default=80, help="Largeur de la zone de direction")
    parser.add_argument("--min_va_ratio", type=float, default=0.3, help="Ratio minimal de rapprochement pour un aller")
    parser.add_argument("--min_retour_ratio", type=float, default=0.2, help="Ratio minimal de retour")
    parser.add_argument("--color_plot", type=str, default="bleu", help="Couleur des plots à détecter (ex: bleu)")
    parser.add_argument("--confidence_threshold", type=float, default=0.1, help="Seuil de confiance YOLO")
    parser.add_argument("--model_path", type=str, default="yolo11x.pt", help="Chemin vers le modèle YOLO")

    args = parser.parse_args()

    analyser_va_et_vient(
        video_path=args.video_path,
        display=args.display,
        save=args.save,
        cooldown_frames=args.cooldown_frames,
        frame_retention_limit=args.frame_retention_limit,
        direction_zone_width=args.direction_zone_width,
        min_va_ratio=args.min_va_ratio,
        min_retour_ratio=args.min_retour_ratio,
        color_plot=args.color_plot,
        confidence_threshold=args.confidence_threshold,
        model_path=args.model_path
    )

if __name__ == "__main__":
    main()
