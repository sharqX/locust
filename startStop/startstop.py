from locust import User, constant, task

class MyUser(User):

    wait_time = constant(1)

    def on_start(self):
        print("Start")
    
    @task
    def mytask(self):
        print("Task Executing")
    
    def on_stop(self):
        print("Stop")
