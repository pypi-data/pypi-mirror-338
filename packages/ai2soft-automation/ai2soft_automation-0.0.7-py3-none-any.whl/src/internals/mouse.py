import pyautogui


class Mouse():
    def __init__(self, main):
        from autonmation import Automation
        self.__main: Automation = main

    def left_button_down(self, x: int, y: int):
        found, bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            x = bound[0] + x
            y = bound[1] + y
            pyautogui.mouseDown(x, y)
        else:
            print(f'<Mouse/left_button_down> 没有找到窗口 "{self.__main.window_title}" .')
        return self

    def left_button_up(self, x: int = None, y: int = None, duration: float = 0):
        found, bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            x = bound[0] + x
            y = bound[1] + y
            if x is not None and y is not None:
                pyautogui.mouseUp(x, y, duration)
            else:
                pyautogui.mouseUp()
        else:
            print(f'<Mouse/left_button_up> 没有找到窗口 "{self.__main.window_title}" .')
        return self

    def move_to(self, x: int, y: int, duration: float = 0):
        found, bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            x = bound[0] + x
            y = bound[1] + y
            pyautogui.moveTo(x, y, duration)
        else:
            print(f'<Mouse/move_to> 没有找到窗口 "{self.__main.window_title}" .')
        return self

    def right_button_down(self):

        return self

    def right_button_up(self):
        return self

    def left_button_click(self, x: int, y: int):
        return self

    def drag_move(self, x1: int, y1: int, x2: int, y2: int, duration: float = 0):
        found, bound = self.__main.screenShot.try_get_window_bound(self.__main.window_title)
        if found:
            x1 = bound[0] + x1
            y1 = bound[1] + y1
            x2 = bound[0] + x2
            y2 = bound[1] + y2
            pyautogui.mouseDown(x1, y1)
            pyautogui.moveTo(x2, y2, duration)
        else:
            print(f'<Mouse/drag_move> 没有找到窗口 "{self.__main.window_title}" .')
        return self
