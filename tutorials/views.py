from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Tutorial
from .models import UserProfile
from .serializers import TutorialSerializer,MyTokenObtainPairSerializer
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
import django_filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
class TutorialFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    #description = django_filters.ChoiceFilter(choices=Tutorial.CATEGORY_CHOICES)
    published_date = django_filters.DateFilter()

    class Meta:
        model = Tutorial
        fields = ['title', 'published_date']


from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 1



class TutorialAPIView(APIView):
    #authentication_classes =[JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    pagination_class = ProductPagination



    def get(self, request):
        tutorials = Tutorial.objects.all()
        #paginator = self.pagination_class()
        #paginated_products = paginator.paginate_queryset(tutorials, request)
        serializer = TutorialSerializer(tutorials, many=True)
        return Response(serializer.data)
        filter_backends = [filters.DjangoFilterBackend,filters.OrderingFilter]
        filterset_class = TutorialFilter
        ordering_fields = ['id', 'title']
        ordering = ['id-']
        ordering = ['id-']


    def post(self, request):
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tutorial = self.get_object(pk)
        tutorial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyTokenObtainPairView(TokenObtainPairView):
    # Specify the serializer class for customizing the token response
    serializer_class = MyTokenObtainPairSerializer
