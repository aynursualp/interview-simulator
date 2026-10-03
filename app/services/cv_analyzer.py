import mediapipe as mp
import cv2
import math

class CVAnalyzer:
    def __init__(self):
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def calculate_posture(self, landmarks):
        # calculate if the user is sitting straight based on shoulder alignment
        # left shoulder index: 11, right shoulder index: 12
        left_shoulder = landmarks.landmark[11].y
        right_shoulder = landmarks.landmark[12].y
        abs_val = abs(left_shoulder - right_shoulder)

        nose = landmarks.landmark[0].y
        shoulder_center = (left_shoulder + right_shoulder) / 2
        neck_distance = shoulder_center - nose

        if abs_val > 0.05:
            status = "Misaligned"
        elif neck_distance < 0.31:
            status = "Slouching"
        else:
            status = "Aligned"

        return {
            "status": status,
            "deviation": round(abs_val, 3),
            "neck_distance": round(neck_distance, 3)
        }

    def analyze_frame(self, frame):
        # convert frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.holistic.process(rgb_frame)

        analysis_data = {
            "face_detected": False,
            "posture": None
        }

        if results.face_landmarks:
            analysis_data["face_detected"] = True

        if results.pose_landmarks:
            analysis_data["posture"] = self.calculate_posture(results.pose_landmarks)

        return analysis_data