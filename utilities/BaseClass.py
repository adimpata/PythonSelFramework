"""
BaseClass for providing common utility methods for test classes.

Methods:
    getLogger():
        Configures and returns a logger instance.
    verifyLinkPresence(text):
        Waits until a link with the specified text is present and returns the element.
    waitForDate():
        Waits until the date field is present and returns the element.
    selectOptionByText(locator, text):
        Selects an option from a dropdown by visible text.
"""

import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        """
        Configures and returns a logger instance.

        Returns:
            Logger: A configured logger instance.
        """
        loggerName = inspect.stack()[0][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        """
        Waits until a link with the specified text is present and returns the element.

        Args:
            text (str): The text of the link to wait for.

        Returns:
            WebElement: The web element for the link.
        """
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def waitForDate(self):
        """
        Waits until the date field is present and returns the element.

        Returns:
            WebElement: The web element for the date field.
        """
        dobField = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='bday']")))
        return dobField

    def selectOptionByText(self, locator, text):
        """
        Selects an option from a dropdown by visible text.

        Args:
            locator (tuple): The locator for the dropdown element.
            text (str): The visible text of the option to select.

        Returns:
            None
        """
        dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        select = Select(dropdown)
        select.select_by_visible_text(text)
