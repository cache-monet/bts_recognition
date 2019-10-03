### BTS RECOGNITION
Identifies BTS members in pictures

usage:
```
# to identify bts
$ python main.py path/to/image

# help menu
$ python main.py --help
Usage: main.py [OPTIONS] IMAGE_TO_CHECK

Options:
  --detection TEXT   Which face detection model to use. Options are "hog" or
                     "cnn".
  --tolerance FLOAT  Tolerance level: (0...1); lower is more accurate, higher
                     for better performance 
  --help             Show this message and exit.
```
