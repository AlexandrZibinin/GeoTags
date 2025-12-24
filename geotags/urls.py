from django.urls import path
from geotags.apps import GeotagsConfig
from geotags.views import PointCreateAPIView, PointRetrieveAPIView, PointListAPIView, PointUpdateAPIView, \
    PointDeleteAPIView

app_name = GeotagsConfig.name

urlpatterns = [
    path('api/points/create/', PointCreateAPIView.as_view(), name='point-create'),
    path('api/points/list/', PointListAPIView.as_view(), name='point-list'),
    path('api/points/<int:pk>/retrieve/', PointRetrieveAPIView.as_view(), name='point-retrieve'),
    path('api/points/<int:pk>/update/', PointUpdateAPIView.as_view(), name='point-update'),
    path('api/points/<int:pk>/delete/', PointDeleteAPIView.as_view(), name='point-delete'),
]