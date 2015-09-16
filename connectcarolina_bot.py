from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RegistryBot:    
    login_url = 'https://ccpa.unc.edu/psp/paprd/EMPLOYEE/EMPL/h/?tab=NC_REDIRECT&TargetPage=Student'

    def __init__(self, username, password):
        self.driver = webdriver.PhantomJS('/library/python/2.7/site-packages/selenium/webdriver/phantomjs/phantomjs')
        #self.driver = webdriver.Firefox() #firefox for visible testing
        self.driver.implicitly_wait(10)
        self.username = username
        self.password = password
    
    def add_class_to_cart(self, class_number):
        '''Class number is unique ID, represents course and section numbers. Selects default recitation options'''
        self.driver.find_element_by_id('DERIVED_REGFRM1_CLASS_NBR').send_keys(class_number)
        self.driver.find_element_by_id('DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$').click()
        self.driver.find_element_by_id('DERIVED_CLS_DTL_NEXT_PB').click()
        self.driver.find_element_by_id('DERIVED_CLS_DTL_NEXT_PB$280$').click()
        
    def close(self):
        self.driver.close()
        
    def login(self):
        '''Logs in to ConnectCarolina with {username:password} and browses to cart'''
        self.driver.get(self.login_url)
        self.driver.find_element_by_name('j_username').send_keys(self.username)
        self.driver.find_element_by_name('j_password').send_keys(self.password, Keys.RETURN)
        self.move_to_cart()
    
    def move_to_cart(self):
        self.driver.switch_to.frame(self.driver.find_element_by_name('TargetContent'))
        self.driver.find_element_by_xpath("(//a[contains(text(),'Enroll')])[2]").click()
        self.driver.find_element_by_id('SSR_DUMMY_RECV1$sels$1$$0').click()
        self.driver.find_element_by_id('DERIVED_SSS_SCT_SSR_PB_GO').click()
    
    def submit_cart(self):
        self.driver.find_element_by_id('DERIVED_REGFRM1_LINK_ADD_ENRL$82$').click()
        self.driver.find_element_by_id('DERIVED_REGFRM1_SSR_PB_SUBMIT').click()
