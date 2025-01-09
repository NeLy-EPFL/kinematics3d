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
$ conda create -n kinematics3d python==3.9
$ conda activate kinematics3d
$ pip install -e .
```
You should now be able to run the scripts mentioned below!

## Folder structure
- ```calibration/``` : Contains a configuration file (e.g., intrinsic and extrinsic parameters) for the camera calibration in SeptaCam setup. See `calibration_init.png` for how cameras are placed.
- ```charuco_board/``` : Contains the details and design of the charuco board used for calibration. See [here](https://github.com/NeLy-EPFL/kinematics3d/wiki) for more details.
- ```config/``` : Contains the configuration files for the Anipose pipeline. See [here](https://github.com/NeLy-EPFL/kinematics3d/wiki/Anipose) for a detailed explanation.
- ```dlc_fxns/``` : Contains the functions to automate the run of DeepLabCut.
- ```imgs/``` : Some images used in the Wiki pages.
- ```kinematics3d/``` : Contains the main functions. Please note that this pipeline is very specific to our lab's folder structure and naming conventions and might not be directly applicable to other datasets! So please test things out before running on your data.
- ```sample/``` : a minimal example of the folder structure and data to test the pipeline.
- ```scripts/``` : Contains the scripts to run the pipeline. The above warning applies here as well.

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

- ```viz_cam_locations```: Visualize the location of the cameras from the calibration file.
    Ecample usage:
    ```bash
    $ viz_cam_locations -cp ../calibration/calibration.toml
    ```
