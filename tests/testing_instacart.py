import time
from typing import TextIO
import fileinput

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Enter_Email = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/form/div[1]/input')

#ser = Service("/usr/bin/chromedriver")
#op = webdriver.ChromeOptions()
#s = webdriver.Chrome(service=ser, options=op)
#driver = webdriver.Chrome('/usr/bin/chromedriver')
#driver.get("https:uat.goquicklly.com")
elem = driver.find_element_by_name("q")
time.sleep(3)
elem.clear()
elem.send_keys("raghu@quicklly.com")
elem.send_keys(Keys.RETURN)
driver.find_element_by_xpath(Enter_Email)

driver.close()


#list1 = [1,2,4,5,8,10,103,200]

#print("Latest order number is:", max(list1))     ##  finding and printing max value

#LatestOrderID=max(list1)
#OrderID=open("OrderID.txt", "r").read()  ### read data  from file
#print("Last Order is =" ,OrderID)

#file = open("OrderID.txt", "w")  ## create file and write last order id
#file.write(str(LatestOrderID))
#file.close()

#for numbers in list1:
#    print("Here")
#    if numbers > int(OrderID):
#        print("Order Number : ", numbers)
#        print("--email sent--")


#import smtplib, ssl

#smtp_server = "smtp.gmail.com"
#port = 587  # For starttls
#sender_email = "Quicklly12345@gmail.com"
#password = input("quickllyauto")
#receiver_email = "Quicklly12345@gmail.com"
#message = """
##Subject: Hi there

#This message is sent from Python."""

# Create a secure SSL context
#context = ssl.create_default_context()

# Try to log in to server and send email
#try:
#    server = smtplib.SMTP(smtp_server,port)
#3   server.ehlo() # Can be omitted
#    server.starttls(context=context) # Secure the connection
#    server.ehlo() # Can be omitted
#    server.login(sender_email, password)
#    # TODO: Send email here
#except Exception as e:
#    # Print any error messages to stdout
#    print(e)
#finally:
#    server.quit()
