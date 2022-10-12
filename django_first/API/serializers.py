from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['data_posted'] = instance.data_posted.strftime('%d-%m-%Y %H:%M:%S')
        return representation