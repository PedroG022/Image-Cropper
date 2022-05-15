import cv2
import argparse

# Main argument parser
parser = argparse.ArgumentParser(
    description="This script crops an image using the given coordinaties")

# Input
parser.add_argument('img', help='the target input file',
                    action='store', type=str)

# Output
parser.add_argument('o', help='the target output file',
                    action='store', type=str)

# Coordinates
parser.add_argument('x1', metavar='x1', help="initial X position",
                    action='store', type=int)
parser.add_argument('x2', help="final X position",
                    action='store', type=int)
parser.add_argument('y1', help="initial Y position",
                    action='store', type=int)
parser.add_argument('y2', help="final Y position",
                    action='store', type=int)

# Parse the arguments
args = parser.parse_args()

if __name__ == "__main__":
    # Converts our namespace to a dict
    argsDict = vars(args)

    # Open our image
    img = cv2.imread(argsDict['img'])

    # Get our coordinates from the dict
    x1 = argsDict['x1']
    x2 = argsDict['x2']

    y1 = argsDict['y1']
    y2 = argsDict['y2']

    # Create a new image by using the coordinates
    cropped_image = img[y1:y2, x1:x2]

    # Finnaly, write the result to the output file
    cv2.imwrite(argsDict['o'], cropped_image)
