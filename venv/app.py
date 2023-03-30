from flask import Flask, render_template
import requests


app = Flask(__name__)  # instance of flask app with name app


import requests

url = 'http://localhost:8080/api/json?tree=jobs[name,color,url,lastBuild[number,duration,timestamp,result]]'
username = 'admin'
password = '11d77a3497adeac8b800862b49fcb1c0e2'

response = requests.get(url, auth=(username, password))
headers = response.headers
print(response.status_code)
count=0

job_list = response.json()['jobs']   # List of dictionaries 
for job in job_list:
    count += 1
    print(job['name'])
    print(job.get('color', 'No color specified'))
    print(job.get('url','No URL Specified'))

@app.route("/")  # when user enters the root URL home function is executed
def home():
    
    if response.status_code == 200:
    
       return render_template('jenkins.html', jobs=job_list, count=count,headers=headers)

