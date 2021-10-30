from resources.config_methods import DataClass
from resources.locators import Category
from resources.page_objects.base_page import BasePage


class GroceryCategories(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def EnterZip(self, zipcode):
        self.find_elements(Category.enter_zip).clear()
        self.find_element(Category.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Category.submit_zip)

    def click_unbeatable(self):
        self.click(Category.UnbeatableDeals)

    def click_GoFresh(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[7]/div[1]/div/div/a[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Category.GoFresh)

    def click_Grocery(self):
        self.click(Category.Grocery)

    def click_Meat(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[7]/div[1]/div/div/a[4]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Beverages(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsGroceryCats > div.clsSliderCats.slick-initialized.slick-slider > div > div > a:nth-child(5) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Organic(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[7]/div[1]/div/div/a[6]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_personalCare(self):
        element = self.driver.find_element_by_css_selector('#searchhide > div.grocerySpecialSlider.clsGroceryCats > div.clsSliderCats.slick-initialized.slick-slider > div > div > a:nth-child(7) > img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Category.PersonalCare)

    def click_Household(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[7]/div[1]/div/div/a[8]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[7]/div[2]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Category.weeklyDeals)
