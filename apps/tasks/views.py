from rest_framework import viewsets, status,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Task, TaskStatusLog
from .serializers import TaskSerializer, StatusLogSerializer,TaskDetailSerializer
from .filters import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = TaskFilter
    ordering_fields = '__all__'
    ordering = ['deadline']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        old_status = instance.status
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Log status change if status is updated
        if 'status' in request.data and request.data['status'] != old_status:
            TaskStatusLog.objects.create(
                task=instance,
                old_status=old_status,
                new_status=request.data['status'],
                changed_by=request.user
            )

        return Response(serializer.data)

class StatusLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaskStatusLog.objects.all()
    serializer_class = StatusLogSerializer
    permission_classes = [IsAuthenticated]




class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = TaskFilter
    ordering_fields = '__all__'
    ordering = ['deadline']

class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated]


class TaskStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        old_status = task.status
        new_status = request.data.get('status')
        if new_status and new_status != old_status:
            task.status = new_status
            task.save()
            TaskStatusLog.objects.create(
                task=task,
                old_status=old_status,
                new_status=new_status,
                changed_by=request.user
            )
            return Response({'status': 'updated'}, status=status.HTTP_200_OK)
        return Response({'error': 'No status change'}, status=status.HTTP_400_BAD_REQUEST)

#