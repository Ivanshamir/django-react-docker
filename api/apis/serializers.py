from rest_framework import serializers
from .models import MyTableModel
 
class MyTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTableModel
        fields = ['text']