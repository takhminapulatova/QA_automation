class TestConfig:
    def __init__(self, base_url: str):
        self.base_url = base_url

config = TestConfig("https://example.com")
print(config.base_url)
assert config.base_url == "https://example.com"
