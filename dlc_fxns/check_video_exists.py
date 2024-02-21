from pathlib import Path
import os


video_list = [
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211014_Fly002_001_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211014_Fly002_001_Beh_Clip.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211014_Fly004_002_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211019_Fly001_002_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211019_Fly001_002_Beh_Clip.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211019_Fly002_001_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211019_Fly003_002_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211019_Fly003_002_Beh_Clip.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211019_Fly005_003_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211020_Fly002_003_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211020_Fly002_003_Beh_Clip.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211020_Fly003_001_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211101_Fly001_003_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211102_Fly001_001_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/2111102_Fly002_002_Beh.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/2111102_Fly002_002_Beh_Clip.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211019_Fly003_Beh3_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211102_Fly002_Beh1_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211102_Fly003_Beh2_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211014_Fly001_Beh3_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211020_Fly001_Beh2_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/211102_Fly004_Beh1_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/220511_006_HF_rest_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/220511_007_HF_left_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/220511_008_HF_right_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/220511_005_HF_rest_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/220511_007_HF_right_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/220511_008_HF_left_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/220511_009_HF_left_cam1.mp4",
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01/videos/220511_009_HF_right_cam1.mp4",
]


# for vid in video_list:
#     if Path(vid).is_file():
#         print('ok')
#     else:
#         print(vid)

main_dir = Path(
    "/home/nely/DLC_annotation/final/cam1/version3/intact_cam1-Melissa-2021-12-01"
)
labeled_data = main_dir / "labeled-data"

i = 0
for x in os.listdir(labeled_data):
    if (main_dir / "videos" / f"{x}.mp4").is_file():
        print(i)
        i += 1
    else:
        print(x + " does not exist")
