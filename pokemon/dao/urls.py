from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.PokemonView.as_view(), name = 'index'),
    path('<pk>', views.PokemonView.as_view()),
]