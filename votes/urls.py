from django.urls import path
from .views import VoteCreateView, VoteTodayResultsView

urlpatterns = [
    path('votes/', VoteCreateView.as_view(), name='vote_create'),
    path('votes/today/', VoteTodayResultsView.as_view(), name='vote_today'),
]