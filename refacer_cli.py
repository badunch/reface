from refacer import Refacer
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Refacer with CLI face input")
    parser.add_argument("--video_dir", help="Path to directory containing video files (or comma-separated list of video paths)")
    parser.add_argument("--origin", required=True, help="Path to the origin face image")
    parser.add_argument("--destination", required=True, help="Path to the destination face image")
    parser.add_argument("--threshold", type=float, default=0.2, help="Similarity threshold (default: 0.2)")
    parser.add_argument("--colab_performance", action="store_true", help="Use Colab performance mode")
    args = parser.parse_args()

    # Create face data from CLI arguments
    faces = [
        {'origin': args.origin, 'destination': args.destination, 'threshold': args.threshold}
    ]

    # Initialize Refacer (optional: use colab_performance for Colab)
    refacer = Refacer(colab_performance=args.colab_performance)

    # Get video paths
    if args.video_dir:
        if os.path.isdir(args.video_dir):
            video_paths = [os.path.join(args.video_dir, f) for f in os.listdir(args.video_dir) if f.endswith(".mp4")] 
        else:
            video_paths = args.video_dir.split(",")
    else:
        # Handle the case where --video_dir is not provided
        video_paths = []  

    # Process each video
    for video_path in video_paths:
        # Get output path (modify as needed)
        output_path = os.path.splitext(video_path)[0] + "_refaced.mp4"

        # Reface the video
        refacer.reface(video_path, faces, output_path)
        print(f"Processed video saved to: {output_path}")

if __name__ == "__main__":
    main()