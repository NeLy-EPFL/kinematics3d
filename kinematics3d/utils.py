""" Utils. """
import pandas as pd
import numpy as np
import toml
import cv2
from mycolorpy import colorlist as mcp


def change_kp_names(hdf_path, replace_dict):
    """ Replaces the column names according to the given dictionary. """
    dataframe = pd.read_hdf(hdf_path, 'df_with_missing')
    bp_index = dataframe.columns.names.index('bodyparts')
    dataframe_changed = dataframe.rename(columns=replace_dict, level=bp_index).copy()
    dataframe_changed.to_hdf(hdf_path, 'df_with_missing')

def load_txt(txt_path: str):
    """ Loads a txt file from the path. """
    txt_path += '.txt' if not txt_path.endswith('.txt') else ''
    return [line.rstrip() for line in open(txt_path)]

def get_bodyparts(data_frame):
    """ Gets the names of bodyparts in a DLC output."""
    return data_frame.columns.get_level_values('bodyparts')

def get_color_list(cmap='rainbow', number=6):
    """ Returns the color codes from a given color map. """
    return mcp.gen_color(cmap=cmap, n=number)

def load_calibration(calib_path):
    """ Loads calibration.toml file from the given path. """
    calib = toml.load(calib_path)
    return calib

def get_cam_matrices(calib):
    """ From the calibration file (Anipose) constructs camera extrinsic matrices. """
    calib.pop('metadata')
    cam_ext_matrices = {}
    for cam_name in calib:
        extrinsic_matrix = np.empty((4,4))
        rotation, _ = cv2.Rodrigues(np.array(calib[cam_name]['rotation']))
        translation = np.array(calib[cam_name]['translation'])

        extrinsic_matrix[:3,:3] = rotation
        extrinsic_matrix[:3,3] = translation 
        extrinsic_matrix[3,:] = np.array([0,0,0,1])

        cam_ext_matrices[cam_name] = extrinsic_matrix
    return cam_ext_matrices
