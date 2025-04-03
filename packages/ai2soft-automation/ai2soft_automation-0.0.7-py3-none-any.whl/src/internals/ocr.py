from models.screenItem import Bound
from internals.paddle.paddleOCR import PaddleOCR
import mss
import numpy as np


class OCR():
    def __init__(self, main):
        from autonmation import Automation
        self.__main: Automation = main
        self.__ocr = PaddleOCR()

    def try_get_text(self, key_identifer_bound: str) -> tuple[bool, str]:
        assert key_identifer_bound is not None and key_identifer_bound in self.__main.ocr_bounds, '参数 "key_identifer_bound" 不能为空, 或者不存在'
        bound = self.__main.ocr_bounds[key_identifer_bound]
        found, window_bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            monitor = {"left": window_bound[0] + bound.x, "top": window_bound[1] + bound.y, "width": bound.w, "height": bound.h}
            with mss.mss() as sct:
                shot = sct.grab(monitor)
                mss.tools.to_png(shot.rgb, shot.size, output='/Volumes/Ramdisk/ocr_single.png')
                screenShot_np = np.array(shot)

                return self.__ocr.extract_from_single_text_block(screenShot_np)
        else:
            print()
            return False, None

    def try_get_text2(self, key_identifer_bound: str, removed: list[Bound] = None) -> tuple[bool, list[str]]:
        """
            使用 paddleOcr 识别出技能. 可以识别出多行<br>
            rect 待截取区域<br>
            removed 从截取的图像中删除的区域
        """
        assert key_identifer_bound is not None and key_identifer_bound in self.__main.ocr_bounds, '参数 "key_identifer_bound" 不能为空, 或者不存在'
        bound = self.__main.ocr_bounds[key_identifer_bound]
        found, window_bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            monitor = {"left": window_bound[0] + bound.x, "top": window_bound[1] + bound.y, "width": bound.w, "height": bound.h}
            with mss.mss() as sct:
                shot = sct.grab(monitor)
                mss.tools.to_png(shot.rgb, shot.size, output='/Volumes/Ramdisk/ocr_multi.png')
                screenShot_np = np.array(shot)
                # 将截图转为 PIL image
                # img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")

                """
                    通过打印 screenShot_np.shape 可得知，截图的 h = shape[0], w = shape[1]
                    其组织形式是
                        0 .. h-1 行， 每行 0 .. w-1 的二维数组
                        shape 是一个二维数组
                        第一维是 高
                        第二维是 宽/长
                    参考 https://numpy.org/doc/stable/user/absolute_beginners.html
                        索引和切片 https://numpy.org/doc/stable/user/absolute_beginners.html#indexing-and-slicing

                    对二维数组进行操作，格式
                    arrar[一维数组索引, 二维数组索引:二维数组的元素个数]
                """
                if removed is not None:
                    # 因为是 mac Retina屏， mss 截图的图像是放大2倍之后的。所以这里的坐标也需要放大
                    for r in removed:
                        x = r['x'] * 2 if self.__main.options.is_mac else r['x']
                        w = x + r['w'] * 2 if self.__main.options.is_mac else r['w']
                        # h = r['h'] * 2
                        h = 5
                        """
                            因为是截图, shape[2] = 4, 表示一个颜色由 4 个值组成，即: rbga, 所以在赋值时也可使用 rgba. 而不是rgb --> screenShot_np[0:5, x:w] = (75, 75, 84)
                        """
                        screenShot_np[0:h, x:w] = (75, 75, 84, 1)
                return self.__ocr.extract_from_multi_text_block(screenShot_np)
        else:
            return False, None
