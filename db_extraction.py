import sqlite3
import os
import shutil
import platform


# Get the os for the proper file directory
if (platform.system() == 'Darwin'):
    source_path = '/Users/' + os.getlogin() + '/library/applicationsupport/google/chrome/default/history'
elif (platform.system() == 'Windows'):
    source_path = 'C:/Users/' + os.getlogin() + '/AppData/Local/Google/Chrome/User Data/default/history'


current_directory = os.getcwd() + "/history"


shutil.copyfile(source_path, current_directory)

connect = sqlite3.connect('history')
cursor = connect.cursor()

keywords = ["youtube", "tiktok", "facebook"]
truth = []

for keyword in keywords:
    query = f"SELECT * FROM urls WHERE title LIKE '%{keyword}%'"
    cursor.execute(query)   
    item = cursor.fetchone()
    if (item):
        truth.append("Your child has been on: " + keyword)


# Process the results (e.g., print them)
for row in truth:
    print(row)

# Close the connection
connect.close()

if (os.path.exists(current_directory)):
    os.remove(current_directory)
    print("File deleted successfully.")
else:
    print("File does not exist")