#!/bin/bash

# Run the entire pipeline on a sample dataset
# 2D pose estimation
run_deeplabcut --txt_dir dirs.txt --pose2d
# Filtering and triangulation
run_anipose --txt_dir dirs.txt --filter_2d --calibrate --triangulate
# Check the 3D pose estimation quality
animate_3d --pose_path pose3d.h5 --export_path pose3d --video