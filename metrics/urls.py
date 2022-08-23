from django.contrib import admin
from django.urls import path, include

from users.views import UserLoginView, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('usuarios/', include('users.urls')),
]
