from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Bet, Variant, Event, BetVariant, EventSubCategory, EventCategory
from django.utils.timezone import now

class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class EventSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        pass

    active = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    active_due_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def get_active(self, obj):
        return (obj.active_due_date - now()).days > 0

    class Meta:
        model = Event
        fields = '__all__'


class BetSerializer(serializers.ModelSerializer):
    event = EventSerializer()

    class Meta:
        model = Bet
        fields = ['id', 'bet_maker', 'event']


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class BetVariantSerializer(serializers.ModelSerializer):
    # variant = VariantSerializer()

    class Meta:
        model = BetVariant
        fields = '__all__'
        depth = 1


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
