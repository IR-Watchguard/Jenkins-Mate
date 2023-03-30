from flask import Flask, render_template
import requests


app = Flask(__name__)  # instance of flask app with name app

# Jenkins 1
username = 'admin'
password = '11d77a3497adeac8b800862b49fcb1c0e2'

url = 'http://localhost:8080/api/json?tree=jobs[name,color,url,lastBuild[number,duration,timestamp,result]]'
response = requests.get(url, auth=(username, password))
headers = response.headers

# Jenkins 2
username2 = 'admin'
password2 = '11604f065eca70b0b975539cd7140d38e3'

url2 = 'http://localhost:8081/api/json?tree=jobs[name,color,url,lastBuild[number,duration,timestamp,result]]'
response2 = requests.get(url2, auth=(username2, password2))
print(response2.status_code)
headers2 = response2.headers


# print(response.status_code)
count=0


# Jenkins 1
job_list = response.json()['jobs']   # List of dictionaries 
for job in job_list:
    count += 1
    ur = job['url'] + 'api/json'
    res1 = requests.get(ur, auth=(username, password))
    job['num'] = res1.json()['lastStableBuild']['number']
    job['lastBuild'] = res1.json()['lastBuild']['number']
    job['lastSuccessfulBuild'] = res1.json()['lastSuccessfulBuild']['number']
    

# Jenkins 2
count2 = 0
job_list2 = response2.json()['jobs']   # List of dictionaries 
for job in job_list2:
    count += 1
    ur2 = job['url'] + 'api/json'
    res1 = requests.get(ur2, auth=(username2, password2))
    job['num'] = res1.json()['lastStableBuild']['number']
    job['lastBuild'] = res1.json()['lastBuild']['number']
    job['lastSuccessfulBuild'] = res1.json()['lastSuccessfulBuild']['number']
    

    #job['lastFailedBuild'] = res1.json()['lastFailedBuild']['number']
    
    
    # job['num'] = res1.json()['lastStableBuild']['number']
    # job['num'] = res1.json()['lastStableBuild']['number'] 
    # # print(res1.json()['lastStableBuild']['number'])
    # print(res1.status_code)
    # jobsdemo = []
    # print(res1.json()['lastStableBuild'['number']])
    # print(ur)
    # print(job['name'])
    # print(job.get('color', 'No color specified'))
    # print(job.get('url','No URL Specified'))


@app.route("/")  # when user enters the root URL home function is executed
def home():
    
    if response.status_code == 200:
    
       return render_template('jenkins.html', jobs=job_list, jobs2=job_list2, count=count,count2=count2, headers=headers,headers2=headers2 )

