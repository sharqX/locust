from locust import User, task, constant


class FirstScript(User):

    wait_time = constant(1)
    weight = 2
    
    @task
    def task1(self):
        print("Task 1: Completed")

    @task
    def task2(self):
        print("Task 2: Completed")

class SecondScript(User):

    wait_time = constant(1)
    weight = 2
    
    @task
    def task1(self):
        print("Task 3: Completed")

    @task
    def task2(self):
        print("Task 4: Completed")

