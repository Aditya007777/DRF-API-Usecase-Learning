from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from api.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),
    
    # path('employees/', views.employeesView.as_view()),
    # path('employees/<int:pk>', views.employeeDetailView.as_view()),
    path('', include(router.urls)),
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('blogs/<int:pk>', views.BlogDetailView.as_view()),
    path('comments/<int:pk>', views.CommentDetailView.as_view()),
]

