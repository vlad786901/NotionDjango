from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Request, RequestMessage
from .serializers import RequestSerializer, RequestMessageSerializer


class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RequestMessageCreateView(generics.CreateAPIView):
    queryset = RequestMessage.objects.all()
    serializer_class = RequestMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request = Request.objects.get(id=self.request.data.get('request'))
        serializer.save(user=self.request.user, request=request)


class RequestDetailView(generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]


class RequestMessageListView(generics.ListAPIView):
    serializer_class = RequestMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RequestMessage.objects.filter(request_id=self.kwargs['request_id'])


class RequestListView(generics.ListAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)
