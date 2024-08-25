from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.select import Select


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f'{"Tulika"}.{"singh"}_{time_stamp}@yahoo.com'


email = generate_email_with_timestamp()

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
random_email = f"{first_name}.{last_name}{fake.email(domain='hotmail.com')}"
common_password = 'QA@123'


def test_create_a_new_user():
    # Test Case 1: Register User

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    #  2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # Click on 'Signup / Login' button
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

    # Verify 'New User Signup!' is visible
    new_user_signup = driver.find_element(By.CSS_SELECTOR, '.signup-form h2').text
    assert 'New User Signup!' in new_user_signup

    # Enter name and email address
    driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(first_name)
    driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(random_email)

    # Click 'Signup' button
    driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    signup = driver.find_element(By.XPATH, '//h2').text.title()
    assert 'Enter Account Information' in signup, f'Sign up Text has been changed Text:{signup}'

    # Fill details: Title, Name, Email, Password, Date of birth
    driver.find_element(By.CSS_SELECTOR, '#id_gender2').click()
    assert driver.find_element(By.CSS_SELECTOR, '#email').get_property('value') == random_email
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(common_password)
    days = driver.find_element(By.CSS_SELECTOR, '#days')
    select_day = Select(days)
    select_day.select_by_index(21)

    month = driver.find_element(By.CSS_SELECTOR, '#months')
    select_month = Select(month)
    select_month.select_by_index(6)

    year = driver.find_element(By.CSS_SELECTOR, '#years')
    select_year = Select(year)
    select_year.select_by_value('2005')
    driver.execute_script("window.scrollBy(0, 500);")

    print(f'first Name is {first_name}\n', f'Email is {random_email}\n')

    # Select checkbox 'Sign up for our newsletter!'
    driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()

    # Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys(first_name)
    driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys(fake.company())
    driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys(fake.building_number())
    driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys(fake.street_name())
    country = driver.find_element(By.CSS_SELECTOR, 'select#country')
    select_country = Select(country)
    select_country.select_by_visible_text('Singapore')
    driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys(fake.state())
    driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys(fake.city())
    driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys(fake.zipcode())
    driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys(fake.basic_phone_number())

    # Click 'Create Account button'
    driver.execute_script("window.scrollBy(0, 500);")
    driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()

    # Verify that 'ACCOUNT CREATED!' is visible
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()

    # Click 'Continue' button
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    # Verify that 'Logged in as username' is visible
    assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == first_name

    # # Click 'Delete Account' button
    # driver.find_element(By.LINK_TEXT, 'Delete Account').click()
    #
    # # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    # assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
    # driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

