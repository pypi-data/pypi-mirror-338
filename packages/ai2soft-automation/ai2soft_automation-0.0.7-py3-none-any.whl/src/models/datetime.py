import datetime
import time


class DateTime():

    @staticmethod
    def now() -> float:
        return time.time()

    @staticmethod
    def delay(minlli_second):
        time.sleep(minlli_second / 1000)

    @staticmethod
    def delay100ms():
        time.sleep(0.2)

    @staticmethod
    def delay200ms():
        time.sleep(0.2)

    @staticmethod
    def delay500ms():
        time.sleep(0.5)

    @staticmethod
    def delay1sec():
        time.sleep(1)

    @staticmethod
    def delay2sec():
        time.sleep(2)

    @staticmethod
    def delay3sec():
        time.sleep(3)

    @staticmethod
    def delay5sec():
        time.sleep(5)

    @staticmethod
    def delay10sec():
        time.sleep(10)

    @staticmethod
    def delay60sec():
        time.sleep(60)

    @staticmethod
    def str_to_time_float(time_str: str) -> float:
        """
        description:
            将时间字符串(hh:mm:ss)转为对应的 float
        args:
            time_str 格式 hh:mm:ss
        """
        # 将字符串时间格式化成完整的日期时间字符串
        full = time.strftime(f'%Y-%m-%d {time_str}', time.localtime())
        # 将日期时间字符串转换为 struct_time
        t = time.strptime(full, "%Y-%m-%d %H:%M:%S")
        # 将 struct_time 转换为 float
        return time.mktime(t)

    @staticmethod
    def time_str_add(time_str: str, to_add: int) -> str:
        """
            将一个时间字符串(hh:mm:ss) 与 一个整数值 相加， 得到另一个时间字符串
        """
        t = DateTime.str_to_time_float(time_str)
        d = datetime.datetime.fromtimestamp(t + float(to_add))
        return f'{d.hour}:{d.minute}:{d.second}'

    @staticmethod
    def time_str_diff(time_smaller: str, time_bigger: str = None) -> float:
        """
            计算时间(hh:mm:ss)差值<br>
            仅计算一天内的 时:分:秒 的差值<br>
            单位秒
        """
        bigger = DateTime.str_to_time_float(time_bigger) if time_bigger is not None else time.time()
        small = DateTime.str_to_time_float(time_smaller)
        return bigger - small

    @staticmethod
    def time_after(time_str: str) -> bool:
        """
            当前时间(hh:mm:ss)在 ... 之后
        """
        small = DateTime.str_to_time_float(time_str)
        return time.time() - small >= 0

    @staticmethod
    def time_between(time_start: str, time_end: str, to_check_time: str = None) -> bool:
        """
            判断给定的时间(to_check_time)是否在一个时间(hh:mm:ss)段[time_start, time_start]内
        """
        start = DateTime.str_to_time_float(time_start)
        end = DateTime.str_to_time_float(time_end)
        check = DateTime.str_to_time_float(to_check_time) if to_check_time is not None else time.time()

        return start <= check <= end

    @staticmethod
    def datetime_to_float(datetime_str: str) -> float:
        """
            将 年-月-日 时:分:秒 转换为 float
        """
        t = time.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        return time.mktime(t)

    @staticmethod
    def __get_datetime_float(datetime_smaller: str, datetime_bigger: str = None) -> tuple[float, float]:
        bigger = DateTime.datetime_to_float(datetime_bigger) if datetime_bigger is not None else time.time()
        smaller = DateTime.datetime_to_float(datetime_smaller)
        return bigger, smaller

    @staticmethod
    def days_diff(datetime_smaller: str, datetime_bigger: str = None) -> int:
        """
            2个日期时间字符串(年-月-日 hh:mm:ss)之间相差的天数 <br>
            时间字符串需要包含 年-月-日 时:分[秒]
        """
        bigger, smaller = DateTime.__get_datetime_float(datetime_smaller, datetime_bigger)
        return (datetime.datetime.fromtimestamp(bigger) - datetime.datetime.fromtimestamp(smaller)).days

    @staticmethod
    def datetime_diff(datetime_smaller: str, datetime_bigger: str = None) -> float:
        """
            计算日期时间差值 <br>
            计算 2 个 日期时间的差 年-月-日 时:分:秒 <br>
            单位: 小时
        """
        bigger, smaller = DateTime.__get_datetime_float(datetime_smaller, datetime_bigger)
        return bigger - smaller
