from rest_framework import serializers
from saveTextApp.models import Savetext, Tag
from django.contrib.auth.models import User


class TextSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=250)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), required=False)
    
    class Meta:
        model = Savetext
        fields = ('title', 'user', 'created_at', 'tag')

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.tag = validated_data.get('tag', instance.tag)
    #     instance.save()
    #     return instance

class TagSerializer(serializers.ModelSerializer):
    tag_title = serializers.CharField(max_length=150)

    class Meta:
        model = Tag
        fields = ('tag_title', )