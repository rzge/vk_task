from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    friends = models.ManyToManyField('CustomUser', blank=True)

    def __str__(self):
        return self.username
# Create your models here.

class Friend_Request(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='to_user', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.from_user}{self.to_user}"
    def from_us(self):
        return f'ee'
# class FriendRequest(models.Model):
#     from_user = models.ForeignKey(CustomUser, related_name='friend_requests_sent', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(CustomUser, related_name='friend_requests_received', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ('from_user', 'to_user')
#
# class Friend(models.Model):
#     user = models.ForeignKey(CustomUser, related_name='friends', on_delete=models.CASCADE)
#     friend = models.ForeignKey(CustomUser, related_name='user_friends', on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('user', 'friend')

