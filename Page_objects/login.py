from Base.Actions import Actions
import time


class Login_page(Actions):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    username_field = "//input[@name='user']"
    password_field = "//input[@name='password']"
    submit_button = "//button[@type='submit']"
    user_avatar_logo = "[alt='User avatar']"
    sign_out_button = "//span[text()='Sign out']"

    def login_in_grafana(self, username, password):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click_on_element(self.submit_button)
        time.sleep(3)

    def log_out_from_grafana(self):
        self.click_on_element(self.user_avatar_logo)
        self.click_on_element(self.sign_out_button)
        time.sleep(5)

