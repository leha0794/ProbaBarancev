from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()  # сейчас нужен гекодрайвер
        self.wd.implicitly_wait(60)  # время на каждое действие, вместо sleep

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div/span/a").click()

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

    def login(self, logi):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(logi.email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(logi.password)
        wd.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[3]/td[2]/input").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://note-pad.net/")

    def destroy(self):
        self.wd.quit()
