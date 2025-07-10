from django.urls import path
from . import views  # 从当前文件夹导入 views.py

# 这个列表定义了本应用内的所有 URL 路由规则
urlpatterns = [
    # 当访问的路径是空的 (比如 'http://.../') 时，
    # 调用 views.py 文件里的 index 函数来处理，
    # 并给这个路由起个名字叫 'index'，方便以后引用。
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    #<int:course_id> 是一个路径转换器，它会匹配一个整数，并把这个整数作为名为 course_id 的参数传递给视图函数。
    #course.id是resources/templates/resources/index.html引用的名字
 path('course/<int:course_id>/posts/', views.post_list, name='post_list'),
 path('course/<int:course_id>/posts/create/', views.create_post, name='create_post'),
 path('course/<int:course_id>/post/<int:post_id>/', views.post_detail, name='post_detail'),
]
