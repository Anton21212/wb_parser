from rest_framework import serializers


class CardSerializer(serializers.Serializer):
    articles_file = serializers.FileField(required=False)
    article = serializers.IntegerField(required=False)

    def validate(self, data):
        articles_file = data.get('articles_file', None)
        article = data.get('article', None)
        if articles_file and article:
            raise serializers.ValidationError('Должно быть указано только одно из полей')
        return data

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
