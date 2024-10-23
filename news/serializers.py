from rest_framework import serializers
from .models import News, Media, Url


class MediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Media
    fields = ('media', 'media_type',)


class UrlSerializer(serializers.ModelSerializer):
  class Meta:
    model = Url
    fields = ('title', 'url',)


class NewsSerializer(serializers.ModelSerializer):
  media = MediaSerializer(many=True, read_only=True)
  urls = UrlSerializer(many=True, read_only=True)

  class Meta:
    model = News
    fields = ('title', 'text', 'created_at', 'updated_at', 'media', 'urls',)
