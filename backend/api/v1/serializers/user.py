from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'date_of_birth',
            'phone_number',
            'city',
            'passport_series',
            'passport_number',
            'passport_issue_date',
            'passport_issued_by',
            'consent_to_rights',
            'сonsent_to_processing'
        ]

    def create(self, validated_data):
        return UserAccount.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        validators=[validate_password]
    )
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')

        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                {'message': 'Пароли не совпадают.'}
            )

        return attrs


class UserApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id']


class UserSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'phone_number'
        )
