import requests

def get_companies_data():
    companies = {
        "Wildberries":87021,
        "Ozon":2180,
        "Avito":84585,
        "Tinkoff":78638,
        "Sber":3529,
        "Точка":2324020,
        "Lamoda":780654,
        "Альфа-Банк":80,
        "Яндекс":1740,
        "VK":15478
    }

    company_data = []

    for company in companies.items():
        industry = "IT"
        location = "Москва"
        description = "Описание компании"

        company_data.append({
            "company_id": company[1],
            "name": company[0],
            "industry": industry,
            "location": location,
            "description": description
        })

    return company_data

def get_vacancies_data():
    companies = {
        "Wildberries":87021,
        "Ozon":2180,
        "Avito":84585,
        "Tinkoff":78638,
        "Sber":3529,
        "Точка":2324020,
        "Lamoda":780654,
        "Альфа-Банк":80,
        "Яндекс":1740,
        "VK":15478
    }

    vacancies = []

    for company in companies.items():
        url = "https://api.hh.ru/vacancies"
        params = {
            "area": 1,
            "per_page": 5,
            "employer_id": company[1]
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for item in data["items"]:
                vacancy_id = item["id"]
                company_id = item["employer"]["id"]
                title = item["name"]
                salary = item["salary"]["from"] if item.get("salary") else "No salary info"
                link = item["alternate_url"]
                description = item["snippet"]["requirement"]
                vacancies.append({
                    "vacancy_id": vacancy_id,
                    "company_id": company_id,
                    "link": link,
                    "company": company[0],
                    "description": description,
                    "title": title,
                    "salary": salary
                })
        else:
            print(f"Failed to fetch vacancies for {company}. Status code: {response.status_code}")

    return vacancies

if __name__ == "__main__":
    vacancies = get_vacancies_data()
    for vacancy in vacancies:
        print(vacancy)
    companies = get_companies_data()
    for company in companies:
        print(company)
