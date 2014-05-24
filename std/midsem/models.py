from django.db import models

class Student(models.Model):
    enroll = models.IntegerField()
    name = models.CharField(max_length=200)

    def __unicode__(self):  
        msg = "Enroll : "+str(self.enroll)+"   Name : "+self.name
        return msg 
    
class ExamResult(models.Model):
    enroll = models.ForeignKey(Student)
    sub_mark = models.IntegerField(default=0)
    sub_name = models.CharField(max_length=200)

    def __unicode__(self):  
        msg = "Subject : "+self.sub_name+"   Marks : "+str(self.sub_mark)
        return msg

