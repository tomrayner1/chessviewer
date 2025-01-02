from src.screen_capture import *
import cv2


def show_preprocessed_image():
  screen = get_screen()

  preprocessed = preprocess_screen_image(screen)

  cv2.imshow("preprocessed", preprocessed)
  cv2.waitKey(0)


if __name__ == "__main__":
  show_preprocessed_image()