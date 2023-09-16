from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import JobForm
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

class BrowseJobsList(APIView):
  def get(self, request, format=None):
    jobs = Job.objects.all()
    categories = request.GET.get('categories', '')
    searchText = request.GET.get('searchText', '')
    
    if categories:
      jobs = jobs.filter(category_id__in=categories.split(','))
    
    if searchText:
      jobs = jobs.filter(title__icontains=searchText)
    
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

class MyJobsView(APIView):
  authentication_classes = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  
  def get(self, request, format=None):
    jobs = Job.objects.filter(created_by=request.user)
    serializer = JobDetailSerializer(jobs, many=True)

    return Response(serializer.data)

class CreateJobsView(APIView):
  authentication_classes = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  
  def post(self, request):
    form = JobForm(request.data)
    if form.is_valid():
      job = form.save(commit=False)
      job.created_by = request.user
      job.save()

      return Response({'status': 'Created successfully!'})
    else:
      return Response({'status': 'errors', 'error': form.errors})

  def put(self, request, pk):
    job = Job.objects.get(pk=pk, created_by=request.user)
    form = JobForm(request.data, instance=job)
    form.save()

    return Response({'status': 'Updated successfully!'})

  def delete(self, request, pk):
    job = Job.objects.get(pk=pk, created_by=request.user)
    job.delete()

    return Response({'status': 'Deleted successfully!'})

