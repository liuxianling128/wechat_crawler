from selenium.common.exceptions import NoAlertPresentException


class alert_is_present(object):

    def is_alert(driver):
        try:
            alert = driver.switch_to.alert
            alert.text
            return alert
        except NoAlertPresentException:
            return False