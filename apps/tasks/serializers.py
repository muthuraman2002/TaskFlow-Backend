from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_user', 'deadline', 'priority', 'status']

class TaskDetailSerializer(serializers.ModelSerializer):
    status_history = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_user', 'deadline', 'priority', 'status', 'status_history']

    def get_status_history(self, obj):
        return obj.status_logs.all().values('task_id', 'old_status', 'new_status', 'timestamp', 'user')
# ...existing code...

class StatusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task.status_logs.rel.related_model  # Assuming status_logs is a related_name for StatusLog model
        fields = ['task_id', 'old_status', 'new_status', 'timestamp', 'user']

# ...existing code...