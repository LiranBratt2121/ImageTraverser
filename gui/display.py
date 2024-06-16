import cv2
from os.path import join
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

    def show(self) -> None:
        key = None
        while key != KEY_QUIT:
            path, idx = self.images.get_current()

            full_image = cv2.imread(join('images', path))
            image = cv2.resize(full_image, (480, 640))
            window_name = f"Image - {idx}"

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
