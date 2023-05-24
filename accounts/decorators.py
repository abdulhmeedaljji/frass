from functools import wraps
from django.shortcuts import redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import CustomUser
from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from .models import Subscription,tender,Archivetender,ArchiveFile


def check_items_exist(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


def check_activations(name,name1):
    if name==name1:
        return True
    else:
        False






def cheak_user_subscription():
    def user_has_subscription(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect(reverse('login'))

            if  Subscription.objects.filter(user=user).exists():
                
                subraction=Subscription.objects.filter(user=user)
                
                activite=subraction.values('activite')[0]
                activite_name=bool(activite.get('activite')) 
                             
                plans=subraction.values('plan__name')
                print(plans)
                
                plan_list = [item['plan__name'] for item in plans]
                
                print("here is plan list")               
                print(plan_list)
                
                print(kwargs.get('id'))
                tenders=tender.objects.filter(id=kwargs.get('id'))
                
                tenders_plans=tenders.values('sectoer__name')
                tenders_list = [item['sectoer__name'] for item in tenders_plans]
                print("  here is tender list ") 
                print(tenders_list)
                
                print(check_items_exist(tenders_list,plan_list))
                check=check_items_exist(tenders_list,plan_list)  
                
                 
                if check and activite_name== True :

                    # Redirect to error page or login page with error message
                    return view_func(request, *args, **kwargs)
                else:
                      return redirect(reverse('tender_prevent'))
            else:
                
                 return redirect(reverse('Home'))
                
                
        return wrapper

    return user_has_subscription



from django.http import Http404
from functools import wraps

def staff_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            return func(request, *args, **kwargs)
        return redirect("Home")
    return wrapper







def cheak_tender_subscription():
    def user_has_subscription(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect(reverse('login'))

            if  Subscription.objects.filter(user=user).exists():
                
                subraction=Subscription.objects.filter(user=user)
                
                activite=subraction.values('activite')[0]
                activite_name=bool(activite.get('activite')) 
                             
                plans=subraction.values('plan__name')
                print(plans)
                
                plan_list = [item['plan__name'] for item in plans]
                
                print("here is plan list")               
                print(plan_list)
                
                print(kwargs.get('id'))
                tenders=Archivetender.objects.filter(id=kwargs.get('id'))
                
                tenders_plans=tenders.values('sectoer__name')
                tenders_list = [item['sectoer__name'] for item in tenders_plans]
                print("  here is tender list ") 
                print(tenders_list)
                
                print(check_items_exist(tenders_list,plan_list))
                check=check_items_exist(tenders_list,plan_list)  
                
                 
                if check :

                    # Redirect to error page or login page with error message
                    return view_func(request, *args, **kwargs)
                else:
                      return redirect(reverse('tender_prevent'))
            else:
                
                 return redirect(reverse('Home'))
                
                
        return wrapper

    return user_has_subscription
