from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from .models import Quiz, Question, Answer


class QuizListView(ListView):
    model = Quiz
    context_object_name = 'quizes'
    template_name = 'home.html'


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questions.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['quiz'] = self.quiz
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.quiz = get_object_or_404(Quiz, pk=self.kwargs.get('pk'))
        queryset = self.quiz.questions.order_by('question')
        return queryset


class AnswerListView(ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = 'question_answers.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['question'] = self.question
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.question = get_object_or_404(Question, quiz=self.kwargs.get('pk'), pk=self.kwargs.get('question_pk'))
        queryset = self.question.answers.order_by('question')
        return queryset


@login_required
def ChooseAnswerView(request, pk, question_pk, quiz_pk):
    answer = get_object_or_404(Answer, pk=quiz_pk)
    answer.choose = True
    answer.save()

    question = get_object_or_404(Question, pk=question_pk)
    question.status = 'Pending'
    question.save()

    return redirect('quiz_questions', pk=answer.question.quiz.pk,)
