"""
HomePage class for handling interactions on the home page of a web application.

Attributes:
    shop (tuple): Locator for the shop link.
    name (tuple): Locator for the name input field.
    email (tuple): Locator for the email input field.
    password (tuple): Locator for the password input field.
    checkBox (tuple): Locator for the checkbox.
    status (tuple): Locator for the status radio button.
    gender (tuple): Locator for the gender dropdown.
    successMessage (tuple): Locator for the success message.
    submit (tuple): Locator for the submit button.

Methods:
    __init__(driver):
        Initializes the HomePage with a web driver.
    shopItems():
        Clicks the shop link and returns an instance of CheckoutPage.
    getName():
        Returns the web element for the name input field.
    getEmail():
        Returns the web element for the email input field.
    getPassword():
        Returns the web element for the password input field.
    getBox():
        Returns the web element for the checkbox.
    getStatus():
        Returns the web element for the status radio button.
    getGender():
        Returns the web element for the gender dropdown.
    submitForm():
        Returns the web element for the submit button.
    getSuccessMessage():
        Returns the web element for the success message.
"""

from selenium.webdriver.common.by import By

from pageObjects.Checkoutpage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        """
        Initializes the HomePage with a web driver.

        Args:
            driver (WebDriver): The web driver instance.
        """
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    status = (By.ID, "inlineRadio1")
    gender = (By.ID, "exampleFormControlSelect1")
    successMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    submit = (By.XPATH, "//input[@value='Submit']")

    def shopItems(self):
        """
        Clicks the shop link and returns an instance of CheckoutPage.

        Returns:
            CheckoutPage: An instance of the CheckoutPage class.
        """
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        """
        Returns the web element for the name input field.

        Returns:
            WebElement: The web element for the name input field.
        """
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        """
        Returns the web element for the email input field.

        Returns:
            WebElement: The web element for the email input field.
        """
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        """
        Returns the web element for the password input field.

        Returns:
            WebElement: The web element for the password input field.
        """
        return self.driver.find_element(*HomePage.password)

    def getBox(self):
        """
        Returns the web element for the checkbox.

        Returns:
            WebElement: The web element for the checkbox.
        """
        return self.driver.find_element(*HomePage.checkBox)

    def getStatus(self):
        """
        Returns the web element for the status radio button.

        Returns:
            WebElement: The web element for the status radio button.
        """
        return self.driver.find_element(*HomePage.status)

    def getGender(self):
        """
        Returns the web element for the gender dropdown.

        Returns:
            WebElement: The web element for the gender dropdown.
        """
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        """
        Returns the web element for the submit button.

        Returns:
            WebElement: The web element for the submit button.
        """
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        """
        Returns the web element for the success message.

        Returns:
            WebElement: The web element for the success message.
        """
        return self.driver.find_element(*HomePage.successMessage)
