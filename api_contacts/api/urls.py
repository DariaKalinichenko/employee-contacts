from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientView, EmployeeView, ContactView

router = DefaultRouter()
router.register('clients', ClientView, basename='clients')
router.register('employee', EmployeeView, basename='employee')
router.register('contact', ContactView, basename='contact')


urlpatterns = [
    path('', include(router.urls)),
]
