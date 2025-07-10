from django.db import models
#课程
class Course(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="课程名称")
    description = models.TextField(blank=True, null=True, verbose_name="课程描述")

    def __str__(self):
        return self.name
#资源列表
class ResourceFile(models.Model):
    title = models.CharField(max_length=50, verbose_name="资料标题")
    file = models.FileField(upload_to='%Y/%m/%d/', verbose_name="文件")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='resources', verbose_name="所属课程")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
#Course: 第一个参数，指明了这个外键要关联到哪个模型。在这里，我们把 ResourceFile 关联到了 Course。
#on_delete=models.CASCADE: 级联删除。这是一个非常重要的删除规则。它规定了：如果所关联的那个 Course 对象被删除了
#（比如你删除了“高等数学”这门课），那么所有属于这门课的 ResourceFile 记录也应该自动被一并删除。
#related_name='resources': 反向关联名称。这是一个方便的“快捷方式”。它允许我们能从一个 Course 对象，
#轻松地反向查询所有属于它的 ResourceFile。
    def __str__(self):
        return self.title


#帖子
class Post(models.Model):
    # 关联到课程，一个课程下可以有很多帖子
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='posts', verbose_name="所属课程")

    title = models.CharField(max_length=200, verbose_name="帖子标题")

    # TextField 用于存放帖子正文
    content = models.TextField(verbose_name="帖子内容")

    # 如果你想支持上传图片，可以加一个 ImageField
    # 需要安装 Pillow 库: pip install Pillow
    image = models.ImageField(upload_to='post_images/%Y/%m/%d/', blank=True, null=True, verbose_name="帖子图片")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")

    # 如果未来有用户系统，可以关联作者
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


#回复
class Reply(models.Model):
    # 关联到帖子，一个帖子下可以有很多回复
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies', verbose_name="所属帖子")

    content = models.TextField(verbose_name="回复内容")

    image = models.ImageField(upload_to='reply_images/%Y/%m/%d/', blank=True, null=True, verbose_name="回复图片")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="回复时间")

    def __str__(self):
        return f"Reply to '{self.post.title}'"