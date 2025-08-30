from locust import SequentialTaskSet, HttpUser, task, constant
from readcsv import ReadCsv
import json

class Mytasks(SequentialTaskSet):

    @task
    def createUser(self):
        data = ReadCsv("dataParameterization/names.csv").read()
        payload = {
            "name": data['name'],
            "email": data['email']
        }
        name = f"User created for {data['name']}"
        with self.client.post("/users", catch_response=True, data=json.dumps(payload), name=name, headers={"content-type":"application/json"}) as response:
            if response.status_code == 201 and data['name'] in response.text:
                response.success()
            else:
                response.failure(f"User not created for {data['name']}")


class MyUser(HttpUser):
    host = "http://localhost:5000"
    tasks = [Mytasks]
    wait_time = constant(1)
