from library_api.viewsets import AuthorViewset
from library_api.viewsets import BookViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', AuthorViewset)
router.register('book', BookViewset)