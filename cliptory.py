import rumps
import sys
import clipboard
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk


class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App")
        self.menu = ["Clipboard", "Silly button", "Say hi"]

    @rumps.clicked("Clipboard")
    def prefs(self, _):
        cb = clipboard.get_cb()
        rumps.alert("your clipboard is {}".format(cb))

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")



if __name__ == "__main__":
    AwesomeStatusBarApp().run()
