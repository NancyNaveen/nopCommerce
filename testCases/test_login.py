import pytest
from selenium import webdriver
import time

from pageObjects.Login import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

# Verifying if homepage loading successfully

    def test_homePageTitle(self, setup):

        self.logger.info("****************Test_001_Login****************")
        self.logger.info("****************Verifying Home Page Title****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.quit()
            self.logger.info("****************Home Page Title Test is Passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.quit()
            self.logger.error("****************Home Page Title Test is Failed ****************")
            assert False

    def test_login(self, setup):
        self.logger.info("****************Verifying Login Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****************Login Test is Passed ****************")
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
            self.driver.quit()
            self.logger.error("****************Login Test is Failed ****************")
            assert False

