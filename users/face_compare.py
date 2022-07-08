import face_recognition
import cv2
import os

def face_test():
     video_capture = cv2.VideoCapture(0)

     known_face_names = []
     known_face_encodings = []

     path =('C:/Users/Ahmed/Desktop/New folder/two/django_project/users/face/users')
     for file in os.listdir(path):
          load = face_recognition.load_image_file(f'C:/Users/Ahmed/Desktop/New folder/two/django_project/users/face/users/{file}')
          encode = face_recognition.face_encodings(load)[0]
          known_face_encodings.append(encode)
          filename = os.fsdecode(file)
          known_face_names.append(filename)

     while True:
          
          ret, frame = video_capture.read()
          rgb_frame = frame[:, :, ::-1]
          face_locations = face_recognition.face_locations(rgb_frame)
          face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
          
          for (top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
               
               matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
               name = 'unknown'
               
               if True in matches:
                    first_match = matches.index(True)
                    name = known_face_names[first_match]
                    newname= name[:-4]
                    return newname
               if name == 'unknown':
                    return False
                    
 