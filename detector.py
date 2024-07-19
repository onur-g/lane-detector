import cv2 as cv

def main():
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

            dims = (frame.shape[1] // 2, frame.shape[0] // 2)
            
            frame = cv.resize(frame, dims)

            # Display the original frame
            cv.namedWindow("original")
            cv.imshow("original", frame)

            # Apply canny edge detection to the frame
            canny = do_canny(frame)

            # Display the frame with canny edge detection applied in a separate window, shifted over
            cv.namedWindow("canny")
            cv.moveWindow("canny", dims[0], 0)
            cv.imshow("canny", canny)

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

def do_canny(frame):
    # Convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

    # Apply canny edge detector
    canny = cv.Canny(gray, 50, 150)

    return canny

def do_segment(frame):
    pass

if __name__ == "__main__":
    main()