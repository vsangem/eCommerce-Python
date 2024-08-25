from selenium import webdriver
from selenium.webdriver.common.by import By


def test_verify_feedback_for_us():
    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click on 'Contact Us' button
    driver.find_element(By.LINK_TEXT, 'Contact us').click()

    # 5. Verify 'Feedback For Us' is visible.
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-4 div.contact-info h2').text == 'Feedback For Us'.upper()

    # 6. Verify email id - 'feedback@automationexercise.com' is visible.
    assert driver.find_element(By.CSS_SELECTOR, 'address a u').text == 'feedback@automationexercise.com'