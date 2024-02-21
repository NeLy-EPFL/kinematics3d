from pathlib import Path


def get_video_list(videos_dir):
    videolist = []
    for vname in Path(videos_dir).glob("*.mp4"):
        videolist.append(vname.as_posix())
    return videolist


if __name__ == "__main__":
    # videos_dir = Path('/home/nely/DLC_annotation/final/cam2/pose_estimation/gizem')
    videos_dir = Path(
        "/home/nely/DLC_annotation/final/cam2/cam2-Olivia-2022-03-10/videos"
    )
    videos_dir = Path(
        "/home/nely/DLC_annotation/final/cam3/version4/intact_cam3-Melissa-2021-12-01/videos"
    )

    videos_list = videos_dir.glob("*.mp4")

    for vname in sorted(videos_list):
        print(str(vname))
