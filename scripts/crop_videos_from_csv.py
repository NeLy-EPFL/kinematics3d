import os
from kinematics3d import utils
from kinematics3d import ffmpeg

MAIN_DIR = '/Volumes/data/GO/7cam'
OUT_DIR = '/Users/ozdil/Desktop/GIT/kinematic-analysis-pipeline/notebooks/2211_anipose/pitch_analysis'

csv_data = utils.read_csv("/Users/ozdil/Desktop/GIT/kinematic-analysis-pipeline/notebooks/2211_anipose/pitch.csv")

video_names_pitch = []
# Get config
row_no = 20
for row_no in range(1,len(csv_data)):
    if csv_data[row_no][6] == 'TRUE':
        date = csv_data[row_no][0]
        fly_no = csv_data[row_no][1]
        trial_no = csv_data[row_no][2]
        start = round(float(csv_data[row_no][3]) - 1)
        end = round(float(csv_data[row_no][4]) + 1)
        # side = csv_data[row_no][4][1]

        start_stamp = f'00:{start//60:02d}:{start%60:02d}'
        end_stamp = f'00:{end//60:02d}:{end%60:02d}'

        camera_name = 2 #if side == 'L' else 4

        dir_name = f'{MAIN_DIR}/{date}_aJO-GAL4xUAS-CsChr/Fly{int(fly_no):03d}/{int(trial_no):03d}_Beh/behData/videos/camera_{camera_name}.mp4'
        out_name = f'{OUT_DIR}/{date}_aJO-GAL4xUAS-CsChr_Fly{int(fly_no):03d}_{int(trial_no):03d}_Beh_{row_no}.mp4'

        video_names_pitch.append(out_name)

        # from IPython import embed; embed()

        # print(dir_name)
        # ffmpeg.trim_video(dir_name, start_stamp, end_stamp, out_name)


ffmpeg.make_grid_16_videos(video_names_pitch, f'{OUT_DIR}/pitch_grid.mp4')

ffmpeg.changed_video_speed(f'{OUT_DIR}/pitch_grid.mp4', 4, f'{OUT_DIR}/pitch_grid_0.25x.mp4')

# OUT_DIR = '/Users/ozdil/Desktop/GIT/kinematic-analysis-pipeline/notebooks/2211_anipose/roll_analysis'

# video_names_right = [
#     f'{OUT_DIR}/R_220405_aJO-GAL4xUAS-CsChr_Fly001_001_Beh_46.mp4',
#     f'{OUT_DIR}/R_220405_aJO-GAL4xUAS-CsChr_Fly001_002_Beh_48.mp4',
#     f'{OUT_DIR}/R_220405_aJO-GAL4xUAS-CsChr_Fly002_001_Beh_54.mp4',
#     f'{OUT_DIR}/R_220405_aJO-GAL4xUAS-CsChr_Fly002_002_Beh_56.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly001_001_Beh_50.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly001_002_Beh_23.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly001_002_Beh_24.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly001_003_Beh_25.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly001_004_Beh_28.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly002_001_Beh_29.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly002_003_Beh_32.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly002_004_Beh_33.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly002_004_Beh_34.mp4',
#     f'{OUT_DIR}/R_220413_aJO-GAL4xUAS-CsChr_Fly003_004_Beh_37.mp4',
#     f'{OUT_DIR}/R_220513_aJO-GAL4xUAS-CsChr_Fly002_003_Beh_42.mp4',
#     f'{OUT_DIR}/R_220513_aJO-GAL4xUAS-CsChr_Fly002_004_Beh_44.mp4',
# ]


# video_names_left = [
#     f'{OUT_DIR}/L_220405_aJO-GAL4xUAS-CsChr_Fly001_001_Beh_45.mp4',
#     f'{OUT_DIR}/L_220405_aJO-GAL4xUAS-CsChr_Fly001_002_Beh_47.mp4',
#     f'{OUT_DIR}/L_220405_aJO-GAL4xUAS-CsChr_Fly001_003_Beh_49.mp4',
#     f'{OUT_DIR}/L_220405_aJO-GAL4xUAS-CsChr_Fly001_003_Beh_51.mp4',
#     f'{OUT_DIR}/L_220405_aJO-GAL4xUAS-CsChr_Fly001_004_Beh_52.mp4',
#     f'{OUT_DIR}/L_220405_aJO-GAL4xUAS-CsChr_Fly002_001_Beh_53.mp4',
#     f'{OUT_DIR}/L_220405_aJO-GAL4xUAS-CsChr_Fly002_003_Beh_57.mp4',
#     f'{OUT_DIR}/L_220413_aJO-GAL4xUAS-CsChr_Fly001_003_Beh_26.mp4',
#     f'{OUT_DIR}/L_220413_aJO-GAL4xUAS-CsChr_Fly002_001_Beh_30.mp4',
#     f'{OUT_DIR}/L_220413_aJO-GAL4xUAS-CsChr_Fly002_002_Beh_31.mp4',
#     f'{OUT_DIR}/L_220413_aJO-GAL4xUAS-CsChr_Fly003_004_Beh_36.mp4',
#     f'{OUT_DIR}/L_220413_aJO-GAL4xUAS-CsChr_Fly003_004_Beh_38.mp4',
#     f'{OUT_DIR}/L_220413_aJO-GAL4xUAS-CsChr_Fly003_004_Beh_39.mp4',
#     f'{OUT_DIR}/L_220513_aJO-GAL4xUAS-CsChr_Fly001_004_Beh_40.mp4',
#     f'{OUT_DIR}/L_220525_aJO-GAL4xUAS-CsChr_Fly001_003_Beh_21.mp4',
#     f'{OUT_DIR}/L_220527_aJO-GAL4xUAS-CsChr_Fly002_003_Beh_58.mp4',
# ]
# # from IPython import embed; embed()

# # ffmpeg.make_grid_16_videos(video_names_left, f'{OUT_DIR}/left_grid.mp4')
# # ffmpeg.make_grid_16_videos(video_names_right, f'{OUT_DIR}/right_grid.mp4')

# # ffmpeg.changed_video_speed(f'{OUT_DIR}/left_grid.mp4', 4, f'{OUT_DIR}/left_grid_0.25x.mp4')
# # ffmpeg.changed_video_speed(f'{OUT_DIR}/right_grid.mp4', 4, f'{OUT_DIR}/right_grid_0.25x.mp4')

