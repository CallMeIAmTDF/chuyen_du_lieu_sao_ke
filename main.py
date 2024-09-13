import csv
import mysql.connector
import datetime
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='testdata')
cursor = cnx.cursor()

# CSV file path
csv_file_path = './csv/data_1_31.csv'
count = 1
with open(csv_file_path, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        print(f"dang xuat dong {count}")
        date_str = row[0]
        formatted_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
        row[0] = formatted_date
        cursor.execute("INSERT INTO test (date, no, credit, detail) VALUES (%s, %s, %s, %s)", row)
        count+=1
cnx.commit()
cursor.close()
cnx.close()