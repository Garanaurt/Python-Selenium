import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

#Регистрация маркеров
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "user_test: mark test as a user test",
    )
    config.addinivalue_line(
        "markers", "need_review: need review from stepik",
    )


#Обработчики функций
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, fr...")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption('language') # значение языка
    browser_name = request.config.getoption("browser_name") # значение браузер
    browser = None
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test.. lang = {lang}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)


    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test.. lang = {lang}")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", lang)
        browser = webdriver.Firefox(firefox_profile=fp)


    yield browser
    print("\nquit browser..")
    browser.quit()
    