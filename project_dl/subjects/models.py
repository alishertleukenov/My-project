from django.db import models

# Create your models here.

class Student(models.Model):
    class Meta:
        db_table = "students"
    student_name = models.CharField(max_length=200)
    student_surname = models.CharField(max_length=200)
    parent_name = models.CharField(max_length=200)
    parent_student_id = models.IntegerField()

class Parent(models.Model):
    class Meta:
        db_table = "parents"
    parent_name = models.CharField(max_length=200)
    parent_surname = models.CharField(max_length=200)
#
# class Comment(models.Model):
#     class Meta:
#         db_table = 'comments_s'
#     comment_text = models.TextField()
#     comment_subject = models.ForeignKey(Student, on_delete=models.CASCADE)