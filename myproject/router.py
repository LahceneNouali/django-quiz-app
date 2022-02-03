from boards.api.viewsets import QuestionViewSet, AnswerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionViewSet, basename='questions')
router.register('answers', AnswerViewSet)

# for url in router.urls:
#     print(url, '\n')