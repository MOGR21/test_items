import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Выберите язык: (en/ru/es/fr/....)")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\Запуск браузера..")
    browser = webdriver.Chrome(options=options)
    yield browser
    # ожидание чтобы визуально оценить на каком языке открылся браузер
    time.sleep(5)
    print("\Закрытие браузера..")
    browser.quit()