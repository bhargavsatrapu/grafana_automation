import time

class Actions:
    def __init__(self, page):
        self.page = page
        
    def launch_application(self,url):
        self.page.goto(url)
        time.sleep(5)

    def send_keys(self, locator, input):
        self.page.fill(locator, input)
        time.sleep(1)

    def click_on_element(self, locator):
        self.page.click(locator)
        time.sleep(3)
