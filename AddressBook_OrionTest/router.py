from app.viewsets import UserViewset, TelephoneViewset, EmailViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewset)
router.register('user/telephone', TelephoneViewset)
router.register('user/email', EmailViewset)