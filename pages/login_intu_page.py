from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginIntuPage(BasePage):
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'loginbtn')

    def login(self, email, password):
        self.enter_text(self.USERNAME_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)