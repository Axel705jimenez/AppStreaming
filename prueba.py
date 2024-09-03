import cv2

video_path = 'static/video.mp4'
video_capture = cv2.VideoCapture(video_path)

while True:
    success, frame = video_capture.read()
    if not success:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
