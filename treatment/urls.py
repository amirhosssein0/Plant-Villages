from django.urls import path
from .views import TreatmentView, TreatmentResultView

app_name = 'treatment'

urlpatterns = [
    path('', TreatmentView.as_view(), name='treatment'),
    path('result/<str:task_id>/', TreatmentResultView.as_view(), name='treatment-result'),
]