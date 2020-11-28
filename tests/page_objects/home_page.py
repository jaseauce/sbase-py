from seleniumbase import BaseCase


class HomePage(BaseCase):
    logo_icon = ".site-branding img"
    shop_menu_link = "//ul[@id='menu-main']//a[contains(text(),'Shop')]"
    nav_links = "//*[starts-with(@id, 'menu-item')]"

    def open_page(self):
        self.open("https://practice.automationbro.com/")

    def get_nav_links_text(self):
        nav_links_el = self.find_elements(self.nav_links)
        nav_links_text = []
        for link in nav_links_el:
            nav_links_text.append(link.text)
        return nav_links_text
