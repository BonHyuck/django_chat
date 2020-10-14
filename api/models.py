from django.db import models

# Create your models here.
class ChatInfo(models.Model):
    # 보낼 메시지
    message = models.TextField()
    # 보낼 시간 (시, 24시간 기준)
    chat_hour = models.IntegerField()
    # 보낼 시간 (분)
    chat_minute = models.IntegerField()
    # 보낼 곳
    # 기본값 = 구본혁(테스트용)
    send_to = models.CharField(max_length=200)