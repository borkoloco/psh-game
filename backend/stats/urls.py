from django.urls import path
from .views import ReportView

urlpatterns = [
    path('api/stats/', ReportView.as_view(), name='stats-report'),
]
