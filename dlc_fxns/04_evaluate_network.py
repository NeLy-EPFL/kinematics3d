""" Evaluates the trained network. """

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
    "--plot",
    default=False,
    action="store_true",
    help="Plots the evaluation results",
)
args = parser.parse_args()

if args.config_path is None:
    config_path = (
        "/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml"
    )
else:
    config_path = args.config_path


if tf.test.is_gpu_available():
    deeplabcut.evaluate_network(config_path, Shuffles=[1], plotting=args.plot)
else:
    print("GPU is not found!")

