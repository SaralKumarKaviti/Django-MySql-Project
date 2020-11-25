"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.addTask,name='add'),
    path('view/',views.viewTask),
    path('edit/<str:pk>',views.editTask,name='edit'),
    path('delete/<str:pk>',views.deleteTask,name='delete'),
    path('csv',views.getfile),

    # path('show',views.viewTask),
    # path('edit/<int:id>',views.edit),
    # path('update/<int:id>',views.update),
    # path('delete/<int:id>',views.destroy),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('tasks.urls'))
# ]
