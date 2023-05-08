import subprocess
import cv2
import imutils
import matplotlib.pyplot as plt

if __name__=='__main__':

    subprocess.run(['anipose','draw-calibration'])

    anipose_board = cv2.imread('calibration.png')
    cv_board = cv2.imread('./design/220405_charucoboard_design.png')

    # from IPython import

    anipose_board = imutils.resize(anipose_board, height = 200)
    cv_board = imutils.resize(cv_board, height = 200)

    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,5))
    anipose_board = imutils.resize(anipose_board, height = 200)
    ax1.imshow(anipose_board)
    ax1.set_title('Anipose reconstructions')
    cv_board = imutils.resize(cv_board, height = 200)
    ax2.imshow(cv_board)
    ax2.set_title('OpenCV reconstructions')
    ax1.axis('off')
    ax2.axis('off')
    plt.show()


    diff = anipose_board.copy()
    cv2.absdiff(anipose_board, cv_board, diff)

    print(diff)

    if cv2.__version__ != '4.5.5':
        print('Calibration boards might not be the same!\n Please check calibration.png and 220405_charucoboard_design.png')