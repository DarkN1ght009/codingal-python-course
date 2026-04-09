import cv2
import time
import pyautogui
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Configurations
SCROLL_SPEED = 300
SCROLL_DELAY = 1
CAM_WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, 
            mp_hands.HandLandmark.MIDDLE_FINGER_TIP, 
            mp_hands.HandLandmark.RING_FINGER_TIP, 
            mp_hands.HandLandmark.PINKY_TIP]
    
    # Check fingers (except thumb) - compares tip y-coord to knuckle y-coord
    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)
            
    # Check thumb
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    
    # Handedness check to correctly identify open thumb
    if (handedness == "Right" and thumb_tip.x > thumb_ip.x) or \
       (handedness == "Left" and thumb_tip.x < thumb_ip.x):
        fingers.append(1)
    
    # Return gesture based on finger count
    if sum(fingers) == 5:
        return "scroll_up"
    elif sum(fingers) == 0:
        return "scroll_down"
    else:
        return "none"

# Setup Camera
cap = cv2.VideoCapture(0) # Use 0 or 1 based on available webcams
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

last_scroll = time.time()
print("Gesture Scroll Control Active\nOpen palm: Scroll Up\nFist: Scroll Down\nPress 'q' to exit")

while cap.isOpened():
    success, img = cap.read()
    if not success: continue

    # Flip for mirror view and convert to RGB
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Draw landmarks
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Detect gesture
            gesture = detect_gesture(hand_landmarks, handedness.classification[0].label)
            
            # Perform scroll
            if time.time() - last_scroll > 0.5:
                if gesture == "scroll_up":
                    pyautogui.scroll(SCROLL_SPEED)
                    last_scroll = time.time()
                elif gesture == "scroll_down":
                    pyautogui.scroll(-SCROLL_SPEED)
                    last_scroll = time.time()
                
            cv2.putText(img, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Gesture Scroll Control", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
