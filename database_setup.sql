drop table if exists vacancies;
drop table if exists companies;

-- Создание таблицы companies для хранения данных о компаниях
CREATE TABLE IF NOT EXISTS companies (
    company_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    industry VARCHAR(255),
    location VARCHAR(255),
    description TEXT
);

-- Создание таблицы vacancies для хранения данных о вакансиях
CREATE TABLE IF NOT EXISTS vacancies (
    vacancy_id INT PRIMARY KEY,
    company_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    salary INT,
    link VARCHAR(255),
    description TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
