#!/usr/bin/env python
# coding: utf-8

# In[7]:


import mysql.connector
from tabulate import tabulate
import csv

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1062@lbn",
            database="students"
        )
        print("Connected to the MySQL database!")
        return conn
    except mysql.connector.Error as error:
        print("Failed to connect to the MySQL database: {}".format(error))
        return None

def generate_cutoff_list(conn, merit_pct, sc_pct, st_pct, ews_pct, merit_count, sc_count, st_count, ews_count):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students.st_name")
        students = cursor.fetchall()

        cutoff_list = []

        merit_students = [student for student in students if student[-2] >= merit_pct]
        cutoff_list.extend(merit_students[:merit_count])

        sc_students = [student for student in students if student[-1] == 'SC' and student[-2] >= sc_pct]
        cutoff_list.extend(sc_students[:sc_count])

        ews_students = [student for student in students if student[-1] == 'EWS' and student[-2] >= ews_pct]
        cutoff_list.extend(ews_students[:ews_count])

        st_students = [student for student in students if student[-1] == 'ST' and student[-2] >= st_pct]
        cutoff_list.extend(st_students[:st_count])

        return cutoff_list

    except mysql.connector.Error as error:
        print("Failed to fetch data from the MySQL database: {}".format(error))
        return []

def print_cutoff_list(cutoff_list):
    headers = ["Student ID", "Name", "Total Percentage", "Reservation Category"]
    table_data = []

    for student in cutoff_list:
        student_id = student[0]
        name = student[1]
        total_pct = student[-2]
        reservation_category = student[-1]
        table_data.append([student_id, name, total_pct, reservation_category])

    print("Cutoff List:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def download_cutoff_list_csv(cutoff_list):
    headers = ["Student ID", "Name", "Total Percentage", "Reservation Category"]
    rows = [[student[0], student[1], student[-2], student[-1]] for student in cutoff_list]
    file_name = "cutoff_list.csv"

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"CSV file '{file_name}' has been created successfully.")

def main():
    connection = connect_to_db()

    if connection:
        merit_pct = float(input("Enter the cutoff percentage for the merit category: "))
        sc_pct = float(input("Enter the cutoff percentage for the SC category: "))
        st_pct = float(input("Enter the cutoff percentage for the ST category: "))
        ews_pct = float(input("Enter the cutoff percentage for the EWS category: "))
        merit_count = int(input("Enter the number of students to include from the merit category: "))
        sc_count = int(input("Enter the number of students to include from the SC category: "))
        st_count = int(input("Enter the number of students to include from the ST category: "))
        ews_count = int(input("Enter the number of students to include from the EWS category: "))

        cutoff_list = generate_cutoff_list(
            connection,
            merit_pct,
            sc_pct,
            st_pct,
            ews_pct,
            merit_count,
            sc_count,
            st_count,
            ews_count
        )

        print_cutoff_list(cutoff_list)

        option = input("Do you want to download the cutoff list as a CSV file? (yes/no): ")
        if option.lower() == "yes":
            download_cutoff_list_csv(cutoff_list)

        connection.close()

if __name__ == '__main__':
    main()

