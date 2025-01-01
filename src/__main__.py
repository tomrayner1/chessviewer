import pyautogui
import numpy
import cv2


def main():
  screen = pyautogui.screenshot()

  frame = numpy.array(screen)
  frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

  cv2.imshow("Current desktop", frame)
  cv2.waitKey(0)

  return


if __name__ == "__main__":
  main()