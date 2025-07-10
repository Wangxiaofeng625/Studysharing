from django.contrib import admin
from .models import Course, ResourceFile,Post, Reply # 导入两个模型

# 把模型注册到 admin 后台
admin.site.register(Course)
admin.site.register(ResourceFile)
admin.site.register(Post)
admin.site.register(Reply)