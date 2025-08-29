from locust import HttpUser, constant, task


class TryHttpUser(HttpUser):

    host = ("http://127.0.0.1:5000/")
    wait_time = constant(1)

    @task(weight=1)
    def createUser(self):
        res = self.client.post(
            "/users", data='{ "name" : "Jack", "email" : "jack@gmail.com" }', headers={"Content-Type": "application/json"})
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task(weight=2)
    def getUser(self):
        res = self.client.get("/users")
        print(res.text)
        print(res.status_code)
        print(res.headers)
