import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pshgame.settings')  


django.setup()

import requests
from random import randint
from stats.models import PlayerStat

def simulate_stats():
    try:
       
        response = requests.get("https://randomuser.me/api/")
        if response.status_code == 200:
            user_data = response.json()["results"][0]
            player_id = randint(1, 10000)
            
      
            if PlayerStat.objects.filter(player_id=player_id).exists():
                print(f"Duplicate player_id {player_id}. Skipping.")
                return

        
            PlayerStat.objects.create(
                player_id=player_id,
                nickname=user_data["login"]["username"],
                profile_image=user_data["picture"]["large"],
                score=randint(1, 100),
            )
            print("New stat created!")
        else:
            print(f"API request failed with status {response.status_code}")
    except Exception as e:
        print(f"Error in simulate_stats: {e}")


simulate_stats()


