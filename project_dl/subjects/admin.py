from django.contrib import admin
from .models import Parent, Student
# Register your models here.


class ParentAdmin(admin.ModelAdmin):
    class Meta:
        db_table = "teachers"

    fields = ['parent_name', 'parent_surname']


class StudentAdmin(admin.ModelAdmin):
    class Meta:
        db_table = "students"

    fields = ['student_name', 'student_surname', 'parent_name', 'parent_student_id']

admin.site.register(Parent, ParentAdmin)
admin.site.register(Student, StudentAdmin)
