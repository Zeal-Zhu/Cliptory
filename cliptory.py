import rumps
import sys
import clip_board

if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk


def sayhello(sender):
    print('hello {}'.format(sender))


def print_f(_):
    print(f)


def onebitcallback(_):
    print(f)

def copy_from_selected_callback(sender):
    clip_board.copy_from_selected(str(sender.title))

class Cliptory(rumps.App):
    def __init__(self):
        super(Cliptory, self).__init__("Cliptory") # app名字
        self.icon = "app.icns" # 设置icon

        self.menu = [
            rumps.MenuItem('A', callback=print_f, key='F'),
            ('B', ['1', 2, '3', [4, [5, (6, range(7, 14))]]]),
            'C',
            rumps.MenuItem("Clipboard", callback=sayhello),
            rumps.MenuItem("Silly button"),
            rumps.MenuItem("Say hi"),
            rumps.separator,
            rumps.MenuItem("sayhello", callback=sayhello),
            {'Arbitrary':
             {"Depth": ["Menus", "It's pretty easy"],
              "And doesn't": ["Even look like Objective C", rumps.MenuItem("One bit", callback=onebitcallback)]
              }
            }
        ]

        # 从本地json取值，然后添加到menu里面
        cb = clip_board.list_cb_content() 
        for c in cb:
            self.menu["Clipboard"].add(rumps.MenuItem(
                c, callback=copy_from_selected_callback))

    @rumps.clicked("Clipboard")
    def prefs(self, _):
        cb = clip_board.get_cb()
        rumps.alert("your clipboard is {}".format(cb))

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")


if __name__ == "__main__":
    Cliptory().run()
