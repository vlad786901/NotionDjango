from django.urls import path
from .views import (
    RequestCreateView,
    RequestMessageCreateView,
    RequestDetailView,
    RequestMessageListView,
    RequestListView
)

urlpatterns = [
    path('requests/',
         RequestListView.as_view(), name='request-list'),
    path('requests/<int:pk>/',
         RequestDetailView.as_view(), name='request-detail'),
    path('requests/create/',
         RequestCreateView.as_view(), name='request-create'),
    path('requests/<int:request_id>/messages/',
         RequestMessageListView.as_view(), name='request-messages'),
    path('requests/<int:request_id>/messages/create/',
         RequestMessageCreateView.as_view(), name='request-message-create'),
]
