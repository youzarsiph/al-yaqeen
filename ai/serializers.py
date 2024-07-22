""" Serializers for blog.ai """

from rest_framework import serializers


# Create your serializers here.
class BaseSerializer(serializers.Serializer):
    """Base Serializer that provides model field for subclasses"""

    model = serializers.CharField(
        max_length=64,
        required=False,
        help_text="HuggingFace model name",
    )


class QuestionAnsweringSerializer(BaseSerializer):
    """Serializer for text QA"""

    question = serializers.CharField(
        max_length=1024,
        help_text="Question",
    )


class ChatSerializer(BaseSerializer):
    """Serializer for chat completion"""

    message = serializers.CharField(
        max_length=1024,
        help_text="Prompt",
    )


class TranslationSerializer(BaseSerializer):
    """Serializer for translation"""

    source = serializers.CharField(
        max_length=5,
        help_text="Source language for example en_XX",
    )
    target = serializers.CharField(
        max_length=5,
        help_text="Target language for example ar_XX",
    )
