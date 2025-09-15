# from django.db import models
# from django.contrib.auth.models import User


# owner = models.ForeignKey(User, related_name='projects_projects_owner', on_delete=models.CASCADE)
# assigned_user = models.ForeignKey(User, related_name='projects_tasks_assigned_user', on_delete=models.SET_NULL, null=True)

# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     owner = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Task(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('blocked', 'Blocked'),
#     ]

#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     assigned_user = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True)
#     deadline = models.DateTimeField()
#     priority = models.IntegerField(default=1)  # 1: Low, 2: Medium, 3: High
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


from django.db import models
from django.conf import settings  # ✅ use settings.AUTH_USER_MODEL instead of User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ✅ swapped user model
        related_name='projects',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('blocked', 'Blocked'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ✅ swapped user model
        related_name='tasks',
        on_delete=models.SET_NULL,
        null=True
    )

    deadline = models.DateTimeField()
    priority = models.IntegerField(default=1)  # 1: Low, 2: Medium, 3: High
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
