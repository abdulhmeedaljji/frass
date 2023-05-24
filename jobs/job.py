from django.conf import settings
import json
from accounts.models import Subscription,tender,File,ArchiveFile,Archivetender
from django.http import JsonResponse
from datetime import date
import os

from django.core.files.base import ContentFile



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
    check_tender_end_date()
    print('Scheduling API ok') 
    
    
    
    
    
def check_tender_end_date():
    print("here issssssssssss tender end date")

    tenders = tender.objects.all()
    expired_tenders= []
    for tender1 in tenders:
        print("tenders")
        print(tender1.end_time)
        print(date.today())
        
        if tender1.end_time == date.today():
            
            archivetender = Archivetender.objects.create(
            tittle=tender1.tittle,
            start_date=tender1.start_date,
            end_time=tender1.end_time,
            state=tender1.state,
            activity=tender1.activity
        )
            
            archivetender.sectoer.set(tender1.sectoer.all())
            
            files = File.objects.filter(tender=tender1)
            for file in files:
                file_path = file.file.path
                archive_file = ArchiveFile(tender=archivetender)
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(file_path)
                    archive_file.file.save(file_name, ContentFile(file_data))
                    archive_file.save()
            
            
            
            print("delete subscription")
            tender1.delete()
            expired_tenders.append(tender1.id)
        else:
            print("No tender ended after")
            
                
    if expired_tenders:
        return JsonResponse({'message': f'The following subscriptions have ended: {expired_tenders}'})
    else:
        return JsonResponse({'message': 'No subscriptions have ended.'})

    