class TestConfig:
    ENVIRONMENTS = {
        "dev": "http://127.0.0.1:5000",
        "staging": "https://staging.example.com",
        "prod": "https://www.saucedemo.com"
    }

    def __init__(self, environment: str):
        self.environment = environment
        self.base_url = self.ENVIRONMENTS[environment]


config = TestConfig("dev")

print(config.base_url)