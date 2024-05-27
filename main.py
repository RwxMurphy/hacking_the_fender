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

# Scramble password 
slash_null_sig = r"""
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

with open('new_passwords.csv', 'w') as new_password_obj:
    new_password_obj.write(slash_null_sig)
    