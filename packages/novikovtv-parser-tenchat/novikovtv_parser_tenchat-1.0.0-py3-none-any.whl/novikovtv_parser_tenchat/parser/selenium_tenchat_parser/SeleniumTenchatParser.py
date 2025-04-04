import asyncio

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import csv
import io

class SeleniumTenchatParser:
    def __init__(self, driver, minimal_wait_time):
        self.driver = driver
        self.minimal_wait_time = minimal_wait_time

    async def __click_element_when_clickable(self, element: str):
        await asyncio.sleep(self.minimal_wait_time)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element))).click()

    async def __click_element_when_clickable_by_css_selector(self, selector: str):
        await asyncio.sleep(self.minimal_wait_time)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()

    async def __click_element_when_clickable_by_class_name(self, class_name: str):
        await asyncio.sleep(self.minimal_wait_time)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, class_name))).click()

    async def __get_element_when_located(self, element: str):
        await asyncio.sleep(self.minimal_wait_time)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))

    async def __get_element_when_located_by_css_selector(self, selector: str):
        await asyncio.sleep(self.minimal_wait_time)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    async def __wait_elements_when_located_by_class_name(self, class_name: str):
        await asyncio.sleep(self.minimal_wait_time)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    async def __get_elements_when_located_by_class_name(self, class_name: str):
        await asyncio.sleep(self.minimal_wait_time)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    async def login_tenchat(self, phone_number, password):
        self.driver.get("https://tenchat.ru/auth/sign-in")

        time.sleep(5)

        phone_input = await self.__get_element_when_located_by_css_selector('input[type="tel"]')
        phone_input.send_keys(phone_number)

        await self.__click_element_when_clickable_by_css_selector('[data-cy="country-code"] button')
        await self.__click_element_when_clickable_by_css_selector('[data-cy="country-268"] button')
        await self.__click_element_when_clickable("//button[@data-test-id='other-verification-methods']")
        await self.__click_element_when_clickable("//div[@data-test-id='verificationMethod_password']")

        password_input = await self.__get_element_when_located("//input[@name='password' and @type='password']")

        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

    async def search_communities(self, query):
        await self.__click_element_when_clickable("//a[@href='/groups']")

        search_box = await self.__get_element_when_located("//input[@type='text' and @id='groups_list_search']")
        search_box.send_keys(query)

        time.sleep(1)
        await self.__click_element_when_clickable("//button[contains(@class, 'ui_search_button_search')]")

    async def get_community_links(self, max_communities=500):
        links = []

        await self.__wait_elements_when_located_by_class_name("groups_row")

        current_communities_count = 0
        while True:
            communities = self.driver.find_elements(By.CLASS_NAME, "groups_row")
            new_communities_count = len(communities)

            if current_communities_count == new_communities_count or new_communities_count >= max_communities:
                break
            else:
                current_communities_count = new_communities_count
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                await self.__wait_elements_when_located_by_class_name("groups_row")

        if new_communities_count >= max_communities:
            communities = communities[:max_communities - 1]

        for community in communities:
            try:
                link_element = community.find_element(By.TAG_NAME, "a")
                link = link_element.get_attribute("href")
                title = community.text.split("\n")[1]
                if link and title:
                    links.append((title, link))
            except:
                continue

        return links

    @classmethod
    def extract_plain_text_and_links(cls, element) -> str:
        if isinstance(element, str):
            return element.strip()

        if element.name in ['script', 'style']:
            return ''

        text_parts = []

        if 'href' in element.attrs:
            href = element.attrs['href']
            if href.startswith('/'):
                href = 'https://vk.com' + href
            text_parts.append(href.strip())

        text_parts.append(' '.join(cls.extract_plain_text_and_links(child) for child in element.contents))

        return ' '.join(filter(None, text_parts))

    @classmethod
    def find_data_in_html(cls, html: str, title: str):
        soup = BeautifulSoup(html, 'html.parser')

        description = ''
        phone = ''
        website = ''
        address = ''
        links = ''
        contacts = ''

        desc_element = soup.find("div", class_="group_info_row info", title="Description")
        if desc_element:
            text_element = desc_element.find("div", class_="line_value")
            if text_element:
                description = text_element.get_text(separator=" ", strip=True)

        phone_element = soup.find("div", class_="group_info_row phone", title="Phone")
        if phone_element:
            phone_link = phone_element.find("a", href=True)
            if phone_link:
                phone = phone_link.get_text(separator=" ", strip=True)

        website_element = soup.find("div", class_="group_info_row site", title="Website")
        if website_element:
            website_link = website_element.find("a", href=True)
            if website_link:
                website = website_link.get_text(separator=" ", strip=True)

        address_element = soup.find("div", class_="group_info_row address")
        if address_element:
            address_link = address_element.find("a", class_="address_link")
            if address_link:
                address = address_link.get_text(separator=" ", strip=True)

        links_section = soup.find("aside", {"aria-label": "Links"})
        if links_section:
            links = cls.extract_plain_text_and_links(links_section)

        contacts_section = soup.find("aside", {"aria-label": "Contacts"})
        if contacts_section:
            contacts = cls.extract_plain_text_and_links(contacts_section)

        return {
            'title': title,
            'description': description,
            'phone': phone,
            'website': website,
            'address': address,
            'links': links,
            'contacts': contacts
        }

    async def parse(self, community_links):
        parsed_data = []

        for title, link in community_links:
            self.driver.get(link)

            await self.__click_element_when_clickable_by_class_name("groups-redesigned-info-more")

            group_info_box = await self.__get_elements_when_located_by_class_name("group-info-box")

            group_info_html = group_info_box.get_attribute("outerHTML")
            parsed_data.append(SeleniumTenchatParser.find_data_in_html(group_info_html, title))
            print(f"HTML сохранен для группы: {title}")
        return parsed_data

    @staticmethod
    def get_csv_result_string(data: list) -> str:
        output = io.StringIO()
        field_names = ['title', 'description', 'phone', 'website', 'address', 'links', 'contacts']

        string_writer = csv.DictWriter(output, fieldnames=field_names)
        string_writer.writeheader()

        for row in data:
            string_writer.writerow(row)

        csv_content = output.getvalue()
        output.close()
        return csv_content