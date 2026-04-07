import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL  # Required for Pycaw
import screen_brightness_control as sbc

# Initialize MediaPipe Hands
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
TH, IX = mp_Hands.HandLandmark.THUMB_TIP, mp_Hands.HandLandmark.INDEX_FINGER_TIP

# Initialize Pycaw Volume Control
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume.__uuid__, CLSCTX_ALL, None)
    volctl = interface.QueryInterface(IAudioEndpointVolume)
    minv, maxv = volctl.GetVolumeRange()[:2]
except Exception as e:
    print(f"Pycaw error: {e}"); exit()

# Webcam Setup
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible."); exit()

WIN = "Hand Gesture Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

while True:
    ok, img = cap.read()
    if not ok: break
    img = cv2.flip(img, 1) # Flip for selfie view
    h, w, c = img.shape
    
    # Process image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = hands.process(imgRGB)
    
    if res.multi_hand_landmarks and res.multi_handedness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handedness[i].classification[0].label
            mp_draw.draw_landmarks(img, hand, mp_Hands.HAND_CONNECTIONS)
            
            # Get Landmark Coordinates
            lm = hand.landmark
            tp = (int(lm[TH].x * w), int(lm[TH].y * h))
            ip = (int(lm[IX].x * w), int(lm[IX].y * h))
            
            cv2.circle(img, tp, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(ip, 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, tp, ip, (0, 255, 0), 3)
            
            # Calculate Distance
            dist = float(np.hypot(ip[0] - tp[0], ip[1] - tp[1]))
            
            # Volume Control (Left hand handles volume due to flip)
            if label == "Left":
                # Linear interpolation for volume range
                v = np.interp(dist, [30, 250], [minv, maxv])
                volctl.SetMasterVolumeLevel(v, None)
                
                # Visual Bar
                bar = int(np.interp(dist, [30, 250], [400, 150]))
                pct = int(np.interp(dist, [30, 250], [0, 100]))
                cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
                cv2.rectangle(img, (50, bar), (85, 400), (0, 255, 0), cv2.FILLED)
                
