from django.db import models


# Create your models here.
class BaseClassInfo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    create_ts = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, null=True)
    update_ts = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50, null=True)
    delete_ts = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class UserInfo(BaseClassInfo):
    # Нельзя знаки все кроме ['_', '.']
    name = models.CharField(max_length=255, null=False)
    nickname = models.CharField(max_length=255, null=False)
    telephone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    retype_password = models.CharField(max_length=100)
    email = models.EmailField(null=False)

    class Meta:
        managed = True


