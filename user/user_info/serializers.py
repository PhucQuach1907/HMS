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
        extra_kwargs = {
            'password': {'write_only': True},
        }

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
        fullname = validated_data.get('fullname', None)
        address = validated_data.get('address', None)

        if fullname:
            if instance.fullname:
                FullnameSerializer.update(FullnameSerializer(), instance=instance.fullname,
                                          validated_data=fullname)
            else:
                instance.fullname = Fullname.objects.create(**fullname)

        if address:
            if instance.address:
                AddressSerializer.update(AddressSerializer(), instance=instance.address, validated_data=address)
            else:
                instance.address = Address.objects.create(**address)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
