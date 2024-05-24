import csv

compromised_users = []
with open('passwords.csv', newline='') as password_file:
    password_csv = csv.DictReader(password_file)
    for psw_row in password_csv:
        compromised_users.append(psw_row['Username'])

print(compromised_users)