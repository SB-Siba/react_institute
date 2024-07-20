from django.urls import path
from users import views
from users.forms import CustomPasswordResetForm, PasswordChangeForm
from users.user_views import user_views
from django.contrib.auth import views as auth_view

app_name = 'users'


urlpatterns = [
    #Authentication urls
    path('signup', views.Registration.as_view(), name = "signup"),
    path('login', views.Login.as_view(), name = "login"),
    path("passwordChange/",auth_view.PasswordChangeView.as_view(template_name = 'users/authtemp/changepassword.html',form_class = PasswordChangeForm,success_url = '/passwordchangedone'),name='passwordchange'),
    path("passwordchangedone/",auth_view.PasswordChangeDoneView.as_view(template_name = 'users/authtemp/changepassworddone.html'),name='passwordchangedone'),
    path('password-reset/', views.CustomPasswordResetView.as_view(),name='password-reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',views.CustomPasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('logout/', views.Logout.as_view(), name = "logout"),


    #user profile
    path('profile',user_views.ProfileView.as_view(),name="profile"),
    path('alladdress',user_views.AllAddress.as_view(),name="alladdress"),
    path('addaddress',user_views.AddAddress.as_view(),name="addaddress"),
    path('delete-address/<str:address_id>/', user_views.DeleteAddress.as_view(), name='delete_address'),
    path('updateprofile/',user_views.UpdateProfileView.as_view(),name="updateprofile"),
]