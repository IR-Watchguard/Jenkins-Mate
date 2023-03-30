import requests

url = 'http://localhost:8080/api/json?tree=jobs[name]'
username = 'admin'
password = '11d77a3497adeac8b800862b49fcb1c0e2'

response = requests.get(url, auth=(username, password))
print(response.status_code)

job_list = response.json()['jobs']   # List of dictionaries 
for job in job_list:
    print(job['name'])
    print(job.get('color', 'No color specified'))
    print(job.get('url','No URL Specified'))
    
  
    
    
    