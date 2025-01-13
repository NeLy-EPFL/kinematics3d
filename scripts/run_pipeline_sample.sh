#!/bin/bash

# Run the entire pipeline on a sample dataset
# 2D pose estimation
run_deeplabcut --txt_dir dirs.txt --pose2d
# Filtering and triangulation
run_anipose --txt_dir dirs.txt --filter_2d --calibrate --triangulate
# Check the 3D pose estimation quality
folder_path=$(head -1 dirs.txt)
echo $folder_path
animate_3d --pose_path ${folder_path}/001_step_3sec/behData/pose-3d/pose3d.h5 --export_path ${folder_path}/001_step_3sec/behData/pose-3d/pose3d_video --video