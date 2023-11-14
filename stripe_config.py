from dotenv import dotenv_values
# from os import environ as env
import stripe

env = dotenv_values('.env')


def use_stripe_test():
    stripe.api_key = env.get('STRIPE_TEST_API_KEY')


def use_stripe_live():
    stripe.api_key = env.get('STRIPE_LIVE_API_KEY')


def init():
    use_stripe_test()
