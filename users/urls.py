from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (signup, new_manager, Index, UserDetail, OsteoDetail, FMSDetail, JumpDetail, ProfileFVDetail, 
                    ProfileFVGraph, BilateralDetail, ManagerView, ManagerDetail, manager_update, AccountDetail,
                    PasswordChange, PasswordChangeDone, user_update)
from osteo.views import FlexUpdate, PainUpdate, MeasuresUpdate
from fms.views import FmsUpdate
from neuro.views import SJUpdateView, CMJUpdateView, DROPSUpdateView, QUpdateView
from bilateral.views import BilateralUpdateView, BilateralCreateView
from profile_fv.views import ProfileUpdateView, ProfileCreateView

app_name = 'users'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cuenta/<int:id>', AccountDetail.as_view(), name='account_detail'),
    path('cuenta/contrasena', PasswordChange.as_view(), name='password_change'),
    path('cuenta/contrasena-actualizada', PasswordChangeDone.as_view(), name='password_change_done'),
    path('empresarios/', ManagerView.as_view(), name='managers'),
    path('empresarios/nuevo/', new_manager, name='new_manager'),
    path('empresarios/<int:id>', manager_update, name='manager_detail'),
    path('deportistas/nuevo/', signup, name='signup'),
    path('deportistas/<int:id>/', UserDetail.as_view(), name='user_detail'),
    path('deportistas/<int:id>/osteo', OsteoDetail.as_view(), name='osteo_detail'),
    path('deportistas/<int:id>/fms', FMSDetail.as_view(), name='fms_detail'),
    path('deportistas/<int:id>/neuromuscular', JumpDetail.as_view(), name='jump_detail'),
    path('deportistas/<int:id>/bilateral', BilateralDetail.as_view(), name='bilateral_detail'),
    path('deportistas/<int:id>/perfil_fv', ProfileFVDetail.as_view(), name='profile_fv_detail'),
    path('deportistas/<int:id>/perfil_fv_graph', ProfileFVGraph.as_view(), name='profile_fv_graph'),
    path('<int:id>/editar-usuario', user_update, name='user_update'),
    path('<int:id>/editar-dolor', PainUpdate.as_view(), name='pain_update'),
    path('<int:id>/editar-medidas', MeasuresUpdate.as_view(), name='measures_update'),
    path('<int:id>/editar-flex', FlexUpdate.as_view(), name='flex_update'),
    path('<int:id>/editar-fms', FmsUpdate.as_view(), name='fms_update'),
    path('<int:id>/editar-sj', SJUpdateView.as_view(), name='sj_update'),
    path('<int:id>/editar-cmj', CMJUpdateView.as_view(), name='cmj_update'),
    path('<int:id>/editar-drops', DROPSUpdateView.as_view(), name='drops_update'),
    path('<int:id>/editar-q', QUpdateView.as_view(), name='q_update'),
    path('<int:id>/editar-bilateral', BilateralUpdateView.as_view(), name='bilateral_update'),
    path('crear-bilateral', BilateralCreateView.as_view(), name='bilateral_create'),
    path('<int:id>/editar-perfil', ProfileUpdateView.as_view(), name='profile_update'),
    path('crear-perfil', ProfileCreateView.as_view(), name='profile_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
