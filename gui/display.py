import cv2
import numpy as np

from typing import Tuple
from os.path import join, splitext
from .images import Images

KEY_LEFT_ARROW = ord('D'), ord('d')
KEY_RIGHT_ARROW = ord('A'), ord('a')
KEY_QUIT = ord('Q'), ord('q')


class Display:
    def __init__(self, images: Images):
        self.images = images

    def copy_path_on_click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.images.copy_path_to_clipboard()

    def __get_img(self, path: str, idx: int) -> Tuple[str, np.ndarray]:
        supported_formats = {'.png', '.jpg', '.jpeg'}
        _, ext = splitext(path.lower())
        
        if ext not in supported_formats:
            window_name = f"Unsupported format - {idx}"
            image = np.zeros((480, 640, 3), dtype=np.uint8)
            cv2.putText(image, "Unsupported format", (60, 240), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 250), 2)
        else:
            full_image = cv2.imread(join('images', path))
            image = cv2.resize(full_image, (480, 640))
            window_name = f"Image - {idx}"

        return window_name, image

    def show(self) -> None:
        key = None
        while key != KEY_QUIT:
            path, idx = self.images.get_current()

            window_name, image = self.__get_img(path, idx)

            cv2.imshow(window_name, image)
            cv2.setMouseCallback(window_name, self.copy_path_on_click)
            key = cv2.waitKey(0)
            cv2.destroyWindow(window_name)

            if key in KEY_LEFT_ARROW:
                self.images.forward()
            elif key in KEY_RIGHT_ARROW:
                self.images.back()
            elif key in KEY_QUIT:
                break

        cv2.destroyAllWindows()
