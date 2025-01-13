import schedule
import time
from django.core.management.base import BaseCommand
import requests
from random import randint
from stats.models import PlayerStat

class Command(BaseCommand):
    help = 'Simulates player stats every 5 minutes'

    def handle(self, *args, **kwargs):
        print("Starting the simulation...")

        # Simulate stats immediately on startup
        self.simulate_stats()

        # Schedule task to run every 5 minutes
        schedule.every(5).minutes.do(self.simulate_stats)

        # Start the scheduling loop
        while True:
            print("Running pending tasks...")  # Add this print to see it's working
            schedule.run_pending()  # This keeps checking every second for scheduled tasks
            time.sleep(1)  # Wait for a second before checking again

    def simulate_stats(self):
        print("Making the API request now...")
        try:
            # Fetch data from the API
            response = requests.get('https://randomuser.me/api/')
            print(f"API Status Code: {response.status_code}")  # Should print 200 for success
            
            if response.status_code == 200:
                user_data = response.json()['results'][0]
                print(f"API Response: {user_data['login']['username']}")  # Print the username
                player_id = randint(1, 10000)

                # Check if player_id already exists in the database
                if PlayerStat.objects.filter(player_id=player_id).exists():
                    print(f"Duplicate player_id {player_id} found. Skipping this record.")
                    return  # Skip this iteration if a duplicate is found

                nickname = user_data['login']['username']
                profile_image = user_data['picture']['large']
                score = randint(1, 100)

                # Create a new record in the database
                player_stat = PlayerStat.objects.create(player_id=player_id, nickname=nickname, profile_image=profile_image, score=score)
                print(f"Added new stat for {nickname} with score {score}")
            else:
                print(f"API request failed with status: {response.status_code}")
        except Exception as e:
            print(f"Error in simulate_stats: {e}")


