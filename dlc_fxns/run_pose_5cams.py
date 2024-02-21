"""
CAMERA 3:
python 05_run_pose_estimation.py --video_dir /home/nely/DLC_annotation/final/cam3/version4/pose_estimation/gizem-new-dataset --config_path /home/nely/DLC_annotation/final/cam3/version4/intact_cam3-Melissa-2021-12-01/config.yaml

CAMERA 2:

CAMERA 1:

"""

import os
import argparse
import deeplabcut
import tensorflow as tf

parser = argparse.ArgumentParser()
parser.add_argument(
    "--video_dir",
    type=str,
    default=None,
    help="Video dir",
)
args = parser.parse_args()

config_path_cam1 = (
    "/home/nely/DLC_annotation/final/cam1/intact_cam1-Melissa-2021-12-01/config.yaml"
)
config_path_cam2 = (
    "/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml"
)
config_path_cam3 = (
    "/home/nely/DLC_annotation/final/cam3/intact_cam3-Melissa-2021-12-01/config.yaml"
)

video_main = args.video_dir

videos_side = [
    os.path.join(video_main, "camera_1.mp4"),
    os.path.join(video_main, "camera_5.mp4"),
]

videos_side_front = [
    os.path.join(video_main, "camera_2.mp4"),
    os.path.join(video_main, "camera_4.mp4"),
]

videos_front = [
    os.path.join(video_main, "camera_3.mp4"),
]


if tf.test.is_gpu_available():
    deeplabcut.analyze_videos(config_path_cam1, videos_side, videotype="mp4")
    deeplabcut.create_labeled_video(config_path_cam1, videos_side)

    deeplabcut.analyze_videos(config_path_cam2, videos_side_front, videotype="mp4")
    deeplabcut.create_labeled_video(config_path_cam2, videos_side_front)

    deeplabcut.analyze_videos(config_path_cam3, videos_front, videotype="mp4")
    deeplabcut.create_labeled_video(config_path_cam3, videos_front)

else:
    raise RuntimeError("GPU is not found!")
