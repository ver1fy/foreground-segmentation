import cv2 as cv
import mbs
import os

INPUT_FRAME = 15

# Load in the frames.
sequence = mbs.load_sequence("input/HighwayII", "png")
input_frame = sequence[INPUT_FRAME]
# Estimate background over n frames (0 to 50).
background = mbs.estimate_background(sequence[0:50])
# Compute the foreground mask for a specific frame.
threshold = 32
mask = mbs.foreground_mask(input_frame, background, threshold)

# Extract ground truth.
GROUND_TRUTH_FILENAME = "gt{0}.png".format(str(INPUT_FRAME).zfill(6))
GROUND_TRUTH_PATH = os.path.join("groundtruth/HighwayII", GROUND_TRUTH_FILENAME)
ground_truth = cv.imread(GROUND_TRUTH_PATH, cv.IMREAD_GRAYSCALE)
# Compute stats.
print("PSNR: %f" % (cv.PSNR(ground_truth, mask)))

# Create output directory.
OUTPUT_PATH = 'output'
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)
# Write results to disk.
cv.imwrite(os.path.join(OUTPUT_PATH, 'background.png'), background)
cv.imwrite(os.path.join(OUTPUT_PATH, 'mask.png'), mask)
