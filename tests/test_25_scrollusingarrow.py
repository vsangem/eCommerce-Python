from selenium import webdriver
from selenium.webdriver.common.by import By


def test_verify_scroll_up_button():
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

    # 6. Click on arrow at bottom right side to move upward
    driver.find_element(By.CSS_SELECTOR, '#scrollUp').click()

    # 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' \
    # text is visible on screen
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-6 h2').text \
        == 'Full-Fledged practice website for Automation Engineers'
    driver.close()
