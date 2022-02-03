from boards.models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class QuestionViewSet(viewsets.ViewSet):

    # list, create, retrieve, update, partial_update, destroy

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    # @action(methods=['get'], detail=False)
    # def newest(self, request):
        # newest = self.get_queryset().order_by('created').last()
        # serializer = self.get_serializer_class()(newest)
        # return Response(serializer.data)
