from .views import NotificationList, NotificationDetail, StudentDetail, FacultyList
from django.urls import path

urlpatterns = [
	path('notifications/', NotificationList.as_view()),
	path('notifications/<int:pk>/', NotificationDetail.as_view()),
	path('faculty/', FacultyList.as_view()),
	path('<str:slug>/', StudentDetail.as_view()),
]