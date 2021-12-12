import time
from resources import ui_test_class
from resources.page_objects.biweekly_page import BIWEEKLY
from resources.page_objects.biweekly_page import BiWeekly

class TesBIWEEKLYORDER(ui_test_class.UVXVXVIVClass):
    biweekly_page: BIWEEKLY
    biweekly_page: BiWeekly

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    actual4 = "5"

    @classmethod
    def setUpClass(cls):
        super(TesBIWEEKLYORDER, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesBIWEEKLYORDER, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.biweekly_page.zip("60611")
        self.biweekly_page.submit_zip()
        search = self.biweekly_page.get_attribute(BiWeekly.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.biweekly_page.select_dropdown()
        self.biweekly_page.click_signin()
        self.biweekly_page.EnterEmail("testaccount@quicklly.com")
        self.biweekly_page.EnterPass("123456")
        self.biweekly_page.click_login()
        self.biweekly_page.select_dropdown()
        logoutLabel = self.biweekly_page.get_attribute(BiWeekly.logout, 'innerHTML')
        print(logoutLabel)
        self.assertEqual(self.actual2, logoutLabel)

    def test_biWeeklyOrder(self):
        time.sleep(2)
        self.biweekly_page.click_NationWideShop()
        self.biweekly_page.click_indianSweet()
        self.biweekly_page.click_biweekly()
        self.biweekly_page.click_buildABox()
        self.biweekly_page.click_addMasalaMathai()
        for i in range(4):
            self.biweekly_page.click_plusMasalaMathai()
        quantityLabel = self.biweekly_page.get_attribute(BiWeekly.quantity, 'innerHTML')
        print(quantityLabel)
        self.assertEqual(self.actual4, quantityLabel)

    def test_biWeeklyOrderCheckout(self):
        self.biweekly_page.click_addToCartMasala()
        time.sleep(2)
        self.biweekly_page.click_Cart()
        self.biweekly_page.click_Checkout()
        self.biweekly_page.click_Checkout2()
        self.biweekly_page.click_payment1()
        time.sleep(5)
        self.biweekly_page.click_Pay()
        ThankYouLabel = self.biweekly_page.get_attribute(BiWeekly.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)