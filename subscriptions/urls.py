from django.urls import path
from .views import SubscriptionCreateView, SubscriptionDeleteView, SubscriptionListView


urlpatterns = [
    path('api/v1/subscriptions/', SubscriptionCreateView.as_view()),
    path('api/v1/subscriptions/list/', SubscriptionListView.as_view()),  
    path('api/v1/subscriptions/<str:friend_email>/', SubscriptionDeleteView.as_view(), name='subscription-delete')
    ] 