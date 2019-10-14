import face_recognition
import pickle
import click
import cv2

# @click.command()
# @click.argument('input')
# @click.option('--detection', default='cnn', help='Which face detection model to use. Options are "hog" or "cnn".')
# @click.option('--tolerance', default=0.4, help='Tolerance level: (0...1); lower is more accurate, higher for better performance')

def process(raw_image, encodings):
  encodings = pickle.loads(open(encodings, 'rb').read())
  image = cv2.imread(raw_image)
  return encodings, image

def recognize(image, names, data, detection_method, tolerance):
  rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  print('[INFO] recognizing faces...')
  boxes = face_recognition.face_locations(rgb, model=detection_method)
  detected = face_recognition.face_encodings(image, boxes)
  for face in detected:
  	matches = face_recognition.compare_faces(data['encodings'],
  		face, tolerance)
  	name = '???'
  	if True in matches:
  		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
  		counts = {}
  		for i in matchedIdxs:
  			name = data['names'][i]
  			counts[name] = counts.get(name, 0) + 1
  		name = max(counts, key=counts.get)
  	names.append(name)
  return boxes

def draw(image, boxes, names):
  for ((top, right, bottom, left), name) in zip(boxes, names):
    # draw the predicted face name on the image
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
      0.75, (0, 255, 0), 2)
  print('[INFO] DONE')

def show(image):
  cv2.imshow('Image', image)
  cv2.waitKey(0)
  
