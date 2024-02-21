""" Extract frames for annotation from the config file. """

import argparse

import deeplabcut

parser = argparse.ArgumentParser()
parser.add_argument(
    "--config_path",
    type=str,
    default=None,
    help="Config file",
)
parser.add_argument(
    "--mode",
    type=str,
    default="manual",
    help="manual or automatic",
)
parser.add_argument(
    "--algo",
    type=str,
    default="uniform",
    help="uniform or kmeans",
)
args = parser.parse_args()

if args.config_path is None:
    config_path = (
        "/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml"
    )
else:
    config_path = args.config_path


deeplabcut.extract_frames(
    config_path, mode=args.mode, algo=args.algo, userfeedback=True, crop=False
)
