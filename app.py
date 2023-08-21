import os
from datetime import datetime, timedelta
from random import randint, choice
import time

# Define the start and end dates
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 22)

# Generate a list of all possible dates between start_date and end_date
date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Total number of commits to make
total_commits = 100

# Loop to make commits
for _ in range(total_commits):
    # Pick a random date from the date_range
    random_date = choice(date_range)
    formatted_date = random_date.strftime('%Y-%m-%d %H:%M:%S')  # Format as YYYY-MM-DD HH:MM:SS
    
    # Make a random number of commits on the selected date
    for _ in range(randint(1, 10)):  # Random number of commits per day (1-10)
        with open('file.txt', 'a') as file:
            file.write(f"Commit on {formatted_date}\n")  # Write commit info to the file
        
        # Use the formatted date for the commit
        os.system('git add .')
        os.system(f'git commit --date="{formatted_date}" -m "Random commit"')

    # Wait for a random time before the next batch of commits (e.g., between 5 to 30 seconds)
    wait_time = randint(5, 30)
    print(f"Waiting for {wait_time} seconds before next commit...")
    time.sleep(wait_time)

# Push all changes to the remote repository after all commits are made
os.system('git push -u origin main')
