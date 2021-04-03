from utils.getStringPosition import *
from airtest.core.api import *


def get_app_name(phone, string):
    app_list = phone.list_app()
    output = []
    for app in app_list:
        if app.find(string) > -1:
            output.append(app)
    return output


# 位置测试步长
posStep = 20


# USB 验证应用开关
def toggle_use_app_checker():
    phone = init_device('Android')
    # 测试用，辅助函数，帮助查找应用的具体名称
    for app in get_app_name(phone, 'setting'):
        print(app)

    # 获取设备尺寸
    display_info = phone.get_display_info()

    # 打开设置应用并搜索
    phone.start_app('com.android.settings')
    sleep(1)
    pos = find_string_in_img(phone.snapshot(), '搜索')
    sleep(1)
    phone.touch(pos)

    # 搜索USB相关设置
    sleep(1)
    phone.text('USB')

    # 点击搜索结果中的验证应用并进入设置项
    sleep(5)
    pos = find_string_in_img(phone.snapshot(), '验证应用')
    sleep(1)
    phone.touch(pos)

    # 在指定的设置页面找到验证应用选项的位置
    sleep(3)
    pos = find_string_in_img(phone.snapshot(), '验证应用', True)

    if pos:
        touch((display_info['width'] - 200, pos[1]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    toggle_use_app_checker()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
