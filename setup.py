#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

REQUIREMENTS = [
    'anipose @ git+https://github.com/gizemozd/anipose.git',
    'aniposelib @ git+https://github.com/gizemozd/aniposelib.git',
    'imutils==0.5.4',
    'mycolorpy==1.5.1',
    'toml==0.10.2',
    'pandas==1.2.1',
    'numpy==1.22.4',
    'scipy==1.7.3',
    'opencv-python==4.5.5.64',
    'opencv-contrib-python==4.5.5.64',
  ]

setup(
    author="Gizem Ozdil",
    author_email='pembe.ozdil@epfl.ch',
    python_requires='>=3.8',
    description="Pipeline for calibration, triangulation, and data processing using DeepLabCut and Anipose.",
    install_requires=REQUIREMENTS,
    license="MIT license",
    long_description=README + '\n\n',
    include_package_data=True,
    name='kinematics3d',
    packages=find_packages(
        include=[
            'kinematics3d',
            'kinematics3d.*']),
    test_suite='tests',
    url='https://github.com/NeLy-EPFL/kinematics3d',
    version='0.1.0',
    zip_safe=False,
    scripts=[
        'scripts/run_deeplabcut',
        'scripts/run_anipose',
        'scripts/animate_3d',
        'scripts/viz_cam_locations',
        'scripts/viz_real_vs_pose3d',
    ],
)   
