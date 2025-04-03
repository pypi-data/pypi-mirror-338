import os
import time
from litepolis import get_config

DEFAULT_CONFIG = {
    "capacity": 4,
    "refill_rate": 2
}

#
#
# BASIC RATE LIMITER USING FASTAPI
# USING TOKEN BUCKET ALGO
#
#

class TokenBucket:
    _buckets = {}  # Class-level dictionary to store buckets per session

    def __init__(self):
        # Initialize the token bucket configuration (shared across sessions)
        if (os.environ.get("PYTEST_CURRENT_TEST") or
            os.environ.get("PYTEST_VERSION")):
            self.capacity = DEFAULT_CONFIG["capacity"]
            self.refill_rate = DEFAULT_CONFIG["refill_rate"]
        else:
            package_name = os.path.basename(
                os.path.dirname(os.path.dirname(__file__)))
            self.capacity = get_config(package_name, "capacity")
            self.refill_rate = get_config(package_name, "refill_rate")

    def add_tokens(self, session_id):
        # Add tokens to the bucket based on the time elapsed since the last refill
        bucket = self._buckets.get(session_id)
        if not bucket:
            return  # No bucket for this session yet

        now = time.time()
        if bucket['tokens'] < self.capacity:
            # Calculate the number of tokens to add
            tokens_to_add = (now - bucket['last_refill']) * self.refill_rate
            # Update the token count, ensuring it doesn't exceed the capacity
            bucket['tokens'] = min(self.capacity, bucket['tokens'] + tokens_to_add)
        bucket['last_refill'] = now  # Update the last refill time

    def take_token(self, session_id):
        # Attempt to take a token from the bucket for a given session_id
        if session_id not in self._buckets:
            # Initialize bucket for this session if it doesn't exist
            self._buckets[session_id] = {
                'tokens': self.capacity,  # Start with the bucket full
                'last_refill': time.time()  # Record the initial refill time
            }

        self.add_tokens(session_id)  # Ensure the bucket is refilled based on the elapsed time
        bucket = self._buckets[session_id]
        if bucket['tokens'] >= 1:
            bucket['tokens'] -= 1  # Deduct a token for the API call
            return True  # Indicate that the API call can proceed
        return False  # Indicate that the rate limit has been exceeded
