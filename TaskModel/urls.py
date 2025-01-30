from django.contrib import admin
from django.urls import path, include

from tasks.views import task_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("tasks.urls")),
    path('tasks/', include('tasks.urls')),

]
