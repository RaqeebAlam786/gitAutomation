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
    Intro = (By.XPATH, '//*[@id="searchhide"]/div[3]/p[2]/strong/u')
    Terms = (By.XPATH, '//*[@id="searchhide"]/div[3]/p[2]/strong/u')


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
    googleError = (By.XPATH, '//*[@id="street_number2-error"]')


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
    googleError = (By.XPATH, '//*[@id="street_number-error"]')


class ForgetPassword:
    SI_button = (By.XPATH, '//*[@id="procedcheckoutBtn"]')
    ForgetPassword_button = (By.XPATH, '//*[@id="apiformprodct"]/div[1]/div/div/div[3]/span/a')
    registered_email = (By.XPATH, '//*[@id="email"]')
    submit_button = (By.XPATH, '//*[@id="form"]/div[3]/input')
    Uer_login = (By.XPATH, '//*[@id="signupformmodal"]/div/div/div[2]/div/div[1]/div/div[1]/p[3]/span')
    heading1 = (By.XPATH, '//*[@id="searchhide"]/div[6]/div[1]/div[1]/h3')
    heading2 = (By.XPATH, '//*[@id="searchhide"]/div[6]/div[3]/div[1]/h3')
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
    PriceOfItem = (
        By.CSS_SELECTOR,
        '#minicart > div > div.clsContent > div > div:nth-child(1) > div > p:nth-child(2) > span.price')
    ItemQuantity = (By.XPATH, '//*[@id="qty_cart_270"]/span')
    PlusQuantity = (By.XPATH, '//*[@id="qty_cart_270"]/a[2]')
    MinusQuantity = (By.XPATH, '//*[@id="qty_cart_270"]/a[1]')
    empty_cart = (By.ID, 'lblCartEmpty')
    delete_item = (By.ID, 'lnk_cart_[pid]')
    shop_name = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/div/div/a')
    shopping_carts = (By.CSS_SELECTOR, '#searchhide > div.clsCartBox > div.clsCartStoresItems > div.clsCartStores > h3')
    Email = (By.ID, 'user_email')
    Pass = (By.ID, 'password')
    LoginButton = (By.XPATH, '//*[@id="btn-login"]')
    SignInButton = (By.XPATH, '//*[@id="procedcheckoutBtn"]')
    additem = (By.XPATH, '//*[@id="img_270"]')
    additem2 = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/section[2]/div/a[1]')
    orderFood = (By.XPATH, '//*[@id="searchhide"]/div[4]/div/div/div/div/a[1]')
    express = (By.XPATH, '//*[@id="load_data"]/div[1]/div[2]')
    item1 = (By.XPATH, '//*[@id="load_data"]/div/div/div/div/div[1]/a')
    additem1 = (By.XPATH, '//*[@id="dvDialog-Custom"]/div/div[2]/a')
    addToCart = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/section[2]/div/a[1]')
    clickGrocery = (By.XPATH, '//*[@id="searchhide"]/div[5]/div[1]/div/div/a[2]')
    allStores = (By.XPATH, '//*[@id="stores"]/div/div/a[1]/img')
    shops_name = (By.XPATH, '//*[@id="product"]/div[1]/img')
    shops_name1 = (By.XPATH, '//*[@id="product"]/div[2]/img')
    price_label = (By.XPATH, '//*[@id="stores"]/div/div/a[1]/span[1]')
    count_label = (By.XPATH, '//*[@id="stores"]/div/div/a[1]/span[2]')
    price1 = (By.XPATH, '#stores > div > div > a:nth-child(2) > span.price')
    price2 = (By.XPATH, '#stores > div > div > a:nth-child(3) > span.price')
    CurbsidePickup = (By.XPATH, '//*[@id="searchhide"]/div[3]/div[1]/div[2]/div[1]/a[2]')
    Delivery = (By.XPATH, '//*[@id="searchhide"]/div[3]/div[1]/div[2]/div[1]/a[1]')
    right_arrow = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/i[2]')
    left_arrow = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/i[1]')
    ItemInCart = (By.ID, 'lblCartStoreName')
    drop_down1 = (By.XPATH, '//*[@id="qty_270"]')
    drop_down2 = (By.XPATH, '//*[@id="qty_51875"]')
    remove1 = (By.XPATH, '//*[@id="lnk_270"]')
    remove2 = (By.XPATH, '//*[@id="lnk_51875"]')
    eVoucher_label = (By.XPATH, '//*[@id="couponfrm"]/div[1]/div/div[1]/label')
    reward_label = (By.XPATH, '//*[@id="couponfrm"]/div[1]/div/div[2]/label')
    wallet_label = (By.XPATH, '//*[@id="couponfrm"]/div[1]/div/div[3]/label')
    codeOption = (By.XPATH, '//*[@id="parRadioOne"]/p/span')
    maximum_eVoucher = (By.XPATH, '//*[@id="parRadioOne"]/span')
    rewardPoint = (By.XPATH, '//*[@id="parRadioTwo"]/p/span')
    rewardPointApplicable = (By.XPATH, '//*[@id="parRadioTwo"]/span')
    walletBalance = (By.XPATH, '//*[@id="parRadioThree"]/p/span')
    walletEmpty = (By.XPATH, '//*[@id="parRadioThree"]/span')
    orderSummary = (By.CLASS_NAME, 'cartboxttl')
    groceriesSubTotal = (By.XPATH, '//*[@id="searchhide"]/div[3]/div[2]/div[1]/p[2]/span[1]')
    groceriesItemTotal = (By.XPATH, '//*[@id="lblSubItemsGrocery"]')
    groceriesPrice = (By.XPATH, '//*[@id="lblGrandTotalGrocery"]')
    FoodSubTotal = (By.XPATH, '//*[@id="searchhide"]/div[3]/div[2]/div[1]/p[3]/span[1]')
    FoodItemTotal = (By.XPATH, '//*[@id="lblSubItemsFood"]')
    FoodPrice = (By.XPATH, '//*[@id="lblGrandTotalFood"]')
    EstimatedTax = (By.XPATH, '//*[@id="tax"]')
    EstimatedTaxPrice = (By.CSS_SELECTOR,
                         '#searchhide > div.clsCartBox > div.clsCartOptions > div.cartright-box.cartright-box-two > p:nth-child(4) > span.cartboxitemPrice')
    EstimatedShipping = (By.XPATH, '//*[@id="shippingfee"]/span[1]')
    EstimatedShippingPrice = (By.XPATH, '//*[@id="shippingfee"]/span[2]')
    MinimumCharge = (By.XPATH, '//*[@id="storemincharge"]')
    MinimumChargePrice = (By.CSS_SELECTOR,
                          '#searchhide > div.clsCartBox > div.clsCartOptions > div.cartright-box.cartright-box-two > p:nth-child(6) > span.cartboxitemPrice')
    PackageHandling = (By.XPATH, '//*[@id="pkgcharge"]')
    PackageHandlingPrice = (By.CSS_SELECTOR,
                            '#searchhide > div.clsCartBox > div.clsCartOptions > div.cartright-box.cartright-box-two > p:nth-child(7) > span.cartboxitemPrice')
    Tip = (By.CSS_SELECTOR,
           '#searchhide > div.clsCartBox > div.clsCartOptions > div.cartright-box.cartright-box-two > p.cartboxitemtip > span.cartboxitemName')
    TipPrice = (By.XPATH, '//*[@id="tip"]')
    EstimatedOrder = (By.CSS_SELECTOR,
                      '#searchhide > div.clsCartBox > div.clsCartOptions > div.cartright-box.cartright-box-two > p:nth-child(10) > span.cartboxitemName.cartboxitemNameBold')
    EstimatedOrderPrice = (By.XPATH, '//*[@id="tipadd"]')
    DeliveryLabel = (By.CSS_SELECTOR,
                     '#searchhide > div.clsCartBox > div.clsCartOptions > div.cartright-box.cartright-box-three > p.addrslbl > span')
    ChangeAddress = (By.XPATH, '//*[@id="changeAddrssBtn"]')
    EstimatedDelivery = (By.CSS_SELECTOR, '#deliverystate > strong')
    DeliveryNotes = (By.CSS_SELECTOR,
                     '#searchhide > div.clsCartBox > div.clsCartOptions > div.cartright-box.cartright-box-three > div.delivery_notesbox-wrapper > label > b')
    ProceedToPayment = (By.XPATH, '//*[@id="searchhide"]/div[3]/div[2]/div[2]/div[2]')
    InvalidCoupon = (By.XPATH, '//*[@id="parRadioOne"]/div')
    drop_quantity = (By.XPATH, '//*[@id="qty_51875"]/option[2]')
    eVoucher = (By.CSS_SELECTOR, '#vocherRewardWallet-1')
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
    paypal = (By.XPATH, '//*[@id="paymentbox"]/div/div/div[2]/div/a/img')
    signIn = (By.ID, 'procedcheckoutBtn')
    shopNow = (By.XPATH, '//*[@id="subscribe"]/div/div/div[2]/form/button')
    secondShop = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/div/div/a[2]')
    SecondItemName = (By.XPATH, '//*[@id="minicart"]/div/div[2]/div/div/div/p[1]')
    SecondItemPrice = (By.XPATH, '//*[@id="minicart"]/div/div[2]/div/div/div/p[2]/span[1]')
    SecondItemQuanitity = (By.XPATH, '//*[@id="qty_cart_51875"]/span')
    yourAccount = (By.XPATH, '//*[@id="searchhide"]/header/div[3]/span')
    ChangePaymentMethod = (By.XPATH, '//*[@id="choose-payment-method"]')
    AddPaymentMethod = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/span')
    CreditCardNumber = (By.XPATH, '//*[@id="credit-card-number"]')
    Expiration = (By.ID, 'expiration')
    CVV = (By.ID, 'cvv')
    Pay = (By.ID, 'pay_amount')
    Payment = (By.XPATH, '//*[@id="proceedtopayment"]')
    Department = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]')
    GroceryShop = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[1]/a')
    crossButton = (By.XPATH, '//*[@id="paymentbox"]/div/div/div[1]/button')
    quicklly = (By.XPATH, '/html/body/header/a/img')
    orderID = (By.XPATH, '//*[@id="innerlist-products"]/strong"')
    accountName = (By.XPATH, '//*[@id="searchhide"]/header/div[3]/p')
    eVoucher_text_value = (By.XPATH, '//*[@id="e-vouchercode"]')
    ThankYou = (By.XPATH, '//*[@id="innerlist-products"]/h1')
    GoFresh = (By.XPATH, '//*[@id="searchhide"]/div[7]/div[1]/div/div/a[2]/img')
    clickCredit = (By.XPATH, '//*[@id="container"]/div[1]/div/div[2]/div/form/label')
    SearchForProducts = (By.XPATH, '//*[@id="search_box"]')
    HitSearch = (By.XPATH, '//*[@id="searchbtn"]')


class Coupon:
    zipCode = (By.XPATH, '//*[@id="zipcode"]')
    submitButton = (By.XPATH, '//*[@id="zipsubmitbtn"]')
    yourAccount = (By.XPATH, '//*[@id="searchhide"]/header/div[3]/span')
    SignInButton = (By.XPATH, '//*[@id="procedcheckoutBtn"]')
    Email = (By.ID, 'user_email')
    Pass = (By.ID, 'password')
    LoginButton = (By.XPATH, '//*[@id="btn-login"]')
    additem = (By.XPATH, '//*[@id="img_270"]')
    additem2 = (By.XPATH, '//*[@id="searchhide"]/div[6]/div/section[2]/div/a[1]')
    click_cart = (By.CLASS_NAME, 'clsCart2')
    proceed_to_checkOut = (By.ID, 'lnkProceedToCheckout')
    evoucher_text_box = (By.XPATH, '//*[@id="e-vouchercode"]')
    InvalidCoupon = (By.XPATH, '//*[@id="parRadioOne"]/div')
    Apply = (By.XPATH, '//*[@id="parRadioOne"]/a')
    empty_cart = (By.ID, 'lblCartEmpty')
    GoFresh = (By.XPATH, '//*[@id="searchhide"]/div[7]/div[1]/div/div/a[2]/img')
    item1 = (By.XPATH, '//*[@id="load_data"]/div/div/div/div/div[1]/a')
    addToCart = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/section[2]/div/a[1]')
    checkout2 = (By.XPATH, '//*[@id="dvFoodSuggestPopup"]/div/div/a')


class Department:
    enter_zip = (By.ID, 'zipcode')
    submit_zip = (By.ID, 'zipsubmitbtn')
    yourAccount = (By.XPATH, '//*[@id="searchhide"]/header/div[3]/span')
    SignInButton = (By.XPATH, '//*[@id="procedcheckoutBtn"]')
    Email = (By.ID, 'user_email')
    Pass = (By.ID, 'password')
    LoginButton = (By.XPATH, '//*[@id="btn-login"]')
    proceed_to_checkOut = (By.ID, 'lnkProceedToCheckout')
    additem = (By.XPATH, '//*[@id="img_270"]')
    Pay = (By.ID, 'pay_amount')
    Pot = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/div/div/a[10]/img')
    Department = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]')
    select = (By.XPATH, '//*[@id="nationwide"]/div[2]/div[1]/a')
    Add = (By.XPATH, '//*[@id="img_77024"]')
    AddToCart = (By.XPATH, '//*[@id="searchhide"]/div[2]/div/div[2]/div[3]/a[2]')
    quicklly = (By.XPATH, '//*[@id="searchhide"]/header/a/img')
    right_arrow = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/i[2]')
    Seeti = (By.XPATH, '//*[@id="minicart"]/div/div[1]/div/div/div/a[3]')
    delete = (By.XPATH, '//*[@id="lnk_cart_[pid]"]')
    GoFresh = (By.XPATH, '//*[@id="searchhide"]/div[8]/div[1]/div/div/a[2]/img')
    AddToCartLG = (By.XPATH, '//*[@id="searchhide"]/div[6]/div/section[2]/div/a[1]')
    addSecondItem = (By.XPATH, '//*[@id="img_51875"]')
    AddToCartP = (By.XPATH, '//*[@id="searchhide"]/div[6]/div/section[2]/div/a[1]')
    food = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/div/div/a[3]/img')
    MakkiFastFood = (By.XPATH, '//*[@id="load_data"]/div[2]/a')
    AddTenders = (By.XPATH, '//*[@id="load_data"]/div[2]/div/div[2]/a')
    TendersAddToCart = (By.XPATH, '//*[@id="dvDialog-Custom"]/div/div[2]/a')
    submitTenders = (By.XPATH, '//*[@id="dvDialog-DateTime"]/div/div[2]/a')
    payment = (By.XPATH, '//*[@id="proceedtopayment"]')
    BBQKit = (By.XPATH, '//*[@id="searchhide"]/div[4]/div/div/div/div/a[3]/img')
    chickenTikkaImage = (By.XPATH, '//*[@id="img_132523"]')
    AddTikkaToCart = (By.XPATH, '//*[@id="searchhide"]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/a')
    Catering = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/div/div/a[12]/img')
    HyderabadHouse = (By.XPATH, '//*[@id="Catering"]/div/div[1]/a')
    AddBeefFry = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/div[1]/a')
    AddToCartBeef = (By.XPATH, '//*[@id="dvDialog-Custom"]/div/div[2]/a')
    submitBeef = (By.XPATH, '//*[@id="dvDialog-DateTime"]/div/div[2]/a')
    mealBasket = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/div/div/a[9]/img')
    MealPlan = (By.XPATH, '//*[@id="meal-basket"]/div[2]/div[1]/a')
    AddKorma = (By.XPATH, '//*[@id="searchhide"]/div[3]/div/div[1]/div[1]/div[3]/div[3]/a')
    plusKorma = (By.XPATH, '//*[@id="searchhide"]/div[3]/div/div[1]/div[1]/p/a/span[3]')
    AddToCartCK = (By.XPATH, '//*[@id="searchhide"]/div[2]/p/span[2]/a')
    TiffinServices = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/div/div/a[4]/img')
    ChicagoTiffin = (By.XPATH, '//*[@id="tiffin-services"]/div/div[1]/a')
    VegThali = (By.XPATH, '//*[@id="TiffinServices"]/div[2]/div[1]/a')
    AddToCartVegThali = (By.XPATH, '//*[@id="dvDialog-Custom"]/div/div[2]/a')
    submitVT = (By.XPATH, '//*[@id="dvDialog-DateTime"]/div/div[2]/a')
    MealKit = (By.XPATH, '/html/body/header/div[2]/div/div[1]/div[1]/div/div/ul/li[9]/a')
    CuminClub = (By.XPATH, '//*[@id="home"]/div/div[4]/div/a/div/img')
    selectMealKit = (By.XPATH, '//*[@id="meal-kit"]/div[2]/div[1]/form/a')
    AddPapad = (By.XPATH, '/html/body/div[5]/div/div/div[1]/div[3]/div[3]/a')
    plusPapad = (By.XPATH, '/html/body/div[6]/div/div/div[1]/p/a/span[3]')
    AddToCartPapad = (By.XPATH, '//*[@id="searchhide"]/div[2]/p/span[3]/a')
    Recipes = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[9]/a')
    PalakPaneer = (By.XPATH, '//*[@id="45"]/img')
    AddToBasket = (By.XPATH, '//*[@id="addchekListprodct"]')
    delivery = (By.XPATH, '//*[@id="ddlDeliveryTime"]')
    timeDelivery = (By.XPATH, '//*[@id="ddlDeliveryTime"]/option[2]')
    clickTick = (By.XPATH, '//*[@id="flexCheckDefault"]')
    clickRA = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/i[2]/img')
    OrganicGrocery = (By.XPATH, '//*[@id="searchhide"]/div[4]/div/div/div/div/a[5]/img')
    BuildABox = (By.XPATH, '//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
    AddOrganicJowar = (By.XPATH, '//*[@id="searchhide"]/div[2]/div[3]/div/div[1]/div[3]/div[1]/a')
    AddToCartOrganic = (By.XPATH, '//*[@id="searchhide"]/div[3]/div/div/div[3]/button')
    ThankYou = (By.XPATH, '//*[@id="innerlist-products"]/h1')
    Account = (By.XPATH, '//*[@id="searchhide"]/header/div[3]/span')
    SearchForProducts = (By.XPATH, '//*[@id="search_box"]')
    LeftArrow = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/i[1]/img')
    rightArrow = (By.XPATH, '//*[@id="searchhide"]/div[1]/div/div/i[2]/img')
    rotiKIt = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/div/div/a[5]/img')
    buildRotiBox = (By.XPATH, '//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
    AddWholeWheatRoti = (By.XPATH, '//*[@id="searchhide"]/div[2]/div[3]/div/div[1]/div[3]/div[2]/a')
    AddToCartRoti = (By.XPATH, '//*[@id="searchhide"]/div[3]/div/div/div[3]/button')
    checkout2 = (By.XPATH, '//*[@id="dvFoodSuggestPopup"]/div/div/a')
    liquorStore = (By.XPATH, '//*[@id="searchhide"]/div[5]/div/div/div/div/a[2]/img')
    Beer = (By.XPATH, '//*[@id="searchhide"]/section[1]/div[2]/div/div/div[1]/a/img')
    classicLime = (By.XPATH, '//*[@id="img_138002"]')
    AddToCartBeer = (By.XPATH, '//*[@id="storeproductlist"]/div[1]/div[2]/a')


class ZipCode:
    enter_zip = (By.ID, 'zipcode')
    submit_zip = (By.ID, 'zipsubmitbtn')
    quicklly = (By.XPATH, '//*[@id="searchhide"]/header/a/img')
    grocery = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[1]/a')
    food = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[2]/a')
    BBQKit = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[3]/a')
    RotiKit = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[4]/a')
    Catering = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[5]/a')
    organicGrocery = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[6]/a')
    MealBasket = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[7]/a')
    TiffinServices = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[8]/a')
    MealKit = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[9]/a')
    InstantPot = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[10]/a')
    Recipes = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[8]/a')
    department = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/span')
    cross = (By.XPATH, '//*[@id="popupoffer"]/div/div/div/div/button/img')
    list = (By.XPATH, '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul')


class Contact:
    enter_zip = (By.ID, 'zipcode')
    contact = (By.LINK_TEXT, 'CONTACT')
    name = (By.ID, 'name')
    email = (By.ID, 'email')
    subject = (By.ID, 'mobile')
    comment = (By.ID, 'comment')
    send = (By.XPATH, '//*[@id="main-contact-form"]/div/fieldset/ul/div/button')
    thanks = (By.XPATH, '//*[@id="messages_product_view"]/p')


class SignUp:
    enter_zip = (By.ID, 'zipcode')
    signin = (By.XPATH, '//*[@id="procedcheckoutBtn"]')
    needAccount = (By.XPATH, '//*[@id="signupformmodal"]/div/div/div[2]/div/div[1]/div/div[1]/p[1]/span')
    firstName = (By.XPATH, '//*[@id="reg-form"]/div[1]/input')
    lastName = (By.XPATH, '//*[@id="reg-form"]/div[2]/input')
    Address = (By.XPATH, '//*[@id="autocomplete"]')
    Phone = (By.XPATH, '//*[@id="reg-form"]/div[5]/input[2]')
    email = (By.XPATH, '//*[@id="reg-form"]/div[6]/input')
    password = (By.XPATH, '//*[@id="reg-form"]/div[7]/input')
    confirmpassword = (By.XPATH, '//*[@id="reg-form"]/div[8]/input')
    register = (By.XPATH, '//*[@id="btn-reg"]')
    email2 = (By.XPATH, '//*[@id="user_email"]')
    password2 = (By.XPATH, '//*[@id="password"]')
    logIn = (By.XPATH, '//*[@id="btn-login"]')


class Refer:
    refer = (By.XPATH, '/html/body/header/div/div[2]/a')
    referLink = (By.XPATH, '/html/body/header/div/div[2]/div/div/ul/li[1]/a')
    clickFacebook = (By.XPATH, '//*[@id="referfb"]')
    facebookLink = (By.XPATH, '//*[@id="shareonFacebookBtn"]')
    clickTwitter = (By.XPATH, '//*[@id="refertw"]')
    twitterLink = (By.XPATH, '//*[@id="shareonTwitterBtn"]')


class GuestCheckout:
    enter_zip = (By.ID, 'zipcode')
    goFresh = (By.XPATH, '//*[@id="searchhide"]/div[8]/div[1]/div/div/a[2]/img')
    potatoImage = (By.XPATH, '//*[@id="img_51875"]')
    AddtoCart = (By.XPATH, '//*[@id="searchhide"]/div[6]/div/section[2]/div/a[1]')
    Cart = (By.XPATH, '//*[@id="searchhide"]/header/div[4]/a')
    checkout = (By.XPATH, '//*[@id="lnkProceedToCheckout"]')
    guest = (By.XPATH, '//*[@id="gustusrlogin"]/span')
    Fname = (By.XPATH, '//*[@id="frmGuestAddress"]/div[1]/input')
    Lname = (By.XPATH, '//*[@id="frmGuestAddress"]/div[2]/input')
    Address = (By.XPATH, '//*[@id="autocomplete2"]')
    number = (By.XPATH, '//*[@id="frmGuestAddress"]/div[5]/input[2]')
    email = (By.XPATH, '//*[@id="frmGuestAddress"]/div[6]/input')
    submit = (By.XPATH, '//*[@id="shippingUpprdtcsubbtn"]')
    submit_zip = (By.ID, 'zipsubmitbtn')
    checkout2 = (By.XPATH, '//*[@id="dvFoodSuggestPopup"]/div/div/a')
    shoppingCarts = (By.XPATH, '//*[@id="searchhide"]/div[4]/div[1]/div[1]/h3')
    searchBox = (By.XPATH, '//*[@id="search_box"]')
    searchButton = (By.ID, 'searchbtn')


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
