import unittest
import base64
import time
from fastapi import FastAPI
from fastapi.testclient import TestClient

from litepolis_middleware_rate_limiter.core import add_middleware

class TestRateLimiter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = FastAPI()
        add_middleware(cls.app)

        @cls.app.get("/")
        async def read_root():
            return {"message": "Hello World"}

        cls.client = TestClient(cls.app)

    def test_within_rate_limit(self):
        """Test requests within rate limit succeed"""
        time.sleep(3)
        for _ in range(4):  # Bucket capacity is 4
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"message": "Hello World"})

    def test_exceeds_rate_limit(self):
        """Test requests exceeding rate limit get 429"""
        time.sleep(3)
        # Exhaust the token bucket first
        for _ in range(4):
            self.client.get("/")
        
        # Next request should be rate limited
        response = self.client.get("/")
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.json(), {"detail": "Rate limit exceeded"})

    def test_refill_rate(self):
        """Test tokens are refilled after time passes"""
        time.sleep(3)
        # Exhaust the token bucket
        for _ in range(4):
            self.client.get("/")
        
        # Wait for 1 second (refill rate is 2 tokens/sec)
        time.sleep(1)
        
        # Should have 2 tokens available now
        for _ in range(2):
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

        # Next request should be rate limited again
        response = self.client.get("/")
        self.assertEqual(response.status_code, 429)