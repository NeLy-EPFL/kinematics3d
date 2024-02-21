from kinematics3d.utils import change_and_delete_kp_names
from kinematics3d.constants import KP_NAME_CHANGES


import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument(
    "--video_dir",
    type=str,
    default=None,
    help="Video dir",
)
args = parser.parse_args()

video_main = args.video_dir

pose_2d_path = Path(video_main).parents[1] / "pose-2d"

for camera_id in [1, 2, 4, 5]:
    hdf_path = Path(video_main).rglob(f"*camera_{camera_id}*.h5")
    # from IPython import embed; embed()
    change_and_delete_kp_names(
        hdf_path,
        KP_NAME_CHANGES[f"camera_{camera_id}"],
        pose_2d_path / f"camera_{camera_id}.h5",
    )
