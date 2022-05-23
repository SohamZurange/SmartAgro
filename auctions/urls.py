from django.urls import path

from . import views
app_name = 'auctions'

urlpatterns = [
    path('create/', views.create, name='create'),
    #path('crop_prediction/', views.crop_prediction, name='crop_prediction'),
    path('crop_prediction/', views.crop_prediction, name="crop_prediction"),
    path('index2/', views.index2, name="index2"),

    # path('myauctions/', views.my_auctions, name='my_auctions'),
    # Example: /auctions/
   # path('', views.auctions, name='auctions'),
    path('', views.index, name="index"),
#path("crop_prediction", views.crop_prediction, name='crop_prediction'),
    # Example: /auctions/5/
    path('<int:auction_id>/', views.detail, name='detail'),
    # Example: /auctions/5/results/
    # path('<int:auction_id>/results/', views.results, name='results'),
    # Example: /auctions/5/bid/
    path("contact/", views.contact, name='contact'),
    path('<int:auction_id>/bid/', views.bid, name='bid'),
]
