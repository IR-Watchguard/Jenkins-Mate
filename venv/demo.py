from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://localhost:8080'
    server = Jenkins(jenkins_url, username='admin', password='11d77a3497adeac8b800862b49fcb1c0e2')
    return server

def get_job_details():
    server = get_server_instance()
    for job_name, job_instance in server.get_jobs():
        print(f"Job Name : {job_instance.name}")
        
get_job_details()