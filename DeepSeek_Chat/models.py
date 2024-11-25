from django.db import models
from django.contrib.auth.models import User

# 可以自定义其他字段和功能，例如用户个人信息等
# 目前我们仅使用默认的 User 模型

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 外键关联到用户
    timestamp = models.DateTimeField(auto_now_add=True)  # 自动添加创建时间戳
    html_content = models.TextField()  # 存储聊天的HTML源码

    class Meta:
        unique_together = ('user', 'timestamp')  # 确保每个用户每次对话的记录是唯一的

    def __str__(self):
        return f"Chat with {self.user.username} at {self.timestamp}"
