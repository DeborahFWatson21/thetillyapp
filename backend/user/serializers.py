"""
Serializers for the user API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers

from core.models import Profile, Address, Business, SocialMedia, Client


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user objects."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return a user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class AddressSerializer(serializers.ModelSerializer):
    """Serializer for the address object."""

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Create and return an address."""
        return Address.objects.create(**validated_data)


class BusinessSerializer(serializers.ModelSerializer):
    """Serializer for the business object."""
    address = AddressSerializer()

    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ('id', )
        depth = 1

    def create(self, validated_data):
        # address = validated_data.pop('address')
        social_media = validated_data.pop('social_media')
        print(social_media)
        # address = Address.objects.create(**address)
        business = Business.objects.create(**validated_data)
        #social_media = SocialMedia.objects.create(**social_media, business=business)

        # if social_media is not None:
        #     social_media = SocialMedia.objects.create(**social_media)
        #     social_media.business = business
        #     social_media.save()
        #     return {business, social_media}
        # else:
        return business


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for the client object."""
    business = BusinessSerializer()
    address = AddressSerializer()

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('id', )


class SocialMedia(serializers.ModelSerializer):
    """Serializer for the social media object"""
    business = BusinessSerializer()

    class Meta:
        model = SocialMedia
        fields = '__all__'
        read_only_fields = ('id',)
