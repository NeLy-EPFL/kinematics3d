"""
Extracts the outlier frames from a given set of videos.
The usage is the same as the `05_run_pose_estimation.py`
Make sure that the videos include the pose estimation files from DLC.
If not, run the script number 05 before running this script.

Example usage:
>>> python 06_extract_outlier_refine.py --video_dir /home/nely/DLC_annotation/final/cam3/version4/pose_estimation/gizem-new-dataset --config_path /home/nely/DLC_annotation/final/cam3/version4/intact_cam3-Melissa-2021-12-01/config.yaml
>>> python 06_extract_outlier_refine.py --video_dir /home/nely/DLC_annotation/final/cam2/pose_estimation/gizem-ant-amputation --config_path /home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml
>>> python 06_extract_outlier_refine.py --video_dir /home/nely/DLC_annotation/final/cam1/pose_estimation/gizem-ant-amputation --config_path /home/nely/DLC_annotation/final/cam1/intact_cam1-Melissa-2021-12-01/config.yaml

"""

import argparse
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
    deeplabcut.extract_outlier_frames(
        config_path,
        video_list,
        outlieralgorithm="uncertain",
        extractionalgorithm="kmeans",
    )  # pass a specific video
    deeplabcut.refine_labels(config_path)
    deeplabcut.merge_datasets(config_path)

else:
    raise RuntimeError("GPU is not found!")
