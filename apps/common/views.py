from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheckView(APIView):
    """
    Health check view for monitoring.
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        return Response({
            'status': 'healthy',
            'message': 'TutorConnect Nepal API is running',
            'version': '1.0.0'
        }, status=status.HTTP_200_OK)