import os
import re
import importlib.util

from main_path import get_main_path


def get_developer_list_to_scrape():
    files = os.listdir(get_main_path() + '/scrapes')

    pattern = re.compile(r"_scrape\.py$")

    data = [{
        "developer_id": index,
        "developer_name": file.replace(pattern.search(file).group(), '').replace("_", " ").title()}
        for index, file in enumerate(files, start=1)
        if pattern.search(file)]
    return data


def get_info_from_scrape(number: int):
    data = get_developer_list_to_scrape()

    userChoice = list(filter(lambda item: item['developer_id'] == number, data))
    filename = userChoice[0]['developer_name'].lower().replace(" ", "_") + '_scrape.py'

    spec = importlib.util.spec_from_file_location(filename, f"{get_main_path()}/scrapes/{filename}")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    return [foo.developerData, foo.investmentsData, foo.flatsData]
