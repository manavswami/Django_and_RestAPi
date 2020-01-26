
from rest_framework.serializers import ModelSerializer
from testapp.models import global_database





class global_databaseSerializer(ModelSerializer):
    
    
    
    class Meta:
        model = global_database   #same name model that we created  above  to creat api
        fields = '__all__'

