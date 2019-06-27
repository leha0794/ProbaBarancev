from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()  # сейчас нужен гекодрайвер
        self.wd.implicitly_wait(60)  # время на каждое действие, вместо sleep
        self.session = SessionHelper(self)

    def delete_notepad(self):
        wd = self.wd
        self.return_home_page()
        self.setting_notepad()
        wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/input[2]").click()
        wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[3]/div/button[1]/span").click()

    def setting_notepad(self):
        wd = self.wd
        wd.find_element_by_class_name("settings").click()

    def return_home_page(self):
        wd = self.wd
        wd.find_element_by_class_name("icon_back").click()

    def add_page(self):
        wd = self.wd
        wd.find_element_by_class_name("icon_add_page").click()

    def create_notepad(self):
        wd = self.wd
        wd.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/a").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://note-pad.net/")

    def destroy(self):
        self.wd.quit()
