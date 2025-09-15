from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('projects/', include('apps.projects.urls')),
    path('tasks/', include('apps.tasks.urls')),
]