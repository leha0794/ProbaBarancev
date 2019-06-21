from selenium import webdriver
import time, unittest
from logi import Logi


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()  # сейчас нужен гекодрайвер
        self.wd.implicitly_wait(60)  # время на каждое действие, вместо sleep

    def test_add_Page(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, Logi(email="leha0793@mail.ru", password="qwerty12345"))
        self.create_notepad(wd)
        self.add_page(wd)
        self.return_home_page(wd)
        self.setting_notepad(wd)
        self.delete_notepad(wd)
        self.logout(wd)
        time.sleep(5)

    def logout(self, wd):
        wd.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div/span/a").click()

    def delete_notepad(self, wd):
        wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/input[2]").click()
        wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[3]/div/button[1]/span").click()

    def setting_notepad(self, wd):
        wd.find_element_by_class_name("settings").click()

    def return_home_page(self, wd):
        wd.find_element_by_class_name("icon_back").click()

    def add_page(self, wd):
        wd.find_element_by_class_name("icon_add_page").click()

    def create_notepad(self, wd):
        wd.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/a").click()

    def login(self, wd, logi):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(logi.email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(logi.password)
        wd.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[3]/td[2]/input").click()

    def open_home_page(self, wd):
        wd.get("https://note-pad.net/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
