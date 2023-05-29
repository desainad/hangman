from django.urls import path
from backendApp.views import getMovieTitle
#movie router
urlpatterns = [path('api/movies/', getMovieTitle.as_view())]
