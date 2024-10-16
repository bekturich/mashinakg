from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', CarViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name= 'car_list'),
    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='car_detail'),

    path('user', UserProfileViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='user_list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update', 'delete': 'destroy'}), name='user_detail'),

    path('category', CategoryViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                                        'put': 'update', 'delete': 'destroy'}), name='category_detail'),

    path('CarMake', CarMakeViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='CarMake_list'),
    path('CarMake/<int:pk>/', CarMakeViewSet.as_view({'get': 'retrieve',
                                                     'put': 'update', 'delete': 'destroy'}), name='CarMake_detail'),

    path('model', ModelViewSet.as_view({'get': 'list',
                                        'post': 'create'}), name='model_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='model_detail'),

    path('contact', ContactViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='contact_list'),
    path('contact/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='contact_detail'),

    path('comment', CommentViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='comment_detail'),

    path('Favorite', FavoriteViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='favorite_list'),
    path('Favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='favorite_detail'),

    path('FavoriteCar', FavoriteCarViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='favoriteCar_list'),
    path('FavoriteCar<int:pk>/', FavoriteCarViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='favoriteCar_detail'),
]