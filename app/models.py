from django.db import models

# Create your models here.
class employee(models.Model):
    ename=models.CharField(max_length=50,primary_key=True)
    sal=models.IntegerField()

    def __str__(self):
        return self.ename
class dept(models.Model):
    ename=models.ForeignKey(employee, on_delete=models.CASCADE)
    dname=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.dname
