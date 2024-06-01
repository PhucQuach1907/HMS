from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Fullname, Address


class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = ('id', 'first_name', 'mid_name', 'last_name')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'noHouse', 'street', 'district', 'city', 'country')


class UserSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    address = AddressSerializer()

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'fullname', 'address', 'gender', 'dob', 'phone_number', 'user_type',
            'login_id')
        read_only_fields = ['login_id']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user_type = validated_data.get('user_type', 'patient')
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')

        fullname = Fullname.objects.create(**fullname_data)
        address = Address.objects.create(**address_data)

        validated_data['fullname'] = fullname
        validated_data['address'] = address

        if user_type == 'doctor':
            user = User.objects.create_doctor(**validated_data)
        elif user_type == 'admin':
            user = User.objects.create_admin(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)

        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        fullname_data = validated_data.pop('fullname', None)
        address_data = validated_data.pop('address', None)

        if fullname_data:
            try:
                fullname_instance = Fullname.objects.get(**fullname_data)
            except Fullname.DoesNotExist:
                fullname_instance = Fullname.objects.create(**fullname_data)
            except Fullname.MultipleObjectsReturned:
                fullname_instance = Fullname.objects.filter(**fullname_data).first()

        if address_data:
            try:
                address_instance = Address.objects.get(**address_data)
            except Address.DoesNotExist:
                address_instance = Address.objects.create(**address_data)
            except Address.MultipleObjectsReturned:
                address_instance = Address.objects.filter(**address_data).first()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
