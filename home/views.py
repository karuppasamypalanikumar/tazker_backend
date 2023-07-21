from rest_framework import (
    response, 
    views,
    request,
    permissions,
    renderers,
    status
)

class HomeView(views.APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [renderers.TemplateHTMLRenderer]
    def get(self, request: request.Request):
        return response.Response(
            status=status.HTTP_200_OK,
            template_name="home/index.html"
        )

class HealthCheckView(views.APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [renderers.JSONRenderer]
    def get(self, request: request.Request):
        return response.Response(
            data={
                "status_code": 1,
                "status_message": "site reached successfully"
            },
            status=status.HTTP_200_OK
        )