from .views import NotificationList, NotificationDetail
from django.urls import path

urlpatterns = [
	path('notifications/', NotificationList.as_view()),
	path('notifications/<int:pk>/', NotificationDetail.as_view()),
]