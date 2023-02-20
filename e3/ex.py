import time
from concurrent.futures import ThreadPoolExecutor, Future

import requests


def call_nationalize_api(name: str):
    url = f"https://api.nationalize.io/"
    params = {
        "name": f"{name}"
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Got an error: status code: {res.status_code}")


def call_country_code_api(country_code: str):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.lower()}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Got an error: status code: {res.status_code}")


def get_country_for_single_name(name):
    print('running for ', name)
    try:
        nationalize_res = call_nationalize_api(name)
        max_prob = 0
        for item in nationalize_res["country"]:
            if item["probability"] > max_prob:
                max_prob = item["probability"]
                country_code = item["country_id"]
        country_data = call_country_code_api(country_code)
        country_name = country_data[0]["name"]['common']
        return {'name': name, 'country': country_name}
    except Exception as e:
        print(e)
        return None


def name_done_callback(future: Future):
    try:
        country_and_name = future.result()
        print(country_and_name)
    except Exception as e:
        print("Error", e)


def get_country_for_names(names_list: list[str]):
    with ThreadPoolExecutor() as executor:
        for name in names_list:
            future = executor.submit(get_country_for_single_name, name)
            future.add_done_callback(name_done_callback)


if __name__ == '__main__':
    start = time.time()
    get_country_for_names([
        'Valeria', 'Barel', 'Slava',
        'Daniel', 'Or', 'Avner', 'Nadav', 'Gal'])
    print(time.time() - start)


