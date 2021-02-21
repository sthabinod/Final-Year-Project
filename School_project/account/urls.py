from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.login_now,name="login"),
    path('register',views.register_now,name="register"),
    path('logout',views.logout_user,name='logout'),
    path('reset',auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"),name="reset"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_sent.html"),name="password_reset_done"),
    path('reset_password/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password_enter_form.html"),name="password_reset_confirm"),
    path('reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_done.html"),name="password_reset_complete"),
]