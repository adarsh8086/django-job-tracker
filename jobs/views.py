from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Job, Application

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
