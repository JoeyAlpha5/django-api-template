from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class HealthCheckAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            return Response(
                data={"status": "ok"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                data={"status": "error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )