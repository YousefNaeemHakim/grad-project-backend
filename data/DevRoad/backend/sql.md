# SQL Learning Summary

SQL, or Structured Query Language, is a programming language used to manage and manipulate relational databases. It is an essential tool for data analysts, data scientists, and anyone working with large amounts of data. In this summary, we will cover the basics of SQL, including syntax and commonly used commands.

## Basic SQL Syntax

SQL commands are generally written in capital letters and end with a semicolon (;). The basic syntax for SQL queries is as follows:

```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name
HAVING condition
ORDER BY column_name;

```

## SELECT Statement

The SELECT statement is used to retrieve data from one or more tables in a database. You can select all columns in a table using an asterisk (\*), or you can specify specific columns by name.

```
SELECT *
FROM employees;

```

```
SELECT first_name, last_name, salary
FROM employees;

```

## WHERE Clause

The WHERE clause is used to filter records based on a specified condition. You can use logical operators such as AND, OR, and NOT to combine conditions.

```
SELECT *
FROM employees
WHERE salary > 50000;

```

```
SELECT *
FROM employees
WHERE department = 'Marketing' AND salary > 50000;

```

## ORDER BY Clause

The ORDER BY clause is used to sort records in ascending or descending order based on one or more columns.

```
SELECT *
FROM employees
ORDER BY salary DESC;

```

```
SELECT *
FROM employees
ORDER BY department ASC, salary DESC;

```

## GROUP BY Clause

The GROUP BY clause is used to group records based on one or more columns. You can also use aggregate functions such as SUM, AVG, and COUNT to perform calculations on grouped data.

```
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

```

```
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

```

## HAVING Clause

The HAVING clause is used to filter records based on a specified condition after the GROUP BY clause has been applied.

```
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

```

## Joins

Joins are used to combine data from multiple tables based on a common column. There are several types of joins, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN.

```
SELECT employees.first_name, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;

```

## Subqueries

Subqueries are used to perform queries within queries. They can be used to filter data, perform calculations, or retrieve data from another table.

```
SELECT *
FROM employees
WHERE department_id IN
  (SELECT department_id
   FROM departments
   WHERE department_name = 'Marketing');

```

## Aggregate Functions

Aggregate functions are used to perform calculations on groups of rows. Some commonly used aggregate functions include SUM, AVG, MIN, MAX, and COUNT.

```
SELECT AVG(salary)
FROM employees;

```

```
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

```

## Wildcards

Wildcards are used to match patterns in data. The two most commonly used wildcards are the percent sign (%) and underscore (\_).

```
SELECT *
FROM employees
WHERE last_name LIKE 'Sm%';

```

```
SELECT *
FROM employees
WHERE first_name LIKE '_a%';

```

## NULL Values

NULL values represent missing or unknown data. You can use the IS NULL and IS NOT NULL operators to filter data based on NULL values.

```
SELECT *
FROM employees
WHERE manager_id IS NULL;

```

```
SELECT *
FROM employees
WHERE manager_id IS NOT NULL;

```

These are just a few additional topics you may find helpful when learning SQL. With practice and experience, you can become proficient in using SQL to manage and manipulate data.