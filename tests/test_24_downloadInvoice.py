import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.test_1_RegisterUser import random_email, first_name

fake = Faker()


def test_download_invoice_after_successful_purchase():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Add products to cart
    actions = ActionChains(driver)
    driver.execute_script("window.scrollBy(0, 500);")
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

    # 5. Click 'Cart' button
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # 6. Verify that cart page is displayed
    assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'

    # 7. Click Proceed To Checkout
    driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()

    # 8. Click 'Register / Login' button
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(2) p a').click()

    # 9. Fill all details in Signup and create account
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

    # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    # 11. Verify ' Logged in as username' at top
    assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == first_name

    # 12. Click 'Cart' button
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # 13. Click 'Proceed To Checkout' button
    driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()

    # 14. Verify Address Details and Review Your Order
    assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Trisha')
    review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
    print('You\'re ordering: '+review_your_order.text)

    # 15. Enter description in comment text area and click 'Place Order'
    driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Nothing to Add, Please Proceed!')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()

    # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys('10')
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')

    # 17. Click 'Pay and Confirm Order' button
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()

    # 18. Verify success message 'Your order has been placed successfully!'
    success_message = driver.find_element(By.CSS_SELECTOR, '.col-sm-9 p').text.strip()
    assert success_message == 'Congratulations! Your order has been confirmed!'

    # 19. Click 'Download Invoice' button and verify invoice is downloaded successfully.
    driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 a:nth-child(3)').click()

    # 20. Click 'Continue' button
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    # 21. Click 'Delete Account' button
    driver.find_element(By.LINK_TEXT, 'Delete Account').click()

    # 22. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    driver.close()
