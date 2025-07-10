from django import forms
from .models import ResourceFile
from .models import Post
from .models import Reply

class ResourceFileForm(forms.ModelForm):
    class Meta:
        model = ResourceFile  # 指明这个表单是为 ResourceFile 模型服务的
        fields = ['title', 'file'] # 指定表单中需要用户填写的字段
        # 可以用 'description' 替换 'title'，取决于你的模型
        # Django 会自动根据模型字段的类型生成合适的表单输入框
        # 比如 CharField -> <input type="text">, FileField -> <input type="file">
        #可以自动处理数据验证（比如文件是否为空）、生成 HTML 表单元素、提供更强的安全性。

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 我们只需要用户填写标题、内容和图片
        fields = ['title', 'content', 'image']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content', 'image']
        # 让输入框更友好
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': '写下你的回复...'}),
        }
        labels = {
            'content': '回复内容',
            'image': '上传图片'
        }