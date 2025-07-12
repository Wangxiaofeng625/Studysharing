from django.shortcuts import render, get_object_or_404, redirect
from .models import Course , ResourceFile,Post
from .forms import ResourceFileForm #从 .forms 导入表单类
from .forms import PostForm
from .models import Post, Reply
from .forms import ReplyForm

def index(request):
    # 从数据库获取所有的 Course 对象
    courses = Course.objects.all()

    # 准备要传递给模板的数据
    context = \
    {
        'courses': courses
    }

    # 渲染 templates/resources/index.html 模板，并把 context 数据传过去
    return render(request, 'resources/index.html', context)


def course_detail(request, course_id):
    #先获取课程对象
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        # 1. 如果是 POST 请求，用提交的数据创建表单实例
        form = ResourceFileForm(request.POST, request.FILES)
        if form.is_valid():
            # 2. 如果数据有效，处理并重定向
            new_resource = form.save(commit=False)
            new_resource.course = course
            new_resource.save()
            return redirect('course_detail', course_id=course.id)
        # 3. 如果数据无效，程序会自然地往下走，
        #    这时 'form' 变量里包含了用户的错误信息，正好可以传给模板显示
    else:
        # 4. 如果是 GET 请求，创建一个空的表单实例
        form = ResourceFileForm()

    # 5. 无论上面发生了什么（除了成功的重定向），程序最后都会来到这里
    #    此时，form 变量要么是一个空的表单（GET），要么是一个带有错误信息的表单（POST 失败）
    context = {
        'course': course,
        'form': form, # form 变量在这里总是存在的
    }
    return render(request, 'resources/course_detail.html', context)

def post_list(request, course_id):
    # 获取当前的课程对象，如果不存在则返回 404
    course = get_object_or_404(Course, pk=course_id)

    # 获取这门课程下的所有帖子，并按创建时间倒序排列（最新的在最前面）
    posts = course.posts.all().order_by('-created_at')

    context = {
        'course': course,
        'posts': posts,
    }
    # 渲染一个新的模板文件 course_detail.html
    return render(request, 'resources/post_list.html', context)


def create_post(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.course = course  # 关联到当前课程
            post.save()
            # 发布成功后，重定向到帖子列表页
            return redirect('post_list', course_id=course.id)
    else:
        form = PostForm()

    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'resources/create_post.html', context)


def post_detail(request, course_id, post_id):
    # 用一种更安全的方式获取 post，确保它属于正确的课程
    post = get_object_or_404(Post, pk=post_id, course__id=course_id)

    # 创建一个 course 变量，供模板使用
    course = post.course

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST, request.FILES)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.post = post
            parent_id = request.POST.get('parent_id')
            if parent_id:
                reply.parent = get_object_or_404(Reply, id=parent_id)
            reply.save()
            return redirect('post_detail', course_id=course.id, post_id=post.id)
    else:
        reply_form = ReplyForm()

    # 查询顶级回复
    top_level_replies = post.replies.filter(parent__isnull=True).order_by('created_at')

    # 构建一个包含所有必需变量的 context
    context = {
        'post': post,
        'course': course, # 确保 course 在这里
        'reply_form': reply_form,
        'top_level_replies': top_level_replies,
    }
    return render(request, 'resources/post_detail.html', context)