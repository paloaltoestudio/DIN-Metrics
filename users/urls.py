from django.urls import path

from .views import signup, new_manager, Index, UserDetail, ManagerView, ManagerDetail, manager_update, user_update
from osteo.views import FlexUpdate, PainUpdate, MeasuresUpdate
from fms.views import FmsUpdate
from neuro.views import SJUpdateView, CMJUpdateView, DROPSUpdateView, QUpdateView
from bilateral.views import BilateralUpdateView

app_name = 'users'

urlpatterns = [
    path('deportistas/', Index.as_view(), name='index'),
    path('empresarios/', ManagerView.as_view(), name='managers'),
    path('empresarios/nuevo/', new_manager, name='new_manager'),
    path('empresarios/<int:id>', manager_update, name='manager_detail'),
    path('deportistas/nuevo/', signup, name='signup'),
    path('deportistas/<int:id>/', UserDetail.as_view(), name='user_detail'),
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
]
