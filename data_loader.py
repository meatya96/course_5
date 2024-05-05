import psycopg2
from hh_get_data import get_companies_data, get_vacancies_data

def push_data_into_database(user, password):

    '''
     Данная функция:
     Получаеn данные о компаниях и вакансиях
     Подключается к базе данных
     Заполняет таблицы companies данными
     Заполняет таблицы vacancies данными
     Обрабатывает значения salary или другое значение, которое нужно использовать в случае отсутствия информации о зарплате

     '''

    companies_data = get_companies_data()
    vacancies_data = get_vacancies_data()

    conn = psycopg2.connect(dbname="homework_hh", user=user, password=password, host="localhost", port="5432")
    cur = conn.cursor()

    try:

        for company in companies_data:
            cur.execute("""
                INSERT INTO companies (company_id, name, industry, location, description)
                VALUES (%s, %s, %s, %s, %s)
            """, (company.get('company_id'), company.get('name'), company.get('industry'), company.get('location'), company.get('description')))


        for vacancy in vacancies_data:
            vacancy_id = vacancy.get('vacancy_id')
            company_id = vacancy.get('company_id')
            title = vacancy.get('title')
            salary = vacancy.get('salary')
            link = vacancy.get('link')
            description = vacancy.get('description')


            if salary == "No salary info":
                salary = None  #когда нет зп

            cur.execute("""
                INSERT INTO vacancies (vacancy_id, company_id, title, salary, link, description)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (vacancy_id, company_id, title, salary, link, description))


        conn.commit()
        print("Данные успешно загружены в базу данных.")
    except Exception as e:
        conn.rollback()
        print(f"Произошла ошибка при загрузке данных: {e}")
    finally:

        conn.close()

if __name__ == "__main__":
    push_data_into_database()
