from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from categories.models import Category
from categories.serializers import CategoryListSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()

    serializer_classes = {
        "list": CategoryListSerializer,
        "retrieve": CategorySerializer,
    }

    default_serializer_class = CategoryListSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False)
    def roots(self, request):
        queryset = Category.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
