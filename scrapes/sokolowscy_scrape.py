from services.scrape_logic.scrape_functions import get_developer_info, get_developer_investments, get_investment_flats

developerName = 'Sokołowscy'
baseUrl = 'https://sokolowscynieruchomosci.pl/w-sprzedazy'

investmentHtmlInfo = {'investmentTag': ".find_all('div', class_='col-12 col-md-6 col-lg-4 mt-3')",
                      'investmentName': ".find('h5').get_text()",
                      'investmentLink': ".a['href']"}

flatsHtmlInfo = {'flatTag': ".tbody.find_all('tr')",
                 'floorNumber': "",
                 'roomsAmount': ".find_all('a')[2].get_text()",
                 'area': ".find_all('a')[1].get_text().replace('m2', '').strip()",
                 'price': ".find_all('a')[4].get_text().replace('zł', '').strip().replace(' ', '')",
                 'status': ".find_all('td')[-1].get_text()"}

developerData = get_developer_info(developerName, baseUrl)

investmentsData = get_developer_investments(baseUrl, investmentHtmlInfo)

flatsData = get_investment_flats(investmentsData, flatsHtmlInfo)
