from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Podcast
from .serializers import PodcastSerializer


class PodcastViewSet(ModelViewSet):
    serializer_class = PodcastSerializer
    queryset = Podcast.objects.all()
    permission_classes = [IsAuthenticated]
