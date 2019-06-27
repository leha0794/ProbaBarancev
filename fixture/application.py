from selenium import webdriver

from fixture.notepad import NoteHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()  # сейчас нужен гекодрайвер
        self.wd.implicitly_wait(60)  # время на каждое действие, вместо sleep
        self.session = SessionHelper(self)
        self.notepad = NoteHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://note-pad.net/")

    def destroy(self):
        self.wd.quit()
