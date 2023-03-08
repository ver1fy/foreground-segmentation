# Foreground Segmentation

The goal of foreground segmentation is to separate objects in the foreground from the background. Other synonyms include _background subtraction_ and _foreground detection_. Segmentation is typically not the end goal, but rather a precursor to further image processing (e.g., [object recognition](https://en.wikipedia.org/wiki/Object_detection)). This repository contains a Python implementation of the median subtraction: a simple and inexpensive algorithm to compute the foreground mask (Lo and Velastin, 2001).

## Getting Started
You'll need to install [OpenCV](https://opencv.org/) to execute the script. I prefer to manage my dependencies with [Conda](https://docs.conda.io/en/latest/), although [pip](https://pypi.org/project/pip/) is another great alternative. Once the dependencies have been installed, follow these steps:

1. Amend line 8 in *results.py* to point to the directory containing your input frames. File names should take the form *in000000.ext*, *in000001.ext* etc.
2. Ensure that lines 17 and 18 point to the directory/file containing the ground truth image. Providing you use the format *gt000000.ext*, *gt000001.ext* etc., these should be picked up automatically
3. Adjust any parameters you see fit (e.g. `INPUT_FRAME`)
4. Execute the script by typing the command `python results.py`. This will output the results to the *output* directory and print the PSNR to the console

This demo uses the [Scene Background Initialization (SBI) dataset](https://sbmi2015.na.icar.cnr.it/SBIdataset.html) which is available free of charge.

## Method

As mentioned before, we'll use median background subtraction to extract the foreground. Feel free to skip to [Results](#results) if this isn't of interest. A high level overview of the pipeline is as follows:

1. Perform median background estimation using $n$ frames
   $$B(x,y,t) = \text{median}(I(x,y,t-i))$$
2. Reduce input frame noise with Gaussian blur
   $$G(x,y) = \frac{1}{2 \pi \sigma ^2} e ^{- \frac{x^2 + y^2}{2 \sigma ^2}}$$
3. Subtract background from input frame
   $$R(x,y,t) = | I(x,y,t) - B(x,y,t) |$$
4. Perform binary thresholding
   $$R(x,y,t) > Th$$

## Results
The figure below demonstrates the output of the pipeline when applied to the *HighwayII* image sequence:
![Segmentation results](sample.png?raw=true "Segmentation results")

Background estimation was performed using the first 50 frames (inclusive). As per the algorithm description, a Gaussian blur of size 3 and standard deviation of 0.485 was applied to the input frame. Finally, background subtraction was performed with a binary threshold of 32. When comparing the foreground mask to the ground truth, a PSNR of 13.8808 is generated (higher the better).

![Segmentation results](sample.gif?raw=true "Segmentation results")

## Notes
The contents of this repository are intended for educational purposes only. Use at your own peril! 🙂

## References
Lo, B. P. L. and Velastin, S. A. (2001). Automatic congestion detection system for underground platforms. *Proceedings of 2001 International Symposium on Intelligent Multimedia, Video and Speech Processing.* pp. 158-161.
