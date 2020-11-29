from .page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class CartTest(CartPage):

    def setUp(self):
        super().setUp()
        # self.openHomePage()
        self.open("https://practice.automationbro.com/shop")

    def test_add_to_cart(self):
        # add converse shoe to cart
        self.click(self.converse_add_to_cart_btn)

        # assert 1 product is added to the cart
        self.scroll_to_top()
        self.assert_text('1', self.cart_count_text)

        # open Cart page
        self.openPage()

        # error handling
        try:
            self.scroll_to(self.subtotal_text)
        except NoSuchElementException:
            self.refresh()
            print("refreshed")

        # get the current subtotal
        self.scroll_to(self.subtotal_text)
        text = self.get_text(self.subtotal_text)
        print(text)

        # change cart quantity
        self.set_value(self.product_quantity_input, "2")
        self.send_keys(self.product_quantity_input, Keys.RETURN)
        self.click(self.update_cart_btn)

        # wait for loading to be completed
        # time.sleep(1)
        self.wait_for_element_visible(self.loading_overlay)
        self.wait_for_element_not_visible(self.loading_overlay)

        # self.assert_text('text', "td[class='product-subtotal']")
        # print(self.get_text("td[class='product-subtotal']"))

        # assert subtotal to be different than the original subtotal
        self.wait_for_text("$300.00", self.subtotal_text)
        self.assertNotEqual(text, self.get_text(self.subtotal_text))
