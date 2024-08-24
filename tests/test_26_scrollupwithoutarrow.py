from selenium import webdriver
from selenium.webdriver.common.by import By


def test_verify_able_to_scroll_up_without_arrow_button():
    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Scroll down page to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 5. Verify 'SUBSCRIPTION' is visible
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-3.col-sm-offset-1 h2').text == 'Subscription'.upper()

    # 6. Scroll up page to top
    driver.execute_script("window.scrollTo(0,0);")

    # 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers'
    # text is visible on screen
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-6 h2').text \
        == 'Full-Fledged practice website for Automation Engineers'
    driver.close()
