from rest_framework.views import APIView
from rest_framework.response import Response
from stats.models import PlayerStat
from django.utils import timezone

class ReportView(APIView):
    def get(self, request):
        top_players = PlayerStat.objects.order_by('-score')[:10]
        last_updated = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "topPlayers": [{
                "player_id": player.player_id,
                "nickname": player.nickname,
                "score": player.score,
                "creation_date": player.creation_date,
            } for player in top_players],
            "lastUpdated": last_updated
        }
        return Response(data)

