from library_api.viewsets import WriterViewset
from library_api.viewsets import BookViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('writer', WriterViewset)
router.register('book', BookViewset)