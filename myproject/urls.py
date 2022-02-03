from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .router import router

from accounts import views as accounts_views
from boards import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^$', views.QuizListView.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    url(r'^quizes/(?P<pk>\d+)/$', login_required(views.QuestionListView.as_view()), name='quiz_questions'),
    url(r'^quizes/(?P<pk>\d+)/questions/(?P<question_pk>\d+)/$', login_required(views.AnswerListView.as_view()), name='question_answers'),
    url(r'^quizes/(?P<pk>\d+)/questions/(?P<question_pk>\d+)/answer/(?P<quiz_pk>\d+)/choose/$',
        views.ChooseAnswerView, name='choose'),

    # API base url
    url(r'^api/', include(router.urls), name='api'),
    # DRF auth token
    url(r'^auth-token/', obtain_auth_token),
    # ADMIN
    url(r'^admin/', admin.site.urls),
]
