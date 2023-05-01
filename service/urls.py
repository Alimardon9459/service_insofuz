from .views import *
from django.urls import path, include
from rest_framework import routers
# akk
router = routers.DefaultRouter()
router.register('worker', Worker__ViewSet)
router.register('user', User__ViewSet)
router.register('worker_report', WorkerReport__ViewSet)
router.register('order_for_user', OrderForUser__ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
