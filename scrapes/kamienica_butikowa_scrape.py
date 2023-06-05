from services.scrape_logic.scrape_functions import get_developer_info, get_investment_flats

developerName = 'Kamienica Butikowa'
baseUrl = 'https://www.butikowa-kamienica.pl/apartamenty.html'

investmentsInfo = [{'name': 'Kamienica Butikowa', 'url': 'https://www.butikowa-kamienica.pl/apartamenty.html'}]

flatsHtmlInfo = {'flatTag': ".find(class_='ps552 v43 s493').find_all('div', {'data-popup-group': '0'})",
                 'floorNumber': "",
                 'roomsAmount': ".p.find_next_sibling().get_text().split()[2]",
                 'area': ".p.find_next_sibling().find_next_sibling().get_text().split()[1]"
                         ".replace('m2', '').replace(',','.').strip()",
                 'price': "",
                 'status': ".p.find_next_sibling().find_next_sibling().find_next_sibling().get_text().split()[1]"}

developerData = get_developer_info(developerName, baseUrl)

investmentsData = investmentsInfo

flatsData = get_investment_flats(investmentsInfo, flatsHtmlInfo)
