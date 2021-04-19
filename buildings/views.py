from rest_framework import permissions, serializers,status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Home, ImageFiles
from . serializers import HomeSerializer, HomeDetailSerializer, ImageFilesSerializer

#from rest_framework import filters

# Create your views here.
class HomeListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = HomeSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field='slug'

class HomeDetailAPIView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = HomeDetailSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field='slug'

class ImageView(APIView):
    def get(self, request, pk, format=None):
        home = Home.objects.get(pk=pk)
        images = home.images.all()
        serializer = ImageFilesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from django.db.models import Q, query
class Search(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data=self.request.data
        str=data['str']
        price_from=data['price_from']
        price_to=data['price_to']
        city=data['city']
        q=(Q(description__icontains=str)) | (Q(title__icontains=str))
        queryset=Home.objects.filter(is_published=True).filter(price__gte=price_from).filter(price__lte=price_to).filter(city__iexact=city)
        queryset=queryset.filter(q)
        serializer=HomeSerializer(queryset, many=True)
        return Response(serializer.data)



