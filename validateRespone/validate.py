from locust import SequentialTaskSet, task, constant, HttpUser

class MyTasks(SequentialTaskSet):

    @task
    def accessAlpha(self):
        result = self.client.get("/alpha", name="ALPHA")
        print(result)

    @task
    def getContent(self):
        with self.client.get("/alpha", catch_response=True, name="RESPONSE") as response:
            result = True if "Alpha" in response.text else False
            print(self.getContent.__name__, result)
            response.success()

    @task
    def getFailure(self):
        result = "Failed"
        with self.client.get("/alpha", catch_response=True, name="CODENAME") as response:
            if "Alpha" in response.text:
                result = "Success"
                response.failure("Not a failure")  # Marking this success request intentional failure
            print(self.getFailure.__name__, result)


    @task
    def get404(self):
        with self.client.get("/404", catch_response=True, name="404") as response:
            if response.status_code == 404:
                response.failure("Got 404!") # Failed request
            else:
                response.success()

class MyTest(HttpUser):
    tasks = [MyTasks]
    wait_time = constant(1)