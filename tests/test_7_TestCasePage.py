from selenium import webdriver
from selenium.webdriver.common.by import By


def test_verify_Test_case_page():
    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click on 'Test Cases' button
    driver.find_element(By.XPATH, '//button[text()="Test Cases"]').click()

    # 5. Verify user is navigated to test cases page successfully
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2 b').text.strip() == 'Test Cases'.upper()
    driver.close()