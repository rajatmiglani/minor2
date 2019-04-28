from django.conf.urls import url,include
from rest_framework import routers
from fileupload_rest.viewsets import Uploadfileviewset


router = routers.DefaultRouter()
router.register('file',Uploadfileviewset,'files')

urlpatterns=[
	url(r'^', include(router.urls))
]