from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('post', views.PostModelView)
router.register('category', views.CategoryModelView)
router.register('comment', views.CommentModelView)

urlpatterns = [
    path('', include(router.urls)),
]
