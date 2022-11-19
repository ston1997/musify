from django.template.defaulttags import url
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_swagger.views import get_swagger_view
from music.models import Track
from music.serializers import TrackListSerializer, TrackDetailSerializer

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]


class TrackAPIViewSet(ReadOnlyModelViewSet):
    queryset = Track.objects.order_by('title').prefetch_related("genres", "singer", "similar_tracks", "rating",
                                                                "album").all()

    def get_serializer_class(self):
        if self.action == "list":
            return TrackListSerializer
        return TrackDetailSerializer
