import cv2 as cv

# Open the video file for reading
video_path = "test_video.mp4"
cap = cv.VideoCapture(video_path)

try:
    while cap.isOpened():
        # Read the next frame from the video
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            break
        
        # Display the frame
        cv.imshow(video_path, frame)

        # Display at 30 frames per second and fetch any key press, cleaning for num lock state
        # 1000 ms / 30 fps = about 33 ms / frame
        key = cv.waitKey(33) & 0b11111111

        # Quit if the q key is pressed
        if key == ord('q'):
            break
finally:
    # Release the VideoCapture object and close all windows
    cap.release()
    cv.destroyAllWindows()