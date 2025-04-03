import os


class Bound():
    def __init__(self, x: int, y: int, w: int, h: int):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    def __str__(self):
        return f'x={self.__x}, y={self.__y}, w={self.__w}, h={self.__h}'


class ScreenItem():
    """
        匹配项<br>
        将 image_file 指定的图像 与 屏幕上 指定区域 bound 进行比较<br>
        要求 bound区域的大小 要比 image_file图像的大小要略大
    """
    # image 可以是汉字
    def __init__(self, image_file: str, bound: Bound, matched_callback=None, threshold: float = 0.9):
        assert image_file is not None and len(image_file) > 0
        self.__image_file = image_file
        self.__bound = bound
        self.__action = matched_callback
        self.__threshold = threshold

    @property
    def image_file(self):
        return self.__image_file

    @property
    def Bound(self):
        return self.__bound

    @property
    def threshold(self):
        return self.__threshold

    def set_matched(self, value: bool, position: list):
        if value and self.__action:
            self.__action(position)

    def __str__(self):
        return '文件: %s, 区域: %s' % (os.path.basename(self.__image_file), self.__bound)

    def half(self):
        return (self.__bound.w // 2, self.__bound.h // 2)
