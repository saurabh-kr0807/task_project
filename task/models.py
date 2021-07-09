from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class TaskDetail(models.Model):
    task_author = models.ForeignKey('auth.User', related_name='author',on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200)
    assign_to = models.ForeignKey('auth.User', related_name='assign_to',on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    complete_date = models.DateField()

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.task_title
