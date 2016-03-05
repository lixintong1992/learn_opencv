import cv2
import numpy as np

_author__ = 'Lust'


def my_function():
    cap = cv2.VideoCapture(0)
    stop = False
    while(not stop):

        # Capture frame-by-frame

        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blur = cv2.GaussianBlur(gray, (7, 7), 1.5)
        # edges = cv2.Canny(blur, 0, 30)

        corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
        try:
            corners = np.int0(corners)
            for i in corners:
                x, y = i.ravel()
                cv2.circle(frame, (x, y), 3, 255, -1)
        except Exception:
            print "nope~"
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) > 0:
            stop = True
    cv2.destroyAllWindows()
    return


if __name__ == '__main__':
    my_function()
