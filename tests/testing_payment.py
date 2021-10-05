import time
from resources import ui_test_class
from resources.page_objects.payment import Payment
from resources.page_objects.payment import Pay


class TesPAYMENT(ui_test_class.UVXVIIClass):
    payment_page: Pay
    payment_page: Payment

    actual1 = "Thank you"
    actual2 = "Your account"
    actual3 = "Search for products..."
    actual4 = "Add Payment Method"
    actual5 = "Use saved payment method"
    expected_res = "Card Number"
    expected_res1 = "Expiration Date"
    expected_res2 = "CVV"
    mp = {}

    @classmethod
    def setUpClass(cls):
        super(TesPAYMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesPAYMENT, cls).tearDownClass()
        cls.driver.quit()

    def compare_placeholders(self):

        cardNumber_placeholder = self.payment_page.get_attribute(Payment.cardNumber, 'placeholder')
        expiry_placeholder = self.payment_page.get_attribute(Payment.expiry, 'placeholder')
        Cvv_placeholder = self.payment_page.get_attribute(Payment.CVV, 'placeholder')

        if self.expected_res == cardNumber_placeholder:
            self.mp['Card Number'] = True

        else:
            self.mp['Card Number'] = False

        if self.expected_res1 == expiry_placeholder:
            self.mp['Expiration Date'] = True

        else:
            self.mp['Expiration Date'] = False

        if self.expected_res2 == Cvv_placeholder:
            self.mp['CVV'] = True

        else:
            self.mp['CVV'] = False

        print(self.mp)

    def test_EnterZipCode(self):
        self.payment_page.zip("60611")
        self.payment_page.submit_zip()
        search = self.payment_page.get_attribute(Payment.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIN(self):
        self.payment_page.select_dropdown()
        self.payment_page.click_signin()
        self.payment_page.EnterEmail("testaccount@quicklly.com")
        self.payment_page.EnterPass("123456")
        self.payment_page.click_login()
        AccountLabel = self.payment_page.get_attribute(Payment.Account, 'innerHTML')
        print(AccountLabel)
        self.assertEqual(self.actual2, AccountLabel)

    def test_additem(self):
        time.sleep(2)
        self.payment_page.click_fresh()
        self.payment_page.click_additem()
        self.payment_page.click_ADDLG()
        time.sleep(5)
        self.payment_page.click_MiniCart1()
        self.payment_page.click_Checkout()
        self.payment_page.click_Checkout2()

    def test_clickPayment(self):
        self.payment_page.click_payment1()

    def test_paymentMethod(self):
        self.payment_page.click_paymentMethod()
        # self.payment_page.label()
        # AddPaymentLabel = self.payment_page.get_attribute(Payment.AddMethod, 'innerHTML')
        # print(AddPaymentLabel)
        # self.assertEqual(self.actual4, AddPaymentLabel)
        time.sleep(10)

    def test_paymentMethodAddingLink(self):
        self.payment_page.click_AddPaymentMethod()
        time.sleep(15)
        SavePaymentLabel = self.payment_page.get_attribute(Payment.savePaymentMethod, 'innerHTML')
        print(SavePaymentLabel)
        self.assertEqual(self.actual5, SavePaymentLabel)
        time.sleep(10)


    def test_paymentMethodDetails1(self):
        self.payment_page.EnterCardNumber("5555444433331111")
        self.payment_page.EnterExpiry("0225")
        self.payment_page.EnterCVV("158")
        time.sleep(10)

    def test_paymentMethodDetails(self):
        self.compare_placeholders()

    def test_paymentMethodPay(self):
        self.payment_page.click_AddMethod()
        self.payment_page.click_Pay()
        time.sleep(15)