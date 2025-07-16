from pathlib import Path


def get_video_list(videos_dir, camera_id=None):
    videolist = []
    if camera_id is not None:
        videos = Path(videos_dir).rglob(f"camera_{camera_id}*.mp4")
    else:
        videos = Path(videos_dir).glob("*.mp4")

    for vname in videos:
        videolist.append(vname.as_posix())
    return videolist


if __name__ == "__main__":
    # videos_dir = Path('/home/nely/DLC_annotation/final/cam2/pose_estimation/gizem')
    videos_dir = Path(
        "/mnt/upramdya_data/FH/250618_aJO-CsChr/Fly1"
    )
    videos_ajo = get_video_list(videos_dir, camera_id=5)
    for v in videos_ajo:
        print(v)

    # videos_dir = Path(
    #     "/home/nely/DLC_annotation/final/cam3/version4/intact_cam3-Melissa-2021-12-01/videos"
    # )

    # videos_list = videos_dir.glob("*.mp4")

    # for vname in sorted(videos_list):
    #     print(str(vname))
