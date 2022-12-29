import argparse
from pathlib import Path
import deeplabcut
import tensorflow as tf


parser = argparse.ArgumentParser()
parser.add_argument(
    "--config_path",
    type=str,
    default=None,
    help="Config file",
)
args = parser.parse_args()

if args.config_path is None:
    config_path = '/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml'
else:
    config_path = args.config_path


if tf.test.is_gpu_available():
    video_list = [
    '/home/nely/DLC_annotation/final/cam2/pose_estimation/legs/new/220412_Fly001_Beh2_cam2.mp4',
    ]
    videotype = Path(video_list[0]).suffix
    #deeplabcut.analyze_videos(config_file, video_list, videotype='.mp4')
    deeplabcut.create_labeled_video(config_path,video_list,trailpoints=5)
else:
    raise RuntimeError('GPU is not found!')