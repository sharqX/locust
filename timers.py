from locust import User, task, constant, between, constant_pacing
import time

class MyUser(User):
    

    # wait_time = constant(1)
    # wait_time = between(2,5)
    wait_time = constant_pacing(2)

    # @task
    # def constantDelay(self):
    #     print("Delay of 1 second") # from wait_time = constant(1)

    # @task
    # def variableDelay(self):
    #     print("Delay 2 to 5 seconds") # from wait_time = between(2,5)
    
    @task 
    def constantPacingDelay(self):
        time.sleep(3)
        print("This is Constant Pacing") # this task is taking 3 seconds to complete, extra wait time will not apllied to keep the delay constant betweeen tasks

