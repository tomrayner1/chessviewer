import pyautogui
import numpy
import cv2


def main():
  screen = pyautogui.screenshot()

  frame = numpy.array(screen)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # For demo purposes
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  pattern_size = (7, 7)
  ret, corners = cv2.findChessboardCorners(gray, pattern_size)

  if ret:
    print("Chessboard found.")

    cv2.drawChessboardCorners(frame, pattern_size, corners, ret)
  else:
    print("Couldn't find a chessboard.")

  cv2.imshow("frame", frame)
  cv2.waitKey(0)

  return


if __name__ == "__main__":
  main()