"""
URL configuration for StudyShareProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
#确保从 django.urls 导入了 include
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    #此处admin相当于调用了模板

    # 将所有匹配空路径 '' 的请求，
    # 都转交给 'resources.urls' 这个文件去进一步处理。
    path('', include('resources.urls')),
]
# 只有在 DEBUG 模式下（即开发模式），才添加这个URL路由规则
# 个人测试的时候，用来处理看看是否真的能够下载文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)