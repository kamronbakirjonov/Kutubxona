from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',salom),
    path('mualumot/',index),
    path('talabalar/',talabalar),
    # path('mualiflar/',mualliflar),
    path('delete/student/<int:id>/',delete_student),
]




