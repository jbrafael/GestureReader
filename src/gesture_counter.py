def count_fingers(hand_landmarks):

    finger_tips = [4, 8, 12, 16, 20] 
    finger_states = []

    for i, tip in enumerate(finger_tips):
        if i == 0:  # Polegar
            if hand_landmarks.landmark[tip].x > hand_landmarks.landmark[tip - 1].x:
                finger_states.append(1)
            else:
                finger_states.append(0)
        else:  # Outros dedos
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                finger_states.append(1)
            else:
                finger_states.append(0)

    return sum(finger_states)