# using signals

from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
# from api.auth import CustomAuthToken
# creating router project
router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename = 'student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/', obtain_auth_token),
    # path('gettoken/', CustomAuthToken.as_view()),

]
