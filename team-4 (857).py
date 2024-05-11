#Working code

# Import required libraries
import cv2
import dlib

# Connects to your computer's default camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Failed to open camera.")
    exit()

# Detect the coordinates
detector = dlib.get_frontal_face_detector()

# Capture frames continuously
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    frame = cv2.flip(frame, 1)
    #make sure that u have python IDE in ur system.

    # RGB to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # Iterator to count faces
    i = 0

    for face in faces:
        # Get the coordinates of faces
        x = face.left()
        y = face.top()
        x1 = face.right()
        y1 = face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        # Increment iterator for each face in faces
        i += 1

        # Display the box and faces
        cv2.putText(frame, 'Face ' + str(i), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # This command lets us quit with the "q" button on a keyboard.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
