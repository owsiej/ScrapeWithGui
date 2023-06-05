from services.scrape_logic.scrape_functions import get_developer_info, get_developer_investments, \
    get_all_buildings_from_investment, \
    get_investment_flats

developerName = 'Kombinat Budowlany'
baseUrl = 'https://www.kombinatbud.com.pl'
baseTag = '/Inwestycje'

investmentsHtmlInfo = {'investmentTag': ".find_all(class_='covers')[0].find_all('a')",
                       'investmentName': ".find('h3').get_text()",
                       'investmentLink': "['href']"}

investmentsInfo = get_developer_investments(baseUrl + baseTag, investmentsHtmlInfo)

investmentBuildingsHtmlInfo = {'buildingTag': ".find_all(class_='button w-100', attrs={'href': re.compile(r'\B/.*')})",
                               'buildingName': "['name'] + ' ' + building.get_text().strip()",
                               'buildingLink': "['href']"}

buildingsInfo = get_all_buildings_from_investment(investmentsInfo, investmentBuildingsHtmlInfo, baseUrl)

flatsReservedHtmlInfo = {'flatTag': ".tbody.find_all('tr', class_='reserved')",
                         'floorNumber': ".find(class_='desktop').get_text()",
                         'roomsAmount': ".find(class_='desktop').find_next_sibling().get_text()",
                         'area': ".find(class_='desktop').find_next_sibling().find_next_sibling().get_text()"
                                 ".replace('m²','').replace(',','.')",
                         'price': ".find(class_='text-danger').find_next_sibling('b').get_text()"
                                  ".replace('PLN', '').replace(' ', '').strip() if flat.find(class_='text-danger')"
                                  "else flat.find(class_='desktop').find_next_sibling().find_next_sibling()"
                                  ".find_next_sibling().get_text().replace('PLN', '').strip()",
                         'status': "['title']"}

flatsReservedInfo = get_investment_flats(buildingsInfo, flatsReservedHtmlInfo, baseUrl)

flatsRestHtmlInfo = {'flatTag': ".tbody.select('tr')",
                     'floorNumber': ".find(class_='desktop').get_text()",
                     'roomsAmount': ".find(class_='desktop').find_next_sibling().get_text()",
                     'area': ".find(class_='desktop').find_next_sibling().find_next_sibling().get_text()"
                             ".replace('m²','').replace(',','.')",
                     'price': ".find(class_='text-danger').find_next_sibling('b').get_text()"
                              ".replace('PLN', '').replace(' ', '').strip() if flat.find(class_='text-danger') else "
                              "flat.find(class_='desktop').find_next_sibling().find_next_sibling().find_next_sibling()"
                              ".get_text().replace('PLN', '').strip()",
                     'status': ""}

flatsRestInfo = get_investment_flats(buildingsInfo, flatsRestHtmlInfo, baseUrl)

developerData = get_developer_info(developerName, baseUrl)

investmentsData = list(map(lambda item: {
    'name': item['name'],
    'url': baseUrl + item['url']
}, buildingsInfo))

flatsData = flatsReservedInfo + flatsRestInfo
