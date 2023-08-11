# OutreachMAB

The Hungry Hungry Bandits (working title) application is designed to demonstrate Multi-Armed Bandits and Contextual
Multi-Armed Bandits.

## Instructions for usage

- Requires Python 3.10
- Install dependencies by running `pip install -r requirements.txt`
- Run the application by calling `python src/main.py`

### Modifying Configurations

Bandit Algorithm Parameters and Restaurant Configurations can be modified via the `config.json` file.
Config file is in the form of a json nested dictionary

- Number of Frames to simulate
    - Defaults to `100`
    - Value must be between `1` and `1024`
    - Less than 100 not recommended as MAB performance will suffer
- Number of Arms
    - Defaults to `5`
    - Value must be between `1` and `5`
    - Runs simulation using the first `n` arms specified in `config.json`
- Bandit Model
    - Select model to run from drop-down in application
    - Bandit parameters are passed as keyword arguments when the bandit model is instantiated
- Restaurants
    - Each restaurant's reward distribution follows a normal distribution with a mean and standard deviation set in the
      config file
    - Each restaurant's context settings are also set in the config file, contextual penalty calculations can be found
      below
- Contextual Modifiers
    - Change the rate of decay and scaling of the reward penalties given to restaurant samples during contextual
      simulations

### Context

Context penalties are only applied during contextual runs.

Distance penalty increases with a negative exponential decay approaching distance_penalty_ratio with the distance from
the restaurant. Locations are measured as a tuple of two floats (x, y) with each value ranging from 0 to 10.

Distance penalty increases with a negative exponential decay approaching time_penalty_ratio with the distance from the
time_peak value of the restaurant. Time is measured as a float with the value representing hours in the day ranging from
0 to 24

## Todo list

List of current ideas to implement. No order or priority is established.
Some ideas are not finalized yet.

### Additional features
- Allow in-app parameter modification
- Add comparison simulation
- Check if `ttk.Text` widget is better for paragraphs than `ttk.Label`
- Add restaurant distribution overlay to sampling charts

### Known Bugs

- No active bugs, add as discovered

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
