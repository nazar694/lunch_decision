from rest_framework import generics, permissions
from .models import Vote
from .serializers import VoteSerializer
from django.utils import timezone
from rest_framework.response import Response
from django.db.models import Count


class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class VoteTodayResultsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = timezone.now().weekday()
        return (
            Vote.objects.filter(day=today)
            .values('restaurant__name')
            .annotate(votes=Count('id'))
            .order_by('-votes')
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
