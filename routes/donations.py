from app import v1, limiter
from flask import request, jsonify
import stripe
import stripe_config


FILTER_START_DATE = 1700064000


# @v1.post('/start-donation')
# @limiter.limit("30/minute")
# def start_donation():


@v1.get('/donations')
@limiter.limit('30/minute')
def list_donations():
    stripe_config.use_stripe_live()

    donations = stripe.PaymentIntent.list().data
    donations = list(filter(lambda d: d.status == 'succeeded', donations))

    if not request.args.get('list_all'):
        donations = list(filter(lambda d: d.created > FILTER_START_DATE, donations))

    stripe_config.use_stripe_test()

    return jsonify({
        'count': len(donations),
        'total': sum([don.amount for don in donations]) // 100,
    }), 200
