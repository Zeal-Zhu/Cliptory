import rumps
import sys
import clip_board
import re

if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk

def copy_from_selected_callback(sender):
    content = str(sender.title)
    patt = r"^\[\ [0-9] *\ \]\t*"
    match = str(re.findall(patt, content)[0])
    con = content.replace(match, "")
    clip_board.copy_from_selected(con)

def doing_clear_history(self):
    # 删除json
    clip_board.clear_cb_data(clip_board.FILENAME)
    # 删除menu
    self.menu["Clipboard"].clear()

def clear_history_callback():
    wind = rumps.Window()
    wind.title = "Are you sure to clear the history?"

    wind.add_button

class Cliptory(rumps.App):
    def __init__(self):
        super(Cliptory, self).__init__("Cliptory")  # app名字
        self.icon = "app.icns"  # 设置icon

        self.menu = [
            "History",
            rumps.MenuItem("Clipboard"),
            rumps.separator,
            rumps.MenuItem("Clear History"),
            rumps.MenuItem("Preference", key=","),
            # rumps.MenuItem("test",callback=doing_clear_history),
            None
        ]

        # 从本地json取值，然后添加到menu里面
        cb = clip_board.list_cb_content()
        if cb is not None:
            flag = 0
            for c in cb:
                flag += 1
                self.menu["Clipboard"].add(rumps.MenuItem(
                    "[ {} ]\t{}".format(flag, c), callback=copy_from_selected_callback))

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
