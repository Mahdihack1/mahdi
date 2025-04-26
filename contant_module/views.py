from django.shortcuts import render
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,permissions
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .serializers import ContactSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ContactFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains')
    phone=django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model=Contact
        fields=('name','phone')

class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ContactFilter

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
