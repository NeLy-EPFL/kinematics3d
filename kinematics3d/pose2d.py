# pylint: disable=logging-format-interpolation, invalid-name
""" Script to run DeepLabCut on all data in a directory. """
import re
import logging
from pathlib import Path
from sys import platform
from typing import List

from kinematics3d.utils import change_kp_names
from kinematics3d.constants import KP_NAME_CHANGES, DLC_CONFIG_PATH

# Check the OS to decide the NAS folder.
if platform in ("linux", "linux2"):
    SOURCE = '/mnt/nas/GO/7cam/'
elif platform == "darwin":
    SOURCE = '/Volumes/data2/GO/7cam/'

# Change the logging level here
logging.basicConfig(
    level=logging.INFO,
    format=' %(asctime)s - %(levelname)s- %(message)s')


def search_string(word: str, pattern: List[str]) -> bool:
    """Searches a list of strings in a word.

    Parameters
    ----------
    word : str
        Word to be searched.
    pattern : List[str]
        List of patterns to search.

    Returns
    -------
    bool
        True if any of the pattern exists in the word.
    """
    if len(pattern) <= 1:
        return bool(re.search(pattern[0], word))

    return bool(re.search('|'.join(pattern), word))


def get_folder_names(
        date_upper: int,
        date_lower: int,
        genotype: str,
        **kwargs) -> List:
    """ Gets folders fitting the given date interval, genotypo, and experiment type.

    Parameters
    ----------
    date_upper : int
        Latest date that the experiments are done.
    date_lower : int
        Earliest date that the experiments are done.
    genotype : str
        Genotype of the fly.

    Returns
    -------
    List
        List of paths that fit the conditions.
    """
    assert date_upper >= date_lower, 'Date upper must be higher than lower!'

    exps_to_include = kwargs.get('exps_to_include', [''])
    export_path = kwargs.get('export_path', None)

    directories_to_add = []

    for folder_name in Path(SOURCE).iterdir():
        if genotype.lower() in folder_name.as_posix().lower():
            experiment_date = int(folder_name.parts[-1].split('_')[0])
            if date_upper >= experiment_date >= date_lower:
                directories = folder_name.glob('*/*')
                directories_to_add += [d.as_posix() + '\n' for d in directories if search_string(
                    d.parts[-1], exps_to_include) and not d.parts[-1].startswith('.')]

    if export_path is not None:
        with open(export_path, 'w+') as f:
            f.write(''.join(directories_to_add))
        logging.info(f'Files saved at {export_path}')

    return directories_to_add


def get_video_paths(
        input_dir: str,
        camera_id: int,
        export_path: str = None) -> List:
    """ Writes paths of experimental folders in a txt file given.

    Parameters
    ----------
    input_dir : str
        e.g. /mnt/nas/GO/7cam/210307_aJO-GAL4xUAS-CsChr/Fly001/001_Beh
    camera_id: int
        Camera number (e.g., 1)
    export_path: str
        Saves the directories in the path given
        NOTE: For now, I don't empty the text file so be sure to give an empty txt
        e.g. ./paths_rlf_cam3.txt
    """

    path_list = []

    input_dir = input_dir.rstrip(
        '\n') if input_dir.endswith('\n') else input_dir
    video_paths = Path(input_dir).rglob(f'*/videos/camera_{camera_id}.mp4')

    # from IPython import embed; embed()
    if not video_paths:
        logging.warning(f'{input_dir} does not contain videos!')
        return []

    for video_path in video_paths:
        # Check if pose 2d folder exists, if not create it
        pose_2d = video_path.parents[1] / 'pose-2d'
        if not pose_2d.is_dir():
            pose_2d.mkdir()
            path_list.append(video_path.as_posix() + '\n')
        else:
            dlc_path = pose_2d / f'camera_{camera_id}.h5'
            if dlc_path.is_file():
                logging.info(f'{video_path} DLC exists! Skipping...')
                continue
            else:
                path_list.append(video_path.as_posix() + '\n')

    if export_path is not None:
        with open(export_path, 'a') as f:
            f.write(''.join(path_list))
        logging.info(f'Files saved at {export_path}')

    return path_list


def run_dlc(
        camera_id: int,
        paths: List[str],
        show_kp: bool = False,
        video_type: str = 'mp4') -> None:
    """ Runs DLC on the videos.

    Parameters
    ----------
    camera_id : int
        camera id, 1-5
    paths : List[str]
        list of video paths to run dlc
    show_kp : bool, optional
        create labeled videos, by default False
    video_type : str, optional
        video extension, by default 'mp4'
    """
    import deeplabcut as dlc

    for p in paths:
        video_path = p.rstrip('\n')
        pose_2d_path = Path(video_path).parents[1] / 'pose-2d'
        logging.info(f'Running DLC on {video_path}')

        dlc.analyze_videos(
            DLC_CONFIG_PATH[f'camera_{camera_id}'],
            [video_path],
            destfolder=pose_2d_path,
            videotype=video_type)
        # rename the pose estimation file
        list(pose_2d_path.glob(
            f'camera_{camera_id}*.h5'))[0].rename(pose_2d_path / f'camera_{camera_id}.h5')
        if show_kp:
            dlc.create_labeled_video(
                DLC_CONFIG_PATH[f'camera_{camera_id}'],
                [video_path], destfolder=pose_2d_path,
                videotype=video_type)
        if camera_id in [1, 4, 5]:
            change_kp_names(
                pose_2d_path / f'camera_{camera_id}.h5',
                KP_NAME_CHANGES[f'camera_{camera_id}'])
