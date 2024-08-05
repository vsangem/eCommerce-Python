import os.path
import time
from datetime import datetime


from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# # Test Case 1: Register User
#
# driver = webdriver.Edge()
# driver.maximize_window()
# driver.get('https://www.automationexercise.com/')
# homepage = driver.find_element(By.XPATH, '//h1').text
#
# # 3. Verify that home page is visible successfully
# assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'
#
# # 4. Click on 'Signup / Login' button
# driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
#
# # 5. Verify 'New User Signup!' is visible
# newUserSignup = driver.find_element(By.CSS_SELECTOR,'.signup-form h2').text
# assert 'New User Signup!' in newUserSignup
#
#
# 6. Enter name and email address
def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f'{"Tulika"}.{"singh"}_{time_stamp}@yahoo.com'


randomEmail = generate_email_with_timestamp()

name = 'Tulika Singh'
# driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
# driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(randomEmail)
#
# # 7. Click 'Signup' button
# driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
#
# # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# signup = driver.find_element(By.XPATH, '//h2').text.title()
# assert 'Enter Account Information' in signup, f'Sign up Text has been changed Text:{signup}'
#
# # 9. Fill details: Title, Name, Email, Password, Date of birth
# driver.find_element(By.CSS_SELECTOR, '#id_gender2').click()
# assert driver.find_element(By.CSS_SELECTOR, '#email').get_property('value') == randomEmail
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
# # 10. Select checkbox 'Sign up for our newsletter!'
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#newsletter').click()
#
# # 11. Select checkbox 'Receive special offers from our partners!'
# driver.find_element(By.CSS_SELECTOR, '.checkbox div span input#optin').click()
#
# # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
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
# # 13. Click 'Create Account button'
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()
# print(randomEmail)
#
# # 14. Verify that 'ACCOUNT CREATED!' is visible
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Created!'.upper()
#
# # 15. Click 'Continue' button
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
# # 16. Verify that 'Logged in as username' is visible
# assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
#
# # 17. Click 'Delete Account' button
# driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#
# # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
# driver.close()
#
#
# # # Test Case 2: Login User with correct email and password
# #
# # # 1. Launch browser
# # driver = webdriver.Edge()
# # driver.maximize_window()
# #
# # # 2. Navigate to url 'http://automationexercise.com'
# # driver.get('https://www.automationexercise.com/')
# #
# # # 3. Verify that home page is visible successfully
# # homepage = driver.find_element(By.XPATH, '//h1').text
# # assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'
# #
# # # 4. Click on 'Signup / Login' button
# # driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
# #
# # # 5. Verify 'Login to your account' is visible
# # loginUser = driver.find_element(By.CSS_SELECTOR,'.login-form h2').text
# # assert 'Login to your account' in loginUser
# #
# # # 6. Enter correct email address and password
# # driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Tulika.singh_20240803222313@yahoo.com')
# # driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')
# #
# # # 7. Click 'login' button
# # driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
# # time.sleep(2)
# #
# # # 8. Verify that 'Logged in as username' is visible
# # # name = 'Tulika Singh'
# # assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name
# #
# # # 9. Click 'Delete Account' button
# # driver.find_element(By.LINK_TEXT, 'Delete Account').click()
# #
# # # 10. Verify that 'ACCOUNT DELETED!' is visible
# # assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
# # driver.close()
#
#
# # Test Case 3: Login User with incorrect email and password
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
# # 6. Enter incorrect email address and password
# driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys(randomEmail)
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
# assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Test Cases'.upper()
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


# Test Case 14: Place Order: Register while Checkout

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
name = 'BatMan'
driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(randomEmail)
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

# 11. Verify 'Logged in as username' at top
assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name

# 12.Click 'Cart' button
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
fake = Faker()
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys('10')
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')

# 17. Click 'Pay and Confirm Order' button
driver.execute_script("window.scrollBy(0,500);")
driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()

# 18. Verify success message 'Your order has been placed successfully!'
# success_message_element = driver.find_element(By.CSS_SELECTOR, "div#success_message div")
# success_message = success_message_element.text
# expected_message = "Your payment has been successfully processed!"
# assert success_message == expected_message, f"Expected message: '{expected_message}', but got: '{success_message}'"

# 19. Click 'Delete Account' button
driver.find_element(By.LINK_TEXT, 'Delete Account').click()

# 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
driver.close()


# Test Case 15: Place Order: Register before Checkout

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
name = 'BatMan'
driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(name)
driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(randomEmail)
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
assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name

# 8. Add products to cart
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

# 9. Click 'Cart' button
driver.find_element(By.LINK_TEXT, 'Cart').click()

# 10. Verify that cart page is displayed
assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'

# 11. Click Proceed To Checkout
driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()

# 12. Verify Address Details and Review Your Order
assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Trisha')
review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
print('You\'re ordering: '+review_your_order.text)

# 13. Enter description in comment text area and click 'Place Order'
driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Nothing to Add, Please Proceed!')
driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()

# 14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
fake = Faker()
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys('10')
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')

# 15. Click 'Pay and Confirm Order' button
driver.execute_script("window.scrollBy(0,500);")
driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()

# 16. Verify success message 'Your order has been placed successfully!'
# success_message_element = driver.find_element(By.CSS_SELECTOR, "div#success_message div")
# # success_message = success_message_element.text
# # expected_message = "Your payment has been successfully processed!"
# # assert success_message == expected_message, f"Expected message: '{expected_message}', but got: '{success_message}'"

# 17. Click 'Delete Account' button
driver.find_element(By.LINK_TEXT, 'Delete Account').click()

# 18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
driver.close()


# Test Case 16: Place Order: Login before Checkout

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

# 5. Fill email, password and click 'Login' button
name = 'Tulika'
driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Tulika.singh_20240803222313@yahoo.com')
driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')
driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
time.sleep(2)

# 6. Verify 'Logged in as username' at top
assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name

# 7. Add products to cart
actions = ActionChains(driver)
driver.execute_script("window.scrollBy(0, 500);")
first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[2]
actions.move_to_element(first_product).perform()
driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[2].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[3]
actions.move_to_element(second_product).perform()
driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[3].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()

# 8. Click 'Cart' button
driver.find_element(By.LINK_TEXT, 'Cart').click()

# 9. Verify that cart page is displayed
assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'

# 10. Click Proceed To Checkout
driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()

# 11. Verify Address Details and Review Your Order
assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__('Tulika')
review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
print('You\'re ordering: '+review_your_order.text)

# 12. Enter description in comment text area and click 'Place Order'
driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Nothing to Add, Please Proceed!')
driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()

# 13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
fake = Faker()
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(fake.name_male())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys('10')
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')

# 14. Click 'Pay and Confirm Order' button
driver.execute_script("window.scrollBy(0,500);")
driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()

# 15. Verify success message 'Your order has been placed successfully!'
# success_message_element = driver.find_element(By.CSS_SELECTOR, "div#success_message div")
# success_message = success_message_element.text
# expected_message = "Your payment has been successfully processed!"
# assert success_message == expected_message, f"Expected message: '{expected_message}', but got: '{success_message}'"

# 16. Click 'Delete Account' button
driver.find_element(By.LINK_TEXT, 'Delete Account').click()

# 17. Verify 'ACCOUNT DELETED!' and click 'Continue' button
assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
driver.close()



































