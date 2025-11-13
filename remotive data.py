import requests
import csv

# Step 1: API URL
url = "https://remotive.com/api/remote-jobs"

# Step 2: Fetch data from the website
response = requests.get(url)
data = response.json()

# Step 3: Extract job list
jobs = data['jobs']

# Step 4: Save to CSV file (in Download folder)
with open('/storage/emulated/0/Download/remotive_jobs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Company", "Category", "Location"])

    for job in jobs:
        writer.writerow([
            job["title"],
            job["company_name"],
            job["category"],
            job["candidate_required_location"]
        ])

print("✅ Data saved successfully in 'Download/remotive_jobs.csv'")