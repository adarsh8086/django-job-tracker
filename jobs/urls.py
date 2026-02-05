from django.urls import path
from .views import ApplyJobAPIView

urlpatterns = [
    path("apply/<int:job_id>/", ApplyJobAPIView.as_view(), name="apply-job"),
]
