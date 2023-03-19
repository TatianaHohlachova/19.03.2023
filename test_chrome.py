import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser(unittest.TestCase):

    def setUp(self) -> None:
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["appium:platformVersion"] = "9"
        desired_caps["appium:deviceName"] = "10.0.2.5:5555"
        desired_caps["appium:automationName"] = "Appium"
        desired_caps["appium:browserName"] = "Chrome"
        desired_caps["appium:chromedriverExecutable"] = "chromedriver.exe"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        self.driver.get("https://www.demoblaze.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_web_app(self):
        logo = self.driver.find_element(by=AppiumBy.CSS_SELECTOR, value="#nava")
        ### oczekiwanie na element
        # btn = wait_for_element(
        #     self.driver,
        #     by=AppiumBy.CSS_SELECTOR,
        #     value="#nava",
        #     timeout=10
        # )
		self.assertNotNone(logo)


def wait_for_element(driver, by, value, timeout=10, poll_frequency=0.5):
    return WebDriverWait(
        driver,
        timeout=timeout,
        poll_frequency=poll_frequency
    ).until(lambda x: x.find_element(by, value), message="wait_for_element timeout")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBrowser)
    unittest.TextTestRunner(verbosity=2).run(suite)
