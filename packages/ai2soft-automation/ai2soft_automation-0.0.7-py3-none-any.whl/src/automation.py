from internals.mouse import Mouse
from internals.ocr import OCR
from internals.screenShot import ScreenShot, Bound
from models.datetime import DateTime
from models.screenItem import ScreenItem


class Options():
    def __init__(self, is_mac: bool = False, ocr_generator=None, ocr_language: str = 'ch'):
        self.__is_mac = is_mac
        self.__ocr_generator = ocr_generator
        self.__ocr_language = ocr_language

    @property
    def is_mac(self) -> bool:
        return self.__is_mac

    @property
    def ocr_generator(self):
        return self.__ocr_generator

    @property
    def ocr_language(self):
        return self.__ocr_language


class Automation():

    def __init__(self, window_title: str, options: Options):
        assert window_title is not None and len(window_title) > 0, '参数 "window_title" 不能为空'
        assert options is not None, '参考 "options" 不能为空'
        self.__window_title = window_title
        self.__options = options
        self.__ocr = OCR(self) if self.__options.ocr_generator is None else self.__options.ocr_generator(self)

        self.__mouse = Mouse(self)
        self.__screenShot = ScreenShot(self)

        self.__datetime = DateTime()
        self.__screen_items: dict = {}
        self.__ocr_bounds: dict = {}

    def add_ScreenItem(self, key: str, item: ScreenItem):
        assert key is not None and len(key) > 0 and key not in self.__screen_items, '"key" is none or empty or aready exists'
        assert item is not None, '参数 "item" 不能为空'
        self.__screen_items[key] = item

    def add_ScreenItems(self, items: list[list[str, ScreenItem]]):
        assert items is not None and len(items) > 0
        for item in items:
            self.add_ScreenItem(item[0], item[1])

    def add_ocr_bound(self, key: str, bound: Bound):
        assert key is not None and len(key) > 0 and key not in self.__ocr_bounds, '"key" is none or empty or aready exists'
        assert bound is not None, '参数 "bound" 不能为空'
        self.__ocr_bounds[key] = bound

    def add_ocr_bounds(self, bounds: list[list[str, Bound]]):
        assert bounds is not None and len(bounds) > 0
        for item in bounds:
            self.add_ocr_bound(item[0], item[1])

    @property
    def window_title(self) -> str:
        return self.__window_title

    @property
    def screen_items(self):
        return self.__screen_items

    @property
    def ocr_bounds(self):
        return self.__ocr_bounds

    @property
    def options(self):
        return self.__options

    @property
    def datetime(self):
        return self.__datetime

    @property
    def ocr(self):
        return self.__ocr

    @property
    def mouse(self):
        return self.__mouse

    @property
    def screenShot(self):
        return self.__screenShot
