import os
import re
import importlib.util

from main_path import get_main_path


class DeveloperScrapeList:
    files = os.listdir(get_main_path() + '/scrapes')

    @classmethod
    def get_developer_list(cls):
        pattern = re.compile(r"_scrape\.py$")

        data = [{
            "developer_id": index,
            "developer_name": file.replace(pattern.search(file).group(), '').replace("_", " ").title()}
            for index, file in enumerate(cls.files, start=0)
            if pattern.search(file)]

        return data


class ScrapeDeveloper(DeveloperScrapeList):
    def __init__(self, index):
        self.index = index
        self.developerData = None
        self.investmentsData = None
        self.flatsData = None
        userChoice = list(filter(lambda item: item['developer_id'] == self.index, self.get_developer_list()))
        self.filename = userChoice[0]['developer_name'].lower().replace(" ", "_") + '_scrape.py'

    def get_developer_data(self):
        spec = importlib.util.spec_from_file_location(self.filename, f"{get_main_path()}/scrapes/{self.filename}")
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)

        self.developerData = foo.developerData
        self.investmentsData = foo.investmentsData
        self.flatsData = foo.flatsData
