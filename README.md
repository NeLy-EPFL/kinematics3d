## kinematics3d
Pipeline for calibration, triangulation, and data processing using DeepLabCut and Anipose.


<details>
<summary>TO-DO</summary>

  + [x] Test the dlc and anipose pipeline
  + [x] Tuning for filtering parameters
  + [x] Calibration videos and files
  + [x] Figure out the axes and dimension
  + [x] Check other constraints
  + [ ] Documentation - docstrings
  + [ ] [WIP] Documentation - steps, wiki about calibration etc.
  + [ ] Add loading of points as a sep fnc and fix the indices. (?)
  + [x] Right now if a given directory already exists. Anipose does not run in that directory. Add a function to delete directories.
  + [ ] Change server names.
  + [x] Implement the new approach with the animal calibration.
  + [ ] TODO after the annotation -> reduce the constraints during triangulation
  + [ ] TODO after the annotation -> only take one side of the pose predictions on the side cameras.

### DLC to-do
+ [ ] Merge different annotations for cam 3 and 5
+ [ ] Check the annotations again
+ [ ] Annotate the newest experiments
+ [ ] Double check the key points. Exclude the key points that are merely visible from one camera (e.g. right thorax coxa is rarely visible from the left front view.)

</details>
