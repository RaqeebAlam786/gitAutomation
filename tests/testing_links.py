# import time
from resources import ui_test_class
from resources.page_objects.link import Links
from resources.page_objects.link import ContactUsLinks


class TesLINKS(ui_test_class.UVXIVClass):
    link_page: Links
    link_page: ContactUsLinks

    expected = "Facebook"
    expected1 = "https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png"
    expected2 = "Sign up for free to get more"
    expected3 = "Tweets"
    expected4 = "16 subscribers"
    expected5 = "Quicklly's best boards"

    @classmethod
    def setUpClass(cls):
        super(TesLINKS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesLINKS, cls).tearDownClass()
        cls.driver.quit()

    def test_facebookLink(self):
        self.link_page.click_Facebook()
        self.driver.get("https://www.facebook.com/quickllyfoodandgroceries/")
        # label = self.link_page.get_attribute(Links.fbLabel, 'innerHTML')
        self.driver.get("https://www.uat.quicklly.com/")
        self.assertEqual(label, self.expected)

    def test_twitterLink(self):
        self.link_page.click_twitter()
        self.driver.get("https://twitter.com/Quicklly_")
        label1 = self.link_page.get_attribute(Links.tweetLabel, 'textContent')
        self.driver.get("https://www.uat.quicklly.com/")
        self.assertEqual(label1, self.expected3)

    def test_linkedinLink(self):
        self.link_page.click_linkedin()
        self.driver.get("https://www.linkedin.com/company/myvalue365-e-commerce-pvt-ltd-/?originalSubdomain=in")
        label2 = self.link_page.get_attribute(Links.linkedinLabel, 'innerHTML')
        self.driver.get("https://www.uat.quicklly.com/")
        self.assertEqual(label2, self.expected2)

    def test_youtubeLink(self):
        self.link_page.click_youtubeLink()
        self.driver.get("https://www.youtube.com/channel/UCNHYZ9SGLVejqPwHG8j6EKw")
        label3 = self.link_page.get_attribute(Links.youtubeLabel, 'textContent')
        self.driver.get("https://www.uat.quicklly.com/")
        self.assertEqual(label3, self.expected4)

    def test_instagramLink(self):
        self.link_page.click_instagramLink()
        self.driver.get("https://www.instagram.com/quicklly_official/?r=nametag")
        label4 = self.link_page.get_attribute(Links.instagramSRC, 'src')
        self.driver.get("https://www.uat.quicklly.com/")
        self.assertEqual(label4, self.expected1)

    def test_pinterestLink(self):
        self.link_page.click_pinterest()
        self.driver.get("https://www.pinterest.com/Quicklly2020/")
        label5 = self.link_page.get_attribute(Links.pinterestLabel, 'innerHTML')
        self.driver.get("https://www.uat.quicklly.com/")
        self.assertEqual(label5, self.expected5)
