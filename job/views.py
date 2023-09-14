from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer

class CategoriesListView(APIView):
  def get(self, request, format=None):
    categories = Category.objects.all()[0:4]
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

class NewestJobsList(APIView):
  def get(self, request, format=None):
    jobs = Job.objects.all()[0:4]
    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data)

class NewestJobDetailView(APIView):
  def get(self, request, pk, format=None):
    job = Job.objects.get(pk=pk)
    serializer = JobDetailSerializer(job)

    return Response(serializer.data)

# class SelectedJobsList(APIView):
#   def get(self, request, pk, format=None):
#     selectedJobs = Job.objects.get