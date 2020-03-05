from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from browse_configure import*
from time import sleep

class BrowseBot():
    def __init__ (self):
        self.driver = webdriver.Chrome(executable_path=PATH)
    
    def login(self):
        self.driver.get('https://instagram.com')

        sleep(2)

        facebook_auth_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/button')
        facebook_auth_login.click()
         
        sleep(3)

        facebook_auth_email_insert = self.driver.find_element_by_xpath('//*[@id="email"]')
        facebook_auth_email_insert.send_keys(username)

        facebook_auth_pw_insert = self.driver.find_element_by_xpath('//*[@id="pass"]')
        facebook_auth_pw_insert.send_keys(password)

        facebook_login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        facebook_login_btn.click()
        
        #getting rid of being notified if anyone followed the instagram user.
        notification_btn = ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm")))
        notification_btn.click()

    

    def scroll_to_check(self):
        check_page = self.driver.find_element_by_tag_name('body')
        
        for _ in range(3):
            check_page.send_keys(Keys.END)
            sleep(2)
            check_page.send_keys(Keys.HOME)
            sleep(2)


  
    def explore(self):

        explore_instagram = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
        explore_instagram.click()


        
    def scroll_to_browse(self):
        check_instagram_page = self.driver.find_element_by_tag_name('body')

        for _ in range(3):
            check_instagram_page.send_keys(Keys.PAGE_DOWN)
            sleep(3)

            check_instagram_page.send_keys(Keys.PAGE_DOWN)
            sleep(3)

            check_instagram_page.send_keys(Keys.PAGE_UP)
            sleep(2)

         
    def select_image(self):
        select_instagram_image = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div[1]/div/div[6]/div[3]/a')
        select_instagram_image.click()

        sleep(3)


        next_right_image = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')

        for _ in range(5):
            next_right_image.click()
            sleep(3)
            next_right_image.click()
        
        sleep(4)

        explore_user_tag = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a')
        explore_user_tag.click()

     
    
    def new_search(self):
        search_user = ui.WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'XTCLo')]")))
        search_user.send_keys(person)
        
       
        sleep(10)

        select_user = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
        select_user.click()
    
    def repeat_scroll(self):
        check_instagram_page = self.driver.find_element_by_tag_name('body')

        for _ in range(3):
            check_instagram_page.send_keys(Keys.PAGE_DOWN)
            sleep(3)

            check_instagram_page.send_keys(Keys.PAGE_DOWN)
            sleep(3)

    def new_image_select(self):
        choose_image = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[6]/div[2]/a')
        choose_image.click()
    
    def close(self):
        sleep(5)
        
        close_image = self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')
        close_image.click()

    def instagram_home(self):
        home_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a')
        home_btn.click()



#Sequencing of bot actions
bot = BrowseBot() 

bot.login()

bot.scroll_to_check()

bot.explore()

bot.scroll_to_browse()

bot.select_image()

bot.new_search()

bot.repeat_scroll()

bot.new_image_select()

bot.close()

bot.instagram_home()



