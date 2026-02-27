from rest_framework.routers import DefaultRouter
from .views import CRUD_Discussion, CRUD_Comment, CRUD_Community


router = DefaultRouter()
router.register("discussions", CRUD_Discussion)
router.register("comments", CRUD_Comment )
router.register("communities", CRUD_Community)

urlpatterns = router.urls

