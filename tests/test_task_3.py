import time
from unittest import TestCase
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestYandexAuth(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = configparser.ConfigParser()
        cls.config.read('settings.ini')
        cls.login = cls.config['Tokens']['your_login']
        cls.password = cls.config['Tokens']['your_password']

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://passport.yandex.ru/auth')

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def wait_element(self, by, value, delay=10):
        try:
            return WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            print(f'Element not found after {delay} seconds')
            return None

    def test_successful_authorization(self):
        login_field = self.wait_element(By.ID, 'passp-field-login')
        if not login_field:
            self.fail('Login field not found')
        login_field.send_keys(self.login)
        time.sleep(10)

        submit_button = self.wait_element(By.ID, 'passp:sign-in')
        if not submit_button:
            self.fail('Submit button not found')
        submit_button.click()
        # time.sleep(2)

        password_field = self.wait_element(By.ID, 'passp-field-passwd')
        if not password_field:
            self.fail('Password field not found')
        password_field.send_keys(self.password)
        # time.sleep(2)

        submit_password_button = self.wait_element(By.ID,
                                                   'passp:sign-in')
        if not submit_password_button:
            self.fail('Submit password button not found')

        submit_password_button.click()
        # time.sleep(2)

        # Проверка успешной авторизации
        profile_element = self.wait_element(By.CLASS_NAME,
                                            'UserID-Avatar')
        self.assertTrue(
            profile_element and profile_element.is_displayed(),
            'Авторизация не выполнена')
        # time.sleep(10)
