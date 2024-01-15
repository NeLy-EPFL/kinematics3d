import subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import argparse


def parse_args():
    """Argument parser."""
    parser = argparse.ArgumentParser(
        description="Pipeline to automatize Anipose run",
        formatter_class=(
            lambda prog: argparse.HelpFormatter(prog, max_help_position=50)
        ),
    )
    parser.add_argument(
        "-txt",
        "--txt_dir",
        type=str,
        default=None,
        help="Input text directory",
    )
    return parser.parse_args()


def run_animation(pose_3d):
    subprocess.run(
        [
            "animate_3d",
            "-p",
            str(pose_3d),
            "--export_path",
            str(pose_3d.parents[0] / "3d_video.mp4"),
            "--exp",
            "Beh",
            "--azim",
            "0",
            "--elev",
            "0",
            "--video",
        ]
    )


if __name__ == "__main__":
    # load text file
    txt_dir = parse_args().txt_dir

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

    # get pose3d.h5
    pose_3d_paths = [
        sorted(list(path_exp.rglob("pose3d.h5")))[-1] for path_exp in path_list
    ]

    with ProcessPoolExecutor(max_workers=16) as executor:
        executor.map(run_animation, pose_3d_paths)
