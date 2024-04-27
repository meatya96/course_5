import psycopg2

class DBManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        query = """
            SELECT companies.name, COUNT(vacancies.company_id) AS vacancy_count
            FROM companies
            LEFT JOIN vacancies ON companies.company_id = vacancies.company_id
            GROUP BY companies.name;
        """
        self.cur.execute(query)
        return {row[0]: row[1] for row in self.cur.fetchall()}

    def get_all_vacancies(self):
        query = """
            SELECT company_id, title, salary, link, description
            FROM vacancies;
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_avg_salary(self):
        query = """
            SELECT AVG(salary) AS avg_salary
            FROM vacancies
            WHERE salary IS NOT NULL;
        """
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result[0] if result else None

    def get_vacancies_with_higher_salary(self):
        avg_salary = self.get_avg_salary()
        if not avg_salary:
            return []
        query = """
            SELECT company_id, title, salary, link, description
            FROM vacancies
            WHERE salary > %s;
        """
        self.cur.execute(query, (avg_salary,))
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        query = """
            SELECT company_id, title, salary, link, description
            FROM vacancies
            WHERE LOWER(title) LIKE %s;
        """
        self.cur.execute(query, ('%' + keyword.lower() + '%',))
        return self.cur.fetchall()

    def close_connection(self):
        self.conn.close()
