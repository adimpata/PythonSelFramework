"""
CheckoutPage class for handling the checkout process in a web application.

Attributes:
    cardTitle (tuple): Locator for the card title elements.
    cardFooter (tuple): Locator for the card footer elements.
    checkOut (tuple): Locator for the checkout button.

Methods:
    __init__(driver):
        Initializes the CheckoutPage with a web driver.
    getCardTitle():
        Returns a list of web elements representing the card titles.
    getCardFooter():
        Returns a list of web elements representing the card footers.
    checkOutItems():
        Clicks the checkout button and returns an instance of ConfirmPage.
"""
from selenium.webdriver.common.by import By

from pageObjects import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        """
             Returns a list of web elements representing the card titles.

             Returns:
                 list[WebElement]: A list of web elements for the card titles.
             """
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        """
               Returns a list of web elements representing the card footers.

               Returns:
                   list[WebElement]: A list of web elements for the card footers.
               """
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        """
               Clicks the checkout button and returns an instance of ConfirmPage.

               Returns:
                   ConfirmPage: An instance of the ConfirmPage class.
               """
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
