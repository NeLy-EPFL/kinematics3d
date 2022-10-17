# pylint: disable=logging-format-interpolation, invalid-name
""" Anipose pipeline run. """
import os
from pathlib import Path
import logging
import shutil
import subprocess
import toml
import numpy as np

import kinematics3d

# Change the logging level here
logging.basicConfig(
    level=logging.INFO,
    format=' %(asctime)s - %(levelname)s- %(message)s')

CONFIG_PATH = Path(kinematics3d.__path__[0]).parents[0] / 'config'


def check_config_exists(main_path: Path, overwrite: bool = True):
    """ Checks if config exists in the main directory, if not copies the default one.

    Parameters
    ----------
    main_path : Path
        Path where anipose pipeline runs.
        Usually under the experiment directory,
        e.g. /mnt/nas2/GO/7cam/220710_aDN2-GAL4xUAS-CsChr/Fly001
    overwrite : bool, optional
        If config exists and overwrite is True,
        then replaces the existing config with the default one, by default True
    """
    if not (main_path / 'config.toml').is_file() or overwrite:
        logging.info(f'Copying default config from {CONFIG_PATH} into {main_path}')
        shutil.copy(CONFIG_PATH / 'config.toml', main_path / 'config.toml')


def check_calib_exists(main_path: Path):
    """ Checks if calibration exists in the main directory, if not copies the default one.
    After copying the calibration, then changes the directory in the config file.

    Parameters
    ----------
    main_path : Path
        Path where anipose pipeline runs.
        Usually under the experiment directory,
        e.g. /mnt/nas2/GO/7cam/220710_aDN2-GAL4xUAS-CsChr/Fly001
    """
    config_data = toml.load(main_path / 'config.toml')
    calib_dir = config_data['pipeline']['calibration_results']

    try:
        shutil.copytree(calib_dir, main_path / 'calibration')
    except FileExistsError:
        logging.info('Removing the existing calibration file...')
        shutil.rmtree(main_path / 'calibration')
        shutil.copytree(calib_dir, main_path / 'calibration')

    logging.info(f'Copying default calibration into {main_path}')

    # Change calibration directory in the config file
    config_data['pipeline']['calibration_results'] = (main_path / 'calibration').as_posix()
    config_data['calibration']['calibration_init'] = (main_path / 'calibration/calibration_init.toml').as_posix()

    f_open = open(main_path / 'config.toml', 'w')
    toml.dump(config_data, f_open)
    f_open.close()
    logging.info('Config file is updated!')


def check_folder_exists(main_path: Path, folder_name: str):
    """ Anipose does not run triangulation if a file with the same name already exists.
    This function checks if pose 3d exists in the main directory,
    if so deletes the existing one.

    Parameters
    ----------
    main_path : Path
        Path where anipose pipeline runs.
        Usually under the experiment directory,
        e.g. /mnt/nas2/GO/7cam/220710_aDN2-GAL4xUAS-CsChr/Fly001
    folder_name: str
        Folder name that anipose uses to store data, e.g., pose_2d
    """
    if folder_name not in ['pose_3d', 'pose_2d', 'pose_2d_filter']:
        raise ValueError(
    "Folder name {} is invalid! It should be either of pose_3d, pose_2d, pose_2d_filter".format(folder_name)
    )

    config_data = toml.load(main_path / 'config.toml')
    pose_name = config_data['pipeline'][folder_name]
    pose_dirs = main_path.rglob(f'*/{pose_name}')

    if pose_dirs:
        for pose_dir_name in pose_dirs:
            logging.info(f'Pose folder exists, deleting the directory {pose_dir_name.as_posix()}')
            shutil.rmtree(pose_dir_name)


def anipose_pipeline(
        main_dir: Path,
        filter_2d: bool = True,
        calibrate: bool = True,
        triangulate: bool = True):
    """ Runs anipose pipeline. """

    logging.info(f'Running anipose on {main_dir}')
    os.chdir(main_dir)

    if filter_2d:
        subprocess.run(['anipose', 'filter'], check=True)
    if calibrate:
        subprocess.run(['anipose', 'calibrate'], check=True)
    if triangulate:
        subprocess.run(['anipose', 'triangulate'], check=True)


def run_pipeline_from_txt(txt_dir: str, remove_pose3d: bool = False, **kwargs):
    """ Run Anipose pipeline from a txt file containing the directories.
        kwargs are the arguments for the anipose pipeline, such as filter_2d.
    """
    txt_dir += '.txt' if not txt_dir.endswith('.txt') else ''

    assert os.path.isfile(f'{txt_dir}'), f'Please create `{txt_dir}`!'
    assert os.path.getsize(f'{txt_dir}'), f'{txt_dir} is empty!!'

    logging.info(f'Running Anipose on the folders inside {txt_dir}')
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
        if parts[0] == "/":
            new_parts = parts[:7]
        else:
            raise ValueError(f"Directory {p_name} is faulty!\nPlease, check it again.")

        new_path = Path(*new_parts)
        path_list.append(new_path)

    for p_name in np.unique(path_list):
        check_config_exists(p_name)
        check_calib_exists(p_name)
        if remove_pose3d:
            check_folder_exists(p_name, folder_name='pose_3d')
        anipose_pipeline(p_name, **kwargs)
