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


# import schedule
# import time
# from django.core.management.base import BaseCommand
# import requests
# from random import randint
# from stats.models import PlayerStat

# class Command(BaseCommand):
#     help = 'Simulates player stats every 5 minutes'

#     def handle(self, *args, **kwargs):
#         print("Starting the simulation...")

#         # Directly add test data to check database
#         self.simulate_stats()

#         # Schedule task to run every 5 minutes
#         schedule.every(5).minutes.do(self.simulate_stats)

#         # Start the scheduling loop
#         while True:
#             print("Running pending tasks...")  # Add this print to see it's working
#             schedule.run_pending()  # This keeps checking every second for scheduled tasks
#             time.sleep(1)  # Wait for a second before checking again

#     def simulate_stats(self):
#         print("Making the API request now...")
#         try:
#             # Check if the schedule is working
#             print("Running scheduled task...")

#             response = requests.get('https://randomuser.me/api/')
#             print(f"API Status Code: {response.status_code}")  # Should print 200 for success
            
#             if response.status_code == 200:
#                 user_data = response.json()['results'][0]
#                 print(f"API Response: {user_data['login']['username']}")  # Print the username
#                 player_id = randint(1, 10000)

#                 # Check if player_id already exists in the database
#                 if PlayerStat.objects.filter(player_id=player_id).exists():
#                     print(f"Duplicate player_id {player_id} found. Skipping this record.")
#                     return  # Skip this iteration if a duplicate is found

#                 nickname = user_data['login']['username']
#                 profile_image = user_data['picture']['large']
#                 score = randint(1, 100)

#                 # Try to create a record in the database
#                 player_stat = PlayerStat.objects.create(player_id=player_id, nickname=nickname, profile_image=profile_image, score=score)
#                 print(f"Added new stat for {nickname} with score {score}")
#             else:
#                 print(f"API request failed with status: {response.status_code}")
#         except Exception as e:
#             print(f"Error in simulate_stats: {e}")

#         # Directly add a record to check if the database is working
#         print("Directly adding test record to database...")
#         test_player_id = 9999
#         if PlayerStat.objects.filter(player_id=test_player_id).exists():
#             print(f"Duplicate test player_id {test_player_id} found. Skipping this record.")
#         else:
#             test_stat = PlayerStat.objects.create(player_id=test_player_id, nickname="testuser", profile_image="https://testimage.url", score=50)
#             print(f"Direct test stat added: {test_stat.nickname} with score {test_stat.score}")


# import schedule
# import time
# from django.core.management.base import BaseCommand
# import requests
# from random import randint
# from stats.models import PlayerStat

# class Command(BaseCommand):
#     help = 'Simulates player stats every 5 minutes'

#     def handle(self, *args, **kwargs):
#         print("Starting the simulation...")

#         # Directly add test data to check database
#         self.simulate_stats()

#         # Schedule task to run every 5 minutes
#         schedule.every(5).minutes.do(self.simulate_stats)

#         # Start the scheduling loop
#         while True:
#             print("Running pending tasks...")  # Add this print to see it's working
#             schedule.run_pending()  # This keeps checking every second for scheduled tasks
#             time.sleep(1)  # Wait for a second before checking again

#     def simulate_stats(self):
#         print("Making the API request now...")
#         try:
#             # Check if the schedule is working
#             print("Running scheduled task...")

#             response = requests.get('https://randomuser.me/api/')
#             print(f"API Status Code: {response.status_code}")  # Should print 200 for success
            
#             if response.status_code == 200:
#                 user_data = response.json()['results'][0]
#                 print(f"API Response: {user_data['login']['username']}")  # Print the username
#                 player_id = randint(1, 10000)
#                 nickname = user_data['login']['username']
#                 profile_image = user_data['picture']['large']
#                 score = randint(1, 100)

#                 # Try to create a record in the database (test database insertion)
#                 player_stat = PlayerStat.objects.create(player_id=player_id, nickname=nickname, profile_image=profile_image, score=score)
#                 print(f"Added new stat for {nickname} with score {score}")
#             else:
#                 print(f"API request failed with status: {response.status_code}")
#         except Exception as e:
#             print(f"Error in simulate_stats: {e}")
            
#         # Directly add a record to check if the database is working
#         print("Directly adding test record to database...")
#         test_stat = PlayerStat.objects.create(player_id=9999, nickname="testuser", profile_image="https://testimage.url", score=50)
#         print(f"Direct test stat added: {test_stat.nickname} with score {test_stat.score}")


# import schedule
# import time
# from django.core.management.base import BaseCommand
# import requests
# from random import randint
# from stats.models import PlayerStat

# class Command(BaseCommand):
#     help = 'Simulates player stats every 5 minutes'

#     def handle(self, *args, **kwargs):
#         print("Starting the simulation...")

#         # Test without scheduling first (simple immediate task)
#         self.simulate_stats()  # Check if immediate task works

#         # Uncomment this section once immediate task works
#         # schedule.every(5).minutes.do(self.simulate_stats)

#         # Running pending tasks indefinitely
#         while True:
#             schedule.run_pending()  # Run scheduled tasks
#             time.sleep(1)  # Check every second if there's a task to run

#     def simulate_stats(self):
#         print("Making the API request now...")
#         try:
#             # Check if the schedule is working
#             print("Running scheduled task...")

#             response = requests.get('https://randomuser.me/api/')
#             print(f"API Status Code: {response.status_code}")  # Should print 200 for success
            
#             if response.status_code == 200:
#                 user_data = response.json()['results'][0]
#                 print(f"API Response: {user_data['login']['username']}")  # Print the username
#                 player_id = randint(1, 10000)
#                 nickname = user_data['login']['username']
#                 profile_image = user_data['picture']['large']
#                 score = randint(1, 100)

#                 # Try to create a record in the database (test database insertion)
#                 player_stat = PlayerStat.objects.create(player_id=player_id, nickname=nickname, profile_image=profile_image, score=score)
#                 print(f"Added new stat for {nickname} with score {score}")
#             else:
#                 print(f"API request failed with status: {response.status_code}")
#         except Exception as e:
#             print(f"Error in simulate_stats: {e}")
            
#         # Directly add a record to check if the database is working
#         print("Directly adding test record to database...")
#         test_stat = PlayerStat.objects.create(player_id=9999, nickname="testuser", profile_image="https://testimage.url", score=50)
#         print(f"Direct test stat added: {test_stat.nickname} with score {test_stat.score}")


# from django.core.management.base import BaseCommand
# import schedule
# import time
# import requests
# from random import randint
# from stats.models import PlayerStat

# class Command(BaseCommand):
#     help = 'Simulates player stats every 5 minutes'

#     def handle(self, *args, **kwargs):
#         print("Starting the simulation...")
#         schedule.every(5).minutes.do(self.simulate_stats)

#         # Run the first simulation immediately for testing
#         self.simulate_stats()

#         while True:
#             print("Running pending tasks...")
#             schedule.run_pending()
#             time.sleep(60)  # Sleep for 1 minute to avoid high CPU usage
#     # def handle(self, *args, **kwargs):
#     #     print("Starting the simulation...")
#     #     schedule.every(5).minutes.do(self.simulate_stats)
#     #     self.simulate_stats()  # Manually trigger a task immediately for testing
#     #     while True:
#     #         print("Checking for scheduled tasks...")
#     #         schedule.run_pending()
#     #         print("Waiting for the next scheduled task...")
#     #         time.sleep(60)  # Sleep for 60 seconds to avoid high CPU usage

#     # def handle(self, *args, **kwargs):
#     #     print("Starting the simulation...")
#     #     schedule.every(5).minutes.do(self.simulate_stats)
#     #     while True:
#     #         schedule.run_pending()
#     #         time.sleep(1)

#     def simulate_stats(self):
#         print("Making the API request now...")
#         response = requests.get('https://randomuser.me/api/')
#         print(f"API Status Code: {response.status_code}")  # Should print 200 for success
#         if response.status_code == 200:
#             user_data = response.json()['results'][0]
#             print(f"API Response: {user_data['login']['username']}")  # Print the username
#             player_id = randint(1, 10000)
#             nickname = user_data['login']['username']
#             profile_image = user_data['picture']['large']
#             score = randint(1, 100)
#             PlayerStat.objects.create(player_id=player_id, nickname=nickname, profile_image=profile_image, score=score)
#             print(f"Added new stat for {nickname} with score {score}")


# from django.core.management.base import BaseCommand
# import requests
# from random import randint
# from stats.models import PlayerStat

# class Command(BaseCommand):
#     help = 'Simulates player stats every 5 minutes'

#     def handle(self, *args, **kwargs):
#         self.simulate_stats()

#     def simulate_stats(self):
#         print("Making the API request now...")
#         response = requests.get('https://randomuser.me/api/')
#         print(f"API Status Code: {response.status_code}")  # Should print 200 for success
#         if response.status_code == 200:
#             user_data = response.json()['results'][0]
#             print(f"API Response: {user_data['login']['username']}")  # Print the username
#             player_id = randint(1, 10000)
#             nickname = user_data['login']['username']
#             profile_image = user_data['picture']['large']
#             score = randint(1, 100)
#             PlayerStat.objects.create(player_id=player_id, nickname=nickname, profile_image=profile_image, score=score)
#             print(f"Added new stat for {nickname} with score {score}")


# import schedule
# import time
# import requests
# from random import randint
# from django.core.management.base import BaseCommand
# from stats.models import PlayerStat

# class Command(BaseCommand):
#     help = 'Simulates player stats every 5 minutes'

#     def handle(self, *args, **kwargs):
#         print("Starting the simulation...")
#         schedule.every(5).minutes.do(self.simulate_stats)
        
#         while True:
#             print("Waiting for the next simulation...")
#             schedule.run_pending()
#             time.sleep(1)

#     def simulate_stats(self):
#         print("Making the API request now...")
#         response = requests.get('https://randomuser.me/api/')
        
#         print(f"API Status Code: {response.status_code}")  # Should print 200 for success
        
#         if response.status_code == 200:
#             try:
#                 user_data = response.json()['results'][0]
#                 print(f"API Response: {user_data['login']['username']}")  # Print the username
                
#                 player_id = randint(1, 10000)
#                 nickname = user_data['login']['username']
#                 profile_image = user_data['picture']['large']
#                 score = randint(1, 100)

#                 # Add the player stat to the database
#                 PlayerStat.objects.create(player_id=player_id, nickname=nickname, profile_image=profile_image, score=score)
#                 print(f"Added new stat for {nickname} with score {score}")
#             except Exception as e:
#                 print(f"Error parsing the response: {e}")
#         else:
#             print(f"Failed to fetch data from the API. Status Code: {response.status_code}")


# import schedule
# import time
# import requests
# from django.core.management.base import BaseCommand
# from stats.models import PlayerStat
# from random import randint

# class Command(BaseCommand):
#     help = 'Simulates player stats every 5 minutes'

#     def handle(self, *args, **kwargs):
#         schedule.every(5).minutes.do(self.simulate_stats)
#         while True:
#             schedule.run_pending()
#             time.sleep(1)

#     def simulate_stats(self):
#         response = requests.get('https://randomuser.me/api/')
#         user_data = response.json()['results'][0]
#         player_id = randint(1, 10000)
#         nickname = user_data['login']['username']
#         profile_image = user_data['picture']['large']
#         score = randint(1, 100)

#         PlayerStat.objects.create(player_id=player_id, nickname=nickname, profile_image=profile_image, score=score)
#         print(f"Added new stat for {nickname} with score {score}")
