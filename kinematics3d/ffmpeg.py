""" Functions for commonly used ffmpeg operations. """
from typing import List
import subprocess


def scale_video(video_path: str, output_path: str, height: float = None, width: float = None):
    """ Rescales the width and height of a video. """
    if height is None and width is None:
        raise ValueError('either height or width should be non-zero.')

    y = height if height is not None else -1
    x = width if width is not None else -1

    subprocess.call(
        [
            'ffmpeg', '-i', video_path, '-vf', f'scale={x}:{y}',
            '-preset', 'slow', '-crf', '18', output_path
        ]
    )


def put2videos_together(video1_path: str, video2_path: str, output_path: str):
    """ Concatenates two videos horizontally. """
    subprocess.call(['ffmpeg', '-i', video1_path, '-i', video2_path,
                     '-filter_complex', 'hstack', '-c:a', 'ffv1', output_path])


def changed_video_speed(video_path: str, speed_rate: float, output_path: str):
    """ Changes the video speed.

    Parameters
    ----------
    video_path : str
        Path of the video
    speed_rate : float
        > 1 for slowing down
        < 1 for speeding up
    output_path : str
        Export directory.
    """
    subprocess.call(
        ['ffmpeg', '-i', video_path, '-vf', f"setpts={speed_rate}*PTS", output_path]
    )


def trim_video(video_path: str, trim_from: str, trim_to: str, output_path: str):
    """
    Parameters
    ----------
    video_path : str
        Path of the video
    trim_from : str
        Starting time of the video in the format
        "hh:mm:ss"
    trim_to : str
        Ending time of the video in the format
        "hh:mm:ss"
    output_path : str
        Export directory.

    Example usage:
    for cam_number in [0,1,2,3,4]:
        ffmpeg.trim_video(
            f'camera_{cam_number}.mp4', '00:00:00',
            '00:00:57', f'camera_{cam_number}.mp4'
            )

    """
    subprocess.call(
        ['ffmpeg', '-i', video_path, '-ss', trim_from, '-to', trim_to, '-c:v', 'copy', output_path]
    )


def make_grid_16_videos(video_list: List[str], output_path: str):
    """ Make a 4x4 grid out of 16 videos given in the list."""
    assert len(video_list) >= 9, 'Min number of videos is 16!'

    subprocess.call(
        [
            'ffmpeg',
            '-i', video_list[0],
            '-i', video_list[1],
            '-i', video_list[2],
            '-i', video_list[3],
            '-i', video_list[4],
            '-i', video_list[5],
            '-i', video_list[6],
            '-i', video_list[7],
            '-i', video_list[8],
            '-i', video_list[9],
            '-i', video_list[10],
            '-i', video_list[11],
            '-i', video_list[12],
            '-i', video_list[13],
            '-i', video_list[14],
            '-i', video_list[15],
            '-c:v', 'libx264',
            # '-profile:v', 'baseline',
            '-c:a', 'aac',
            '-filter_complex',
            '''[0:v][1:v][2:v][3:v][4:v][5:v][6:v][7:v][8:v][9:v][10:v][11:v][12:v][13:v][14:v][15:v]xstack=inputs=16:layout=0_0|w0_0|w0+w1_0|w0+w1+w2_0|0_h0|w4_h0|w4+w5_h0|w4+w5+w6_h0|0_h0+h4|w8_h0+h4|w8+w9_h0+h4|w8+w9+w10_h0+h4|0_h0+h4+h8|w12_h0+h4+h8|w12+w13_h0+h4+h8|w12+w13+w14_h0+h4+h8''',
            output_path
        ]
    )


def make_grid_9_videos(video_list: List[str], output_path: str):
    """ Make a 3x3 grid out of 9 videos given in the list."""
    assert len(video_list) >= 9, 'Min number of videos is 9!'

    subprocess.call(
        ['ffmpeg', '-i', video_list[0],
         '-i', video_list[1],
         '-i', video_list[2],
         '-i', video_list[3],
         '-i', video_list[4],
         '-i', video_list[5],
         '-i', video_list[6],
         '-i', video_list[7],
         '-i', video_list[8],
         '-filter_complex',
         '''[0:v][1:v][2:v][3:v][4:v][5:v][6:v][7:v][8:v]xstack=inputs=9:layout=0_0|w0_0|w0+w1_0|0_h0|w2_h0|w2+w3_h0|0_h0+h2|w3_h0+h2|w4+w3_h0+h2''',
         output_path])
