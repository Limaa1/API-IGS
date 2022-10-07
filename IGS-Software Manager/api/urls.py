from django.contrib import admin
from django.urls import path, include
from core.views import EmployeesViewSet, DepartmentViewSet, EmployeesListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employee', EmployeesViewSet)
router.register(r'department', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("index/", EmployeesListView.as_view())
]

