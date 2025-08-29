from locust import SequentialTaskSet, task, HttpUser, constant

class MySequence(SequentialTaskSet):

    @task
    def task1(self):
        res = self.client.get("/epsilon")
        print(res.text)

    @task
    def task2(self):
        res = self.client.get("/delta")
        print(res.text)

class MyHttpUser(HttpUser):
    tasks = [MySequence]
    wait_time = constant(1)