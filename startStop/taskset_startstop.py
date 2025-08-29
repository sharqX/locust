from locust import HttpUser, TaskSet, task, constant
import json


# Task are being executed randomly between getUser and accessAlpha
class MyLoadTest(TaskSet):

    payload = {
        "name": "Jack",
        "email": "cactus@gmail.com"
    }

    def on_start(self):
        res = self.client.post("/users", data=json.dumps(self.payload),
                               headers={"Content-Type": "application/json"})
        print(res.text)
        print(res.status_code)

    @task
    def getUser(self):
        res = self.client.get("/users/1")
        print(res.text)
        print(res.status_code)

    @task
    def accessAlpha(self):
        res = self.client.get("/alpha")
        print(res.text)

    def on_stop(self):
        self.client.delete("/users/1")
        print("Delted User: Jack")


class MyUser(HttpUser):
    host = "http://localhost:5000"
    wait_time = constant(1)
    tasks = [MyLoadTest]
