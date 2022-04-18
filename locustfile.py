from locust import TaskSet, HttpUser, task
    

class UserBehaviour(TaskSet):
    
    @task(1)
    def test_ping(self):
        self.client.get('/ping')
    
    @task(2)
    def test_slow_ping(self):
        self.client.get('/slow-ping')


class WebsiteUser(HttpUser):
    tasks = [UserBehaviour, ]
