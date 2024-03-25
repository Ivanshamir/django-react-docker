from django.db import models

# Create your models here.
class MyTableModel(models.Model):
  id = models.AutoField(primary_key=True)  
  text = models.TextField(null=False, blank=False) 

  def __str__(self):
    return self.text[:20]

  class Meta:
        db_table = 'mytable'
        ordering = ['-id']