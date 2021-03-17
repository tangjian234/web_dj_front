from django.urls import path

from . import views

#
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/detai/5/
    path('detail/<int:question_id>/', views.detail, name='detail-1'),
    # ex: /polls/5/results/
    path('result/<int:question_id>', views.results, name='results'),
    # ex: /polls/5/vote/
    path('vote/<int:question_id>', views.vote, name='vote'),

    path('detail_view/<int:pk>',
         views.QuestionDetailView.as_view(), name='detail_view'),
    path('list_view',
         views.QuestionListView.as_view(), name='list_view'),
    path('choice_list_view',
         views.ChoiceListView.as_view(), name='choice_list_view'),
    path('background',
         views.run_background_app, name='background_test'),

]
