from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveAPIView,RetrieveDestroyAPIView, RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from . serializers import AgentSerializer
from . models import Agent

# Create your views here.
class AgentListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all().order_by('-id')
    serializer_class = AgentSerializer
    pagination_class = None

class AgentDetailView(RetrieveAPIView):
    queryset = Agent.objects.all().order_by('-id')
    serializer_class = AgentSerializer

class TopSellerListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.filter(top_seller=True)
    serializer_class = AgentSerializer
    pagination_class = None