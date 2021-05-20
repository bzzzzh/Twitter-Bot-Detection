# Twitter Bot Detection

Team member:
* Yuteng Zhang
* Bohan Zhang

## Data preparation

**Step 1:** Given the raw dataset `twitter_human_bots_dataset.csv`, crawl the user object into `result.json` file.

```bash
python3 data_prep.py
```

**Step 2:** Convert the `result.json` file into `step1.csv`, with adding the labels from `twitter_human_bots_dataset.csv`.

```bash
is_bot.py
```
Now we can finally dig into the `step1.csv` to do further analysis.

## Main section
The main code for the remaining data preparation and analysis are in the：
* `botdet.ipynb` for cycle 1
* `NewFeatures.ipynb` for cycle 2

## License
[MIT](https://choosealicense.com/licenses/mit/)
