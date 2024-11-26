from rest_framework import serializers
from .models import Produit, Categorie , Metier
from .models import *



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create the User instance
        user = User.objects.create_user(**validated_data)


        return user


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['username', 'email', 'first_name', 'last_name','telephone']  

class MetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = ['id_metier', 'nom_metier', 'description']


class ProfessionalRequestSerializer(serializers.ModelSerializer):
    metiers = serializers.PrimaryKeyRelatedField(
        queryset=Metier.objects.all(),  # Allow selecting existing Metier objects
        many=True  # Since it's a many-to-many field
    )

    class Meta:
        model = Professional
        fields = ['metiers', 'localisation', 'description_experience', 'image_url']

    def create(self, validated_data):
        metiers_data = validated_data.pop('metiers')
        professional = Professional.objects.create(**validated_data)
        professional.metiers.set(metiers_data)  # Set the many-to-many relationship
        return professional
    


class ProfessionalSerializer(serializers.ModelSerializer):
    client = ClientSerializer()  # Nested serializer for client details

    class Meta:
        model = Professional
        fields = ['id', 'metiers', 'localisation', 'description_experience', 'avis_moyenne', 'status', 'image_url', 'client']

class ProfessionalStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ['status']




class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'  #  ['id_categorie', 'nom', 'description']

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'  # ['id_produit', 'nom', 'description', 'prix', 'categorie']

