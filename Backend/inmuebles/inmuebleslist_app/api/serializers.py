from inmuebleslist_app.models import Inmueble
from rest_framework import serializers # type: ignore

def column_longitud(value):
    if len(value)<2:
        raise serializers.ValidationError("el valor es demasiado corta")
    

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    _direccion = serializers.CharField(validators=[column_longitud])
    pais = serializers.CharField(validators=[column_longitud])
    description = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance._direccion  = validated_data.get('_direccion',instance._direccion)
        instance.pais  = validated_data.get('pais',instance.pais)
        instance.description  = validated_data.get('description',instance.description)
        instance.imagen  = validated_data.get('imagen',instance.imagen)
        instance.active  = validated_data.get('active',instance.active)
        instance.save()
        return instance
    def validate(self, data):
        if data['_direccion'] == data['pais']:
            raise serializers.ValidationError("La dirección y el país no pueden ser iguales")
        else:
            return data
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("La url de la imagen es demasiado corta")
        else:
            return data