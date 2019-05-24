import clipboard
import json
import os
import datetime as dt

FILENAME = 'data.json'  # 文件地址

"""
操作clipboard
"""


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


"""
操作menu
"""


def list_cb_content():
    """
    列出clipboard内容，返回list
    """
    data = load_local_cb(FILENAME)
    if data is None:
        pass
    else:
        list_data = sorted(data.keys())
        return list_data


def check_if_latest():
    """
    check if new
    """
    pass


def sort_cb_content():
    """
    sort by time
    """
    pass


"""
操作json文件
"""


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


def save_cb_to_local(content, filename):
    """
    先载入，再添加新的
    保存到本地json
    """
    load_cb = load_local_cb(FILENAME)
    if load_cb is not None:
        contents = load_cb.keys()
        if content not in contents and contents is not None:
            new_data = {content: str(dt.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"))}  # get clipboard value and time
            data = load_local_cb(filename)
            if data is None:
                data = new_data
            else:
                data.update(new_data)

            js_data = str(json.dumps(data))

            with open(filename, 'w') as json_file:
                json.dump(json.loads(js_data), json_file)
    else:
        new_data = {content: str(dt.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"))}  # get clipboard value and time
        js_data = str(json.dumps(new_data))
        with open(filename, 'w') as json_file:
            json.dump(json.loads(js_data), json_file)


def clear_cb_data(filename):
    """
    empty the json file content
    """
    with open(filename, 'w') as json_file:
        json_file.seek(0)
        json_file.truncate()


# cb = clip_board()
# save_cb_to_local(get_cb(),FILENAME)
# load_local_cb(FILENAME)
# clear_cb_data(FILENAME)
# list_cb_content()
