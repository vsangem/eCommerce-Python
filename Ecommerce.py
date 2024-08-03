import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Test Case 1: Register User

driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://www.automationexercise.com/')
homepage = driver.find_element(By.XPATH, '//h1').text

# 3. Verify that home page is visible successfully
assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

# 4. Click on 'Signup / Login' button
driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

# 5. Verify 'New User Signup!' is visible
newUserSignup = driver.find_element(By.CSS_SELECTOR,'.signup-form h2').text
assert 'New User Signup!' in newUserSignup


# 6. Enter name and email address
def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f'{"Tulika"}.{"singh"}_{time_stamp}@yahoo.com'


randomEmail = generate_email_with_timestamp()

name = 'Tulika Singh'
driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(randomEmail)

# 7. Click 'Signup' button
driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()

# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
signup = driver.find_element(By.XPATH, '//h2').text.title()
assert 'Enter Account Information' in signup, f'Sign up Text has been changed Text:{signup}'

# 9. Fill details: Title, Name, Email, Password, Date of birth
driver.find_element(By.CSS_SELECTOR, '#id_gender1').click()
assert driver.find_element(By.CSS_SELECTOR, '#email').get_property('value') == randomEmail
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('QA@123')
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

# 10. Select checkbox 'Sign up for our newsletter!'
driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()

# 11. Select checkbox 'Receive special offers from our partners!'
driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()

# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys("Deekshitha")
driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys('Ponugoti')
driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys('AliBaba')
driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys('Hyderabad')
driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys('Telangana')
country = driver.find_element(By.CSS_SELECTOR, 'select#country')
select_country = Select(country)
select_country.select_by_visible_text('Singapore')
driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys('Central Region')
driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys('Marine Parade')
driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys('449307')
driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys('8541072106')

# 13. Click 'Create Account button'
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()
print(randomEmail)

# 14. Verify that 'ACCOUNT CREATED!' is visible
assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()

# 15. Click 'Continue' button
driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

# 16. Verify that 'Logged in as username' is visible
assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name

# 17. Click 'Delete Account' button
driver.find_element(By.LINK_TEXT, 'Delete Account').click()

# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
driver.close()


# # Test Case 2: Login User with correct email and password
#
# # 1. Launch browser
# driver = webdriver.Edge()
# driver.maximize_window()
#
# # 2. Navigate to url 'http://automationexercise.com'
# driver.get('https://www.automationexercise.com/')
#
# # 3. Verify that home page is visible successfully
# homepage = driver.find_element(By.XPATH, '//h1').text
# assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'
#
# # 4. Click on 'Signup / Login' button
# driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
#
# # 5. Verify 'Login to your account' is visible
# loginUser = driver.find_element(By.CSS_SELECTOR,'.login-form h2').text
# assert 'Login to your account' in loginUser
#
# # 6. Enter correct email address and password
# driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Tulika.singh_20240803222313@yahoo.com')
# driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')
#
# # 7. Click 'login' button
# driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
# time.sleep(2)
#
# # 8. Verify that 'Logged in as username' is visible
# # name = 'Tulika Singh'
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
#
# # 9. Click 'Delete Account' button
# driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#
# # 10. Verify that 'ACCOUNT DELETED!' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# driver.close()


# Test Case 3: Login User with incorrect email and password

# 1. Launch browser
driver = webdriver.Edge()
driver.maximize_window()

# 2. Navigate to url 'http://automationexercise.com'
driver.get('https://www.automationexercise.com/')

# 3. Verify that home page is visible successfully
homepage = driver.find_element(By.XPATH, '//h1').text
assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

# 4. Click on 'Signup / Login' button
driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

# 5. Verify 'Login to your account' is visible
loginUser = driver.find_element(By.CSS_SELECTOR,'.login-form h2').text
assert 'Login to your account' in loginUser

# 6. Enter incorrect email address and password
driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys(randomEmail)
driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')

# 7. Click 'login' button
driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()

# 8. Verify error 'Your email or password is incorrect!' is visible
assert driver.find_element(By.CSS_SELECTOR, '[action="/login"] p').text == 'Your email or password is incorrect!'
driver.close()


# Test Case 4: Logout User

# 1. Launch browser
driver = webdriver.Edge()
driver.maximize_window()

# 2. Navigate to url 'http://automationexercise.com'
driver.get('https://www.automationexercise.com/')

# 3. Verify that home page is visible successfully
homepage = driver.find_element(By.XPATH, '//h1').text
assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

# 4. Click on 'Signup / Login' button
driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

# 5. Verify 'Login to your account' is visible
loginUser = driver.find_element(By.CSS_SELECTOR,'.login-form h2').text
assert 'Login to your account' in loginUser

# 6. Enter correct email address and password
driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Tulika.singh_20240803225822@yahoo.com')
driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')

# 7. Click 'login' button
driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()

# 8. Verify that 'Logged in as username' is visible
assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name

# 9. Click 'Logout' button
driver.find_element(By.LINK_TEXT, 'Logout').click()

# 10. Verify that user is navigated to login page
assert 'Login to your account' in loginUser
driver.close()

# Test Case 5: Register User with existing email

# 1. Launch browser
driver = webdriver.Edge()
driver.maximize_window()

# 2. Navigate to url 'http://automationexercise.com'
driver.get('https://www.automationexercise.com/')

# 3. Verify that home page is visible successfully
homepage = driver.find_element(By.XPATH, '//h1').text
assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

# 4. Click on 'Signup / Login' button
driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

# 5. Verify 'New User Signup!' is visible
newUserSignup = driver.find_element(By.CSS_SELECTOR,'.signup-form h2').text
assert 'New User Signup!' in newUserSignup

# 6. Enter name and already registered email address
driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys('Tulika.singh_20240803225822@yahoo.com')

# 7. Click 'Signup' button
driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()

# 8. Verify error 'Email Address already exist!' is visible
assert driver.find_element(By.CSS_SELECTOR, '[action="/signup"] p').text == 'Email Address already exist!'
driver.close()

# Test Case 6: Contact Us Form

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

# 5. Verify 'GET IN TOUCH' is visible
assert driver.find_element(By.CSS_SELECTOR, '.col-sm-8 div h2').text == 'Get In Touch'.upper()

# 6. Enter name, email, subject and message

# 7. Upload file

# 8. Click 'Submit' button

# 9. Click OK button

# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible

# 11. Click 'Home' button and verify that landed to home page successfully























