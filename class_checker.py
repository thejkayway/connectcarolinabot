from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from connectcarolina_bot import RegistryBot

class Class_Checker_Bot:
    
    search_url = 'https://cccsrpt.unc.edu/psp/csreportsns/EMPLOYEE/UNC_CSNS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL?QRB=840&FolderPath=PORTAL_ROOT_OBJECT.NC_CUSTOM_PUBLIC.NC_CLASS_SEARCH_PUBLIC_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%25252cIsFolder'
    
    def __init__(self, username, password, dept, course_number, class_number):
        self.username = username
        self.password = password
        self.dept = dept
        self.course_number = course_number
        self.class_number = class_number
        
        # start browser
        #self.driver = webdriver.PhantomJS('/library/python/2.7/site-packages/selenium/webdriver/phantomjs/phantomjs')
        self.driver = webdriver.Firefox() # use firefox for testing
        self.driver.implicitly_wait(10)
        
        self.search_loop()
    
    def search_loop(self):
        while True:
            self.search_for_class()
            time.sleep(15)
    
    def search_for_class(self):
        self.driver.get(self.search_url)
        self.driver.switch_to.frame(self.driver.find_element_by_name('TargetContent'))
        
        select = Select(self.driver.find_element_by_id('CLASS_SRCH_WRK2_STRM$35$'))
        select.select_by_visible_text('2015 Spring')
        time.sleep(0.5)
        self.driver.find_element_by_id('SSR_CLSRCH_WRK_SUBJECT$0').send_keys(self.dept)
        time.sleep(0.5)
        self.driver.find_element_by_id('SSR_CLSRCH_WRK_SSR_OPEN_ONLY$3').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('SSR_CLSRCH_WRK_CATALOG_NBR$1').send_keys(self.course_number)
        #really weird, but in phantomjs, the open class only button is deselected by default, uncomment 42 if problems
        #self.driver.find_element_by_id('SSR_CLSRCH_WRK_SSR_OPEN_ONLY_LBL$3').click()
        self.driver.find_element_by_name('DERIVED_CLSRCH_SSR_EXPAND_COLLAPS$149$$IMG$1').click()
        self.driver.find_element_by_id('SSR_CLSRCH_WRK_CLASS_NBR$8').send_keys(self.class_number)
        self.driver.find_element_by_id('CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH').click()
        time.sleep(0.5)
        self.driver.save_screenshot('test.jpg')
        alt_text = self.driver.find_element_by_class_name('SSSIMAGECENTER').get_attribute('alt')
        if (alt_text == 'Open' or alt_text == 'Wait Listed'):
            robot = RegistryBot(self.username, self.password)
            robot.login()
            robot.submit_cart()
            time.sleep(1)
            robot.close()