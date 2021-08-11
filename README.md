# Chess analysis model

## Data Cleaning
### Steps for cleaning the data and getting it set up:
1. `cd` into the `data-cleaning` folder to begin the data cleaning
2. Run `players.py` to webscrape the players dataset into the `grandmasters` SQL table
3. Run `games-updated.py` to get the games dataset with FIDE_ID in the `games_id` SQL table
4. Run `merge.py` to combine the games database and the players database in the `merge` SQL table
5. Run `gm_age.py` to get the updated statistics for each database in the `games_new` SQL table
