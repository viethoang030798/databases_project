from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'Courses', views.CourseViewSet)
router.register(r'Curriculums', views.CurriculumViewSet)
router.register(r'Degreeprograms', views.DegreeprogramViewSet)
router.register(r'Implementations', views.ImplementationViewSet)
router.register(r'Rooms', views.RoomViewSet)
router.register(r'RoomImplementations', views.RoomImplementationViewSet)
router.register(r'Subgroups', views.SubgroupViewSet)
router.register(r'SubgroupImplementations', views.SubgroupImplementationViewSet)
router.register(r'Teachers', views.TeacherViewSet)
router.register(r'TeacherDegreeprograms', views.TeacherDegreeprogramViewSet)
router.register(r'TeacherImplementations', views.TeacherImplementationViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
