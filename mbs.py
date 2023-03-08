import cv2 as cv
import glob
import numpy as np

def load_sequence(dir, ext):
  # Extract frames from directory.
  path = "{dir}/*.{ext}".format(dir = dir, ext = ext)
  frames = glob.glob(path)
  # Stitch image sequence together in chronological order.
  return [cv.imread(frame, cv.IMREAD_GRAYSCALE) for frame in sorted(frames)]

def estimate_background(sequence):
  return np.median(sequence, axis=0).astype(dtype=np.uint8)

def foreground_mask(frame, background, threshold):
  # Apply gaussian filter.
  filtered_frame = cv.GaussianBlur(frame, (3, 3), 0.485)
  # Compute absolute difference between input frame and background.
  diff = cv.absdiff(filtered_frame, background)
  # Apply threshold to result.
  _, result = cv.threshold(diff, threshold, 255, cv.THRESH_BINARY)
  return result
