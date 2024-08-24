import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_Add_to_cart_from_recommendations():
    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Scroll to bottom of page
    recommended_items = driver.find_elements(By.CSS_SELECTOR, '.title.text-center')
    if len(recommended_items) > 1:
        recommended_item = recommended_items[1]
        driver.execute_script("arguments[0].scrollIntoView(true);", recommended_item)
        recommended_item_text = recommended_item.text

    # 4. Verify 'RECOMMENDED ITEMS' are visible
        assert recommended_item_text == 'recommended items'.upper()

    # 5. Click on 'Add To Cart' on Recommended product
    recommended_products = driver.find_elements(By.XPATH, '//*[@id="recommended-item-carousel"]/div/div/div/div/div/div/p')
    if recommended_products:
        random_product_index = random.randint(0, len(recommended_products) - 1)
        selected_product = recommended_products[random_product_index]
        selected_product_name = selected_product.text
        add_to_cart_button = WebDriverWait(selected_product, 10).until(EC.element_to_be_clickable((By.XPATH, './following-sibling::a/i')))
        add_to_cart_button.click()

    # 6. Click on 'View Cart' button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-content div:nth-child(2) a'))).click()

    # 7. Verify that product is displayed in cart page
    assert driver.find_element(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(2) h4').text == selected_product_name
    driver.close()