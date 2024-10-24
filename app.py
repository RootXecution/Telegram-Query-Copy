import os
from datetime import datetime, timedelta
from random import randint, choice

# Define the start and end dates
start_date = datetime(2024, 8, 1)
end_date = datetime(2025, 1, 21)

# Generate a list of all possible dates between start_date and end_date
date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Randomly pick dates for commits
for _ in range(365):  # Adjust the number of total commits as needed
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

# Push all changes to the remote repository
os.system('git push -u origin main')
