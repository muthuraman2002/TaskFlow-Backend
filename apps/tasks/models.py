# from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings

# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     owner = models.ForeignKey(User, related_name='tasks_projects_owned', on_delete=models.CASCADE)  # changed

#     def __str__(self):
#         return self.name

# class Task(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('blocked', 'Blocked'),
#     ]
#     PRIORITY_CHOICES = [
#         (1, 'Low'),
#         (2, 'Medium'),
#         (3, 'High'),
#         (4, 'Critical'),
#     ]

#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     project = models.ForeignKey(Project, related_name='tasks_tasks', on_delete=models.CASCADE)  # changed
#     assigned_user = models.ForeignKey(User, related_name='tasks_tasks_assigned', on_delete=models.SET_NULL, null=True)  # changed
#     deadline = models.DateTimeField()
#     priority = models.IntegerField(choices=PRIORITY_CHOICES)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

# class TaskStatusLog(models.Model):
#     task = models.ForeignKey(Task, related_name='status_logs', on_delete=models.CASCADE)
#     old_status = models.CharField(max_length=20)
#     new_status = models.CharField(max_length=20)
#     changed_at = models.DateTimeField(auto_now_add=True)
#     changed_by = models.ForeignKey(User, related_name='tasks_status_changes', on_delete=models.CASCADE)  # changed

#     def __str__(self):
#         return f"Task {self.task.id} changed from {self.old_status} to {self.new_status} by {self.changed_by.username} on {self.changed_at}"


from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_projects_owned', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('blocked', 'Blocked'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks_tasks', on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_tasks_assigned', on_delete=models.SET_NULL, null=True)
    deadline = models.DateTimeField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TaskStatusLog(models.Model):
    task = models.ForeignKey(Task, related_name='status_logs', on_delete=models.CASCADE)
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_status_changes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Task {self.task.id} changed from {self.old_status} to {self.new_status} by {self.changed_by.username} on {self.changed_at}"