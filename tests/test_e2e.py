"""
TestOne class for executing an end-to-end test on a web application.

Methods:
    test_e2e():
        Executes the end-to-end test.
"""

from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        """
        Executes the end-to-end test.

        This method performs the following steps:
        1. Logs the start of the test.
        2. Navigates to the shop page and retrieves all card titles.
        3. Clicks the footer button of the card with the title "Blackberry".
        4. Proceeds to the checkout page.
        5. Enters the country name "rom" and verifies the presence of the link "Romania".
        6. Selects "Romania" from the list.
        7. Accepts the terms and conditions.
        8. Submits the form.
        9. Verifies that the success message is displayed.

        Asserts:
            The success message contains "Success! Thank you!".
        """
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Getting all the card titles")
        cards = checkoutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        confirmPage = checkoutPage.checkOutItems()
        log.info("Entering country name as rom")
        self.driver.find_element(By.ID, "country").send_keys("rom")
        self.verifyLinkPresence("Romania")

        self.driver.find_element(By.LINK_TEXT, "Romania").click()
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is " + textMatch)

        assert ("Success! Thank you!" in textMatch)
