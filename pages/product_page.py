from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
     def add_product_to_basket(self):
         selected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
         selected_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
     
         ## add product to basket
         self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        
         ## get code
         self.solve_quiz_and_get_code()

         ## check basket
         added_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
         assert selected_product_name == added_product_name, "Added product name is not equal selected product name"

         added_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
         assert selected_product_price == added_product_price, "Added product price is not equal selected product price"

     def add_product_to_basket_without_code(self):
         selected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
         selected_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
     
         ## add product to basket
         self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        
         ## check basket
         added_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
         assert selected_product_name == added_product_name, "Added product name is not equal selected product name"

         added_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
         assert selected_product_price == added_product_price, "Added product price is not equal selected product price"

     def should_not_be_success_message(self):
         assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
             "Success message is presented, but should not be"

     def should_success_message_disappeared(self):
         assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
             "Success message should disappear"
