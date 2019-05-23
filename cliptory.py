import rumps
import sys
import clip_board
import re
import time
import threading

if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as Tk
else:
    # Python 3
    import tkinter as Tk
    import tkinter.messagebox as messagebox


def copy_from_selected_callback(sender):
    content = str(sender.title)
    patt = r"^\[\ [0-9] *\ \]\t*"
    match = str(re.findall(patt, content)[0])
    con = content.replace(match, "")
    clip_board.copy_from_selected(con)


class ClipboardWatcher(threading.Thread): 
    def __init__(self, window,pause=5.):
        super(ClipboardWatcher, self).__init__()
        self._pause = pause
        self._stopping = False
        self._window= window

    def run(self,*window):
        recent_value = ""
        while not self._stopping:
            tmp_value = clip_board.get_cb()
            if tmp_value != recent_value:
                recent_value = tmp_value
                print("found change:{}", recent_value)
                temp = []
                temp.append(recent_value)
                self._window.add_menu(temp)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True


class Cliptory(rumps.App):
    def __init__(self):
        super(Cliptory, self).__init__("Cliptory")  # app名字
        self.icon = "app.icns"  # 设置icon

        self.menu.add("History")
        self.menu.add(rumps.MenuItem("Clipboard"))
        self.menu.add(rumps.separator)
        self.menu.add(rumps.MenuItem("Clear History"))
        self.menu.add(rumps.MenuItem("Preference", key=","))

       # 从本地json取值，然后添加到menu里面
        cb = clip_board.list_cb_content()
        self.add_menu(list(cb))

        # 实时监测clipboard变化
        watcher = ClipboardWatcher(self, 0.5)
        watcher.start()

    FLAG = 0

    def add_menu(self, menu_list):
        if menu_list is not None:
            for menu_name in menu_list:
                self.menu["Clipboard"].add(rumps.MenuItem(
                    "[ {} ]\t{}".format(self.FLAG, menu_name), callback=copy_from_selected_callback))
                self.FLAG += 1

    @rumps.clicked("Clipboard")
    def prefs(self, _):
        cb = clip_board.get_cb()
        rumps.alert("your clipboard is {}".format(cb))

    @rumps.clicked("Clear History")
    def clear_history(self, sender):
        # 删除json
        clip_board.clear_cb_data(clip_board.FILENAME)
        # 删除menu
        self.menu["Clipboard"].clear()
        # wind = rumps.Window(message="Are you sure to clear the history?",
        #                     title="Warnning", ok="OK")
        # wind.run()
        # print(sender)
        # print(sender.state)

    @rumps.clicked("Preference")
    def preferWind(self, _):
        w = rumps.Window(message='US Mobile login name/email',
                         title='Login',
                         dimensions=(250, 24),
                         default_text="your@email.com")
        w.run()


if __name__ == "__main__":
    Cliptory().run()
