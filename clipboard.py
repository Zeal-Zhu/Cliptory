from AppKit import NSPasteboard, NSStringPboardType
import json
import datetime as dt

def get_cb():
    """
    获取clipboard数据
    """
    cb = NSPasteboard.generalPasteboard()
    cbstring = cb.stringForType_(NSStringPboardType)
    return cbstring

def load_local_cb():
    """
    载入本地json的clipboard
    """
    pass

def save_cb_to_local():
    """
    保存到本地json
    """
    data = [{get_cb():str(dt.datetime.now())}] # 中文问题没有解决
    # js  = json.dumps(data)
    # print(js)
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)


def check_if_latest():
    """
    检测是否最新
    """
    pass

def clear_cb_data():
    """
    清空clipboard的json文件内容
    """
    pass

save_cb_to_local()
