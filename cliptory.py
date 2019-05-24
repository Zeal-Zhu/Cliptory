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
    patt = r"^\[\ [0-9] *\ \]\ *"
    match = str(re.findall(patt, content)[0])
    con = content.replace(match, "")
    clip_board.copy_from_selected(con)


class ClipboardWatcher(threading.Thread):
    """
    use threading to dectect clipboard changes
    """

    def __init__(self, window, pause=5.):
        super(ClipboardWatcher, self).__init__()
        self._pause = pause
        self._stopping = False
        self._window = window

    def run(self):
        recent_value = ""
        while not self._stopping:
            recent_value = clip_board.get_cb()
            load_cb = clip_board.load_local_cb()
            if load_cb is not None:
                contents = load_cb.keys()
                if recent_value is not None:
                    if recent_value not in contents:
                        self.add_clipboard_content(recent_value)
            else :
                if recent_value is not None:
                    self.add_clipboard_content(recent_value)

        time.sleep(self._pause)

    def stop(self):
        self._stopping = True

    def add_clipboard_content(self,value):
        print("found change:{}", value)
        temp = []
        temp.append(value)
        self._window.add_menu(temp)
        clip_board.save_cb_to_local(value)


class Cliptory(rumps.App):
    def __init__(self):
        super(Cliptory, self).__init__("Cliptory")  # set app name
        self.icon = "app.icns"  # set icon

        self.menu.add("History")
        self.menu.add(rumps.MenuItem("Clipboard"))
        self.menu.add(rumps.separator)
        self.menu.add(rumps.MenuItem("Clear History"))
        self.menu.add(rumps.MenuItem("Preference", key=","))

        # get menu items from local json file, and then add the menu
        cb = clip_board.list_cb_content()
        if cb is not None:
            self.add_menu(list(cb))

        # watch clipboard changes using threading
        watcher = ClipboardWatcher(self, 0.5)
        watcher.start()

    FLAG = 1

    def add_menu(self, menu_list):
        if menu_list is not None:
            for menu_name in menu_list:
                self.menu["Clipboard"].add(rumps.MenuItem(
                    "[ {} ] {}".format(self.FLAG, menu_name), callback=copy_from_selected_callback))
                self.FLAG += 1

    @rumps.clicked("Clipboard")
    def prefs(self, _):
        cb = clip_board.get_cb()
        rumps.alert("your clipboard is {}".format(cb))

    @rumps.clicked("Clear History")
    def clear_history(self, sender):
        # delete json
        clip_board.clear_cb_data()
        # delete submenu
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
