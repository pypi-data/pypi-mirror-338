from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from novikovtv_parser_tenchat.parser.selenium_tenchat_parser.SeleniumTenchatParser import SeleniumTenchatParser


async def make_csv_text(phone_number, password, search_query, max_communities=500):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    selenium_tenchat_parser = SeleniumTenchatParser(driver, 0.1)

    await selenium_tenchat_parser.login_tenchat(phone_number, password)
    await selenium_tenchat_parser.search_communities(search_query)
    community_links = await selenium_tenchat_parser.get_community_links(max_communities)
    parsed_data = await selenium_tenchat_parser.parse(community_links)

    return SeleniumTenchatParser.get_csv_result_string(parsed_data)

#load_dotenv()
#
#login = os.getenv("LOGIN")
#password = os.getenv("PASSWORD")
#max_communities = int(os.getenv("MAX_COMMUNITIES"))
#search_query = "Компания"
#
#csv_text = make_csv_text(login, password, search_query, max_communities)