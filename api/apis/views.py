from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MyTableModel
from .serializers import MyTableSerializer
from .utils import *
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'home': '/',
        'all_items': '/news/',
        'Create': '/news/create/'
    }
 
    return Response(api_urls)

@api_view(['GET'])
def news_list(request):
    try:
        cached_news = get_news_from_cache()
        if not cached_news:
            news = MyTableModel.objects.all()
            serializer = MyTableSerializer(news, many=True)
            
            add_news_to_cache(serializer.data)
            
            return Response({'isCached': False, 'news': serializer.data}, status=status.HTTP_200_OK)
        return Response({'isCached': True, 'news': cached_news}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_news(request):
    try:
        serializer = MyTableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        delete_news_from_cache()
        return Response({'message': 'News created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': 'Error creating news'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)