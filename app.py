import os
from datetime import datetime, timedelta
from random import randint

# Define the start and end dates
start_date = datetime(2024, 8, 1)
end_date = datetime(2025, 1, 21)

# Calculate the number of days between the start and end dates
delta = end_date - start_date

# Iterate over each day in the specified range
for i in range(delta.days + 1):
    current_date = start_date + timedelta(days=i)
    d = current_date.strftime('%Y-%m-%d') + ' days ago'

    # Create a random number of commits for each day
    for j in range(randint(1, 10)):
        with open('file.txt', 'a') as file:
            file.write(d + '\n')  # Write to file with a newline for clarity
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')
        
        # Push changes to the remote repository
        os.system('git push -u origin main')
