"""Turn an image/video into a plinko board

Example usage:

# image file
python example.py -i images/pyimage_combo.png

# video file
python example.py -i path/to/video.mp4

# webcam
python example.py -i 0
"""

import argparse
from cv_plinko import PlinkoBoard

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required=True,
                help='Path to input image/video to be used as game board.')
ap.add_argument('-w', '--width', default=600, type=int,
                help='Width to resize input image to (use 0 no resize)')
ap.add_argument('-p', '--pieceSize', default=6, type=int,
                help='Radius of game piece size in pixels')
args = vars(ap.parse_args())

plinko = PlinkoBoard(background_path=args['input'],
                     piece_size=args['pieceSize'],
                     background_width=args['width'])
plinko.play()
