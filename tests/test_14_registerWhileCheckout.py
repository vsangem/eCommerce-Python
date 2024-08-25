import random
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.test_1_RegisterUser import first_name, random_email, last_name


def test_register_new_user_while_checkout_():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()
    fake = Faker()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Add products to cart
    actions = ActionChains(driver)
    first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')
    random_first_product = random.choice(first_product)
    driver.execute_script('arguments[0].scrollIntoView(true);', random_first_product)
    actions.move_to_element(random_first_product).perform()
    random_first_product.find_element(By.CSS_SELECTOR, '.product-overlay div a').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()

    second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')
    random_second_product = random.choice(second_product)
    driver.execute_script('arguments[0].scrollIntoView(true);', random_second_product)
    actions.move_to_element(random_second_product).perform()
    random_second_product.find_element(By.CSS_SELECTOR, '.product-overlay div a').click()
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
    select_month.select_by_index(random.randint(0,11))

    year = driver.find_element(By.CSS_SELECTOR, '#years')
    select_year = Select(year)
    select_year.select_by_value('1998')
    driver.execute_script("window.scrollBy(0, 500);")
    driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()

    driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()

    driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys(first_name)
    driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys(fake.company())
    driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys(fake.street_name())
    driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys(fake.address())
    country = driver.find_element(By.CSS_SELECTOR, 'select#country')
    select_country = Select(country)
    select_country.select_by_visible_text('Singapore')
    driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys(fake.state())
    driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys(fake.city())
    driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys(fake.zipcode())
    driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys(fake.phone_number())

    driver.execute_script("window.scrollBy(0, 500);")
    driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()

    # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    # 11. Verify 'Logged in as username' at top
    assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == first_name

    # 12.Click 'Cart' button
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # 13. Click 'Proceed To Checkout' button
    driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()

    # 14. Verify Address Details and Review Your Order
    assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__(first_name)
    review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
    print('You\'re ordering: '+review_your_order.text)

    # 15. Enter description in comment text area and click 'Place Order'
    driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys(fake.paragraph(nb_sentences=5))
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()

    # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    fake = Faker()
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys(fake.month())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')

    # 17. Click 'Pay and Confirm Order' button
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()

    # 18. Verify success message 'Your order has been placed successfully!'
    success_message = driver.find_element(By.CSS_SELECTOR, '.col-sm-9 p').text.strip()
    assert success_message == 'Congratulations! Your order has been confirmed!'

    # 19. Click 'Delete Account' button
    driver.find_element(By.LINK_TEXT, 'Delete Account').click()

    # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    driver.close()