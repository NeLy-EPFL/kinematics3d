from pathlib import Path
import deeplabcut
import tensorflow as tf
from get_videos_list import get_video_list

if __name__ == "__main__":
    # Set up the directories 
    directories = {
        "AJO": [
            "/mnt/upramdya_data/FH/250618_aJO-CsChr/Fly1",
            "/mnt/upramdya_data/FH/250618_aJO-CsChr/Fly2", # Ball pushing a lot 
            "/mnt/upramdya_data/FH/250618_aJO-CsChr/Fly3",
            "/mnt/upramdya_data/FH/250702_aJO-CsChr/Fly1",
            "/mnt/upramdya_data/FH/250702_aJO-CsChr/Fly2",
        ],
        "ABN2": [
            "/mnt/upramdya_data/FH/250620_aBN2-CsChr/Fly1",
            "/mnt/upramdya_data/FH/250620_aBN2-CsChr/Fly2",
            "/mnt/upramdya_data/FH/250620_aBN2-CsChr/Fly3",
            "/mnt/upramdya_data/FH/250714_aBN2-CsChr/Fly1",
        ],
        "ADN1": [
            "/mnt/upramdya_data/FH/250625_aDN1-CsChr/Fly2",
            "/mnt/upramdya_data/FH/250625_aDN1-CsChr/Fly3",
            "/mnt/upramdya_data/FH/250702_aDN1-CsChr/Fly1",
            "/mnt/upramdya_data/FH/250702_aDN1-CsChr/Fly2",
            "/mnt/upramdya_data/FH/250714_aDN1-CsChr/Fly1",
        ]
    }

    config_path = Path("/home/ozdil/Projects/kinematics3d/DLC_annotation/final/cam3/intact_cam3-Melissa-2021-12-01/config.yaml")
    
    if not tf.test.is_gpu_available():
        raise RuntimeError("GPU is not found!")

    for genotype, paths in directories.items():
        print(f"Processing genotype: {genotype}")
        for path in paths:
            print(f"Processing path: {path}")
            video_list = get_video_list(path, camera_id=5)
            if not video_list:
                print(f"No videos found for path: {path}")
                continue
            videotype = Path(video_list[0]).suffix
            deeplabcut.analyze_videos(config_path, video_list, videotype=videotype)
            deeplabcut.create_labeled_video(
                config_path, video_list
            )
