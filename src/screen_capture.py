import pyautogui
import numpy
import cv2


def get_screen():
  screen = pyautogui.screenshot()

  array = numpy.array(screen)

  frame = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

  return frame

def preprocess_screen_image(frame):
  # First we need to convert the image to greyscale before it can be worked
  # with
  grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Reduce noise with a gaussian blur
  blurred = cv2.GaussianBlur(grey, (5, 5), 0)

  # TODO: swap out magic values 
  thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY_INV, 11, 2)

  return thresh