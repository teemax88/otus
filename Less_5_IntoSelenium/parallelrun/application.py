import time

from selenium import webdriver


class Application:
    def __init__(self, browser_name):
        self.browser = browser_name
        if self.browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            self.wd = webdriver.Firefox()

    def test_git(self):
        self.wd.get("https://git-scm.com/")
        time.sleep(3)
        self.wd.quit()

    def test_google(self):
        self.wd.get("https://www.google.com/")
        time.sleep(3)
        self.wd.quit()
