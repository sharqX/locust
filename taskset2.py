from locust import TaskSet, HttpUser, constant, task

# Nested TaskSet
# class GetAplha(TaskSet):

#     @task
#     def getAplha(self):
#         res = self.client.get("/alpha")
#         print(res.text)
        
#     @task
#     class GetGamma(TaskSet):

#         @task
#         def getGamma(self):
#             res = self.client.get("/gamma")
#             print(res.text)
#             self.interrupt(reschedule=False) # if set True returns to parent class immediately 

class GetBeta(TaskSet):

    @task
    def getAplha(self):
        res = self.client.get("/beta")
        print(res.text, "🟢")
        self.interrupt(reschedule=False)

class GetDelta(TaskSet):

    @task
    def getAplha(self):
        res = self.client.get("/delta")
        print(res.text, "🔴")
        self.interrupt(reschedule=False)


class MyHttpUser(HttpUser):
    host = "http://localhost:5000"
    tasks = [GetBeta, GetDelta]
    wait_time = constant(1)