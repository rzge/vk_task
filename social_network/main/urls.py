from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.index, name='home'),
    path('search_results/', views.search_results, name='search_results'), #перенаправит на страницу поиска
    path('search_results/', views.search_results, name='search_results'),
    path('search_results/send_friend_request/<int:userID>', users_views.send_friend_request, name='send_friend_request'),
    path('search_results/accept_friend_request/<int:requestID>', users_views.accept_friend_request, name='accept_friend_request'),
]