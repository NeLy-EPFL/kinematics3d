"""
Train the network given in the configuration file.

Example usage:
>>> python 03_train_network.py   --config_path /home/nely/DLC_annotation/final/cam3/intact_cam3-Melissa-2021-12-01/config.yaml
>>> python 03_train_network.py --config_path /home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml
>>> python 03_train_network.py --config_path /home/nely/DLC_annotation/final/cam1/intact_cam1-Melissa-2021-12-01/config.yaml
"""

import argparse

import deeplabcut
import tensorflow as tf


parser = argparse.ArgumentParser()
parser.add_argument(
    "--config_path",
    type=str,
    default=None,
    help="Config file",
)
parser.add_argument(
    "--maxiters",
    type=int,
    default=200000,
    help="Max number of iterations",
)
args = parser.parse_args()

if args.config_path is None:
    config_path = (
        "/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml"
    )
else:
    config_path = args.config_path


if tf.test.is_gpu_available():
    deeplabcut.train_network(
        config_path,
        shuffle=1,
        displayiters=10000,
        saveiters=10000,
        maxiters=args.maxiters,
    )
else:
    print("GPU is not found!")
