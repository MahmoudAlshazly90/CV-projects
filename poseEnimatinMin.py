import mediapipe as mp
import time
import cv2

#1:3:40
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# Replace with your video path
video_path = r"E:\AI\Advanced Computer Vision with Python\projects\chapter2\posevideos\2.mp4"
cap = cv2.VideoCapture(video_path)   # Capture video

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks :
        mpDraw.draw_landmarks(img , results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
    
    
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    img = cv2.resize(img, (620, 480))
    cv2.putText(img, str(int(fps)), (30, 60), cv2.FONT_HERSHEY_COMPLEX, 3, (50, 10, 90), 3)
    
    cv2.imshow("Images", img)
    
    cv2.waitKey(10)