"""
    Scripts to run Anipose pipeline:
    - 2D filtering
    - Camera calibration based on the tracked key points.
    - Triangulation of multi-view 2D poses.
"""

import os
from typing import Optional
from pathlib import Path
import logging
import shutil
import subprocess
import toml
import numpy as np

import kinematics3d

# Change the logging level here
logging.basicConfig(
    level=logging.INFO, format=" %(asctime)s - %(levelname)s- %(message)s"
)

CONFIG_PATH = Path(kinematics3d.__path__[0]).parents[0] / "config"


def check_config_exists(main_path: Path, overwrite: Optional[bool] = True) -> None:
    """Checks if anipose config exists in the main directory.
    If overwrite is true or it does not exist, then copies the
    default one into the main path.

    Parameters
    ----------
    main_path : Path
        Path where anipose pipeline runs.
        e.g. /mnt/nas2/GO/7cam/220710_aDN2-GAL4xUAS-CsChr/Fly001
    overwrite : bool, optional
        If config exists and overwrite is True,
        then replaces the existing config with the default one, by default True
    """
    if not (main_path / "config.toml").is_file() or overwrite:
        logging.info(f"Copying default config into {main_path}")
        shutil.copy(CONFIG_PATH / "config.toml", main_path / "config.toml")


def check_calib_exists(main_path: Path, overwrite: Optional[bool] = True) -> None:
    """Checks if calibration folder exists in the main directory.
    If overwrite is true or it does not exist, then copies the
    default one into the main path.
    The code automatically handles the calibration file path in the
    configuration file.

    Parameters
    ----------
    main_path : Path
        Path where anipose pipeline runs.
        e.g. /mnt/nas2/GO/7cam/220710_aDN2-GAL4xUAS-CsChr/Fly001
    overwrite : bool, optional
        If config exists and overwrite is True,
        then replaces the existing config with the default one, by default True
    """
    config_data = toml.load(main_path / "config.toml")
    calib_dir = config_data["pipeline"]["calibration_results"]

    if (main_path / "calibration").is_dir():
        if overwrite:
            shutil.rmtree(main_path / "calibration")
            shutil.copytree(calib_dir, main_path / "calibration")
            logging.info("Removing the existing calibration file...")
        else:
            logging.info("Keeping the existing calibration file...")
    else:
        shutil.copytree(calib_dir, main_path / "calibration")
        logging.info(f"Copying default calibration into {main_path}")

    # Change calibration directory in the config file
    config_data["pipeline"]["calibration_results"] = (
        main_path / "calibration"
    ).as_posix()
    config_data["calibration"]["calibration_init"] = (
        main_path / "calibration/calibration_init.toml"
    ).as_posix()

    with open(main_path / "config.toml", "w") as f_open:
        toml.dump(config_data, f_open)

    logging.info("Config file is updated!")


def check_pose_folder_exists(main_path: Path, folder_name: str) -> None:
    """Checks if pose folders exist in the main directory and removes
    them because Anipose does not run in a directory if the pose folders
    already exist.

    Parameters
    ----------
    main_path : Path
        Path where anipose pipeline runs.
        e.g. /mnt/nas2/GO/7cam/220710_aDN2-GAL4xUAS-CsChr/Fly001
    folder_name: str
        Folder name that anipose uses to store data, e.g., pose_2d for 2D pose
    """
    # These names are the default ones in the config.
    # If you use a different naming, change the below list.
    if folder_name not in ["pose_3d", "pose_2d", "pose_2d_filter"]:
        raise ValueError(
            "Folder name {} is invalid! It should be either of pose_3d, pose_2d, pose_2d_filter".format(
                folder_name
            )
        )

    config_data = toml.load(main_path / "config.toml")
    pose_name = config_data["pipeline"][folder_name]
    pose_dirs = main_path.rglob(f"*/{pose_name}")

    if pose_dirs:
        for pose_dir_name in pose_dirs:
            logging.info(
                f"Pose folder exists, deleting the directory {pose_dir_name.as_posix()}"
            )
            try:
                shutil.rmtree(pose_dir_name)
            except:
                print("not found")


def anipose_pipeline(
    main_dir: Path,
    filter_2d: Optional[bool] = True,
    calibrate: Optional[bool] = True,
    triangulate: Optional[bool] = True,
):
    """Runs anipose pipeline in a given directory.

    Parameters
    ----------
    main_dir : Path
        Path where anipose pipeline runs.
        e.g. /mnt/nas2/GO/7cam/220710_aDN2-GAL4xUAS-CsChr/Fly001
    filter_2d : Optional[bool], optional
        Filtering 2D poses, by default True
    calibrate : Optional[bool], optional
        Calibration, by default True
    triangulate : Optional[bool], optional
        Triangulation, by default True
    """

    logging.info(f"Running anipose on {main_dir}")
    os.chdir(main_dir)

    if filter_2d:
        subprocess.run(["anipose", "filter"], check=True)
    if calibrate:
        subprocess.run(["anipose", "calibrate"], check=True)
    if triangulate:
        subprocess.run(["anipose", "triangulate"], check=True)


def run_pipeline_from_txt(
    txt_dir: str,
    remove_calib: Optional[bool] = False,
    remove_pose3d: Optional[bool] = False,
    remove_pose2dfilt: Optional[bool] = False,
    **kwargs,
):
    """Run Anipose pipeline from a txt file containing the main directories.
    kwargs are the arguments for the anipose_pipeline() function,
    see its optional arguments.
    """
    txt_dir += ".txt" if not txt_dir.endswith(".txt") else ""

    assert os.path.isfile(f"{txt_dir}"), f"Please create `{txt_dir}`!"
    assert os.path.getsize(f"{txt_dir}"), f"{txt_dir} is empty!!"

    if remove_pose2dfilt:
        deletepose2dfilt = input(
            "Existing pose-2d-filter folders will be deleted! Are you sure? [y/n]"
        )
        remove_pose2dfilt = False if deletepose2dfilt.lower() == "n" else True

    if remove_pose3d:
        deletepose3d = input(
            "Existing pose-3d folders will be deleted! Are you sure? [y/n]"
        )
        remove_pose3d = False if deletepose3d.lower() == "n" else True

    if remove_calib:
        deletecalib = input(
            "Existing calibration folders will be deleted! Are you sure? [y/n]"
        )
        remove_calib = False if deletecalib.lower() == "n" else True

    logging.info(f"Running Anipose on the folders inside {txt_dir}")
    path_list = []
    for line in open(txt_dir):
        p_name = Path(line.rstrip())
        parts = p_name.parts
        if len(parts) < 7:
            raise IndexError(
                """
                Directory should have at least 7 parts.
                Example: ('/','mnt','nas','GO','7cam','220504_aJO-GAL4xUAS-CsChr', 'Fly001')
                """
            )

        # If child directory is given, we take the parent directory.
        fly_index = [i for i, word in enumerate(parts) if "Fly" in word]
        new_parts = parts[: int(fly_index[-1]) + 1]

        if len(fly_index) > 1:
            raise ValueError(f"Directory {p_name} is faulty!\nPlease, check it again.")

        new_path = Path(*new_parts)
        path_list.append(new_path)

    for p_name in np.unique(path_list):
        check_config_exists(
            p_name, overwrite=(remove_calib or remove_pose2dfilt or remove_pose3d)
        )
        check_calib_exists(p_name, overwrite=remove_calib)
        if remove_pose2dfilt:
            check_pose_folder_exists(p_name, folder_name="pose_2d_filter")
        if remove_pose3d:
            check_pose_folder_exists(p_name, folder_name="pose_3d")
        anipose_pipeline(p_name, **kwargs)
