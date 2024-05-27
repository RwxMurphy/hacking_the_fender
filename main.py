import csv
import json
import boss_message as bm

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
    
# Notify the boss
with open('boss_message.json', 'w') as boss_message:
    json.dump(bm.boss_message_dict, boss_message)
