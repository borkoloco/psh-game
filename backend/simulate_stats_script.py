import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pshgame.settings')  # Replace 'pshgame.settings' with your actual settings module

# Setup Django
django.setup()

import requests
from random import randint
from stats.models import PlayerStat

def simulate_stats():
    try:
        # Make API request to fetch player data
        response = requests.get("https://randomuser.me/api/")
        if response.status_code == 200:
            user_data = response.json()["results"][0]
            player_id = randint(1, 10000)
            
            # Check if player_id already exists in the database
            if PlayerStat.objects.filter(player_id=player_id).exists():
                print(f"Duplicate player_id {player_id}. Skipping.")
                return

            # Create a new record in the database
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

# Call the function to simulate stats
simulate_stats()


# # simulate_stats_script.py

# import requests
# from random import randint
# from stats.models import PlayerStat

# def simulate_stats():
#     try:
#         # Make API request to fetch player data
#         response = requests.get("https://randomuser.me/api/")
#         if response.status_code == 200:
#             user_data = response.json()["results"][0]
#             player_id = randint(1, 10000)
            
#             # Check if player_id already exists in the database
#             if PlayerStat.objects.filter(player_id=player_id).exists():
#                 print(f"Duplicate player_id {player_id}. Skipping.")
#                 return

#             # Create a new record in the database
#             PlayerStat.objects.create(
#                 player_id=player_id,
#                 nickname=user_data["login"]["username"],
#                 profile_image=user_data["picture"]["large"],
#                 score=randint(1, 100),
#             )
#             print("New stat created!")
#         else:
#             print(f"API request failed with status {response.status_code}")
#     except Exception as e:
#         print(f"Error in simulate_stats: {e}")

# # Call the function to simulate stats
# simulate_stats()
