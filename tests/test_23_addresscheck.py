import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.test_1_RegisterUser import random_email, first_name


def test_verify_address_in_checkout_page():
    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click 'Signup / Login' button
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

    # 5. Fill all details in Signup and create account
    driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(first_name)
    driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(random_email)
    driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
    driver.find_element(By.CSS_SELECTOR, '#id_gender2').click()
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('QA@123')
    days = driver.find_element(By.CSS_SELECTOR, '#days')
    select_day = Select(days)
    select_day.select_by_index(28)

    month = driver.find_element(By.CSS_SELECTOR, '#months')
    select_month = Select(month)
    select_month.select_by_index(5)

    year = driver.find_element(By.CSS_SELECTOR, '#years')
    select_year = Select(year)
    select_year.select_by_value('1998')
    driver.execute_script("window.scrollBy(0, 500);")
    driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()

    driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()

    driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys("Trisha")
    driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys('Krishnan')
    driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys('Kollywood Film Industry')
    driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys('Chennai')
    driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys('TamilNadu')
    country = driver.find_element(By.CSS_SELECTOR, 'select#country')
    select_country = Select(country)
    select_country.select_by_visible_text('Singapore')
    driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys('Central Region')
    driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys('Marine Parade')
    driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys('449307')
    driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys('9876543210')

    driver.execute_script("window.scrollBy(0, 500);")
    driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()

    # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    # 7. Verify ' Logged in as username' at top
    assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == first_name

    # 8. Add products to cart
    actions = ActionChains(driver)
    first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
    actions.move_to_element(first_product).perform()
    driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
    second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[1]
    actions.move_to_element(second_product).perform()
    driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[1].click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()

    # 9. Click 'Cart' button
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # 10. Verify that cart page is displayed
    assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'

    # 11. Click Proceed To Checkout
    driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()

    # 12. Verify that the delivery address is same address filled at the time registration of account
    assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Trisha')

    # 13. Verify that the billing address is same address filled at the time registration of account
    assert driver.find_elements(By.CSS_SELECTOR, 'li.address_firstname.address_lastname')[1].text.__contains__('Trisha')

    # 14. Click 'Delete Account' button
    driver.find_element(By.LINK_TEXT, 'Delete Account').click()

    # 15. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    driver.close()