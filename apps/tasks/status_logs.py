from django.db import models
from django.contrib.auth.models import User

class StatusLog(models.Model):
    task_id = models.IntegerField()
    old_status = models.CharField(max_length=50)
    new_status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Task {self.task_id}: {self.old_status} -> {self.new_status} by {self.user.username} on {self.timestamp}"