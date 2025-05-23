from rest_framework import serializers
from blog.models import Author


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    created_at=serializers.DateTimeField(required=True)
    is_published = serializers.BooleanField(required=False)


    def create(self, validated_data):
        """
        Create and return a new `Author` instance, given the validated data.
        """
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Author` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.last_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        
        instance.save()
        return instance
    
class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    completed = serializers.BooleanField()
    author=serializers.IntegerField()