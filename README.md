# Twitter_Bot_Detection
- Bohan Zhang bz771
- Yuteng Zhang yz7436

To run the program:
```
$ python3 data_prep.py
```
This will generate a json file result.json containing all the user information.
Next, run:
```
$ python3 is_bot.py
```
This will match the label with the user id in the two dataset, and generate a csv file step1.csv.
