from django.urls import path

from fields import views
from fields.views import FieldCreateView , FieldDetail , FieldEditView , FieldsView

app_name = 'fields'

urlpatterns = [
    path('add/', FieldCreateView.as_view(), name='add_field'),
    path('edit/<slug:slug>/', FieldEditView.as_view(), name='edit_field'),
    path('', FieldsView.as_view(), name='field_list'),
    path('<slug:slug>/', FieldDetail.as_view(), name='field_detail'),
    # path('crops/', CropView.as_view(), name='crop_list')
]
