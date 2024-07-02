from locust import HttpUser, task, constant_pacing
import random


class QuickstartUser(HttpUser):
    wait_time = constant_pacing(1)

    @task
    def chat_ramdom(self):
        num_choices = random.randint(1, 500)
        choices = [
            {"message": "Client response", "author": "Client"},
            {"message": "Agent response", "author": "Agent"},
        ] * num_choices
        data = {
            "message": "Second",
            "history": random.choices(choices, k=num_choices),
        }
        self.client.post("/", json=data)

    @task
    def chat_small(self):
        data = {
            "message": "Second",
            "history": [
                {"message": "First", "author": "Client"},
                {"message": "First response", "author": "Agent"},
                {"message": "Second", "author": "Client"},
            ],
        }
        self.client.post("/", json=data)

    @task
    def chat_large(self):
        messages = [
            {"message": "Client response", "author": "Client"},
            {"message": "Agent response", "author": "Agent"},
        ] * 500
        data = {
            "message": "Second",
            "history": messages,
        }
        self.client.post("/", json=data)
