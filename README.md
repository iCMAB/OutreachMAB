# OutreachMAB

Repository to store the codebase for the multi-armed bandit and context MAB application examples

## Instructions for usage

- Requires Python 3.10
- Install dependencies by running `pip install -r requirements.txt`
- Run the application by calling `python src/main.py`

### Modifying Configurations

Configurations can be modified via the `config.json` file. These settings will act as defaults, and the below values
can be overridden in the application itself:

- Number of Frames to simulate
    - Defaults to `100`
    - Value must be between `1` and `1024`
    - Less than 100 not recommended as MAB performance will suffer
- Number of Arms
    - Defaults to `5`
    - Value must be between `1` and `5`
    - Runs simulation using the first `n` arms specified in `config.json`
- Bandit Model
    - Select from drop-down
    - Bandit parameters must be specified in `config.json`

## Todo list

List of current ideas to implement. No order or priority is established.
Some ideas are not finalized yet.

### Additional features
- Change GUI counting to be 1-based instead of 0-based
- Add image scaling
- Allow in-app parameter modification
- Add contextual bandit simulation
- Add comparison simulation
- Check if `ttk.Text` widget is better for paragraphs than `ttk.Label`
- Add restaurant distribution overlay to sampling charts

### Known Bugs

- Header text not centered

### Ideas for context options:

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

### Ideas for user code modification:
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

### Ideas for model comparison:
 - Explicit run as comparison simulation
   - Compare long-term reward/regret averages
   - Should be able to compare contextual and simple bandits
   - Much more work, both for coding and UI development
 - Previous saved run comparison
   - Requires more user work
   - Requires static random seeding
   - Much easier to implement
