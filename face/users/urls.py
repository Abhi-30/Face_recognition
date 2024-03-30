from django.urls import path,include
from . views import Checkuserexist

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('checkuserexists/',Checkuserexist.as_view(),name='checkuser')
]