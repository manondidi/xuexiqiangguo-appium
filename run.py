from time import sleep
from appium import webdriver
import random

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
driver = None
FULL_SCREEN_BAR_HEIGHT = 130
desire_caps = {
    "platformName": "Android",
    "deviceName": "53b0f53c0005",
    "platformVersion": "8.1.0",
    "appPackage": "cn.xuexi.android",
    "appActivity": "com.alibaba.android.rimet.biz.SplashActivity",
    "newCommandTimeout": "1000",
    "noReset": True
}


def random_sleep():
    time = random.randint(5, 8) + random.random()
    sleep(time)


def get_random_read_distance():
    return random.randint(500, 1000)


def prepare():
    global SCREEN_WIDTH, SCREEN_HEIGHT, driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
    SCREEN_HEIGHT = driver.get_window_size()['height']
    SCREEN_WIDTH = driver.get_window_size()['width']
    sleep(10)


def start_learn_article(count):
    tap_learn_tab()
    for i in range(count):
        read_aricle(i)


def start_learn_video(count):
    tap_video_tab()
    tap_video_tab()
    for i in range(count):
        watch_video(i)


def scroll_recyclerview(distance):
    driver.swipe(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + distance, SCREEN_WIDTH / 2,
                 SCREEN_HEIGHT / 2, 5000)
    random_sleep()


def tap_recyclerview_first_item():
    driver.tap([(SCREEN_WIDTH / 2, 350)], 500)  # 点击列表中的第一个item
    random_sleep()


def tap_learn_tab():
    driver.find_element_by_id('cn.xuexi.android:id/home_bottom_tab_button_work').click()
    random_sleep()


def tap_video_tab():
    driver.find_element_by_id('cn.xuexi.android: id / home_bottom_tab_button_contact').click()
    random_sleep()


def read_aricle(i):
    random_sleep()
    if i == 0:
        scroll_recyclerview(820)  # 调过banner
    elif i % 2 == 0:
        if i <= 3:
            driver.tap([((i + 1) + 200, 265)], 500)  # 切换tab
        else:
            driver.tap([(SCREEN_WIDTH / 2 + 300, 265)], 500)  # 切换tab
        random_sleep()
        scroll_recyclerview(230)
    else:
        scroll_recyclerview(230)
    tap_recyclerview_first_item()
    for i in range(12):
        distance = get_random_read_distance()
        if i > 6:
            distance = -distance
        scroll_recyclerview(distance)  # 模拟滚动屏幕看文章
        time = random.randint(10, 15)
        sleep(time)
    random_sleep()
    # collect(i)
    # share(i)
    driver.back()
    random_sleep()


def watch_video(i):
    random_sleep()
    if i == 0:
        pass
    else:
        scroll_recyclerview(810)
    tap_recyclerview_first_item()
    random_sleep()
    for i in range(4):
        tap_video_reply()
        sleep(50)

    random_sleep()
    driver.back()
    random_sleep()


def tap_video_reply():
    driver.tap([(SCREEN_WIDTH / 2, 380)], 500)


def main():
    global FULL_SCREEN_BAR_HEIGHT
    prepare()
    FULL_SCREEN_BAR_HEIGHT = 0  # 全面屏
    # 学习文章
    start_learn_article(6)
    # 学习视频
    # start_learn_video(6)


if __name__ == '__main__':
    main()
