
BASE_URL = "https://api.66skins.com"
#
#
#
#
# from locust import HttpLocust, TaskSet, task, HttpUser
#
# import json
#
#
# class UserBehavior(TaskSet):
#     #Execute before any task.
#     def on_start(self):
#         pass
#
#
#     @task(1)
#     def list_header(self):
#         r = self.client.post("/register/queryRegister", json={"modelName": None})
#         if json.loads((r.content))["code"] != 200:
#             r.failure("Got wrong response:"+r.content)
#
#
# class WebUserLocust(HttpUser):
#     # Speicify the weight of the locust.
#     weight = 1
#     # The taskset class name is the value of the task_set.
#     tasks = [UserBehavior]
#     #Wait time between the execution of tasks.
#     min_wait = 5000
#     max_wait = 15000


