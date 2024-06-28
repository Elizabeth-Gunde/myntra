from baseclass import BaseClass


class Testmyntrakid(BaseClass):
    def test_cheapest_kids_tshirts(self):


        #A = ActionChains(self.driver)
        self.driver.get("https://www.myntra.com/")
        self.driver.maximize_window()
