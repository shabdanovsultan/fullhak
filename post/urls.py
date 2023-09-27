from django.urls import path, include
from .views import PostView, PostCategorySearchView, PostRecommendationsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostView)


urlpatterns = [
    # path('', include(router.urls)),
    path('api/v1/posts/', PostView.as_view({'post': 'create', 'get': 'list'})),
    path('api/v1/posts/<int:pk>/', PostView.as_view({'delete': 'destroy','get':'retrieve'})),
    path('api/v1/posts/search/',PostCategorySearchView.as_view()),
    path('api/v1/recomendations/', PostRecommendationsView.as_view()),
]

