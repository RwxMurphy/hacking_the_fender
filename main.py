import csv

# Read csv
compromised_users:str = []
with open('passwords.csv', newline='') as password_file:
    password_csv = csv.DictReader(password_file)
    for psw_row in password_csv:
        compromised_users.append(psw_row['Username'])

# Create txt file save comp_users
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + '\n')
    
