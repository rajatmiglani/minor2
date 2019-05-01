from django.conf.urls import url,include
from rest_framework import routers
from fileupload_rest.viewsets import UploadfileViewSet
#from rest_framework.urlpatterns import format_suffix_patterns



router = routers.DefaultRouter()
router.register('file',UploadfileViewSet,'files')
app_name="fileupload_rest"
urlpatterns=[
	url(r'^', include(router.urls))
]