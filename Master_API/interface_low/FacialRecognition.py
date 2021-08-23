import face_recognition
import cv2
import numpy as np
import os
import glob

class  FacialRecognition:
    def __getKnownFaces(self):
        """
        Return a list of the known faces that are in the folder known_faces/
        """
        known_face_encodings = []
        known_face_names = []
        dirname = os.getcwd()
        path = os.path.join(dirname, 'known_people\\')

        list_of_files = [f for f in glob.glob(path+'*.jpg')]
        number_files = len(list_of_files)

        names = list_of_files.copy()

        for i in range(number_files):
            globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
            globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
            known_face_encodings.append(globals()['image_encoding_{}'.format(i)])

            # Create array of known names
            names[i] = names[i].replace(path, "")
            known_face_names.append(names[i])
        
        return known_face_encodings, known_face_names

    def getFacesNameAndLocation(self, img):
        """
        Return
        """
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Recognize faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # Import faces from folder known_faces/
        known_face_encodings, known_face_names = self.__getKnownFaces()

        # Check if faces look like the ones of known people
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
        return face_locations, face_names
