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

def load_local_cb(filename):
    """
    载入本地json的clipboard
    """
    with open(filename, 'r') as json_file:
        content = json_file.readline()
        js = json.loads(content)
        return js

def save_cb_to_local(filename):
    """
    先载入，再添加新的
    保存到本地json
    """
    data = load_local_cb(filename)
    new_data = [{get_cb():str(dt.datetime.now())}] # 中文问题没有解决
    data.append(new_data) # 格式有问题
    js  = json.dumps(data)
    print(js)
    with open(filename, 'w') as json_file:
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
    with open(filname, 'w') as json_file:
        json_file.seek(0)
        json_file.truncate()


save_cb_to_local('data.json')
# load_local_cb('data.json')
#clear_cb_data('data.json')
