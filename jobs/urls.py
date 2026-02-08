from django.urls import path
from .views import ApplyJobAPIView,JobListAPIView,job_list_view,apply_job_ui, my_applications_view

urlpatterns = [
    path("", job_list_view, name="job-list-page"),
    path("api/", JobListAPIView.as_view(), name="job-list-api"),
    path("apply/<int:job_id>/", ApplyJobAPIView.as_view(), name="apply-job"),
     path("apply-ui/<int:job_id>/", apply_job_ui, name="apply-job-ui"),  #  ui
     path("my-applications/", my_applications_view, name="my-applications"), #  ui
]
