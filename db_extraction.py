import sqlite3

connect = sqlite3.connect('history')
# connect = sqlite3.connect('/Users/thomasmerritt/library/applicationsupport/google/chrome/default/history')
cursor = connect.cursor()

keywords = ["youtube", "tiktok"]
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
