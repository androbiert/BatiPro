
from rest_framework import serializers
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
        fields = ['id','username', 'email', 'first_name', 'last_name','telephone' ,'image_url']  

class ClientGenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['username','first_name', 'last_name' ,'image_url']


class MetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = ['id_metier', 'nom_metier', 'description']


class ProfessionalRequestSerializer(serializers.ModelSerializer):
    metiers = serializers.PrimaryKeyRelatedField(
        queryset=Metier.objects.all(),  
        many=True  
    )

    class Meta:
        model = Professional
        fields = [
            'metiers', 'localisation', 'about_me', 'description_experience',
            'birth_date', 'postal_code', 'image_url'
        ]

    def create(self, validated_data):
        metiers_data = validated_data.pop('metiers')
        professional = Professional.objects.create(**validated_data)
        professional.metiers.set(metiers_data)  

        return professional
    
class ProfessionalSerializer(serializers.ModelSerializer):
    client = ClientSerializer()  
    metiers = MetierSerializer(many=True)
    class Meta:
        model = Professional
        fields = ['id', 'metiers', 'localisation', 'description_experience','about_me' , 'birth_date','postal_code', 'avis_moyenne', 'status','join_date', 'image_url', 'client']

class ProfessionalUpdateSerializer(serializers.ModelSerializer):
    metiers = serializers.PrimaryKeyRelatedField(
        queryset=Metier.objects.all(),
        many=True
    )

    class Meta:
        model = Professional
        fields = ['metiers', 'description_experience', 'about_me', 'localisation', 'image_url']

    def update(self, instance, validated_data):
        metiers_data = validated_data.pop('metiers', None)  
        for attr, value in validated_data.items():
            setattr(instance, attr, value) 
        if metiers_data:
            instance.metiers.set(metiers_data)  
        instance.save()
        return instance
class ProfessionalStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ['status']


class AvisProfSerializer(serializers.ModelSerializer):
    client = ClientGenSerializer()  
    class Meta:
        model = AvisProf
        fields = ['note','commentaire' , 'date_avis' , 'client']
        read_only_fields = ['client', 'professionnel']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id_notification', 'contenu', 'date_recoi', 'id_receveur']
        read_only_fields = ['id_notification', 'date_recoi']  


class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        fields = ['id_annonce', 'titre', 'contenu', 'vu_par', 'image_url', 'date_publication']
        read_only_fields = ['professionnel']