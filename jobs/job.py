from django.conf import settings
import json
from accounts.models import Subscription
from django.http import JsonResponse
from datetime import date


def check_subscription_end_date():
    print("here issssssssssss")
    subscriptions = Subscription.objects.all()
    expired_subscriptions = []
    for subscription in subscriptions:
        print("Subscription")
        print(subscription.end_date)
        print(type(subscription.end_date))
        print("date todays")
        print(date.today())
        
        if subscription.end_date == date.today():
           
            print("delete subscription")
            subscription.delete()
            expired_subscriptions.append(subscription.id)
        else:
            print("No subscription ended after")    
    if expired_subscriptions:
        return JsonResponse({'message': f'The following subscriptions have ended: {expired_subscriptions}'})
    else:
        return JsonResponse({'message': 'No subscriptions have ended.'})




def schedule_api():
    check_subscription_end_date()
    print('Scheduling API ok') 