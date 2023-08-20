from rest_framework import (
    response,
    request,
    views,
    status
)

# Create your views here.
class TaskView(views.APIView):
    def get(self, obj):
        pass