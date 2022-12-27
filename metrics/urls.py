from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from users.views import UserLoginView, logout_view, ResetPasswordView

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]

handler404 = 'users.views.error_404_view'