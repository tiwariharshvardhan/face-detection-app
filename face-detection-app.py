import cv2
import sys

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_and_blur_faces(image):
    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Apply blur to each face detected
    for (x, y, w, h) in faces:
        # Extract the region of interest (the face)
        face_region = image[y:y+h, x:x+w]
        # Apply Gaussian blur to the face region
        face_region = cv2.GaussianBlur(face_region, (99, 99), 30)
        # Place the blurred face region back into the original image
        image[y:y+h, x:x+w] = face_region
    
    return image

def detect_faces_in_image(file_path):
    # Load the image from file
    image = cv2.imread(file_path)
    if image is None:
        print("Could not read the image.")
        sys.exit()

    # Detect and blur faces
    output_image = detect_and_blur_faces(image)

    # Show the output image
    cv2.imshow("Face Detection", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_faces_from_webcam():
    # Open the webcam
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not open webcam.")
        sys.exit()

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Detect and blur faces
        output_frame = detect_and_blur_faces(frame)

        # Display the frame with blurred faces
        cv2.imshow("Face Detection", output_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close any OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

# Main program
print("Choose an option:")
print("1. Detect faces in an image")
print("2. Detect faces using webcam")
choice = input("Enter 1 or 2: ")

if choice == "1":
    file_path = input("Enter the path to the image file: ")
    detect_faces_in_image(file_path)
elif choice == "2":
    print("Starting webcam. Press 'q' to quit.")
    detect_faces_from_webcam()
else:
    print("Invalid choice. Exiting.")
