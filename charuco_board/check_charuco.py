import subprocess
import cv2
import imutils

if __name__=='__main__':

    subprocess.run(['anipose','draw-calibration'])

    anipose_board = cv2.imread('calibration.png')
    cv_board = cv2.imread('./design/220405_charucoboard_design.png')

    # from IPython import embed; embed()
    # check later
    anipose_board = imutils.resize(anipose_board, height = 200)
    cv_board = imutils.resize(cv_board, height = 200)

    diff = anipose_board.copy()
    cv2.absdiff(anipose_board, cv_board, diff)

    print(diff)

    if cv2.__version__ != '4.5.5':
        print('Calibration boards might not be the same!\n Please check calibration.png and 220405_charucoboard_design.png')