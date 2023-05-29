from rest_framework.views import APIView
from .models import s_movie
from .serializers import movieSerializer
from django.db.models import Min, Max

from django.http.response import JsonResponse
import random

# Create your views here.
            
class getMovieTitle(APIView):
      def get(self, request):
            print('in get')
            foundMovie = False
            min_id = s_movie.objects.all().aggregate(min_id=Min("id"))['min_id']
            max_id = s_movie.objects.all().aggregate(max_id=Max("id"))['max_id']
            print('max_id', max_id)
            counter = 0
            while not foundMovie:
                  counter += 1
                  if counter > 6:
                        return JsonResponse("Oops, couldn't find a movie title for you.", status=404)
                  pk = random.randint(min_id, max_id)
                  print('pk', pk)

                  queryset = s_movie.objects.filter(pk=pk).values()
                  print(queryset)
                  movieTitle = queryset.first()
                  print(type(movieTitle))
                  foundMovie = True
                  return JsonResponse(movieTitle['movie_title'], safe=False)

