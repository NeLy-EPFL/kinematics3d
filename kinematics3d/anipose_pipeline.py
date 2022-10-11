# pylint: disable=logging-format-interpolation, invalid-name
""" Anipose pipeline run. """
import os
from pathlib import Path
import logging
import shutil
import subprocess
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
        e.g. /mnt/nas2/GO/7cam/220710_aDN2-GAL4xUAS-CsChr
    overwrite : bool, optional
        If config exists and overwrite is True,
        then replaces the existing config with the default one, by default True
    """
    if not (main_path / 'config.toml').is_file() or overwrite:
        logging.info(f'Copying default config into {main_path}')
        shutil.copy(CONFIG_PATH / 'config.toml', main_path / 'config.toml')
    else:
        return


def anipose_pipeline(
        main_dir: Path,
        filter_2d: bool = True,
        triangulate: bool = True):
    """ Runs anipose pipeline. """

    logging.info(f'Running anipose on {main_dir}')
    os.chdir(main_dir)

    if filter_2d:
        subprocess.run(['anipose', 'filter'], check=True)
    if triangulate:
        subprocess.run(['anipose', 'triangulate'], check=True)


def run_pipeline_from_txt(txt_dir: str, **kwargs):
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
        if len(parts) < 6:
            raise IndexError(
                """
                Directory should have at least 6 parts.
                Example: ('/','mnt','nas','GO','7cam','220504_aJO-GAL4xUAS-CsChr')
                """
            )

        # If child directory is given, we take the parent directory.
        if "/" == parts[0]:
            new_parts = parts[:6]
        else:
            raise ValueError(f"Directory {p} is faulty!\nPlease, check it again.")

        new_path = Path(*new_parts)
        path_list.append(new_path)

    for p in np.unique(path_list):
        check_config_exists(p)
        anipose_pipeline(p, **kwargs)
