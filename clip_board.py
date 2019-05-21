# from AppKit import NSPasteboard, NSStringPboardType
import clipboard
import json
import os
import datetime as dt

FILENAME = 'data.json'


def get_cb():
    """
    获取clipboard数据
    """
    # cb = NSPasteboard.generalPasteboard()
    # cbstring = cb.stringForType_(NSStringPboardType)

    # return cbstring

    text = clipboard.paste()
    return text


def copy_from_selected(msg):
    clipboard.copy(msg)


def load_local_cb(filename):
    """
    载入本地json的clipboard
    """
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        # ... your code for else case ...
        with open(filename, 'r') as json_file:
            content = json_file.readline()
            js = json.loads(content)
            return js
    else:
        # Non empty file exists
        # ... your code ...
        return None


def save_cb_to_local(filename):
    """
    先载入，再添加新的
    保存到本地json
    """

    new_data = {get_cb(): str(dt.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"))}  # 获取当前的clipboard，保存成dict
    data = load_local_cb(filename)
    if data is None:
        data = new_data
    else:
        data.update(new_data)

    js_data = str(json.dumps(data))

    with open(filename, 'w') as json_file:
        json.dump(json.loads(js_data), json_file)


def list_cb_content():
    """
    列出clipboard内容，返回list
    """
    data = load_local_cb(FILENAME)
    if data is None:
        pass
    else:
        list_data = data.keys()
        return list_data


def check_if_latest():
    """
    检测是否最新
    """
    pass


def clear_cb_data(filename):
    """
    清空clipboard的json文件内容
    """
    with open(filename, 'w') as json_file:
        json_file.seek(0)
        json_file.truncate()


# cb = clip_board()
# save_cb_to_local(FILENAME)
# load_local_cb('data.json')
# clear_cb_data('data.json')
list_cb_content()
