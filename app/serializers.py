from rest_framework import serializers
from .models import Ganre, Category, Period, Authors, Book
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        

class UserUpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'profile_picture']

class UserUpdateSecuritySerializer(serializers.ModelSerializer):
    new_password = serializers.SerializerMethodField()

    def New_password(self, obj):
        result = obj.new_password
        return result

    class Meta:
        model = User
        fields = ['email', 'password', 'new_password']


class AuthorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['id', 'full_name', "image", "birth_date", "death_date", "period"]

class AuthorsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['full_name', "image", "birth_date", 
                  "death_date", 'bio', 'country'
                  ]


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'poster', 'category', 'author']


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'poster', 'author', 'pages', 
                  'published', 'price', 'ganre', 'description',
                  ]
        

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['id', 'name']

class AuthorsDetailSerializer(serializers.ModelSerializer):
    author_books = BookListSerializer(many=True)


    class Meta:
        model = Authors
        fields = ['id', 'full_name', 'bio', 'image', 'birth_date', 'death_date', 'country', 'author_books']


class BookDetailSerializer(serializers.ModelSerializer):
    author_books = BookListSerializer(many=True)



    class Meta:
        model = Book        
        fields  = ['id','title', 'poster', 'pages', 
                  'published', 'price', 'ganre', 'description', 'author_books']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    

    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return super().validate(attrs)
    


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email'])
        if not user.exists():
            raise serializers.ValidationError({'msg': 'User yo\'q'})
        user = user.first()
        if not user.check_password(attrs.get('password')):
            raise serializers.ValidationError({
                'msg': "Pasword xato"
            })
        
        return attrs