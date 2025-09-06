def recognize_gesture(finger_count):

    gestures = {
        0: "Punho fechado ✊",
        1: "Número 1 ☝️",
        2: "Paz e Amor ✌️",
        3: "Número 3 🤟",
        4: "Número 4 ✋",
        5: "Mão aberta 🖐️"
    }
    return gestures.get(finger_count, "Gesto desconhecido 🤔")
