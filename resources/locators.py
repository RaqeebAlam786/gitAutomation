# from typing import Tuple

from selenium.webdriver.common.by import By


class LogIn:
    # Main page locators
    learn_more_link = (By.ID, 'learn-more-link')
    back_to_safety_button = (By.ID, 'primary-button')
    SignIn_button = (By.ID, 'procedcheckoutBtn')
    email_textbox = (By.ID, 'user_email')
    email = (By.XPATH, '//*[@id="user_email"]')
    pasw = (By.XPATH, '//*[@id="password"]')
    password_textbox = (By.ID, 'password')
    login_button = (By.ID, 'btn-login')
    login_heading = (By.CLASS_NAME, 'frmheading')
    email_text = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[1]/label')
    password_text = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[2]/label')
    email_field_error = (By.XPATH, '//*[@id="user_email-error"]')
    password_field_error = (By.XPATH, '//*[@id="password-error"]')
    needanaccount_signin = (By.XPATH, '//*[@id="signupformmodal"]/div/div/div[2]/div/div[1]/div/div[1]/p[1]/span')
    ContinueAsGuest_link = (By.XPATH, '//*[@id="gustusrlogin"]/span')
    ForgotPassword_link = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[3]/span/a')
    text_1 = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[4]/span/text()[1]')
    text_2 = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[4]/span/text()[2]')
    privacy_link = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[4]/span/a')
    terms_link = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[4]/span/strong/a')
    home_button = (By.XPATH, '//*[@id="searchhide"]/div[2]/ul/li[1]/a')
    doesnt_match = (By.XPATH, '//*[@id="error"]/div')


class ContinueAsGuest:
    ContinueAsGuest_button = (By.XPATH, '//*[@id="gustusrlogin"]/span')
    firstname = (By.NAME, 'fname')
    lastname = (By.NAME, 'lname')
    fullAddress = (By.NAME, 'full_address')
    Apartment = (By.NAME, 'apt')
    MobileNumber = (By.NAME, 'mobile')
    EmailAddress = (By.NAME, 'email')
    submit_button = (By.ID, 'shippingUpprdtcsubbtn')
    signin_button = (By.XPATH, '//*[@id="procedcheckoutBtn"]')
    Shipping_address = (By.XPATH, '//*[@id="loginpanelguess"]/div/span')
    Submit_name = (By.XPATH, '//*[@id="shippingUpprdtcsubbtn"]')
    firstname_error = (By.XPATH, '//*[@id="frmGuestAddress"]/div[1]/label')
    Address_error = (By.XPATH, '//*[@id="frmGuestAddress"]/div[3]/label')
    Mobile_error = (By.XPATH, '//*[@id="frmGuestAddress"]/div[5]/label')
    email_error = (By.XPATH, '//*[@id="frmGuestAddress"]/div[5]/label')
    user_login = (By.XPATH, '//*[@id="signupformmodal"]/div/div/div[2]/div/div[1]/div/div[1]/p[3]/span')
    needanaccount_signin = (By.XPATH, '//*[@id="signupformmodal"]/div/div/div[2]/div/div[1]/div/div[1]/p[1]/span')
    invalid_mobile = (By.XPATH, '//*[@id="mobile-error"]')
    invalid_Email = (By.XPATH, '//*[@id="email-error"]')


class NeedAnAccount:
    NeedAnAccount_button = (By.XPATH, '//*[@id="signupformmodal"]/div/div/div[2]/div/div[1]/div/div[1]/p[1]/span')
    firname = (By.CSS_SELECTOR, '#reg-form > div:nth-child(2) > input')
    lasname = (By.XPATH, '//*[@id="reg-form"]/div[2]/input')
    enteraddress = (By.XPATH, '//*[@id="autocomplete"]')
    apartmentno = (By.ID, 'apt_no')
    mobileno = (By.XPATH, '//*[@id="reg-form"]/div[5]/input[2]')
    email2 = (By.XPATH, '//*[@id="reg-form"]/div[6]/input')
    pass2 = (By.XPATH, '//*[@id="reg-form"]/div[7]/input')
    ConfirmPassword = (By.NAME, 'confpassword')
    register_button = (By.ID, 'btn-reg')
    signin = (By.XPATH, '//*[@id="procedcheckoutBtn"]')
    registertext = (By.XPATH, '//*[@id="signuppanel"]/div/span')
    firstname_error = (By.XPATH, '//*[@id="fname-error"]')
    address_error = (By.XPATH, '//*[@id="autocomplete-error"]')
    mobile_error = (By.XPATH, '//*[@id="mobile-error"]')
    email_error = (By.XPATH, '//*[@id="email-error"]')
    password_error = (By.XPATH, '//*[@id="password-error"]')
    confirm_password_error = (By.XPATH, '//*[@id="confpassword-error"]')
    userlogin_link = (By.XPATH, '//*[@id="signupformmodal"]/div/div/div[2]/div/div[1]/div/div[1]/p[3]/span')
    continue_as_guest_link = (By.XPATH, '//*[@id="gustusrlogin"]/span')
    mobile_invalid = (By.XPATH, '//*[@id="mobile-error"]')
    address_invalid = (By.XPATH, '//*[@id="street_number-error"]')
    email_invalid = (By.XPATH, '//*[@id="email-error"]')


class ForgetPassword:
    SI_button = (By.XPATH, '//*[@id="procedcheckoutBtn"]')
    ForgetPassword_button = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[3]/span/a')
    registered_email = (By.XPATH, '//*[@id="email"]')
    submit_button = (By.XPATH, '//*[@id="form"]/div[3]/input')
    Uer_login = (By.XPATH, '//*[@id="signupformmodal"]/div/div/div[2]/div/div[1]/div/div[1]/p[3]/span')
    heading1 = (By.XPATH, '//*[@id="searchhide"]/div[5]/div[1]/div[1]/h3')
    heading2 = (By.XPATH, '//*[@id="searchhide"]/div[5]/div[3]/div[1]/h3')
    invalid_email = (By.XPATH, '//*[@id="form"]/div[1]')


class MiniCart:
    enter_zip = (By.ID, 'zipcode')
    submit_zip = (By.ID, 'zipsubmitbtn')
    click_cart = (By.CLASS_NAME, 'clsCart2')
    ItemCount = (By.XPATH, '//*[@id="minicart"]/div/div[1]/p/span')
    min_order = (By.XPATH, '//*[@id="minicart"]/div/div[2]/p[2]')
    proceed_to_checkOut = (By.ID, 'lnkProceedToCheckout')
    Add1 = (By.XPATH, '//*[@id="searchhide"]/div[3]/div[2]/div/div[1]/div[2]/div[2]')
    shop_total = (By.XPATH, '//*[@id="minicart"]/div/div[2]/p[4]')
    image = (By.XPATH, '//*[@id="product"]/div/img')
    NameOfItem = (By.XPATH, '//*[@id="minicart"]/div/div[2]/div/div/div/p[1]')
    PriceOfItem = (By.CSS_SELECTOR, '#minicart > div > div.clsContent > div > div:nth-child(1) > div > p:nth-child(2) > span.price')
    ItemQuantity = (By.XPATH, '//*[@id="qty_cart_270"]/span')
    PlusQuantity = (By.XPATH, '//*[@id="qty_cart_270"]/a[2]')
    MinusQuantity = (By.XPATH, '//*[@id="qty_cart_270"]/a[1]')
    empty_cart = (By.ID, 'lblCartEmpty')
    delete_item = (By.ID, 'lnk_cart_[pid]')
    shop_name = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/div/div/a')
    shopping_carts = (By.XPATH, '//*[@id="searchhide"]/div[4]/div[1]/div[1]/h3')
    Email = (By.ID, 'user_email')
    Pass = (By.ID, 'password')
    LoginButton = (By.XPATH, '//*[@id="btn-login"]')
    SignInButton = (By.ID, 'procedcheckoutBtn')
    additem = (By.XPATH, '//*[@id="load_data"]/div[1]/div/div[2]/div/div/div[1]/a')
    additem2 = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/section[2]/div/a[1]')
    orderFood = (By.XPATH, '//*[@id="searchhide"]/div[4]/div/div/div/div/a[1]')
    express = (By.XPATH, '//*[@id="load_data"]/div[1]/div[2]')
    item1 = (By.XPATH, '//*[@id="load_data"]/div/div/div/div/div[1]/a')
    additem1 = (By.XPATH, '//*[@id="dvDialog-Custom"]/div/div[2]/a')
    addToCart = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/section[2]/div/a[1]')

    allStores = (By.XPATH, '//*[@id="stores"]/a[1]/img')
    shops_name = (By.XPATH, '//*[@id="stores"]/a[2]/img')
    shops_name1 = (By.XPATH, '//*[@id="stores"]/a[3]/img')
    price_label = (By.XPATH, '//*[@id="stores"]/a[1]/span[1]')
    count_label = (By.XPATH, '//*[@id="stores"]/a[1]/span[2]')
    price1 = (By.XPATH, '//*[@id="stores"]/a[2]/span[1]')
    price2 = (By.XPATH, '//*[@id="stores"]/a[3]/span[1]')
    CurbsidePickup = (By.XPATH, '//*[@id="searchhide"]/div[4]/div[1]/div[2]/div[1]/a[2]')
    Delivery = (By.XPATH, '//*[@id="searchhide"]/div[4]/div[1]/div[2]/div[1]/a[1]')
    right_arrow = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/i[2]')
    left_arrow = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/i[1]')
    ItemInCart = (By.ID, 'lblCartStoreName')
    drop_down1 = (By.XPATH, '//*[@id="qty_270"]')
    drop_down2 = (By.XPATH, '//*[@id="qty_51875"]')
    remove1 = (By.XPATH, '//*[@id="lnk_270"]')
    remove2 = (By.XPATH, '//*[@id="lnk_51875"]')
    eVoucher_label = (By.XPATH, '//*[@id="couponfrm"]/div[1]/div/div[1]/label')
    reward_label =(By.XPATH, '//*[@id="couponfrm"]/div[1]/div/div[2]/label')
    wallet_label =(By.XPATH, '//*[@id="couponfrm"]/div[1]/div/div[3]/label')
    codeOption =(By.XPATH, '//*[@id="parRadioOne"]/p/span')
    maximum_eVoucher =(By.XPATH, '//*[@id="parRadioOne"]/span')
    rewardPoint =(By.XPATH, '//*[@id="parRadioTwo"]/p/span')
    rewardPointApplicable =(By.XPATH, '//*[@id="parRadioTwo"]/span')
    walletBalance =(By.XPATH, '//*[@id="parRadioThree"]/p/span')
    walletEmpty =(By.XPATH, '//*[@id="parRadioThree"]/span')
    orderSummary =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[1]/p[1]')
    groceriesSubTotal =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[1]/p[2]/span[1]')
    groceriesItemTotal =(By.XPATH, '//*[@id="lblSubItemsGrocery"]')
    groceriesPrice =(By.XPATH, '//*[@id="lblGrandTotalGrocery"]')
    FoodSubTotal =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[1]/p[3]/span[1]')
    FoodItemTotal =(By.XPATH, '//*[@id="lblSubItemsFood"]')
    FoodPrice =(By.XPATH, '//*[@id="lblGrandTotalFood"]')
    EstimatedTax =(By.XPATH, '//*[@id="tax"]')
    EstimatedTaxPrice =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[1]/p[4]/span[2]')
    EstimatedShipping =(By.XPATH, '//*[@id="shippingfee"]/span[1]')
    EstimatedShippingPrice =(By.XPATH, '//*[@id="shippingfee"]/span[2]')
    MinimumCharge =(By.XPATH, '//*[@id="storemincharge"]')
    MinimumChargePrice =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[1]/p[6]/span[2]')
    PackageHandling =(By.XPATH, '//*[@id="pkgcharge"]')
    PackageHandlingPrice =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[1]/p[7]/span[2]')
    Tip =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[1]/p[8]/span[1]')
    TipPrice =(By.XPATH, '//*[@id="tip"]')
    EstimatedOrder =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[1]/p[9]/span[1]')
    EstimatedOrderPrice =(By.XPATH, '//*[@id="tipadd"]')
    DeliveryLabel =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[2]/p[1]/span')
    ChangeAddress =(By.XPATH, '//*[@id="changeAddrssBtn"]')
    EstimatedDelivery =(By.XPATH, '//*[@id="deliverystate"]/strong')
    DeliveryNotes =(By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[2]/div[1]/label/b')
    ProceedToPayment = (By.XPATH, '//*[@id="searchhide"]/div[4]/div[2]/div[2]/div[2]')
    InvalidCoupon = (By.XPATH, '//*[@id="parRadioOne"]/div')
    drop_quantity = (By.XPATH, '//*[@id="qty_270"]/option[2]')
    eVoucher = (By.XPATH, '//*[@id="vocherRewardWallet-1"]')
    reward = (By.XPATH, '//*[@id="vocherRewardWallet-2"]')
    wallet = (By.XPATH, '//*[@id="vocherRewardWallet-3"]')
    eVoucher_text = (By.XPATH, '//*[@id="e-vouchercode"]')
    reward_text = (By.XPATH, '//*[@id="e-vouchercode"]')
    NoTip = (By.XPATH, '//*[@id="tipzero"]')
    Tip5 = (By.XPATH, '//*[@id="tipthree"]')
    Tip10 = (By.XPATH, '//*[@id="tipfive"]')
    Tip15 = (By.XPATH, '//*[@id="tipseven"]')
    Tip20 = (By.XPATH, '//*[@id="tipten"]')
    clickCross = (By.XPATH, '')
    Notes_text = (By.XPATH, '//*[@id="delivery_notesbox"]')
    Apply = (By.XPATH, '//*[@id="parRadioOne"]/a')






class CommonLocators:
    learn_more_link = (By.ID, 'learn-more-link')
    main_loader = (By.XPATH, '/html/body/header/a/img')

    buttons = (By.XPATH, '//button[@type="submit"]')
    main_heading = (By.XPATH, '//h3')
    table = (By.XPATH, "//table")
    table_xpath = '(//table)[{}]'
    xpath_head = (By.XPATH, "//table[contains(@class,'table')]//th")
    heading_xpath = '(//table[contains(@class,"table")])[{}]//th'
    next_page = (By.XPATH, '//table//a[@aria-label="Next page"]')
    next_page_xpath = '(//table)[{}]//a[@aria-label="Next page"]'
    success_toast_msg = (By.XPATH, "//div[contains(@class,'alert-success')]")
    global_toast_message = (By.XPATH, '//*[local-name()="global-messages"]//div[contains(@class,"alert-")]')
    toast_message_close_button = (By.XPATH, '//*[local-name()="global-messages"]//button')
    table_headings = (By.XPATH, '//thead//th')
    add_button = (By.XPATH, '//span[contains(@class,"btn btn-primary pull-right")]')
    ng_spinner = (By.XPATH, '//div[contains(@class, "ng-spinner-loader")]')
    alert_2 = (By.XPATH, '//*[local-name()="global-messages"]//div[contains(@role,"alert")]')
    spinner = (By.XPATH, '//app-activity-indicator/..')
    verification_textbox = (By.XPATH, '//app-password-verification//input')
    verification_confirm_button = (By.XPATH, '//app-password-verification//button[contains(@class,"btn-primary")]')
    verification_cancel_button = (By.XPATH, '//app-password-verification//button[contains(@class,"cancel_button")]')
    next_page_button = (By.XPATH, '//a[@aria-label="Next page"]')
    # main_loader = (By.XPATH, '//app-activity-indicator//div[@id="loader"]')
    sub_page_loader = (By.XPATH, '//app-spinner')


class PrivacyErrorPageLocators:
    # Privacy Error Page Locators
    learn_more_link = (By.ID, 'learn-more-link')
    err_cert_common_name_invalid = (By.ID, 'error-code')
    improve_chrome_security_checkbox = (By.ID, 'opt-in-checkbox')
    advanced_button = (By.ID, 'details-button')
    proceed_link = (By.ID, 'proceed-link')
    back_to_safety_button = (By.ID, 'primary-button')


def email_textbox_id():
    return None
