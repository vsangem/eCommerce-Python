from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker


fake = Faker()


def test_add_review_to_a_product():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Click on 'Products' button
    driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()

    # 4. Verify user is navigated to ALL PRODUCTS page successfully
    assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'All Products'.upper()

    # 5. Click on 'View Product' button
    driver.execute_script("window.scrollTo(0, 500);")
    driver.find_element(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper div[class="choose"] ul li a').click()

    # 6. Verify 'Write Your Review' is visible
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-12 ul li a').text == 'Write Your Review'.upper()

    # 7. Enter name, email and review
    driver.find_element(By.CSS_SELECTOR, '#name').send_keys(fake.name_male())
    driver.find_element(By.CSS_SELECTOR,'#email').send_keys(fake.email())
    driver.find_element(By.CSS_SELECTOR, '#review').send_keys(fake.text(100))

    # 8. Click 'Submit' button
    driver.execute_script("window.scrollTo(0, 500);")
    driver.find_element(By.CSS_SELECTOR, '#button-review').click()

    # 9. Verify success message 'Thank you for your review.'
    assert driver.find_element(By.CSS_SELECTOR, '.alert-success.alert span').text == 'Thank you for your review.'
