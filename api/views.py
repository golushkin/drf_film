from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from .models import Man
from .serializers import ManSerializer, UserSerializer
from .permissions import isAuthor

class UserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class ManView(ListCreateAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ManDetailView(RetrieveDestroyAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
    permission_classes = [isAuthor]