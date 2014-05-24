from django.contrib import admin

from midsem.models import Student,ExamResult

class ExamInline(admin.TabularInline):
    model = ExamResult
    extra = 5

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Student Information',{'fields': ['enroll','name']})
        ,
        ]
    inlines = [ExamInline]

    list_display = ('enroll', 'name')
    search_fields = ['name','enroll']
admin.site.register(Student,StudentAdmin)

