from locust import TaskSet, between, HttpUser, task
import random
import json


class MyTasks(TaskSet):

    names = ["Alice", "Bob", "Charlie", "David", "Eve",
             "Frank", "Grace", "Hannah", "Ivy", "Jack"]

    @task
    def createUser(self):
        name = random.choice(self.names)
        payload = {
            "name": f"{name}",
            "email": f"{name.lower()}@gmail.com"
        }
        headers = {"Content-Type": "application/json"}

        res = self.client.post(
            "/users", data=json.dumps(payload), headers=headers)
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def getUser(self):
        res = self.client.get("/users")
        print(res.text)
        print(res.status_code)
        print(res.headers)


class MyUser(HttpUser):
    host = "http://127.0.0.1:5000/"
    wait_time = between(1, 3)
    tasks = [MyTasks]
