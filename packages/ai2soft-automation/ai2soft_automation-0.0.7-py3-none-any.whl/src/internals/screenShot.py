from models.screenItem import ScreenItem, Bound
from common.imagesCache import imgCache
from models.datetime import DateTime
import pygetwindow
import mss
import cv2
import numpy as np
import pyautogui


class ScreenShot():
    def __init__(self, main):
        from autonmation import Automation
        self.__main: Automation = main

    def try_get_window_bound(self, window_title: str = None) -> tuple[bool, tuple]:
        """
        description:
            根据窗口标题获取对应的窗口区域。 若窗口标题为 none, 则获取当前桌面的区域
        returns:
            是否检测到窗口标题对应的窗口， 若检测到，则区域大小是
        """
        title = '' if window_title is None else window_title
        windowBound = pygetwindow.getWindowGeometry(title)
        if windowBound is None:
            return False, None
        return True, windowBound

    def try_get_ScreenShot_by_rect(self, rect: Bound) -> tuple[bool, list]:
        """
        description:
            获取 bound 区域的屏幕截图
        returns:
            是否能够获取截图， 截图的 mss->ScreenShot
        """
        assert rect is not None, '参数 "rect" 不能为空'
        found, window_bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            rect = {'left': window_bound[0] + rect.x, 'top': window_bound[1] + rect.y, 'width': rect.w, 'height': rect.h}
            with mss.mss() as sct:
                shot = sct.grab(rect)
                mss.tools.to_png(shot.rgb, shot.size, output='/Volumes/Ramdisk/1.png')
                return True, shot
        else:
            print(f'<ScreenShot/try_get_ScreenShot_by_rect> 没有找到窗口 "{self.__main.window_title}" .')
            return False, None

    def try_get_ScreenShot(self, key_identifer_bound: str) -> tuple[bool, list]:
        """
        description:
            获取 key_identifer_bound 对应 bound 区域的屏幕截图
        returns:
            是否能够获取截图， 截图的 mss->ScreenShot
        """
        assert key_identifer_bound is not None and key_identifer_bound in self.__main.screen_items, '参数 "key_identifer_bound" 不能为空, 或者不存在'
        found, window_bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            item: ScreenItem = self.__main.screen_items[key_identifer_bound]
            bound: Bound = item.Bound
            rect = {'left': window_bound[0] + bound.x, 'top': window_bound[1] + bound.y, 'width': bound.w, 'height': bound.h}
            with mss.mss() as sct:
                shot = sct.grab(rect)
                mss.tools.to_png(shot.rgb, shot.size, output='/Volumes/Ramdisk/1.png')
                return True, shot
        else:
            print(f'<ScreenShot/try_get_screenShot> 没有找到窗口 "{self.__main.window_title}" .')
            return False, None

    def try_wait_until(self, key_identifer_ScreenItem: str, ignored: list[str] = None, timeout: int = 15) -> tuple[bool, tuple, ScreenItem]:
        """
            根据 key_identifer_ScreenItem 找到对应的 ScreenItem<br>
            对当前屏幕截图直到 item 对应的图像被检测到<br>
            ignored 在检测过程中， 可以被忽略的匹配项
        """
        t = DateTime.now()
        while DateTime.now() - t <= timeout:
            found, pos, item = self.is_image_exists(key_identifer_ScreenItem)
            if found:
                return True, pos, item
            if ignored is not None:
                for key in ignored:
                    found, pos, item = self.is_image_exists(key)
                    item.set_matched(found, pos)
        return False, None, None

    def is_image_exists(self, key_identifer_ScreenItem: str) -> tuple[bool, tuple, ScreenItem]:
        """
        description:
            判断 key_identifer_matchItem 对应的匹配项的图像是否在显示在当前屏幕上
        returns:
                是否匹配成功，匹配成功后的左上角坐标(基于屏幕左上角)
        """
        assert key_identifer_ScreenItem is not None and key_identifer_ScreenItem in self.__main.screen_items, '参数 "key_identifer_matchItem" 不能为空, 或者不存在'
        found, window_bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            screen_item: ScreenItem = self.__main.screen_items[key_identifer_ScreenItem]
            template = imgCache.getImg(screen_item.image_file)
            bound: Bound = screen_item.Bound

            shape = template.shape
            assert shape[0] > bound.w or shape[1] > bound.h, '图像 "%s" (%s)的大小(%s,%s)与比较区域(%s,%s)相比较，过大' % (key_identifer_ScreenItem, screen_item.image_file, shape[0], shape[1], bound.w, bound.h)

            rect = {'left': window_bound[0] + bound.x, 'top': window_bound[1] + bound.y, 'width': bound.w, 'height': bound.h}
            with mss.mss() as sct:
                shot = sct.grab(rect)
                mss.tools.to_png(shot.rgb, shot.size, output='/Volumes/Ramdisk/2.png')
                screenShot_np = np.array(shot)
                # 转为 灰度 图
                screenShot_gray = cv2.cvtColor(screenShot_np, cv2.COLOR_BGR2GRAY)
                match = cv2.matchTemplate(screenShot_gray, template, cv2.TM_CCOEFF_NORMED)

                # 注意， cv2.minMaxLoc 返回的坐标原点是左上角。 在 macOS 上, 坐标原点是左下角，可能需要再次转换
                _, max_val, _, pos = cv2.minMaxLoc(match)
                if self.__main.options.is_mac:
                    pos = (rect['left'] + pos[0] // 2, rect['top'] + pos[1] // 2)
                else:
                    pos = (rect['left'] + pos[0], rect['top'] + pos[1])
                return max_val > screen_item.threshold, pos, screen_item
        else:
            print(f'<ScreenShot/try_get_screenShot> 没有找到窗口 "{self.__main.window_title}" .')
            return False, None, None

    def try_get_color(self, x: int, y: int) -> tuple[bool, list]:
        screenShot = pyautogui.screenshot(region=(x, y, 1, 1))
        return True, screenShot.getpixel((0, 0))
