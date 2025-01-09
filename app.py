import os
from datetime import datetime, timedelta
from random import randint, sample

# Define the start and end dates for the new range
start_date = datetime(2024, 10, 1)  # Start from October 1, 2024
end_date = datetime(2025, 1, 31)     # End on January 31, 2025

# Calculate the total number of days in the range
total_days = (end_date - start_date).days

# Generate a list of all possible dates between start_date and end_date
date_range = [start_date + timedelta(days=i) for i in range(total_days + 1)]

# Randomly select a number of unique dates to commit to (you can adjust this number)
num_commits = 100  # Total number of commits you want to make
random_dates = sample(date_range, min(num_commits, len(date_range)))  # Ensure unique dates

# Iterate over each randomly selected date
for random_date in random_dates:
    formatted_date = random_date.strftime('%Y-%m-%d %H:%M:%S')  # Format as YYYY-MM-DD HH:MM:SS
    
    # Make a random number of commits on the selected date
    for _ in range(randint(1, 10)):  # Random number of commits per date (1-10)
        with open('file.txt', 'a') as file:
            file.write(f"Commit on {formatted_date}\n")  # Write commit info to the file
        
        # Use the formatted date for the commit
        os.system('git add .')
        os.system(f'git commit --date="{formatted_date}" -m "Random commit on {formatted_date}"')

# Push all changes to the remote repository
os.system('git push -u origin main')
