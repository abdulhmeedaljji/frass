from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import HomeView,userProfile,archive_details_tender,details_tender,upgrade_subs,tender_prevent,signup,login_view,logout_view,BasicSubscriptionView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import tenders_main
from django.conf.urls.i18n import i18n_patterns
from .views  import delete_basic_user_from_dashboard,need_suburcption,tenders_archive_main,add_newuser_dashboard ,delete_sector_from_dashboard,add_sectoer,change_password,reset_password, added_tender,Dashboard,delete_subrcption_from_dashboard,update_tender_dashboard,delete_usersubrcption_from_dashboard,update_suburption_dashboard








urlpatterns =  [
    path('', HomeView , name='Home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('BasicSubscription/<str:my_string>/', BasicSubscriptionView, name='BasicSubscriptionView'),

    path('tender/', tenders_main, name='tender'),
    path('tenderarchivr/', tenders_archive_main, name='tenderarchivr'),
    path('tenderdetaile/<int:id>/', details_tender, name='tenderdetaile'),
    path('tenderdetaile/<int:id>/', details_tender, name='tenderdetaile'),

    
    path('archive_details_tender/<int:id>/', archive_details_tender, name='archive_details_tender'),
    path('tender_prevent', tender_prevent, name='tender_prevent'),
    path('userprofile/',userProfile,name="userprofile"),
    path('added_tender', added_tender, name='added_tender'),
    path('dashboard', Dashboard, name='dashboard'),
    
    
    
    path('update_tender_dashboard/<int:id>/', update_tender_dashboard, name='update_tender_dashboard'),
    path('update_suburption_dashboard/<int:id>/', update_suburption_dashboard, name='update_suburption_dashboard'),
    
    
    path('need_suburcption/', need_suburcption, name='need_suburcption'),

    path('add_sectoer/', add_sectoer, name='add_sectoer'),
    path('add_newuser_dashboard/', add_newuser_dashboard, name='add_newuser_dashboard'),


    path('delect_setore_dashboard/<int:id>/', delete_sector_from_dashboard, name='delect_setore_dashboard'),
    
    path('delete_basic_user_from_dashboard/<int:id>/', delete_basic_user_from_dashboard, name='delete_basic_user_from_dashboard'),

    path('delect_user_dashboard/<int:id>/', delete_subrcption_from_dashboard, name='delect_user_dashboard'),
    path('delect_usersubration_dashboard/<int:id>/', delete_usersubrcption_from_dashboard, name='delect_usersubration_dashboard'),

    path('change_password/', change_password, name='change_password'),
    path('reset_password/', reset_password, name='reset_password'),
    #path('password_change_done/', views.password_change_done, name='password_change_done'),
    #path('password_reset_done/', views.password_reset_done, name='password_reset_done'),


    # path(
    # 'reset_password/',
    # auth_views.PasswordResetView.as_view(success_url=reverse_lazy('password_reset_done')),
    # name='reset_password'
    # ),
    # path(
    #     'reset_password_sent/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete')),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'reset_password_complete/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'
    # )
    
    
    
    # path('rest_password/', auth_view.PasswordResetView.as_view(), name=''),
    # path('rest_password_sent/', auth_view.PasswordResetDoneView.as_view(), name=''),
    # path('rest/<uid64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name=''),

    # path('rest_password_complete/', auth_view.PasswordResetCompleteView.as_view(), name=''),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
