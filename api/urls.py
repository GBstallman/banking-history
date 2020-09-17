from django.urls import path, include
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register("client", ClientViewset)
router.register("bank_account", Bank_AccountViewset)

urlpatterns = [
	path("", include(router.urls)),
]
