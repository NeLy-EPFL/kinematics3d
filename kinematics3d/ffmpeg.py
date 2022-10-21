import subprocess


def scale_video(video_path, output_path, height=None, width=None):
    if height is None and width is None:
        raise ValueError('either height or width should be non-zero.')
    else:
        y = height if height is not None else -1
        x = width if width is not None else -1

    subprocess.call(
        ['ffmpeg', '-i', video_path, '-vf', f'scale={x}:{y}', '-preset', 'slow', '-crf', '18', output_path]
    )


def put2videos_together(video1_path, video2_path, output_path):

    subprocess.call(
        ['ffmpeg', '-i', video1_path, '-i', video2_path, '-filter_complex', 'hstack', '-c:a', 'ffv1', output_path]
    )


def changed_video_speed(video_path, speed_rate, output_path):
    """_summary_

    Parameters
    ----------
    video_path : _type_
        _description_
    speed_rate : float
        > 1 for slowing down
        < 1 for speeding up
    output_path : _type_
        _description_
    """

    subprocess.call(
        ['ffmpeg', '-i', video_path, '-vf', f"setpts={speed_rate}*PTS", output_path]
    )


def trim_video(video_path, trim_from, trim_to, output_path):
    """
    Parameters
    ----------
    video_path : [type]
        [description]
    trim_from : [type]
        [description]
    trim_to : [type]
        [description]
    output_path : [type]
        [description]

    Example usage:
    for cam_number in [0,1,2,3,4]:
        ffmpeg.trim_video(
            f'camera_{cam_number}.mp4', '00:00:00',
            '00:00:57', f'camera_{cam_number}.mp4'
            )

    """
    # TODO: type check
    subprocess.call(
        ['ffmpeg', '-i', video_path, '-ss', trim_from, '-to', trim_to, '-c:v', 'copy', output_path]
    )
