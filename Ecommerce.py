import os.path
import re
import random
import time
from datetime import datetime

from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
#
#
#
# QA@123

# ************* 14 - Error is thrown check it, Remove All hard coding, 19, 20, 22
# Failed Test Cases 13, 14, 20, 23, 24, 25, 3


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f'{"Tulika"}.{"singh"}_{time_stamp}@yahoo.com'


random_email = generate_email_with_timestamp()
fake = Faker()

# # Test Case 1: Register User
#
# # 1. Launch browser
# driver = webdriver.Edge()
# driver.maximize_window()
#
# #  2. Navigate to url 'http://automationexercise.com'
# driver.get('https://www.automationexercise.com/')
# homepage = driver.find_element(By.XPATH, '//h1').text
# assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'
#
# # Click on 'Signup / Login' button
# driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
#
# # Verify 'New User Signup!' is visible
# new_user_signup = driver.find_element(By.CSS_SELECTOR, '.signup-form h2').text
# assert 'New User Signup!' in new_user_signup
#
# # Enter name and email address
# name = fake.name_female()  # 'Ahaana Singh'
# driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
# driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(random_email)
#
# # Click 'Signup' button
# driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
#
# # Verify that 'ENTER ACCOUNT INFORMATION' is visible
# signup = driver.find_element(By.XPATH, '//h2').text.title()
# assert 'Enter Account Information' in signup, f'Sign up Text has been changed Text:{signup}'
#
# # Fill details: Title, Name, Email, Password, Date of birth
# driver.find_element(By.CSS_SELECTOR, '#id_gender2').click()
# assert driver.find_element(By.CSS_SELECTOR, '#email').get_property('value') == random_email
# driver.find_element(By.CSS_SELECTOR, '#password').send_keys('QA@123')
# days = driver.find_element(By.CSS_SELECTOR, '#days')
# select_day = Select(days)
# select_day.select_by_index(21)
#
# month = driver.find_element(By.CSS_SELECTOR, '#months')
# select_month = Select(month)
# select_month.select_by_index(6)
#
# year = driver.find_element(By.CSS_SELECTOR, '#years')
# select_year = Select(year)
# select_year.select_by_value('2005')
# driver.execute_script("window.scrollBy(0, 500);")
#
# # Select checkbox 'Sign up for our newsletter!'
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()
#
# # Select checkbox 'Receive special offers from our partners!'
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()
#
# # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys("Deekshitha")
# driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys('Ponugoti')
# driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys('AliBaba')
# driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys('Hyderabad')
# driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys('Telangana')
# country = driver.find_element(By.CSS_SELECTOR, 'select#country')
# select_country = Select(country)
# select_country.select_by_visible_text('Singapore')
# driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys('Central Region')
# driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys('Marine Parade')
# driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys('449307')
# driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys('7896541230')
#
# # Click 'Create Account button'
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()
#
# # Verify that 'ACCOUNT CREATED!' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
#
# # Click 'Continue' button
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
# # Verify that 'Logged in as username' is visible
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
#
# # Click 'Delete Account' button
# driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#
# # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()


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
# name_1 = 'Ponugoti'
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name_1
#
# # 9. Click 'Delete Account' button
# driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#
# # 10. Verify that 'ACCOUNT DELETED!' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# driver.close()


# Test Case 3: Login User with incorrect email and password
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
# 4. Click on 'Signup / Login' button
# driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
#
# # 5. Verify 'Login to your account' is visible
# loginUser = driver.find_element(By.CSS_SELECTOR,'.login-form h2').text
# assert 'Login to your account' in loginUser
#
# # 6. Enter incorrect email address and password
# driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys(random_email)
# driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')
#
# # 7. Click 'login' button
# driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
#
# # 8. Verify error 'Your email or password is incorrect!' is visible
# assert driver.find_element(By.CSS_SELECTOR, '[action="/login"] p').text == 'Your email or password is incorrect!'
# driver.close()
#
#
# # Test Case 4: Logout User
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
# driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Tulika.singh_20240803225822@yahoo.com')
# driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')
#
# # 7. Click 'login' button
# driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
#
# # 8. Verify that 'Logged in as username' is visible
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
#
# # 9. Click 'Logout' button
# driver.find_element(By.LINK_TEXT, 'Logout').click()
#
# # 10. Verify that user is navigated to login page
# assert 'Login to your account' in loginUser
# driver.close()
#
# # Test Case 5: Register User with existing email
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
# # 5. Verify 'New User Signup!' is visible
# newUserSignup = driver.find_element(By.CSS_SELECTOR,'.signup-form h2').text
# assert 'New User Signup!' in newUserSignup
#
# # 6. Enter name and already registered email address
# driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
# driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys('Tulika.singh_20240803225822@yahoo.com')
#
# # 7. Click 'Signup' button
# driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
#
# # 8. Verify error 'Email Address already exist!' is visible
# assert driver.find_element(By.CSS_SELECTOR, '[action="/signup"] p').text == 'Email Address already exist!'
# driver.close()
#
# # Test Case 6: Contact Us Form
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
# # 4. Click on 'Contact Us' button
# driver.find_element(By.LINK_TEXT, 'Contact us').click()
#
# # 5. Verify 'GET IN TOUCH' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-8 div h2').text == 'Get In Touch'.upper()
#
# # 6. Enter name, email, subject and message
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name"]').send_keys('Ahhana')
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="email"]').send_keys('Ahhana.Singh@gmail.com')
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="subject"]').send_keys('Regarding My recent Order on Dress')
# driver.find_element(By.CSS_SELECTOR, 'textarea[data-qa="message"]').send_keys('Hello,\nI hope you are doing well, now i want to keep you informed that i got a defect piece in my latest order delivery.\nI hope you sort this as early as possible.\nThank you.')
#
# # 7. Upload file
# filepath = os.path.abspath('C:\\Users\\VENKAT JAYASURYA\\Downloads\\orders.csv')
# driver.find_element(By.NAME, 'upload_file').send_keys(filepath)
# driver.execute_script('window.scrollBy(0, 1000);')
#
# # 8. Click 'Submit' button
# driver.find_element(By.NAME, 'submit').click()
#
#
# # 9. Click OK button
# alert = driver.switch_to.alert
# alert.accept()
#
# # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.status.alert.alert-success').text == \
#        'Success! Your details have been submitted successfully.'
#
# # 11. Click 'Home' button and verify that landed to home page successfully
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-success').click()
# homepage = driver.find_element(By.XPATH, '//h1').text
# assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'
# driver.close()

# # Test Case 7: Verify Test Cases Page
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
# # 4. Click on 'Test Cases' button
# driver.find_element(By.XPATH, '//button[text()="Test Cases"]').click()
#
# # 5. Verify user is navigated to test cases page successfully
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2 b').text.strip() == 'Test Cases'.upper()
# driver.close()
#
# # Test Case 8: Verify All Products and product detail page
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
# # 4. Click on 'Products' button
# driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()
#
# # 5. Verify user is navigated to ALL PRODUCTS page successfully
# assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'All Products'.upper()
#
# # 6. The products list is visible
# products = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')
# assert len(products)>0, 'No products found on the page'
# print(f'Number of products visible: {len(products)}')
#
# # 7. Click on 'View Product' of first product
# driver.execute_script('window.scrollBy(0, 500);')
# driver.find_element(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper div[class="choose"] ul li a').click()
#
# # 8. User is landed to product detail page
# driver.find_element(By.CSS_SELECTOR, '.newarrival').is_displayed()
#
# # 9. Verify that detail is visible: product name, category, price, availability, condition, brand
# product_name = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div h2')
# product_name.is_displayed()
# print('Product Name is: '+product_name.text)
# category = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div p')
# category.is_displayed()
# print(category.text)
# price = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div span:nth-child(1)')
# price.is_displayed()
# print('Price is: '+price.text)
# availability = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div p:nth-child(6)')
# availability.is_displayed()
# print(availability.text)
# condition = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div p:nth-child(7)')
# condition.is_displayed()
# print(condition.text)
# brand = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div p:nth-child(8)')
# brand.is_displayed()
# print(brand.text)
# driver.close()
#
# # Test Case 9: Search Product
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
# # 4. Click on 'Products' button
# driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()
#
# # 5. Verify user is navigated to ALL PRODUCTS page successfully
# assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'All Products'.upper()
#
# # 6. Enter product name in search input and click search button
# searchProduct = 'Green Side Placket Detail T-Shirt'
# driver.find_element(By.CSS_SELECTOR, 'input#search_product').send_keys(searchProduct)
# driver.find_element(By.CSS_SELECTOR, 'button#submit_search').click()
#
# # 7. Verify 'SEARCHED PRODUCTS' is visible
# assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'Searched Products'.upper()
#
# # 8. Verify all the products related to search are visible
# searchedProduct = driver.find_element(By.CSS_SELECTOR, '.productinfo.text-center p')
# searchedProduct.is_displayed()
# assert searchedProduct.text.__contains__('Green Side Placket Detail')
# driver.close()
#
# # Test Case 10: Verify Subscription in home page
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
# # 4. Scroll down to footer
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# # 5. Verify text 'SUBSCRIPTION'
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-3.col-sm-offset-1 h2').text == 'Subscription'.upper()
#
# # 6. Enter email address in input and click arrow button
# driver.find_element(By.ID, 'susbscribe_email').send_keys(randomEmail)
# driver.find_element(By.CSS_SELECTOR, '#subscribe').click()
#
# # 7. Verify success message 'You have been successfully subscribed!' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.alert-success.alert').text == 'You have been successfully subscribed!'
# driver.close()
#
# # Test Case 11: Verify Subscription in Cart page
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
# # 4. Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 5. Scroll down to footer
# driver.execute_script("scrollTo(0, document.body.scrollHeight);")
#
# # 5. Verify text 'SUBSCRIPTION'
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-3.col-sm-offset-1 h2').text == 'Subscription'.upper()
#
# # 6. Enter email address in input and click arrow button
# driver.find_element(By.ID, 'susbscribe_email').send_keys(randomEmail)
# driver.find_element(By.CSS_SELECTOR, '#subscribe').click()
#
# # 7. Verify success message 'You have been successfully subscribed!' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.alert-success.alert').text == 'You have been successfully subscribed!'
# driver.close()
#
#
# # Test Case 12: Add Products in Cart
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
# # 4. Click 'Products' button
# driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()
#
# # 5. Hover over first product and click 'Add to cart'
# actions = ActionChains(driver)
# first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
# actions.move_to_element(first_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
#
# # 6. Click 'Continue Shopping' button
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
#
# # 7. Hover over second product and click 'Add to cart'
# second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[1]
# actions.move_to_element(second_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[1].click()
# time.sleep(2)
#
# # 8. Click 'View Cart' button
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(2) a ').click()
#
# # 9. Verify both products are added to Cart
# added_products = driver.find_elements(By.CSS_SELECTOR, '.table.table-condensed tbody tr')
# number_of_products_add = len(added_products)
# print('Number of Items Added in the Cart is: ', number_of_products_add)
#
# # 10. Verify their prices, quantity and total price
# product_price = driver.find_elements(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(3) p')
# first_product_price = product_price[0].text.strip()
# assert first_product_price.__contains__('500'),f'Expected price 500, but got {first_product_price}'
# second_product_price = product_price[1].text.strip()
# assert second_product_price.__contains__('400'), f'Expected price 400, but got {second_product_price}'
# product_quantity = driver.find_elements(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(4) button')
# first_product_quantity = product_quantity[0].text.strip()
# assert first_product_quantity == '1'
# second_product_quantity = product_quantity[1].text.strip()
# assert second_product_quantity == '1'
# total_price = driver.find_elements(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(5) p')
# first_product_total_price = total_price[0].text.strip()
# assert first_product_total_price.__contains__('500'), f'Expected price 500, but got {first_product_total_price}'
# second_product_total_price = total_price[1].text.strip()
# assert second_product_total_price.__contains__('400'), f'Expected price 500, but got {second_product_total_price}'
# driver.close()
#
#
# # Test Case 13: Verify Product quantity in Cart
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
# # 4. Click 'View Product' for any product on home page
# driver.execute_script('window.scrollBy(0, 500);')
# driver.find_element(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper div[class="choose"] ul li a').click()
#
# # 5. Verify product detail is opened
# driver.find_element(By.CSS_SELECTOR, '.newarrival').is_displayed()
#
# # 6. Increase quantity to 4
# quantity = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div input:nth-child(3)')
# quantity.clear()
# quantity.send_keys('4')
#
# # 7. Click 'Add to cart' button
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.cart').click()
#
# # 8. Click 'View Cart' button
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(2) a').click()
#
# # 9. Verify that product is displayed in cart page with exact quantity
# assert driver.find_element(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(4) button').text.strip() == '4'
# driver.close()
#
#
# # Test Case 14: Place Order: Register while Checkout
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
# # 4. Add products to cart
# actions = ActionChains(driver)
# first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
# actions.move_to_element(first_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
# second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[1]
# actions.move_to_element(second_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[1].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
#
# # 5. Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 6. Verify that cart page is displayed
# assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'
#
# # 7. Click Proceed To Checkout
# driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()
#
# # 8. Click 'Register / Login' button
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(2) p a').click()
#
# # 9. Fill all details in Signup and create account
# driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
# driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(randomEmail)
# driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
# driver.find_element(By.CSS_SELECTOR, '#id_gender2').click()
# driver.find_element(By.CSS_SELECTOR, '#password').send_keys('QA@123')
# days = driver.find_element(By.CSS_SELECTOR, '#days')
# select_day = Select(days)
# select_day.select_by_index(28)
#
# month = driver.find_element(By.CSS_SELECTOR, '#months')
# select_month = Select(month)
# select_month.select_by_index(5)
#
# year = driver.find_element(By.CSS_SELECTOR, '#years')
# select_year = Select(year)
# select_year.select_by_value('1998')
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()
#
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()
#
# driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys("Trisha")
# driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys('Krishnan')
# driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys('Kollywood Film Industry')
# driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys('Chennai')
# driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys('TamilNadu')
# country = driver.find_element(By.CSS_SELECTOR, 'select#country')
# select_country = Select(country)
# select_country.select_by_visible_text('Singapore')
# driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys('Central Region')
# driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys('Marine Parade')
# driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys('449307')
# driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys('9876543210')
#
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()
#
# # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
# # 11. Verify 'Logged in as username' at top
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
#
# # 12.Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 13. Click 'Proceed To Checkout' button
# driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()
#
# # 14. Verify Address Details and Review Your Order
# assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Trisha')
# review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
# print('You\'re ordering: '+review_your_order.text)
#
# # 15. Enter description in comment text area and click 'Place Order'
# driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Nothing to Add, Please Proceed!')
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()
#
# # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
# fake = Faker()
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys('10')
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')
#
# # 17. Click 'Pay and Confirm Order' button
# driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()
#
# # 18. Verify success message 'Your order has been placed successfully!'
# # success_message = WebDriverWait(driver, 10).until(
# #     EC.visibility_of_element_located((By.CSS_SELECTOR, '#success_message div'))).text.strip()
# # assert success_message == 'Your order has been placed successfully!'
#
# # 19. Click 'Delete Account' button
# driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#
# # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
# driver.close()
#
#
# # Test Case 15: Place Order: Register before Checkout
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
# # 4. Click 'Signup / Login' button
# driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
#
# # 5. Fill all details in Signup and create account
# name = 'BatMan'
# driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
# driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(randomEmail)
# driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
# driver.find_element(By.CSS_SELECTOR, '#id_gender2').click()
# driver.find_element(By.CSS_SELECTOR, '#password').send_keys('QA@123')
# days = driver.find_element(By.CSS_SELECTOR, '#days')
# select_day = Select(days)
# select_day.select_by_index(28)
#
# month = driver.find_element(By.CSS_SELECTOR, '#months')
# select_month = Select(month)
# select_month.select_by_index(5)
#
# year = driver.find_element(By.CSS_SELECTOR, '#years')
# select_year = Select(year)
# select_year.select_by_value('1998')
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()
#
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()
#
# driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys("Trisha")
# driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys('Krishnan')
# driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys('Kollywood Film Industry')
# driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys('Chennai')
# driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys('TamilNadu')
# country = driver.find_element(By.CSS_SELECTOR, 'select#country')
# select_country = Select(country)
# select_country.select_by_visible_text('Singapore')
# driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys('Central Region')
# driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys('Marine Parade')
# driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys('449307')
# driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys('9876543210')
#
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()
#
# # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
# # 7. Verify ' Logged in as username' at top
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
#
# # 8. Add products to cart
# actions = ActionChains(driver)
# driver.execute_script("window.scrollBy(0, 500);")
# first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
# actions.move_to_element(first_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
# second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[1]
# actions.move_to_element(second_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[1].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
#
# # 9. Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 10. Verify that cart page is displayed
# assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'
#
# # 11. Click Proceed To Checkout
# driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()
#
# # 12. Verify Address Details and Review Your Order
# assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Trisha')
# review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
# print('You\'re ordering: '+review_your_order.text)
#
# # 13. Enter description in comment text area and click 'Place Order'
# driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Nothing to Add, Please Proceed!')
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()
#
# # 14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
# fake = Faker()
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys('10')
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')
#
# # 15. Click 'Pay and Confirm Order' button
# driver.execute_script("window.scrollBy(0,500);")
# driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()
#
# # 16. Verify success message 'Your order has been placed successfully!'
# # success_message_element = driver.find_element(By.CSS_SELECTOR, "div#success_message div")
# # # success_message = success_message_element.text
# # # expected_message = "Your payment has been successfully processed!"
# # assert success_message == expected_message, f"Expected message: '{expected_message}', but got: '{success_message}'"
#
#
# # 17. Click 'Delete Account' button
# driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#
# # 18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
# driver.close()

# # Test Case 16: Place Order: Login before Checkout
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
# # 4. Click 'Signup / Login' button
# driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
#
# # 5. Fill email, password and click 'Login' button
# name_1 = 'Ponugoti'
# driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Tulika.singh_20240803222313@yahoo.com')
# driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')
# driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
# time.sleep(2)
#
# # 6. Verify 'Logged in as username' at top
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name_1
#
# # 7. Add products to cart
# actions = ActionChains(driver)
# driver.execute_script("window.scrollBy(0, 500);")
# first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[2]
# actions.move_to_element(first_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[2].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
# driver.execute_script("window.scrollBy(0,500);")
# second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[3]
# actions.move_to_element(second_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[3].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
#
# # 8. Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 9. Verify that cart page is displayed
# assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'
#
# # 10. Click Proceed To Checkout
# driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()
#
# # 11. Verify Address Details and Review Your Order
# assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Sowmya')
# review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
# print('You\'re ordering: '+review_your_order.text)
#
# # 12. Enter description in comment text area and click 'Place Order'
# driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Nothing to Add, Please Proceed!')
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()
#
# # 13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
# fake = Faker()
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys('10')
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')
#
# # 14. Click 'Pay and Confirm Order' button
# driver.execute_script("window.scrollBy(0,500);")
# driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()
#
# # 15. Verify success message 'Your order has been placed successfully!'
# # success_message_element = driver.find_element(By.CSS_SELECTOR, "div#success_message div")
# # success_message = success_message_element.text
# # expected_message = "Your payment has been successfully processed!"
# # assert success_message == expected_message, f"Expected message: '{expected_message}', but got: '{success_message}'"
#
#
# # Test Case 17: Remove Products From Cart
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
# # 4. Add products to cart
# actions = ActionChains(driver)
# driver.execute_script("window.scrollBy(0, 1000);")
# first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[4]
# actions.move_to_element(first_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[4].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
# second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[5]
# actions.move_to_element(second_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[5].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
#
# # 5. Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 6. Verify that cart page is displayed
# assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'
#
# # 7. Click 'X' button corresponding to particular product
# delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".cart_quantity_delete")
# for button in delete_buttons:
#     button.click()
#     time.sleep(1)
#
# # 8. Verify that product is removed from the cart
# assert driver.find_element(By.CSS_SELECTOR, 'span#empty_cart p b').text.__contains__('Cart is empty!')
# driver.close()


# # Test Case 18: View Category Products
#
# # 1. Launch browser
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# # 2. Navigate to url 'http://automationexercise.com'
# driver.get('https://www.automationexercise.com/')
#
# # 3. Verify that categories are visible on left sidebar
# driver.execute_script("window.scrollBy(0,500);")
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-3 div.left-sidebar h2').text == 'Category'.upper()
#
# # 4. Click on 'Women' category
# driver.find_element(By.CSS_SELECTOR, 'h4.panel-title a').click()
#
# # 5. Click on any category link under 'Women' category, for example: Dress
# women_categories = driver.find_elements(By.XPATH, '//*[@id="Women"]/div/ul/li/a')
# category_texts = [driver.execute_script("return arguments[0].textContent;", category).strip() for category in women_categories]
# random_options = random.choice(category_texts)
# for category in women_categories:
#     driver.execute_script("arguments[0].scrollIntoView(true);", category)
#     text = driver.execute_script("return arguments[0].textContent;", category).strip()
#     if text == random_options:
#         category.click()
#         break
#
# # 6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
# product_title = driver.find_element(By.CSS_SELECTOR, '.title.text-center').text
# assert "Women - "+random_options+" Products"
#
# # 7. On left sidebar, click on any sub-category link of 'Men' category
# driver.find_elements(By.CSS_SELECTOR, 'h4.panel-title a')[1].click()
# men_categories = driver.find_elements(By.XPATH, '//*[@id="Men"]/div/ul/li/a')
# category_texts = [driver.execute_script("return arguments[0].textContent;", category).strip() for category in men_categories]
# random_options = random.choice(category_texts)
# for category in men_categories:
#     driver.execute_script("arguments[0].scrollIntoView(true);", category)
#     text = driver.execute_script("return arguments[0].textContent;", category).strip()
#     if text == random_options:
#         category.click()
#         break
#
# # 8. Verify that user is navigated to that category page
# product_title = driver.find_element(By.CSS_SELECTOR, '.title.text-center').text
# assert "Men - "+random_options+" Products"
# driver.close()

# # Test Case 19: View & Cart Brand Products
#
# # 1. Launch browser
# driver = webdriver.Edge()
# driver.maximize_window()
#
# # 2. Navigate to url 'http://automationexercise.com'
# driver.get('https://www.automationexercise.com/')
#
# # 3. Click on 'Products' button
# driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()
#
# # 4. Verify that Brands are visible on left sidebar
# driver.execute_script("window.scrollBy(0, 500);")
# assert driver.find_element(By.CSS_SELECTOR, '.brands_products h2').text == 'Brands'.upper()
#
# # 5. Click on any brand name
# brand_names = driver.find_elements(By.CSS_SELECTOR, '.brands-name ul li a')
# select_brand_name = [driver.execute_script("return arguments[0].textContent;", brand).strip() for brand in brand_names]
# random_brand_selection = random.choice(select_brand_name)
# print('1st Brand: ', format(random_brand_selection))
# for brand in brand_names:
#     driver.execute_script("arguments[0].scrollIntoView(true);", brand)
#     text = driver.execute_script("return arguments[0].textContent;", brand).strip()
#     if text == random_brand_selection:
#         brand.click()
#         break
#
# # 6. Verify that user is navigated to brand page and brand products are displayed
# product_title = driver.find_element(By.CSS_SELECTOR, '.title.text-center').text
# assert "Brand - "+random_brand_selection+" Products"
# match = re.search(r'\((\d+)\)', random_brand_selection)
# if match:
#     displayed_count = int(match.group(1))
#     print(f'Displayed Product Count: {displayed_count}')
# else:
#     print('Product count not found in the brand name text.')
#     displayed_count = None
#
# # 7. On left sidebar, click on any other brand link
# brand_names_2 = driver.find_elements(By.CSS_SELECTOR, '.brands-name ul li a')
# select_brand_name_2 = [driver.execute_script("return arguments[0].textContent;", brand).strip() for brand in brand_names_2]
# random_brand_selection_2 = random.choice(select_brand_name_2)
# print('2nd Brand: ', format(random_brand_selection_2))
# for brand_2 in brand_names_2:
#     driver.execute_script("arguments[0].scrollIntoView(true);", brand_2)
#     text = driver.execute_script("return arguments[0].textContent;", brand_2).strip()
#     if text != random_brand_selection:
#         brand_2.click()
#         break
#
# # 8. Verify that user is navigated to that brand page and can see products
# product_title_2 = driver.find_element(By.CSS_SELECTOR, '.title.text-center').text
# assert "Brand - "+random_brand_selection_2+" Products"
# driver.close()

# # Test Case 20: Search Products and Verify Cart After Login
#
# # 1. Launch browser
# driver = webdriver.Edge()
# driver.maximize_window()
#
# # 2. Navigate to url 'http://automationexercise.com'
# driver.get('https://www.automationexercise.com/')
#
# # 3. Click on 'Products' button
# driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()
#
# # 4. Verify user is navigated to ALL PRODUCTS page successfully
# assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'All Products'.upper()
#
# # 5. Enter product name in search input and click search button
# all_products = driver.find_elements(By.CSS_SELECTOR, '.single-products div.productinfo p')
# product_text = [driver.execute_script("return arguments[0].textContent;", product).strip() for product in all_products]
# random_product_text = random.choice(product_text)
# driver.find_element(By.CSS_SELECTOR, 'input#search_product').send_keys(random_product_text)
# driver.find_element(By.CSS_SELECTOR, 'button#submit_search').click()
#
# # 6. Verify 'SEARCHED PRODUCTS' is visible
# assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'Searched Products'.upper()
#
# # 7. Verify all the products related to search are visible
# time.sleep(1.5)
# searchedProduct = driver.find_element(By.CSS_SELECTOR, '.productinfo.text-center p')
# # searchedProduct.is_displayed()
# assert searchedProduct.text == random_product_text, f'random Product:{random_product_text},{searchedProduct}'
#
# # 8. Add those products to cart
# actions = ActionChains(driver)
# first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
# actions.move_to_element(first_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
# time.sleep(1.5)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
#
# # 9. Click 'Cart' button and verify that products are visible in cart
# driver.find_element(By.LINK_TEXT, 'Cart').click()
# added_products = driver.find_element(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(2) h4').text
# assert random_product_text in added_products
#
# # 10. Click 'Signup / Login' button and submit login details
# driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
# driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Tulika.singh_20240803222313@yahoo.com')
# driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')
# driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
#
# # 11. Again, go to Cart page
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 12. Verify that those products are visible in cart after login as well
# assert driver.find_element(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(2) h4').text == random_product_text
# driver.close()

# # Test Case 21: Add review on product
#
# # 1. Launch browser
# driver = webdriver.Edge()
# driver.maximize_window()
#
# # 2. Navigate to url 'http://automationexercise.com'
# driver.get('https://www.automationexercise.com/')
#
# # 3. Click on 'Products' button
# driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()
#
# # 4. Verify user is navigated to ALL PRODUCTS page successfully
# assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'All Products'.upper()
#
# # 5. Click on 'View Product' button
# driver.execute_script("window.scrollTo(0, 500);")
# driver.find_element(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper div[class="choose"] ul li a').click()
#
# # 6. Verify 'Write Your Review' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-12 ul li a').text == 'Write Your Review'.upper()
#
# # 7. Enter name, email and review
# driver.find_element(By.CSS_SELECTOR, '#name').send_keys(fake.name_male())
# driver.find_element(By.CSS_SELECTOR,'#email').send_keys(fake.email())
# driver.find_element(By.CSS_SELECTOR, '#review').send_keys(fake.text(100))
#
# # 8. Click 'Submit' button
# driver.execute_script("window.scrollTo(0, 500);")
# driver.find_element(By.CSS_SELECTOR, '#button-review').click()
#
# # 9. Verify success message 'Thank you for your review.'
# assert driver.find_element(By.CSS_SELECTOR, '.alert-success.alert span').text == 'Thank you for your review.'
#

# # Test Case 22: Add to cart from Recommended items
#
# # 1. Launch browser
# driver = webdriver.Edge()
# driver.maximize_window()
#
# # 2. Navigate to url 'http://automationexercise.com'
# driver.get('https://www.automationexercise.com/')
#
# # 3. Scroll to bottom of page
# recommended_items = driver.find_elements(By.CSS_SELECTOR, '.title.text-center')
# if len(recommended_items) > 1:
#     recommended_item = recommended_items[1]
#     driver.execute_script("arguments[0].scrollIntoView(true);", recommended_item)
#     recommended_item_text = recommended_item.text
#
# # 4. Verify 'RECOMMENDED ITEMS' are visible
#     assert recommended_item_text == 'recommended items'.upper()
#
# # 5. Click on 'Add To Cart' on Recommended product
# recommended_products = driver.find_elements(By.XPATH, '//*[@id="recommended-item-carousel"]/div/div/div/div/div/div/p')
# if recommended_products:
#     random_product_index = random.randint(0, len(recommended_products) - 1)
#     selected_product = recommended_products[random_product_index]
#     selected_product_name = selected_product.text
#     add_to_cart_button = WebDriverWait(selected_product, 10).until(EC.element_to_be_clickable((By.XPATH, './following-sibling::a/i')))
#     add_to_cart_button.click()
#
# # 6. Click on 'View Cart' button
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-content div:nth-child(2) a'))).click()
#
# # 7. Verify that product is displayed in cart page
# assert driver.find_element(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(2) h4').text == selected_product_name
# driver.close()
#
# # Test Case 23: Verify address details in checkout page
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
# # 4. Click 'Signup / Login' button
# driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
#
# # 5. Fill all details in Signup and create account
# driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
# driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(randomEmail)
# driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
# driver.find_element(By.CSS_SELECTOR, '#id_gender2').click()
# driver.find_element(By.CSS_SELECTOR, '#password').send_keys('QA@123')
# days = driver.find_element(By.CSS_SELECTOR, '#days')
# select_day = Select(days)
# select_day.select_by_index(28)
#
# month = driver.find_element(By.CSS_SELECTOR, '#months')
# select_month = Select(month)
# select_month.select_by_index(5)
#
# year = driver.find_element(By.CSS_SELECTOR, '#years')
# select_year = Select(year)
# select_year.select_by_value('1998')
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()
#
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()
#
# driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys("Trisha")
# driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys('Krishnan')
# driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys('Kollywood Film Industry')
# driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys('Chennai')
# driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys('TamilNadu')
# country = driver.find_element(By.CSS_SELECTOR, 'select#country')
# select_country = Select(country)
# select_country.select_by_visible_text('Singapore')
# driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys('Central Region')
# driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys('Marine Parade')
# driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys('449307')
# driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys('9876543210')
#
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()
#
# # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
# # 7. Verify ' Logged in as username' at top
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
#
# # 8. Add products to cart
# actions = ActionChains(driver)
# first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
# actions.move_to_element(first_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
# second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[1]
# actions.move_to_element(second_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[1].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
#
# # 9. Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 10. Verify that cart page is displayed
# assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'
#
# # 11. Click Proceed To Checkout
# driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()
#
# # 12. Verify that the delivery address is same address filled at the time registration of account
# assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Trisha')
#
# # 13. Verify that the billing address is same address filled at the time registration of account
# assert driver.find_elements(By.CSS_SELECTOR, 'li.address_firstname.address_lastname')[1].text.__contains__('Trisha')
#
# # 14. Click 'Delete Account' button
# driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#
# # 15. Verify 'ACCOUNT DELETED!' and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
# driver.close()
#
#
# # Test Case 24: Download Invoice after purchase order
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
# # 4. Add products to cart
# actions = ActionChains(driver)
# driver.execute_script("window.scrollBy(0, 500);")
# first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
# actions.move_to_element(first_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
# second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[1]
# actions.move_to_element(second_product).perform()
# driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[1].click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
#
# # 5. Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 6. Verify that cart page is displayed
# assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'
#
# # 7. Click Proceed To Checkout
# driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()
#
# # 8. Click 'Register / Login' button
# driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(2) p a').click()
#
# # 9. Fill all details in Signup and create account
# driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
# driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(randomEmail)
# driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
# driver.find_element(By.CSS_SELECTOR, '#id_gender2').click()
# driver.find_element(By.CSS_SELECTOR, '#password').send_keys('QA@123')
# days = driver.find_element(By.CSS_SELECTOR, '#days')
# select_day = Select(days)
# select_day.select_by_index(28)
#
# month = driver.find_element(By.CSS_SELECTOR, '#months')
# select_month = Select(month)
# select_month.select_by_index(5)
#
# year = driver.find_element(By.CSS_SELECTOR, '#years')
# select_year = Select(year)
# select_year.select_by_value('1998')
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()
#
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()
#
# driver.find_element(By.CSS_SELECTOR, 'input#first_name').send_keys("Trisha")
# driver.find_element(By.CSS_SELECTOR, 'input#last_name').send_keys('Krishnan')
# driver.find_element(By.CSS_SELECTOR, 'input#company').send_keys('Kollywood Film Industry')
# driver.find_element(By.CSS_SELECTOR, 'input#address1').send_keys('Chennai')
# driver.find_element(By.CSS_SELECTOR, 'input#address2').send_keys('TamilNadu')
# country = driver.find_element(By.CSS_SELECTOR, 'select#country')
# select_country = Select(country)
# select_country.select_by_visible_text('Singapore')
# driver.find_element(By.CSS_SELECTOR, 'input#state').send_keys('Central Region')
# driver.find_element(By.CSS_SELECTOR, 'input#city').send_keys('Marine Parade')
# driver.find_element(By.CSS_SELECTOR, 'input#zipcode').send_keys('449307')
# driver.find_element(By.CSS_SELECTOR, 'input#mobile_number').send_keys('9876543210')
#
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()
#
# # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
# # 11. Verify ' Logged in as username' at top
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
#
# # 12. Click 'Cart' button
# driver.find_element(By.LINK_TEXT, 'Cart').click()
#
# # 13. Click 'Proceed To Checkout' button
# driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()
#
# # 14. Verify Address Details and Review Your Order
# assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Trisha')
# review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
# print('You\'re ordering: '+review_your_order.text)
#
# # 15. Enter description in comment text area and click 'Place Order'
# driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Nothing to Add, Please Proceed!')
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()
#
# # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys('10')
# driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')
#
# # 17. Click 'Pay and Confirm Order' button
# driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()
#
# # 18. Verify success message 'Your order has been placed successfully!'
# # success_message = WebDriverWait(driver, 10).until(
# #     EC.visibility_of_element_located((By.CSS_SELECTOR, '#success_message div'))).text.strip()
# # assert success_message == 'Your order has been placed successfully!'
#
# # 19. Click 'Download Invoice' button and verify invoice is downloaded successfully.
# driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 a:nth-child(3)').click()
#
# # 20. Click 'Continue' button
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
# # 21. Click 'Delete Account' button
# driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#
# # 22. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
# driver.close()
#
#
# # Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
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
# # 4. Scroll down page to bottom
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# # 5. Verify 'SUBSCRIPTION' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-3.col-sm-offset-1 h2').text == 'Subscription'.upper()
#
# # 6. Click on arrow at bottom right side to move upward
# driver.find_element(By.CSS_SELECTOR, '#scrollUp').click()
#
# # 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-6 h2').text == 'Full-Fledged practice website for Automation Engineers'
# driver.close()
#
#
# # Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality
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
# # 4. Scroll down page to bottom
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#
# # 5. Verify 'SUBSCRIPTION' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-3.col-sm-offset-1 h2').text == 'Subscription'.upper()
#
# # 6. Scroll up page to top
# driver.execute_script("window.scrollTo(0, 0);")
#
# # 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-6 h2').text == 'Full-Fledged practice website for Automation Engineers'
# driver.close()

