from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import CustomUser,tender,Choice
# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import Subscription,tender,File,SECTOER_CHOICES
from .decorators import cheak_user_subscription
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail



def HomeView(request):
    if request.user.is_authenticated:
        last_five_objects = tender.objects.all().order_by('-id')[:5]
        subscription=Subscription.objects.filter(user=request.user)
        return render(request,'index.html' , {"last_five_objects":last_five_objects , "subscription":subscription})    
    else:
        last_five_objects = tender.objects.all().order_by('-id')[:5]
        return render(request,'index.html' , {"last_five_objects":last_five_objects ,})
   



from django.contrib.auth import get_user_model
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        
        if password != confirm_password:
            error_msg = 'Passwords do not match'
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')
        
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'signup.html', )

        if User.objects.filter(phone_number=phone_number).exists():
            error_msg = 'phone  already exists'
            messages.error(request, "phone  already exists")

            return render(request, 'signup.html', )
        user = User.objects.create_user(email,email, password)
        user.phone_number = phone_number
        user.save()
        
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')  # replace 'home' with your app's homepage URL
    else:
        return render(request, 'signup.html')
    
    
  
  
  
def login_view(request):
    if request.method == 'POST':
        username = request.POST['phone_number']
        password = request.POST['password']
        

        # Authenticate the user
        user = authenticate(request, phone_number=username, password=password,backend='django.contrib.auth.backends.ModelBackend')

        if user is not None:
            login(request, user ,backend='django.contrib.auth.backends.ModelBackend')
            print("here")
            return redirect('/')
        else:
            # Return an error message if authentication fails
            messages.error(request, "Invalid login cheak phone number and password.")
            return render(request, 'login.html', )
    else:
        # Render the login page
        return render(request, 'login.html')
    
    
    
    
    
def logout_view(request):
    logout(request)
    return redirect("Home")




def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Verify that the email address exists
        try:
            user = CustomUser.objects.get(email=email)
            user_id=CustomUser.objects.filter(email=email).values('id')
       
            
            
        except CustomUser.DoesNotExist:
            return render(request, 'rest_passwords/reset_password.html', {'error': 'No user found with that email address'})

        # Generate a new password for the user
        new_password = CustomUser.objects.make_random_password()
        
        print()

        # Set the new password and save the user object
        user.set_password(new_password)
        user.save()

        # Send an email to the user with the new password
        send_mail(
            'Your new password',
            f'Your new password is: {new_password}',
            'admin@example.com',
            [email],
            fail_silently=False,
        )


        return redirect('login')

    return render(request, 'rest_passwords/reset_password.html')





def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Verify that the current password is correct
        user = CustomUser.objects.get(id=request.user.id)
        if not user.check_password(current_password):
            return render(request, 'rest_passwords/change_password.html', {'error': 'Current password is incorrect'})

        # Verify that the new password matches the confirm password
        if new_password != confirm_password:
            return render(request, 'rest_passwords/change_password.html', {'error': 'New passwords do not match'})

        # Set the new password and save the user object
        user.set_password(new_password)
        user.save()
        login(request, user ,backend='django.contrib.auth.backends.ModelBackend')


        return redirect('Home')

    return render(request, 'rest_passwords/change_password.html')






def BasicSubscriptionView(request,my_string):    
    if request.method == 'POST':
        if  not request.user.is_authenticated:
             messages.info(request, "you need login to regisiter.")
             return redirect('/login')
        selectorlist = request.POST.getlist('my-select[]')
        file = request.FILES.get('file')
        
    
        start=date.today()
        end = date.today() + timedelta(days=30)
        user_sub=CustomUser.objects.filter(phone_number=request.user.phone_number)
        
        
        have_account=Subscription.objects.filter(user=request.user)
        have_account_suburaption=Subscription.objects.all().filter(user=request.user).values('tittle')
        print(f"have_account {have_account_suburaption}")
        
        
        if have_account_suburaption == my_string and have_account:
            messages.info(request, "you have this subscription already.")
            Ch=Choice.objects.all()
            return render(request,"subscription/Basci.html",{'Ch':Ch})

        
        if have_account_suburaption != my_string and have_account:
            have_account.delete()
            Subscriptions=Subscription.objects.create(user=request.user, tittle=my_string,  start_date=start, end_date=end ,img_transition=file)
            for selector in selectorlist:
                Subscriptions.plan.add(selector)

            Subscriptions.save()
            
            messages.info(request, "your have  subscription upgread wait activite account ")
            Ch=Choice.objects.all()
            return render(request,"subscription/Basci.html",{'Ch':Ch})
        
        
        Subscriptions=Subscription.objects.create(user=request.user, tittle=my_string,  start_date=start, end_date=end ,img_transition=file)
        for selector in selectorlist:
         Subscriptions.plan.add(selector)

        Subscriptions.save()
        
        return redirect("Home")


    else:
        Ch=Choice.objects.all()

           
        return render(request,"subscription/Basci.html",{'Ch':Ch})






def upgrade_subs(request):
    return render(request,"tender/updatesubraption.html")




def add_sectoer(request):
    if request.method == "POST": 
        new_choice_name=request.POST.get('name_sector')  

        new_choice = Choice(name=new_choice_name)
        new_choice.save()
        return redirect('dashboard')
    else:
        return redirect('dashboard')




def added_tender(request):
    if not request.user.is_superuser:
        return redirect("Home")
    if request.method=="POST":
       tillle=request.POST.get('tittle')
       state=request.POST.get('state')

       sectors=request.POST.getlist('sectors[]')
       startdate=request.POST.get('startdate')
       enddate=request.POST.get('enddate')
       files = request.FILES.getlist('img')       
       added=tender.objects.create(tittle=tillle,state=state,
                                   start_date=startdate,           
                                   end_time=enddate,
                                   
                                   
                                   )
                    
       
       for selector in sectors:
         added.sectoer.add(selector)
         
         
      
         
       for file in files:
            new_file = File.objects.create(
            tender=added,
            file=file
            )
            
            
       new_file.save()
                 
       
       return redirect('Home')
       
    else:
     Ch=Choice.objects.all()
     return render(request,"tender/add_tender.html",{'Ch':Ch})






def userProfile(request):
    user_name= CustomUser.objects.filter(id=request.user.id)
    subscription=Subscription.objects.filter(user=request.user)
    print(subscription)
    return render(request,"userprofile.html",{'user_name':user_name,"subscription":subscription })


def tenders_main(request):
    if request.method == "POST":
        Ch=Choice.objects.all()

        tittle=request.POST.get('tittle')
        state=request.POST.get('state')
        sectors=request.POST.get('sectors')
        dates=request.POST.get('dates')
        
 
        if not sectors=="":    
            q= Q(sectoer=sectors )
            tenders = tender.objects.filter(q)

        if not tittle=="":
            q=Q(tittle__icontains=tittle ) 
            tenders = tender.objects.filter(q)
            
        if not state=="":
            q=Q(state__icontains=tittle ) 
            tenders = tender.objects.filter(q)
            
        if not dates=="":
            q=Q(start_date__icontains=tittle ) 
            tenders = tender.objects.filter(q)          

    
        return render(request,"tender/tender.html",{'tenders':tenders ,  "Ch":Ch})
    else:
        user_have_sub=Subscription.objects.filter(user_id=request.user.id).exists()
        if  user_have_sub:
            categres=Subscription.objects.filter(user_id=request.user.id).values_list('plan', flat=True)
            Ch=Choice.objects.all()

            tenders = tender.objects.filter(sectoer__id__in=categres)
            return render(request,"tender/tender.html",{'tenders':tenders , "Ch":Ch})
           
    tenders=tender.objects.all()
    Ch=Choice.objects.all()
    return render(request,"tender/tender.html",{'tenders':tenders , "Ch":Ch})




def admin_add_tender(request):
    return render(request,"tender/add_tender.html")

def tender_prevent(request):
    return render(request,"tender/can_not_access.html")



@cheak_user_subscription()
def details_tender(request,id):
    tender_details =tender.objects.filter(id=id)
    
    tender_detailss =tender.objects.get(id=id)

    file_objs = tender_detailss.file_set.all()
  
    return render(request,"tender/tender_detail.html",{'tender_details':tender_details, "file_objs":file_objs })



def Dashboard(request):
    if not request.user.is_superuser:
        return redirect('Home')       
    if request.method =="POST":
         tenders = get_object_or_404(tender, pk=id)
    if request.method == 'POST':
        image=request.FILES.get("image")    
        if image == None:
            title = request.POST.get('tittle')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            state = request.POST.get('state')
            
            results = tender.objects.filter(id=id )
            image_url = results.img_tender.url

            tenders.tittle = title
            tenders.start_date = start_date
            tenders.end_time = end_date
            tenders.state = state
            tenders.img_tender = image_url
            tenders.activity = False
            
            tenders.save()
            return redirect(Dashboard)
        else:
            title = request.POST.get('tittle')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            state = request.POST.get('state')
            image=request.FILES.get("image")    
            tenders.tittle = title
            tenders.start_date = start_date
            tenders.end_time = end_date
            tenders.state = state
            tenders.img_tender = image
            tenders.activity = False
            
            tenders.save()   
        
            return redirect(Dashboard)
            
    else:
        
            
        alluser=CustomUser.objects.all().count()
        activiteaccount=Subscription.objects.filter(activite=True).count()
        notactivites=Subscription.objects.filter(activite=False).count()
        
        Bassicaccount=Subscription.objects.filter(tittle="Basic").count()
        Plan1account=Subscription.objects.filter(tittle="plan1").count()
        Plan2account=Subscription.objects.filter(tittle="plan2").count()
        Plan3account=Subscription.objects.filter(tittle="plan3").count()
        Plan4account=Subscription.objects.filter(tittle="plan4").count()

        table_subscriptions_all = Subscription.objects.all()
        table_subscriptions_register = Subscription.objects.all().filter(activite=True)
        table_subscriptions_notactivite = Subscription.objects.all().filter(activite=False)

        table_tender_all = tender.objects.all()
        
        Choice_list =Choice.objects.all()
        
        tender_file = File.objects.all()
        

        context={
            
            "alluser":alluser,
            "notactivites":notactivites,
            "activiteaccount":activiteaccount,
            
            "Bassicaccount":Bassicaccount,
            "Plan1account":Plan1account,
            "Plan2account":Plan2account,
            "Plan3account":Plan3account,
            "Plan4account":Plan4account,
            
            "table_subscriptions_all":table_subscriptions_all,
            "table_subscriptions_register":table_subscriptions_register,
            "table_subscriptions_notactivite":table_subscriptions_notactivite,
            
            "table_tender_all":table_tender_all,
            "Choice_list":Choice_list,
            "tender_file":tender_file

            
        }
        
        
        return render(request,"dasboard/dashboard.html",context)



def delete_subrcption_from_dashboard(request,id):
    subscription = tender.objects.get(id=id)
    subscription.delete()

    print(id)
    print(subscription)
    return redirect(Dashboard)



def delete_usersubrcption_from_dashboard(request,id):
    subscription = Subscription.objects.get(id=id)
    subscription.delete()

    return redirect(Dashboard)




def delete_sector_from_dashboard(request,id):
    sectors = Choice.objects.get(id=id)
    sectors.delete()

    return redirect(Dashboard)







from django.shortcuts import render, get_object_or_404

def update_tender_dashboard(request,id):
    tenders = get_object_or_404(tender, pk=id)
    if request.method == 'POST':        
        image=request.FILES.getlist("image")
        title = request.POST.get('tittle')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        state = request.POST.get('state')
        sectors = request.POST.getlist('sectors[]')

        if image == "":
            image = tender.objects.filter(id=id).getlist('image')
        
        if title == "":
            title = tender.objects.filter(id=id).values('tittle')
        
        if start_date == "":
            start_date = tender.objects.filter(id=id).values('start_date')
        
        if end_date == "":
            end_date = tender.objects.filter(id=id).values('end_date')
            
        if state == "":
            state = tender.objects.filter(id=id).values('state')
           
        if sectors == "":
            sectors = tender.objects.filter(id=id).values_list('sectors')
              
       
        tenders.tittle = title
        tenders.start_date = start_date
        tenders.end_time = end_date
        tenders.state = state
        
        tenders.sectoer.clear()

        for p in sectors:
            tenders.sectoer.add(p)
               
        
        tenders.save()
        
        
        tenders.file_set.all().delete()

        
                   
        
        for file in image:
            new_file = File.objects.create(
            tender=tenders,
            file=file
            )
        
            new_file.save()
        
        
     
        
    return redirect(Dashboard)





def update_suburption_dashboard(request,id):
    user = get_object_or_404(Subscription, pk=id)
    if request.method == 'POST':
        image_url=request.FILES.get("image")     
        title = request.POST.get('tittle')            
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        active = request.POST.get('active')
        sectors = request.POST.get('select')
        
        sub_plans = Subscription.objects.get(id=id)
        plans = sub_plans.plan.all()
        
                        
            
        if active == '':
            active = Subscription.objects.filter(id=id).values('activite').first()

        if title == '':
            title = Subscription.objects.filter(id=id).values('tittle').first()

        if image_url == None:
            image_url = Subscription.objects.filter(id=id).values('img_transition').first()
      
            image_url=image_url['img_transition']          
                   
        user.tittle = title
        user.start_date = start_date
        user.end_date = end_date
        user.activite = active
        user.img_transition = image_url

        user.save()

        
        for p in plans:
            user.plan.add(p)
        return redirect(Dashboard)
    





