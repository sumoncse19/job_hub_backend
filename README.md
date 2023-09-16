1. `python3 -m venv env`

2. `source env/bin/activate`

3. Then install this packages:
   ```
   pip install django djangorestframework django-cors-headers djoser pillow stripe matplotlib sqlalchemy
   ```
4. `pip install --upgrade pip`

5. Now run this command --> `django-admin startproject <project-name>` --> cd <project-name>

6. In setting.py apply this step:

   a. After `ALLOWED_HOSTS = []`, add this line:

   ```
    USER_CREATE_PASSWORD_RETYPE = False
   ```

   b. In `INSTALLED_APPS` array, add your packages name:

   ```
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
   ```

   c. After `INSTALLED_APPS` array, create a new array like this:

   ```
    CORS_ALLOWED_ORIGINS = [
      'http://localhost:3000',
      'http://localhost:3001',
      'http://localhost:3002',
    ]
   ```

   d. In `MIDDLEWARE` array, add corsheader.middleware at 3rd position like this:

   ```
    'corsheaders.middleware.CorsMiddleware'
   ```

7. In urls.py apply this step:

   a. import `include` from `django.urls`, and add this line in `urlpatterns` :

   ```
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
   ```

8. In this Job_Hub_Backend project now need to setup new app for job, for create new app as name of job we need to run this command:
   a. Create new app and add app name in `INSTALLED_APPS` array under settings.py file.

   ```
     python manage.py startapp job
   ```

   ```
   INSTALLED_APPS = [
    'job',
   ]
   ```

9. In models.py under new app code will look like similarities with the following example:

```
from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters

# Create your models here.
class Category(models.Model):
  # Here i add some other properties to check:
  # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  # name = models.CharField(max_length=255)
  # slug = models.SlugField()
  # description = models.TextField(blank=True, null=True)
  # price = models.DecimalField(max_digits=6, decimal_places=2)
  # image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
  # date_added = models.DateTimeField(auto_now_add=True)

  title = models.CharField(max_length=255)

  class Meta:
    ordering = ('title',)

class Job(models.Model):
  category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  position_salary = models.CharField(max_length=255)
  position_location = models.CharField(max_length=255)
  company_name = models.CharField(max_length=255)
  company_location = models.CharField(max_length=255)
  company_email = models.EmailField()
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)

  class Meta:
    ordering = ('-created_at',)

  def created_at_formatted(self):
    return defaultfilters.date(self.created_at, 'M d, Y')

```

10. Then run this following command:
    a. Make migration command:

    ```
      python manage.py makemigrations
    ```

    ```
      python manage.py migrate
    ```

11. Now create a serializers.py file under job app for load data in fronted, here an example:
    a. Example 1:

    ```
      from rest_framework import serializers

      from .models import Job

      class JobSerializer(serializers.ModelSerializer):
        class Meta:
          model = Job
          fields = (
            "id",
            "title",
            "position_salary",
            "position_location",
            "company_name",
            "created_at_formatted",
          )
    ```

    b. Example 2:

    ```
      from pyexpat import model
      from rest_framework import serializers

      from .models import Category, Product

      class ProductSerializer(serializers.ModelSerializer):
        class Meta:
          model = Product
          fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
          )

    ```

12. Now run the server `python3 manage.py runserver`

13. Now in views.py file under job app need to add this, here an example:
    a. Example 1:

    ```
      from rest_framework import status, authentication, permissions
      from rest_framework.views import APIView
      from rest_framework.response import Response

      from .models import Job, Category
      from .serializers import JobSerializer

      class NewestJobList(APIView):
        def get(self, request, format=None):
          jobs = Job.objects.all()[0:4]
          serializer = JobSerializer(jobs, many=True)

          return Response(serializer.data)
    ```

    b. Example 2:

    ```
      from django.shortcuts import render

      from rest_framework.views import APIView
      from rest_framework.response import Response

      from .models import Product
      from .serializer import ProductSerializer

      class LatestProductList(APIView):
        def get(self, request, format=None):
          products = Product.objects.all()[0:4]
          serializer = ProductSerializer(products, many=True)
          return Response(serializer.data)

    ```

14. Now create a urls.py file under job app and add these code, here an example:
    a. Example 1:

    ```
      from django.urls import path

      from job import views

      urlpatterns = [
          path('newest/', views.NewestJobList.as_view()),
      ]
    ```

    or,

    ```
      from django.urls import path

      from . import views

      urlpatterns = [
          path('newest/', views.NewestJobList.as_view()),
      ]
    ```

    b. Example 2:

    ```
      from django.urls import path, include

      from product import views

      urlpatterns = [
          path('latest-products/', views.LatestProductList.as_view()),
      ]

    ```

15. Now add the below line to urls.py of project folder: `path('api/v1/jobs/', include('job.urls')),`

16. Then run this command:

```
python manage.py makemigrations && python manage.py migrate
python3 manage.py runserver
```

17. Then add this line to admin.py of app:

```
from django.contrib import admin

from .models import Job

admin.site.register(Job)
```

18. Go to terminal run `python manage.py createsuperuser`

19. Summary:

```
  a. Ki ki data insert korbo segula thakbe model ee.
  b. API hit korle kun kun data dekhabe seta thake serializers ee.
  c. views.py theke serializers er data gula niye return korte hoy.
  d. urls.py theke kun api te hit korle views er kun data gula dekhabe seta define korte hoy.
  e. apps er urls.py ta project er urls.py te add korte hobe.
```

20. For creating a custom auth system or registration system:

    a. Create new app or module and add app name in `INSTALLED_APPS` array under settings.py file.

    ```
      python manage.py startapp authuser
    ```

    ```
    INSTALLED_APPS = [
    'authuser',
    ]

    AUTH_USER_MODEL = 'authuser.User'
    ```
