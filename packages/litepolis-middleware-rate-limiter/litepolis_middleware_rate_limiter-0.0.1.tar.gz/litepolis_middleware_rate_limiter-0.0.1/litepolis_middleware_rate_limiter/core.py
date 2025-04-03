import base64
import binascii

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from .utils import DEFAULT_CONFIG, TokenBucket

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, bucket: TokenBucket):
        super().__init__(app)
        self.bucket = bucket

    async def dispatch(self, request: Request, call_next):
        if self.bucket.take_token():
            return await call_next(request)
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded"},
        ) 


def add_middleware(app):
    app.add_middleware(RateLimiterMiddleware, bucket=TokenBucket())
    return app
