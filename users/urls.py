from django.urls import path

from .views import signup, Index, UserDetail, user_update

app_name = 'users'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', signup, name='signup'),
    path('<int:id>/', UserDetail.as_view(), name='user_detail'),
    path('<int:id>/editar-usuario', user_update, name='user_update'),
]
