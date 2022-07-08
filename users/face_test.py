# from msilib.schema import Error
# import face_recognition
# import cv2
# import numpy
# import os
# import sys
# def face_test():
#     # This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
#     # other example, but it includes some basic performance tweaks to make things run a lot faster:
#     #   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#     #   2. Only detect faces in every other frame of video.

#     # PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
#     # OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
#     # specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

#     # Get a reference to webcam #0 (the default one)
#     video_capture = cv2.VideoCapture(0)

#     # Load a sample picture and learn how to recognize it.
#     known_face_names = []
#     known_face_encodings = []

#     path =('C:/Users/Ahmed/Desktop/two/django_project/users/face/users')
#     count = 0
#     for file in os.listdir(path):
#         load = face_recognition.load_image_file(f'C:/Users/Ahmed/Desktop/two/django_project/users/face/users/{file}')
#         # filename = os.path.basename(file)
#         encode = face_recognition.face_encodings(load)[0]
#         known_face_encodings.append(encode)
#         # filename = os.fsdecode(file)
#         # known_face_names.append(filename)
#         count += 1

#         #  images = face_recognition.load_image_file(path ,filename)
#         #  print(filename)
#         #  known_faces += face_recognition.load_image_file(filename)
#         #  print(known_faces)
#         #  known_face_encodings += face_recognition.face_encodings(known_faces[count])[0]
#         #  known_face_names += filename
#         #  print(filename)
#         #  count += 1
        


#     # Load a second sample picture and learn how to recognize it.



#     # Initialize some variables
#     face_locations = []
#     face_encodings = []
#     face_names = []
#     process_this_frame = True

#     while True:
#         # Grab a single frame of video
#         ret, frame = video_capture.read()

#         # Resize frame of video to 1/4 size for faster face recognition processing
#         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

#         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#         rgb_small_frame = small_frame[:, :, ::-1]

#         # Only process every other frame of video to save time
#         if process_this_frame:
#             # Find all the faces and face encodings in the current frame of video
#             face_locations = face_recognition.face_locations(rgb_small_frame)
#             face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#             name = []
#             face_names = []
#             for face_encoding in face_encodings:
#                 # See if the face is a match for the known face(s)
#                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                 name.append("Unknown")

#                 # # If a match was found in known_face_encodings, just use the first one.
                
#                 if True in matches:
#                     return True
#                 else:
#                     return False
#     #                 first_match_index = matches.index(True)
#     #                 name .append(known_face_names[first_match_index])
                
#     #             # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#     #             # best_match_index = np.argmin(face_distances)
#     #             # if matches[best_match_index]:
#     #             #     name = known_face_names[best_match_index]
                    

#     #             face_names.append(name)
#     #     process_this_frame = not process_this_frame


#     #     # Display the results
#     #     for (top, right, bottom, left), name in zip(face_locations, face_names):
#     #         # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#     #         top *= 4
#     #         right *= 4
#     #         bottom *= 4
#     #         left *= 4

#     #         # Draw a box around the face
#     #         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#     #         # Draw a label with a name below the face
#     #         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#     #         font = cv2.FONT_HERSHEY_DUPLEX
#     #         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     #     # Display the resulting image
#     #     cv2.imshow('Video', frame)

#     #     # Hit 'q' on the keyboard to quit!
#     #     if cv2.waitKey(1) & 0xFF == ord('q'):
#     #         break

#     # # Release handle to the webcam
#     # video_capture()
#     # cv2.destroyAllWindows()
import cv2
import face_recognition
import sys

def analyze_face():
    baseimg = face_recognition.load_image_file("ahmed.jpg")
    baseimg = cv2.cvtColor(baseimg, cv2.COLOR_BGR2RGB)
    
    myface = face_recognition.face_locations(baseimg)[0]
    encodemyface = face_recognition.face_encodings(baseimg)[0]
    cv2.rectangle(baseimg, (myface[3], myface[0]), (myface[1], myface[2]), (255, 0, 255), 2)
    
    cv2.imshow('test', baseimg)
    cv2.waitKey(0)
    
    sampeling = face_recognition.load_image_file('ahmed.jpg')
    sampeling = cv2.cvtColor(sampeling, cv2.COLOR_BGR2RGB)
    
    samplefacetest = face_recognition.face_locations(sampeling)[0]
    try:
        encodesamplefacetest = face_recognition.face_encodings(sampeling)[0]
    except IndexError as e:
        print('indexerror.authenticationfield')
        sys.exit()
    
    cv2.rectangle(sampeling, (samplefacetest[3], samplefacetest[0]), (samplefacetest[1], samplefacetest[2]), (255, 0, 255), 2)

    cv2.imshow('test', sampeling)
    cv2.waitKey(0)
    
    result = face_recognition.compare_faces([encodemyface], encodesamplefacetest)
    resultstring = str(result)
    
    if resultstring == '[True]':
        print('user authenticated')
    else:
        print('failed')

analyze_face()