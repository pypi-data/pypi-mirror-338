# LitePolis Rate Limiter Middleware

## Installation

```bash
litepolis-cli add-deps litepolis-middleware-rate-limiter
```
The `RateLimiterMiddleware` implements a token bucket algorithm to control the rate of requests.

## Configuration
`capacity` and `refill_rate` in `~/.litepolis/config.conf`:
```ini
[litepolis_middleware_rate_limiter]
capacity = 4
refill_rate = 2
```

### Citation

The code for this rate limiter is from [fastapi-rate-limiter](https://github.com/jeremiahtalamantes/fastapi-rate-limiter).