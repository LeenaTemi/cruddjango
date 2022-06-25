from django.contrib import admin
from django.urls import path
from .views import BlogAppCreateView

urlpatterns = {
    path('admin/', admin.site.urls),
    path('blog/', Include('blog.urls'))
    path('' BlogAppCreateView.as_view(), 
    name='home')
}