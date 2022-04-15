from locust import HttpUser, task, between


class PingUser(HttpUser):
    wait_time = between(0.5, 2.5)
    
    @task
    def test_ping(self):
        self.client.get('/ping')
    
    @task
    def test_slow_ping(self):
        self.client.get('/slow-ping')
