import cv2
import os

def face_reg(username):
    video = cv2.VideoCapture(0) 
    a = 0
    while True:
        a = a + 1
        check, frame = video.read()
        cv2.imshow("Hit 'Q' to take picture",frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            imgname = f"{username}.jpg".format(a)
            path = 'C:/Users/Ahmed/Desktop/New folder/two/django_project/users/face/users'
            cv2.imwrite(os.path.join(path , imgname),frame)
            video.release()
            cv2.destroyAllWindows 
            break
    # imgname = f"{username}.jpg".format(a)
    # path = 'C:/Users/Ahmed/Desktop/New folder/two/django_project/users/face/users'
    # cv2.imwrite(os.path.join(path , imgname),frame)
    # video.release()
    # cv2.destroyAllWindows 
        if key == 27:
            break