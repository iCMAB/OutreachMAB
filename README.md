# OutreachMAB
Repository to store the codebase for the multi-armed bandit and context MAB application examples 

Ideas for context options:
 - Distance:
   - Decreases reward with distance to restaurant
   - Flat penalty based on distance or sqrt of distance
 - Time of Day:
   - Changes Restaurant reward distribution
   - Scales the entire reward dist, 0 reward if restaurant is closed
   - Normal dist centered around peak time
 - Interest?:
   - Rewards choosing a restaurant with the same type of food
   - Restaurants may have overlapping food tags
   - Last choice might be automatically not interested
   - Might be obtuse and hard to understand
 - Format?: 
   - Restaurant might be tagged with take-out/dine-in, etc.

Ideas for user code modification:
 - Smoke and mirrors
   - No actual code runs, just gets "graded" and the backend runs once they have satisfied requirements
   - Low educational potential
   - Low confusing potential
   - May work well with function matching
 - Functions Matching
   - Give the user complete functions that they need to place at the right place in the algorithms
   - Better educational potential
     - Allows users to gradually modify the code more and more
   - Higher confusion potential
     - Requires lots of comments for directions
