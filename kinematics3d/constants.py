""" Code to change column names in dataframes. """
from pathlib import Path

import kinematics3d

KP_NAME_CHANGES = {
    'camera_1':
    {
        'post_subgen_area': 'post_subgen_area_L',
        'post_vert_brist': 'post_vert_brist_L',
        'maxillary_palp': 'maxillary_palp_L',
        'thorax_coxa_front': 'thorax_coxa_L',
        'coxa_femur_front': 'coxa_femur_L',
        'femur_tibia_front': 'femur_tibia_L',
        'tibia_tarsus_front': 'tibia_tarsus_L',
        'claw_front': 'claw_L',
        'coxa_femur_behind': 'coxa_femur_R',
        'femur_tibia_behind': 'femur_tibia_R',
        'tibia_tarsus_behind': 'tibia_tarsus_R',
        'claw_behind': 'claw_R',
        'base_antenn_front': 'base_anten_L',
        'base_antenn_behind': 'base_anten_R',
        'tip_antenn_front': 'tip_anten_L',
        'tip_antenn_behind': 'tip_anten_R',
        'labellum_tip': 'labellum_tip',
        'dorsal_humeral_L': 'dorsal_humeral_L',
        'ventral_humeral_L': 'ventral_humeral_L',
        'ant_notopleural_L': 'ant_notopleural_L',
        'thorax_wing_L': 'thorax_wing_L',
        'thorax_midpoint_tether': 'thorax_midpoint_tether',
    },
    'camera_4':
    {
        'claw_R': 'claw_L',
        'claw_L': 'claw_R',
        'tibia_tarsus_R': 'tibia_tarsus_L',
        'tibia_tarsus_L': 'tibia_tarsus_R',
        'femur_tibia_R': 'femur_tibia_L',
        'femur_tibia_L': 'femur_tibia_R',
        'coxa_femur_R': 'coxa_femur_L',
        'coxa_femur_L': 'coxa_femur_R',
        # 'thorax_coxa_R': 'thorax_coxa_L',
        'thorax_coxa_L': 'thorax_coxa_R',
        'labellum_tip': 'labellum_tip',
        'maxillary_palp_L': 'maxillary_palp_R',
        'base_anten_L': 'base_anten_R',
        'base_anten_R': 'base_anten_L',
        'tip_anten_R': 'tip_anten_L',
        'tip_anten_L': 'tip_anten_R',
        'ant_orb_brist_R': 'ant_orb_brist_L',
        'ant_orb_brist_L': 'ant_orb_brist_R',
        'post_vert_brist_R': 'post_vert_brist_L',
        'post_vert_brist_L': 'post_vert_brist_R',
        'dorsal_humeral_L': 'dorsal_humeral_R',
        'ventral_humeral_L': 'ventral_humeral_R',
        'ant_notopleural_L': 'ant_notopleural_R',
        'thorax_wing_L': 'thorax_wing_R',
        'thorax_midpoint_tether': 'thorax_midpoint_tether',
    },
    'camera_5':
    {
        'post_subgen_area': 'post_subgen_area_R',
        'post_vert_brist': 'post_vert_brist_R',
        'maxillary_palp': 'maxillary_palp_R',
        'thorax_coxa_front': 'thorax_coxa_R',
        'coxa_femur_front': 'coxa_femur_R',
        'femur_tibia_front': 'femur_tibia_R',
        'tibia_tarsus_front': 'tibia_tarsus_R',
        'claw_front': 'claw_R',
        'coxa_femur_behind': 'coxa_femur_L',
        'femur_tibia_behind': 'femur_tibia_L',
        'tibia_tarsus_behind': 'tibia_tarsus_L',
        'claw_behind': 'claw_L',
        'base_antenn_front': 'base_anten_R',
        'base_antenn_behind': 'base_anten_L',
        'tip_antenn_front': 'tip_anten_R',
        'tip_antenn_behind': 'tip_anten_L',
        'labellum_tip': 'labellum_tip',
        'dorsal_humeral_L': 'dorsal_humeral_R',
        'ventral_humeral_L': 'ventral_humeral_R',
        'ant_notopleural_L': 'ant_notopleural_R',
        'thorax_wing_L': 'thorax_wing_R',
        'thorax_midpoint_tether': 'thorax_midpoint_tether',
    }
}

package_root_dir = Path(kinematics3d.__file__).parent.parent

# DLC_annotation should be under kinematics3d folder
DLC_CONFIG_PATH = {
    'camera_1': package_root_dir / 'DLC_annotation/final/cam1/intact_cam1-Melissa-2021-12-01' / 'config.yaml',
    'camera_2': package_root_dir / 'DLC_annotation/final/cam2/cam2-Olivia-2022-03-10' / 'config.yaml',
    'camera_3': package_root_dir / 'DLC_annotation/final/cam3/intact_cam3-Melissa-2021-12-01' / 'config.yaml',
    'camera_4': package_root_dir / 'DLC_annotation/final/cam2/cam2-Olivia-2022-03-10' / 'config.yaml',
    'camera_5': package_root_dir / 'DLC_annotation/final/cam1/intact_cam1-Melissa-2021-12-01' / 'config.yaml',
}
