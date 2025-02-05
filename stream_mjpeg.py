import cv2
from mjpeg_streamer import MjpegServer, Stream


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

stream = Stream("parking_lot", quality=100, fps=1)

server = MjpegServer("localhost", 8080)
server.add_stream(stream)
server.start()

while True:
    _, frame = cap.read()
    cv2.imshow(stream.name, frame)
    if cv2.waitKey(1) == ord("q"):
        break

    stream.set_frame(frame)

server.stop()
cap.release()
cv2.destroyAllWindows()