from db_utils import DBManager
from data_loader import push_data_into_database

def main():
    # Загрузка данных в базу данных
    push_data_into_database()

    db_manager = DBManager("homework_hh", "postgres", "12345678", "localhost", "5432")
    # Получить список всех компаний и количества вакансий у каждой компании
    companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
    print("Компании и колво вакансий:")
    for company, vacancy_count in companies_and_vacancies_count.items():
        print(f"{company}: {vacancy_count} vacancies")

    # Получить список всех вакансий
    all_vacancies = db_manager.get_all_vacancies()
    print("Все вакансии:")
    for vacancy in all_vacancies:
        print(vacancy)

    # Получить среднюю зарплату по вакансиям
    avg_salary = db_manager.get_avg_salary()
    print(f"Средняя зарплата по вакансиям: {avg_salary}")

    # Получить список вакансий с зарплатой выше средней
    high_salary_vacancies = db_manager.get_vacancies_with_higher_salary()
    print("\nВакансии с зп выше среднего:")
    for vacancy in high_salary_vacancies:
        print(vacancy)

    # Получить список вакансий, в названии которых содержатся ключевые слова
    keyword = "python"
    keyword_vacancies = db_manager.get_vacancies_with_keyword(keyword)
    print(f"\nВакансии с ключевым словом '{keyword}':")
    for vacancy in keyword_vacancies:
        print(vacancy)
    # Закрытие соединения с базой данных
    db_manager.close_connection()

if __name__ == "__main__":
    main()
