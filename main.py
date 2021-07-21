from container import Container
import subprocess
import threading
import requests
import json
from job import Job
import re

containers = [
    Container(1, "172.18.0.2"),
    Container(2, "172.18.0.3"),
    Container(3, "172.18.0.4")
]
jobs = []
stop = False


def docker_compose_up():
  # process = subprocess.Popen(["docker-compose", "--file", "image/docker-compose.yml", "up", "-d", "--scale", "baba=3"]).wait()
  process = subprocess.Popen(["docker-compose", "--file", "image/docker-compose.yml", "up", "-d", "--build", "--scale", "baba=3"]).wait()
def docker_compose_down():
  process = subprocess.Popen(["docker-compose", "--file", "image/docker-compose.yml", "down"]).wait()


def dispatch(container):
  global containers
  job = container.get_job()
  req = requests.get(f"http://{container.get_ip()}:50051/", data=json.dumps({
      "code": job.get_code(),
      "input": job.get_input(),
      "output": job.get_output()
  }))
  print(
      f"• job-{container.get_job()} completed with result {req.json()['status']}")
  container.clear()


def load_balance():
  global containers, jobs
  while not stop:
    for container in containers:
      if len(jobs) != 0 and not container.get_state():
        job = jobs.pop()
        print(f"○ Assigning job-{job} to container-{container.get_id()}")
        container.set_job(job)
        threading.Thread(target=dispatch, args=(container, )).start()


def cli():
  global stop, jobs
  print(">> Machine started...")
  print(">> enter your request or $status to check containers")
  threading.Thread(target=load_balance).start()

  last_job_id = 1

  while True:
    input_command = input()
    if input_command == ":wq":
      stop = True
      docker_compose_down()
      break
    elif input_command == ":status":
      print(">> container states:")
      for container in containers:
        state = "idle"
        if container.get_state():
          state = "active"
        print(f"\t • container {container.get_id()} is {state}")
    else:
      raw_jobs = re.findall("<(.*?)>", input_command)
      for raw_job in raw_jobs:
        last_job_id += 1
        [code, input_path, output_path] = list(
            map(lambda job: job.strip(), raw_job.split(",")))
        jobs.append(Job(last_job_id, code, input_path, output_path))



docker_compose_up()
cli()
