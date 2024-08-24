import random

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_view_products_under_category():

    # 1. Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that categories are visible on left sidebar
    driver.execute_script("window.scrollBy(0,500);")
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-3 div.left-sidebar h2').text == 'Category'.upper()

    # 4. Click on 'Women' category
    driver.find_element(By.CSS_SELECTOR, 'h4.panel-title a').click()

    # 5. Click on any category link under 'Women' category, for example: Dress
    women_categories = driver.find_elements(By.XPATH, '//*[@id="Women"]/div/ul/li/a')
    category_texts = [driver.execute_script("return arguments[0].textContent;", category).strip() for category in women_categories]
    random_options = random.choice(category_texts)
    for category in women_categories:
        driver.execute_script("arguments[0].scrollIntoView(true);", category)
        text = driver.execute_script("return arguments[0].textContent;", category).strip()
        if text == random_options:
            category.click()
            break

    # 6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
    product_title = driver.find_element(By.CSS_SELECTOR, '.title.text-center').text
    assert "Women - "+random_options+" Products"

    # 7. On left sidebar, click on any sub-category link of 'Men' category
    driver.find_elements(By.CSS_SELECTOR, 'h4.panel-title a')[1].click()
    men_categories = driver.find_elements(By.XPATH, '//*[@id="Men"]/div/ul/li/a')
    category_texts = [driver.execute_script("return arguments[0].textContent;", category).strip() for category in men_categories]
    random_options = random.choice(category_texts)
    for category in men_categories:
        driver.execute_script("arguments[0].scrollIntoView(true);", category)
        text = driver.execute_script("return arguments[0].textContent;", category).strip()
        if text == random_options:
            category.click()
            break

    # 8. Verify that user is navigated to that category page
    product_title = driver.find_element(By.CSS_SELECTOR, '.title.text-center').text
    assert "Men - "+random_options+" Products"
    driver.close()