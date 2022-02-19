import time

import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:
    def test_homepage(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        print(actual_links)
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Nav Link Text'
        #homepage_nav.get_nav_link_by_name('Shoes').click()
        num = len(homepage_nav.get_nav_links())
        for indx in range(num):
            homepage_nav.get_nav_links()[indx].click()
            homepage_nav.driver.delete_all_cookies()
            time.sleep(5)
