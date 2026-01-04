from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class TestAurhAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
            return Response({'message': 'Success! You are logged in'})

class PlanListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.serializer_class
        return PlanCreateSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlanRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return PlanUpdateSerializer
        return self.serializer_class

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



