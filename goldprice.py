import requests
import json
from typing import Dict, List

class GetUrl(object):
    
    def __init__(self, url):
        self.url = url

    def info_url(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code}")

class ExtractData(GetUrl):
    def __init__(self, url):
        super().__init__(url)

    def extract_data(self) -> Dict[str, List[Dict[str, str]]]:
        data = self.info_url() 
        extracted_data = {
            "gold": [],
            "currency": []
        }

        for i in data["gold"]:
            r = {"name": i["name"], "price": i["price"], "unit": i["unit"]}
            extracted_data["gold"].append(r)

        for i in data["currency"]:
            r = {"name": i["name"], "price": i["price"], "unit": i["unit"]}
            extracted_data["currency"].append(r)

        return extracted_data

class JSON_FILE(ExtractData):
    def __init__(self, url, file_name):
        super().__init__(url)
        self.file_name = file_name

    def writing(self):
        with open(self.file_name, "w", encoding='utf-8') as ww:
            json.dump(self.extract_data(), ww, ensure_ascii=False, indent=1)  # Added indent for better readability

url = 'https://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency.json'  
file_name = 'data.json'  
json_writer = JSON_FILE(url, file_name)

try:
    json_writer.writing() 
    print(f"Data successfully written to {file_name}.")
except Exception as e:
    print(e)
