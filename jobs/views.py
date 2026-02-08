from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import JobSerializer

from .models import Job, Application

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


class ApplyJobAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response(
                {"error": "Job not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # prevent duplicate application
        if Application.objects.filter(user=request.user, job=job).exists():
            return Response(
                {"error": "Already applied"},
                status=status.HTTP_400_BAD_REQUEST
            )

        Application.objects.create(
            user=request.user,
            job=job
        )

        return Response(
            {"message": "Applied successfully"},
            status=status.HTTP_201_CREATED
        )





class JobListAPIView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]







# normal view for html
def job_list_view(request):
    jobs = Job.objects.all()
    return render(request, "jobs/job_list.html", {"jobs": jobs})




@login_required
def apply_job_ui(request, job_id):
    
    # return redirect("/")
       job = get_object_or_404(Job, id=job_id)


    # prevent duplicate apply
       if Application.objects.filter(user=request.user, job=job).exists():
            messages.error(request, "You already applied for this job")
            return redirect("home")

       if request.method == "POST":
            resume = request.FILES.get("resume")
            cover_letter = request.POST.get("cover_letter")

            Application.objects.create(
                user=request.user,
                job=job,
                resume=resume,
                cover_letter=cover_letter
            )

            messages.success(request, "Applied successfully")
            return redirect("home")

       return render(request, "jobs/apply_job.html", {"job": job})




@login_required
def my_applications_view(request):
    applications = Application.objects.filter(user=request.user).select_related("job")
    return render(request, "jobs/my_applications.html", {
        "applications": applications
    })