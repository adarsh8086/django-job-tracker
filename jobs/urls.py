from django.urls import path
from .views import ApplyJobAPIView,JobListAPIView

urlpatterns = [
    path("api/", JobListAPIView.as_view(), name="job-list-api"),
    path("apply/<int:job_id>/", ApplyJobAPIView.as_view(), name="apply-job"),
]
