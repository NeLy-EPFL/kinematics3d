"""
Creates training dataset from the annotated frames.

Example usage:
>>> python 02_create_training_dataset.py --config_path /home/nely/DLC_annotation/final/cam3/intact_cam3-Melissa-2021-12-01/config.yaml
>>> python 02_create_training_dataset.py --config_path /home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml
>>> python 02_create_training_dataset.py --config_path /home/nely/DLC_annotation/final/cam1/intact_cam1-Melissa-2021-12-01/config.yaml


"""

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
    "--aug_type",
    type=str,
    default="imgaug",
    help="Image augmentation",
)
parser.add_argument(
    "--merge",
    default=False,
    action="store_true",
    help="Merge datasets    ",
)
args = parser.parse_args()

if args.config_path is None:
    config_path = (
        "/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/config.yaml"
    )
else:
    config_path = args.config_path

if args.merge:
    deeplabcut.merge_datasets(config_path)
deeplabcut.create_training_dataset(config_path, augmenter_type=args.aug_type)
