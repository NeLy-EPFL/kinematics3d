## kinematics3d
Pipeline for calibration, triangulation, and data processing using DeepLabCut and Anipose.

## Installation

Download the repository on your local machine by running the following line in the terminal:
```bash
$ git clone https://github.com/NeLy-EPFL/kinematics3d.git
```
After the download is complete, navigate to the folder:
```bash
$ cd kinematics3d
```
In this folder, run the following commands to create a virtual environment with kinematics3d and its required dependencies and activate it:
```bash
$ conda env create -f environment.yml
$ conda activate kinematics3d
```
You should now be able to run the scripts mentioned below!

## Summary of scripts
- ```animate_3d``` : script to animate 3D poses, set the keypoints to be drawn in `KEYPOINTS_DICT` in main. Example usage:
  ```bash
  $ animate_3d --pose_path pose3d.h5 --export_path pose3d_side --video --plot
  ```
- ```run_deeplabcut``` : script to run deeplabcut. Example usage:
    - If you want to create a directory txt file then
    ```bash
    $ run_deeplabcut --date_lower 220424 --date_upper 220525 --genotype aJO-GAL4xUAS-CsChr --export_path dirs.txt --include Beh RLF
    ```
    - If you want to run DLC, just append --pose2d to the above command
    - If you have the txt file ready, then you can skip the specs and run:
    ```bash
    $ run_deeplabcut --txt_dir dirs.txt --pose2d
    ```
- ```run_anipose```: script to run anipose.
    Example use:
    ```bash
    $ run_anipose --txt_dir dirs.txt --filter_2d --calibrate --triangulate --remove3d
    ```
    Note that if such txt does not exist you first need to launch run_deeplabcut to create the file.

- ```viz_cam_locations```:vVisualize the location of the cameras from the calibration file.
    Ecample usage:
    ```bash
    $ viz_cam_locations -cp ../calibration/calibration.toml
    ```


<details>
<summary>TO-DO</summary>

  + [ ] Test the dlc and anipose pipeline after changes (12.22)
  + [ ] [WIP] Documentation - steps, wiki about calibration etc.
  + [ ] Change server names.
  + [x] TODO after the annotation -> reduce the constraints during triangulation
  + [x] TODO after the annotation -> only take one side of the pose predictions on the side cameras. In general, change the key points to be considered in the triangulation. Jumpy key points should be removed -> this does not yield good results
  + [ ] Change ```constants.py``` accordingly.

### DLC to-do
+ [x] Merge different annotations for cam 3 and 5
+ [x] Check the annotations again
+ [x] Annotate the newest experiments
+ [x] Double check the key points. Exclude the key points that are merely visible from one camera (e.g. right thorax coxa is rarely visible from the left front view -removed that and max palp.)

</details>
