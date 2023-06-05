from services.scrape_logic.scrape_functions import get_developer_info, get_developer_investments, get_investment_flats

developerName = 'Yuniversal Podlaski'
baseUrl = 'https://www.yuniversalpodlaski.pl/'
cityTag = '#bialystok'

investmentHtmlInfo = {
    'investmentTag': ".find_all(lambda tagy: tagy.name == 'a' and tagy.get('class') == ['box_inwestycja'] or tagy.get('class') == ['box_inwestycja', 'big2'], "
                     "attrs={'data-city': 'Bialystok'})",
    'investmentName': ".find(class_='nazwa').get_text().encode('iso-8859-1').decode('utf-8')",
    'investmentLink': "['href']"}

investmentsInfo = get_developer_investments(baseUrl + cityTag, investmentHtmlInfo)

flatsHtmlInfo = {'flatTag': ".tbody.find_all('tr', class_='lokal_row')",
                 'floorNumber': ".find(class_='t_pietro').get_text()",
                 'roomsAmount': ".find(class_='t_pokoje').get_text()",
                 'area': ".find(class_='t_metraz').get_text().replace('m²', '').strip()",
                 'price': ".find(class_='t_cena').get_text().split('PLN')[0].strip().replace(',', '.').replace(' ','')",
                 'status': ".find(class_='t_metraz').find_next_sibling().get_text()"
                           ".encode('iso-8859-1').decode('utf-8')"}

developerData = get_developer_info(developerName, baseUrl)

investmentsData = list(map(lambda item: {
    'name': item['name'],
    'url': baseUrl + item['url']
}, investmentsInfo))

flatsData = get_investment_flats(investmentsInfo, flatsHtmlInfo, baseUrl)
