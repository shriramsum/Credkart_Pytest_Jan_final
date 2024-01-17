import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig


class Test_User_Profile:

    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()

    def test_UserRegistration_001(self, setup):
        self.driver = setup
        # 1 Browser Open
        # self.driver = webdriver.Firefox()

        self.ur = UserProfile_Class(self.driver)
        # 2 Go to registration url
        self.driver.get(self.RegistrationUrl)

        # 3 Enter Name
        # driver.find_element(By.ID, 'name').send_keys("Rohit")
        self.ur.Enter_Name("Rohit")

        # 4 Enter EMail Id
        # self.driver.find_element(By.ID, 'email').send_keys("Rohit3442@credence.in")
        self.ur.Enter_Email("TestUser1071@credence.in")

        # 5 Enter Password
        # self.driver.find_element(By.ID, 'password').send_keys("rohit@123")
        self.ur.Enter_Password("Test123")

        # 6 Enter Confirm Password
        # self.driver.find_element(By.ID, "password-confirm").send_keys("rohit@123")
        self.ur.Enter_ConfirmPassword("Test123")

        # 7 Click on Register button
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        self.ur.Click_Login_Or_RegisterButton()

        # 7 Validate Registration
        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Registration Pass")
        #     assert True
        # except:
        #     print("Registration Fail")
        #     assert False

        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            self.driver.save_screenshot(
                "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Registration_Pass.png")
            # self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Registration_Fail.png")
            # self.driver.close()
            assert False

    # def test_UserLogin_002(self, setup):
    #     self.driver = setup
    #     # 1 Browser Open
    #     # 2 Go to Url https://automation.credence.in/login
    #     self.driver.get(self.LoginUrl)
    #     self.ur = UserProfile_Class(self.driver)
    #     # 3 Enter email
    #     # driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Rohit344@credence.in")
    #     self.ur.Enter_Email(self.Username)
    #     # 4 Enter Password
    #     # driver.find_element(By.XPATH, "//input[@id='password']").send_keys("rohit@123")
    #     self.ur.Enter_Password(self.Password)
    #     # 5 Click on Login button
    #     # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    #     self.ur.Click_Login_Or_RegisterButton()
    #     # 6 Validate Login
    #     if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
    #         self.driver.save_screenshot(
    #             "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Pass.png")
    #
    #         # self.driver.close()
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Fail.png")
    #
    #         # self.driver.close()
    #         assert False

# pytest -v --html=HTMLReports/Edge_Report.html --browser chrome -n=5 --alluredir="C:\Users\HP\Desktop\Python revision Jan 24\Pytest_Credkart\AllureReports"
# allure serve "folder Path"


#

# config -- > url, login id pass
# Logs
# Data Driven Test Case
