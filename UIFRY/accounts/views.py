from django.shortcuts import render
from rest_framework.validators import UniqueValidator


def register_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    full_name = request.POST.get('full_name')
    pass


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email',)
        extra_kwargs = {
            # 'full_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"error": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
            #  full_name=validated_data['full_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
