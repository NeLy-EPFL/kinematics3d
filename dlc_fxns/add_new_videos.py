import argparse

import deeplabcut

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

video_list = ['/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/videos/221226_Fly001_002_Beh_cam2.mp4']

deeplabcut.add_new_videos(config_path, video_list)