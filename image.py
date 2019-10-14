import click
# import pickle
# import cv2
from recognize import process, recognize, draw, show

@click.command()
@click.argument('image')
@click.option('--encodings', '-e', default='encodings.pickle', help='path to db of BTS facial encodings.')
@click.option('--detection', default='cnn', help='Which face detection model to use. Options are "hog" or "cnn".')
@click.option('--tolerance', default=0.4, help='Tolerance level: (0...1); lower is more accurate, higher for better performance')

def main(image, encodings, detection, tolerance):
	names = []
	encodings, image = process(image, encodings)
	boxes = recognize(image, names, encodings, detection, tolerance)
	draw(image, boxes, names)
	show(image)

if __name__ == '__main__':
	main()
