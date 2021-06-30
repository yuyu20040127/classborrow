from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from classrooms.models import *
from borrower.models import *

class Log(models.Model):
    borrower = ForeignKey(Borrower, CASCADE)
    Classrooms = ForeignKey(Classrooms, CASCADE)
    checkout = DateTimeField('借閱時間', auto_now_add=True)
    returned = DateTimeField('歸還時間', null=True)  

    def __str__(self):
        return "{} | {} | {}".format(
            self.checkout, 
            self.borrower.realname, 
            self.borrower.title
        )