from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import sys
import time
from PIL import ImageGrab
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Captcha

driver = webdriver.Chrome()
driver.get("https://erp.iitkgp.ac.in/IIT_ERP3/showmenu.htm")
driver.maximize_window()
assert "Welcome to ERP" in driver.title
print("Enter your Roll Number")
roll = input()
print("Enter your Password")
passwd = input()
user = driver.find_element_by_id("user_id")
user.send_keys(roll)
psswd = driver.find_element_by_id("password")
psswd.send_keys(passwd)
time.sleep(1)
question = driver.find_element_by_id("question")
answer = driver.find_element_by_id("answer")
q = question.text
if (len(q) == 0):
    print("Enter valid roll number")
    driver.close()
    sys.exit(1)
print(q)
ans = input()
answer.send_keys(ans)
aca = driver.find_element_by_class_name("btn-primary").click()
print("ATTENTION:")
print(
    "PLEASE DON'T MINIMIZE YOUR BROWSER AND KINDLY DON'T MOVE YOUR MOUSE/TOUCHPAD AND PLEASE DO NOT PRESS ANY KEY UNTIL THE BROWSER CLOSES")
print("IN CASE OF ANY ERROR PLEASE KINDLY RUN THE ERP.exe FILE AGAIN")
time.sleep(6)
driver.maximize_window()
try:
    driver.find_element_by_id("skiplink").click()
except:
    pass

time.sleep(1)

aca = driver.find_elements_by_tag_name('a')
aca[8].click()

time.sleep(1)

fed = driver.find_elements_by_tag_name('a')
for el in fed:
    if (el.text.find("Feedback") != -1):
        el.click()
        time.sleep(.5)
        fed2 = driver.find_elements_by_tag_name('a')
        for el2 in fed2:
            if (el2.text.find("FeedBack Form") != -1):
                el2.click()
                time.sleep(.5)
                break
        break
# -------------------------------------------------------------Inside frame -----------------------------------------------------------
frame = driver.switch_to.frame(driver.find_element_by_id('myframe'))
fed4 = driver.find_elements_by_tag_name("a")
len_fed4 = len(fed4)
for j in range(2):
    for i in range(4):
        for k in range(len_fed4):
            fed4 = driver.find_elements_by_tag_name("a")
            fed4[k].click()
            time.sleep(.5)
            fed5 = driver.find_elements_by_css_selector("input[type='radio'][name='check']")
            try:
            # if (True):
                fed5[i].click()
                time.sleep(3)
                # -------------------------------------------------Captcha--------------------------------------------------------------------------
                img = driver.find_element_by_tag_name('img')
                src = img.get_attribute('src')
                print(src)
                driver.switch_to.default_content()
                driver.execute_script("window.open('');")
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[1])
                driver.get(src)
                time.sleep(3)
                actionChains = ActionChains(driver)
                actionChains.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
                driver.close()
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to.frame(driver.find_element_by_id('myframe'))
                img1 = ImageGrab.grabclipboard()

                img1.save('1.png', 'PNG')
                txt = Captcha.break_captcha('1.png')
                print(txt)
                fed8 = driver.find_element_by_name("passline")
                fed8.send_keys(txt)

                fed6 = driver.find_elements_by_css_selector("input[type='radio'][value='5']")
                fed6 = fed6 + driver.find_elements_by_css_selector("input[type='radio'][value='53']")
                for el3 in fed6:
                    el3.click()
                fed7 = driver.find_elements_by_tag_name("textarea")
                for el3 in fed7:
                    el3.send_keys("No Comments")
                driver.find_element_by_id("sub").click()
                time.sleep(.5)
                pyautogui.typewrite(['enter'])
                time.sleep(.5)
                try:
                    WebDriverWait(driver, 3).until(EC.alert_is_present())
                    alert = driver.switch_to.alert
                    alert.accept()
                    print("alert accepted")
                except TimeoutException:
                    print("no alert")
            except:
                    pass

driver.close()
