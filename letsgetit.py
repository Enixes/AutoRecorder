# import module
from io import BytesIO
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import win32api


chrome_options = Options()
chrome_options.add_extension(r'D:\as\Auto Clicker\ScrcastScreenRecorder13.crx')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'D:\as\Auto Clicker\chromedriver.exe')
win32api.MessageBox(0, 'Start Recording Now', 'Alert', 0x00001000)
# driver = webdriver.Chrome(r"D:\as\Auto Clicker\chromedriver.exe")
driver.get("https://gate.appliedroots.com/lecture/10/engineering-discrete-mathematics/712/why-learn-calculus/16/calculus")
driver.maximize_window()
time.sleep(2) 
driver.switch_to.window(window_name=driver.window_handles[0])
# driver.close()


driver.find_element_by_id("email").send_keys("itsasusingh@gmail.com")
driver.find_element_by_id("password").send_keys("Enixes@13")
driver.find_element(By.XPATH, '//button[text()="LOGIN"]').click()

# find_elements(By.CSS_SELECTOR, ".elements__StyledListItem-sc-197zmwo-0.QbTKh")
chapters = driver.find_elements(By.CSS_SELECTOR, ".card-body.px-4.p-2.card-body-n")
number_of_chapters = len(chapters)
print(number_of_chapters)
encrypted_video_count = 0
youtube_video_count = 0
total_time = 0

def click(element, noOfClicks):
    for i in range(noOfClicks):
        time.sleep(0.5)
        element.click()
        

# def click_complete_button():
#     try:
#         driver.find_element(By.XPATH, '//button[text()="COMPLETE"]').click()
#     except:
#         print("No Complete button found. Is the chapter already marked completed?")

while(number_of_chapters > 0):
    time.sleep(2)
    element = driver.find_element_by_xpath("//span[contains(@class, 'ml-3')]")
    print(element.text)
    duration = int(element.text.split(" ")[1])
    if (len(driver.find_elements_by_id("my-video")) != 0):
        print("Encrypted Video Detected")
        encrypted_video_count += 1
        time.sleep(2)       # Wait for the page to load

        driver.find_element_by_id('btn480p').click()

        element3x = driver.find_element(By.XPATH, "//*[@id='my-video']/div[4]/div[9]/button")
        click(element3x, 4)

        fullScreenElement = driver.find_element(By.XPATH, "//*[@id='my-video']/div[4]/button[10]")
        click(fullScreenElement, 1)

        sleepTime = ((duration*60)/3) + 5
        print("Sleeping for " + str(int(sleepTime/60)) + " minutes " + str(sleepTime%60) + " seconds")
        time.sleep(sleepTime)

        fullScreenElement = driver.find_element(By.XPATH, "//*[@id='my-video']/div[4]/button[10]")
        click(fullScreenElement, 1)

        nextLectureElement = driver.find_element_by_id('nextLectureURL')
        actions = ActionChains(driver)
        actions.move_to_element(nextLectureElement).perform()
        # driver.executeScript("arguments[0].scrollIntoView(true);", nextLectureElement)
        time.sleep(5)
        total_time += sleepTime
        if (total_time/3600 > 3):
            win32api.MessageBox(0, 'Stop Recording Now', 'Alert', 0x00001000)
            break
        nextLectureElement.click()

    elif (len(driver.find_elements_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]')) != 0):
        driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
        print("Youtube Video Detected")
        youtube_video_count += 1
        time.sleep(2)   
        sleepTime = ((duration*60)/3) + 5
        print("Sleeping for " + str(int(sleepTime/60)) + " minutes " + str(sleepTime%60) + " seconds")
        time.sleep(sleepTime)

        nextLectureElement = driver.find_element_by_id('nextLectureURL')
        actions = ActionChains(driver)
        actions.move_to_element(nextLectureElement).perform()
        # driver.executeScript("arguments[0].scrollIntoView(true);", nextLectureElement)
        time.sleep(5)
        total_time += sleepTime
        if (total_time/3600 > 3):
            win32api.MessageBox(0, 'hello', 'title', 0x00001000)
            break
        nextLectureElement.click()
        # click_complete_button()
            


print("Number of enrypted videos in this topic" + str(encrypted_video_count))   
print("Number of youtube videos in this topic" + str(youtube_video_count))    

    
# print(int("Duration: 9 mins".split(" ")[1]))
# driver.quit()
