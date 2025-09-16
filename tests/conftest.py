import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from pages.login_page import LoginPage
from utils.urls import URL
from utils.generators import generate_user_data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        # Прямая ссылка на ChromeDriver
        chrome_driver_path = '/Users/kristinaivanova/Downloads/chromedriver-mac-arm64/chromedriver'
        service = ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get(URL.MAIN_PAGE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(URL.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_and_delete_user():
    user_data = generate_user_data()

    register_response = requests.post(URL.REGISTER_USER_URL, json=user_data)
    access_token = register_response.json()["accessToken"]

    user_data["token"] = f"Bearer {access_token}"

    yield user_data

    headers = {"Authorization": user_data["token"]}
    requests.delete(URL.USER_URL, headers=headers)


@pytest.fixture(scope="function")
def login_user(driver, create_and_delete_user):
    auth_page = LoginPage(driver)
    auth_page.open_login_page()
    auth_page.login(create_and_delete_user["email"], create_and_delete_user["password"])  # Исправлено!
    return driver