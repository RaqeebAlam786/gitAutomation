from resources.config_methods import DataClass
from resources.locators import Weekly
from resources.page_objects.base_page import BasePage

class WEEKLY(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(Weekly.enter_zip).clear()
        self.find_element(Weekly.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Weekly.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_NationWideShop(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(5) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianSweet(self):
        self.click(Weekly.indianSweet)

    def click_buildABox(self):
        self.click(Weekly.buildAbox)

    def click_addMasalaMathai(self):
        self.click(Weekly.addMasalaMathai)

    def click_plusMasalaMathai(self):
        self.click(Weekly.plusMasalaMathai)

    def click_addToCartMasala(self):
        self.click(Weekly.AddToCart)

    def click_Cart(self):
        self.click(Weekly.Cart)

    def click_Checkout(self):
        self.click(Weekly.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(Weekly.Pay)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(Weekly.Email).clear()
        self.find_element(Weekly.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Weekly.Pass).clear()
        self.find_element(Weekly.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        self.click(Weekly.weekly)
