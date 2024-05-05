from db_utils import DBManager
from data_loader import push_data_into_database
from init_db import create_db, create_tables
import os
from dotenv import load_dotenv


def main():
    '''
         Данная функция Загружает данные в базу данных
         Получаеи список всех компаний и количество вакансий у каждой компании
         Получает список всех вакансий
         Получает среднюю зарплату по вакансиям
         Получает список вакансий с зарплатой выше средней
         Получает список вакансий, в названии которых содержатся ключевые слова
        '''
    load_dotenv()
    # Получение данных для подключения из переменных окружения
    user = os.environ.get('PGUSER')
    password = os.environ.get('PGPASSWORD')
    # Создание бд и таблиц
    create_db()
    create_tables("postgres", "12345678")
    # Загрузка данных в базу данных
    push_data_into_database(user, password)

    db_manager = DBManager("homework_hh", user, password, "localhost", "5432")

    companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
    print("Компании и колво вакансий:")
    for company, vacancy_count in companies_and_vacancies_count.items():
        print(f"{company}: {vacancy_count} vacancies")

    all_vacancies = db_manager.get_all_vacancies()
    print("Все вакансии:")
    for vacancy in all_vacancies:
        print(vacancy)

    avg_salary = db_manager.get_avg_salary()
    print(f"Средняя зарплата по вакансиям: {avg_salary}")

    high_salary_vacancies = db_manager.get_vacancies_with_higher_salary()
    print("\nВакансии с зп выше среднего:")
    for vacancy in high_salary_vacancies:
        print(vacancy)

    keyword = "python"
    keyword_vacancies = db_manager.get_vacancies_with_keyword(keyword)
    print(f"\nВакансии с ключевым словом '{keyword}':")
    for vacancy in keyword_vacancies:
        print(vacancy)

    db_manager.close_connection()


if __name__ == "__main__":
    main()
