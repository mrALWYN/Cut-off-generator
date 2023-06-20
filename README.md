# Cut off generator
 The Objective of the python code is to create a cutoff list according to the reservation categories and marks. The programme asks for user input on the cutoff percentages for each reservation categories.
 The programme uses mysql package to import database from mysql server and tabulate package to present the final cutoff list in a tabular form. and it uses inbuilt package csv to download the final list in a csv format

 # Functioning of the Code
 The mysql.connector module allows connecting to and interacting with a MySQL database, while tabulate is a module used for formatting and printing tabular data.
 This is a function connect_to_db() that establishes a connection to a MySQL database. It tries to connect using the provided host, user, password, and database name. If the connection is successful, it prints a success message and returns the connection object. If there's an error, it prints an error message and returns None which means there was an error in . 

 # Basic Requirements to Run the code
 1.MySQL package: to install the package, in cmd run pip install my sql and pip instal mysql-connector
 2.Tabulate Package: Run pip install tabulate 
  

The code you provided is a Python script that connects to a MySQL database, generates a cutoff list of students based on specified criteria, and prints the cutoff list using the tabulate library. Here's a breakdown of the code:
1.	The script imports the mysql.connector library for connecting to the MySQL database and the tabulate library for formatting and printing the cutoff list.
2.	The connect_to_db() function is defined to establish a connection to the MySQL database. It takes no parameters and returns the connection object if successful, or None if there was an error.
3.	The generate_cutoff_list() function is defined to generate the cutoff list of students. It takes several parameters: conn (the database connection object), merit_pct, sc_pct, st_pct, ews_pct (cutoff percentages for each category), merit_count, sc_count, st_count, and ews_count (the number of students to include from each category). It returns the cutoff list as a list of student records.
4.	The print_cutoff_list() function is defined to print the cutoff list in a tabular format. It takes the cutoff_list as a parameter and uses the tabulate library to format and print the data.
5.	The main() function is defined as the entry point of the script. It calls the connect_to_db() function to establish a connection to the MySQL database.
6.	If the connection is successful, the user is prompted to enter the cutoff percentages and the number of students to include from each category.
7.	The generate_cutoff_list() function is called with the specified parameters to generate the cutoff list.
8.	The print_cutoff_list() function is called to print the cutoff list.
9.	The connection to the database is closed.
10.	The script checks if the script is being run as the main module (__name__ == '__main__') and calls the main() function if true.
Requirements:
•	Python: The code requires Python to be installed on the system.
•	mysql.connector library: This library is used to connect to the MySQL database. It can be installed using pip install mysql-connector-python.
•	tabulate library: This library is used to format and print the cutoff list in a tabular format. It can be installed using pip install tabulate.
Please note that the code assumes the existence of a MySQL database named "students" and a table named "st_name" within that database. The table should have columns for student ID, name, total percentage, and reservation category.
