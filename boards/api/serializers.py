from rest_framework import serializers
from boards.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question', 'status', 'note', 'quiz')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('answer', 'choose', 'question')