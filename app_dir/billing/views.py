from django.shortcuts import render

import stripe

stripe.api_key = "sk_test_M2Ho1BLmn1QtcT0AusMvGoN800yHLCmZ7O"

STRIPE_PUB_KEY = 'pk_test_iKAtKIsrSjc9YrWc5hywLQ4a00lsDuS9Eg'


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})
