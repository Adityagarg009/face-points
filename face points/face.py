import cv2 as cv
import mediapipe as mp
mp_face_detect = mp.solutions.mp_face_detect
mp_draw = mp.solutions.drawing_utils
cap = cv.VideoCapture(0)
#webcam
with mp_face_detect.FaceDetection(
    model_selection=0,
    min_detection_confidence = 0.5)as face_detection:
    ()