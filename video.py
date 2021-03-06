# import the necessary packages
from imutils.video import VideoStream
import face_recognition
import click
import imutils
import pickle
import time
import cv2
from recognize import recognize
 
# construct the argument parser and parse the arguments
@click.command()
@click.argument('input')#, help='path to video input')
@click.argument('output')#, help='path to write encoded video to')
@click.option('--display', '-y', default=True,
  help="whether or not to display output frame to screen")
@click.option("--detection", '-d', default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
@click.option('--tolerance', default=0.55, help='Tolerance level: (0...1); lower is more accurate, higher for better performance')
def main(input, output, display, detection, tolerance):
  print("[INFO] loading encodings...")
  data = pickle.loads(open('encodings.pickle', "rb").read())
  print("[INFO] LOADING VIDEO...")
  vid = cv2.VideoCapture(input)
  writer = None
  while True: 
    names = []
    _, frame = vid.read()
    rgb = imutils.resize(frame, width=620)
    r = frame.shape[1] / float(rgb.shape[1])
    boxes = recognize(rgb, names, data, detection, tolerance)
    for ((top, right, bottom, left), name) in zip(boxes, names):
      if name == '???': continue
      top = int(top * r)
      right = int(right * r)
      bottom = int(bottom * r)
      left = int(left * r)
      cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
      y = top - 15 if top - 15 > 15 else top + 15
      cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    # if the video writer is None *AND* we are supposed to write
    # the output video to disk initialize the writer
    if writer is None and output is not None:
      fourcc = cv2.VideoWriter_fourcc(*"MJPG")
      writer = cv2.VideoWriter(output, fourcc, 20,
        (frame.shape[1], frame.shape[0]), True)
    # if the writer is not None, write the frame with recognized
    # faces to disk
    if writer is not None:
      writer.write(frame)
    # check to see if we are supposed to display the output frame to
    # the screen
    if display:
      cv2.imshow("Frame", frame)
      key = cv2.waitKey(1) & 0xFF
      # if the `q` key was pressed, break from the loop
      if key == ord("q"):
        break
  # do a bit of cleanup
  cv2.destroyAllWindows()
  vid.stop()
  # check to see if the video writer point needs to be released
  if writer is not None:
    writer.release()


if __name__ == '__main__':
  main()