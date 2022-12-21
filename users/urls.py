from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (signup, new_manager, Index, UserDetail, ReportDetail, OsteoList, OsteoDetail, FMSDetail, FMSList, JumpDetail, ProfileFVDetail, 
                    FVDetail, ProfileFVGraph, BilateralDetail, FatDetailView, ManagerView, ManagerDetail, manager_update, AccountDetail,
                    PasswordChange, PasswordChangeDone, user_update)
from osteo.views import FlexUpdate, PainUpdate, MeasuresUpdate, OsteoCreateView, OsteoDeleteView, OsteoReportView
from fms.views import FmsUpdate, FMSDeleteView, FMSCreateView
from neuro.views import (NeuroCreateBase, NeuroBaseUpdate, NeuroDelete, 
                        NeuroObservationsView, NeuroObservationsDeleteView,
                        NeuroObservationsEditView)
from bilateral.views import (BilateralUpdateView, BilateralCreateView, BilateralDelete,
                            BilateralObservationCreateView, BilateralObservationUpdateView, BilateralObservationDeleteView, BilateralReportView)
from profile_fv.views import (ProfileUpdateView, ProfileCreateView, ProfileDelete, FVCreateView, FVDelete,
                              ProfileObservationsCreateView, ProfileObservationsUpdateView, ProfileObservationsDeleteView)

from fat.views import FatCreateView, FatDeleteView, FatUpdateView, FatObservationCreateView, FatObservationDeleteView, FatObservationUpdateView

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
    path('deportistas/<int:id>/reporte', ReportDetail.as_view(), name='report_detail'),
    path('deportistas/<int:id>/reporte-osteo', OsteoReportView.as_view(), name='report_osteo'),
    path('deportistas/<int:id>/reporte-bilateral', BilateralReportView.as_view(), name='report_bilateral'),
    path('deportistas/<int:id>/osteo-crear', OsteoCreateView.as_view(), name='osteo_create'),
    path('deportistas/<int:id>/osteo-borrar', OsteoDeleteView.as_view(), name='osteo_delete'),
    path('deportistas/<int:id>/osteo', OsteoList.as_view(), name='osteo_list'),
    path('deportistas/<int:id>/osteo-detalle', OsteoDetail.as_view(), name='osteo_detail'),
    path('deportistas/<int:id>/fms', FMSList.as_view(), name='fms_list'),
    path('deportistas/<int:id>/fms-detalle', FMSDetail.as_view(), name='fms_detail'),
    path('deportistas/<int:id>/fms-borrar', FMSDeleteView.as_view(), name='fms_delete'),
    path('deportistas/<int:id>/fms-crear', FMSCreateView.as_view(), name='fms_create'),
    path('deportistas/<int:id>/neuromuscular', JumpDetail.as_view(), name='jump_detail'),
    path('deportistas/<int:id>/bilateral', BilateralDetail.as_view(), name='bilateral_detail'),
    path('deportistas/<int:id>/perfil_fv/observaciones', ProfileObservationsCreateView.as_view(), name='fv_observation_add'),
    path('deportistas/<int:id>/perfil_fv/editar-observaciones', ProfileObservationsUpdateView.as_view(), name='fv_observation_edit'),
    path('deportistas/<int:id>/perfil_fv/borrar-observaciones', ProfileObservationsDeleteView.as_view(), name='fv_observation_delete'),
    path('deportistas/<int:id>/perfil_fv', ProfileFVDetail.as_view(), name='profile_fv_detail'),
    path('deportistas/<int:id>/crear_perfil_fv', FVCreateView.as_view(), name='profile_fv_create'),
    path('deportistas/<int:id>/eliminar_perfil_fv', FVDelete.as_view(), name='profile_fv_delete'),
    path('deportistas/<int:id>/perfil_fv/detalle_fv', FVDetail.as_view(), name='fv_detail'),
    path('deportistas/<int:id>/perfil_fv/eliminar_fv', ProfileDelete.as_view(), name='fv_delete'),
    path('deportistas/<int:id>/perfil_fv_graph', ProfileFVGraph.as_view(), name='profile_fv_graph'),
    path('<int:id>/editar-usuario', user_update, name='user_update'),
    path('<int:id>/editar-dolor', PainUpdate.as_view(), name='pain_update'),
    path('<int:id>/editar-medidas', MeasuresUpdate.as_view(), name='measures_update'),
    path('<int:id>/editar-flex', FlexUpdate.as_view(), name='flex_update'),
    path('<int:id>/editar-fms', FmsUpdate.as_view(), name='fms_update'),
    path('<int:id>/crear-neuro', NeuroCreateBase.as_view(), name='neuro_create'),
    path('<int:id>/neuro/observaciones', NeuroObservationsView.as_view(), name='neuro_observation_add'),
    path('<int:id>/neuro/editar-observaciones', NeuroObservationsEditView.as_view(), name='neuro_observation_edit'),
    path('<int:id>/neuro/borrar-observaciones', NeuroObservationsDeleteView.as_view(), name='neuro_observation_delete'),
    path('<int:id>/editar-neuro', NeuroBaseUpdate.as_view(), name='neuro_update'),
    path('<int:id>/eliminar-neuro', NeuroDelete.as_view(), name='neuro_delete'),
    path('crear-bilateral', BilateralCreateView.as_view(), name='bilateral_create'),
    path('<int:id>/editar-bilateral', BilateralUpdateView.as_view(), name='bilateral_update'),
    path('<int:id>/eliminar-bilateral', BilateralDelete.as_view(), name='bilateral_delete'),
    path('deportistas/bilateral/crear-observacion', BilateralObservationCreateView.as_view(), name='bilateral_observation_create'),
    path('deportistas/<int:id>/bilateral/editar-observacion', BilateralObservationUpdateView.as_view(), name='bilateral_observation_edit'),
    path('deportistas/<int:id>/bilateral/borrar-observacion', BilateralObservationDeleteView.as_view(), name='bilateral_observation_delete'),
    path('deportistas/grasa/crear-observacion', FatObservationCreateView.as_view(), name='fat_observation_create'),
    path('deportistas/<int:id>/grasa/editar-observacion', FatObservationUpdateView.as_view(), name='fat_observation_edit'),
    path('deportistas/<int:id>/grasa/borrar-observacion', FatObservationDeleteView.as_view(), name='fat_observation_delete'),
    path('deportistas/<int:id>/crear_grasa', FatCreateView.as_view(), name='fat_create'),
    path('<int:id>/eliminar-grasa', FatDeleteView.as_view(), name='fat_delete'),
    path('<int:id>/editar-grasa', FatUpdateView.as_view(), name='fat_update'),
    path('<int:id>/editar-perfil', ProfileUpdateView.as_view(), name='profile_update'),
    path('crear-perfil', ProfileCreateView.as_view(), name='profile_create'),
    path('deportistas/<int:id>/grasa', FatDetailView.as_view(), name='fat_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

