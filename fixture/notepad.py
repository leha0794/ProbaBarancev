



class NoteHelper:

    def __init__(self, app):
        self.app = app

    def delete(self):
        wd = self.app.wd
        self.return_home_page()
        self.setting_notepad()
        wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/input[2]").click()
        wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[3]/div/button[1]/span").click()

    def setting_notepad(self):
        wd = self.app.wd
        wd.find_element_by_class_name("settings").click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_class_name("icon_back").click()

    def add_page(self):
        wd = self.app.wd
        wd.find_element_by_class_name("icon_add_page").click()

    def create(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/a").click()
