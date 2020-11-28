from seleniumbase import BaseCase


class HomeTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.open("https://practice.automationbro.com/")

        # login

    def tearDown(self):
        super().tearDown()
        print("This is the teardown definition")

        # logout

    def test_home_page(self):
        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")
        # assert logo
        self.assert_element_visible(".site-branding img")

        # scroll to bottom and assert copyright
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro")

        # click on the Shop menu link and assert url contains product
        self.click("//ul[@id='menu-main']//a[contains(text(),'Shop')]")
        self.assertIn("product", self.get_current_url())

    def test_menu_links(self):
        expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contact']
        nav_links_el = self.find_elements("//*[starts-with(@id, 'menu-item')]")
        # print(nav_links_el)
        nav_links_text = []
        for link in nav_links_el:
            # print(link.text)
            nav_links_text.append(link.text)
        self.assertEqual(expected_links, nav_links_text)