from django.urls import path

from .views import signup, new_manager, Index, UserDetail, ManagerView, ManagerDetail, user_update

app_name = 'users'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('empresarios/', ManagerView.as_view(), name='managers'),
    path('nuevo-empresario/', new_manager, name='new_manager'),
    path('empresarios/<int:id>', ManagerDetail.as_view(), name='manager_detail'),
    path('signup/', signup, name='signup'),
    path('<int:id>/', UserDetail.as_view(), name='user_detail'),
    path('<int:id>/editar-usuario', user_update, name='user_update'),
]
