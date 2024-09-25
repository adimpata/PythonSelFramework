"""
TestHomePage class for testing form submissions on the home page.

Methods:
    test_form_Submissions(getData):
        Tests the form submission process with provided test data.
    getData(request):
        Fixture that provides test data for the form submissions.
"""

import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_Submissions(self, getData):
        """
        Tests the form submission process with provided test data.

        This method performs the following steps:
        1. Logs the start of the test.
        2. Fills out the form with the provided test data.
        3. Submits the form.
        4. Verifies that the success message is displayed.

        Args:
            getData (dict): A dictionary containing test data for the form.

        Asserts:
            The success message contains "Success".
        """
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getBox().click()
        homePage.getStatus().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        self.waitForDate().send_keys("01/01/2000")

        homePage.submitForm().click()

        alertText = homePage.getSuccessMessage().text
        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        """
        Fixture that provides test data for the form submissions.

        Args:
            request (FixtureRequest): The request object for the fixture.

        Returns:
            dict: A dictionary containing test data for the form.
        """
        return request.param
