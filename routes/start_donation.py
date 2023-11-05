from app import v1, limiter
from flask import request
import stripe

@v1.post('/start-donation')
@limiter.limit("30/minute")
def start_donation():
    try:
        stripe.
    