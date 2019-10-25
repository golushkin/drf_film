from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Man
from .serializers import ManSerializer

class ManView(ListCreateAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer

class ManDetailView(RetrieveDestroyAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer