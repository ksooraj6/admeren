from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from saveTextApp.views.snippet.crud import SnippetCrud
from saveTextApp.views.snippet.tag import TagCrud

router = DefaultRouter(trailing_slash=False)
router.register('snippet', SnippetCrud, basename='crud') 
router.register('tag', TagCrud, basename='tag')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
# urlpatterns=[
# 	path("", views.index, name="index"),
#     ]