from rest_framework import serializers
from .models import MyModel

class MonModeldeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['name', 'description']





# from rest_framework import serializers
# from .models import Mymodel

# class Myseria(serializers.ModelSerializer):
#     class Meta :
#         model = Mymodel
#         fields = ["nom","prenom"]

