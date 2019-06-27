


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, logi):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(logi.email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(logi.password)
        wd.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[3]/td[2]/input").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div/span/a").click()
