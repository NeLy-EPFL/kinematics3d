"""
Runs pose estimation on all of the videos in a directory.
Make sure that the video directory only contains videos of
the same camera as the config file.

Example usage:
>>> python 05_run_pose_estimation.py --video_dir /home/nely/DLC_annotation/final/cam3/version4/pose_estimation/gizem-new-dataset --config_path /home/nely/DLC_annotation/final/cam3/version4/intact_cam3-Melissa-2021-12-01/config.yaml
>>> python 05_run_pose_estimation.py --video_dir /home/nely/DLC_annotation/final/cam2/pose_estimation/gizem-ant-amputation --config_path /home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml
>>> python 05_run_pose_estimation.py --video_dir /home/nely/DLC_annotation/final/cam1/pose_estimation/gizem-ant-amputation --config_path /home/nely/DLC_annotation/final/cam1/intact_cam1-Melissa-2021-12-01/config.yaml


"""

import argparse
from pathlib import Path
import deeplabcut
import tensorflow as tf
from get_videos_list import get_video_list

parser = argparse.ArgumentParser()
parser.add_argument(
    "--config_path",
    type=str,
    default=None,
    help="Config file",
)
parser.add_argument(
    "--video_dir",
    type=str,
    default=None,
    help="Video dir",
)
args = parser.parse_args()

if args.config_path is None:
    config_path = (
        "/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml"
    )
else:
    config_path = args.config_path

video_list = get_video_list(args.video_dir)

if tf.test.is_gpu_available():
    # video_list = [
    #     # '/home/nely/DLC_annotation/final/cam2/pose_estimation/gizem/221221_aJO-GAL4xUAS-CsChr_Fly004_006_RF.mp4',
    #     # '/home/nely/DLC_annotation/final/cam2/pose_estimation/gizem/221221_aJO-GAL4xUAS-CsChr_Fly001_003_Beh.mp4',
    #     # '/home/nely/DLC_annotation/final/cam2/pose_estimation/gizem/221011_aDN2-spGAL4xUAS-CsChr_Fly003_001_opt.mp4',
    #     '/home/nely/DLC_annotation/final/cam4/version2/pose_estimation/new/211014_Fly002_Beh2_cam4.mp4'
    # ]
    videotype = Path(video_list[0]).suffix
    deeplabcut.analyze_videos(config_path, video_list, videotype=videotype)
    deeplabcut.create_labeled_video(
        config_path, video_list
    )  # ,draw_skeleton = True) #trailpoints=5)
else:
    raise RuntimeError("GPU is not found!")
