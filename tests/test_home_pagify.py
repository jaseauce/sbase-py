from seleniumbase import BaseCase
from .page_objects.home_page import HomePage


class HomeTest(HomePage):

    def setUp(self):
        super().setUp()
        self.open_page()

        # login

    def tearDown(self):
        super().tearDown()
        print("This is the teardown definition")

        # logout

    def test_home_page(self):
        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")
        # assert logo
        self.assert_element_visible('HomePage.logo_icon')

        # scroll to bottom and assert copyright
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro")

        # click on the Shop menu link and assert url contains product
        self.click(HomePage.shop_menu_link)
        self.assertIn("shop", self.get_current_url())

    def test_menu_links(self):
        expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contacts']
        self.assertEqual(expected_links, self.get_nav_links_text())