Since we want to only display 4 of the consoles in our final graph we need to remove any row that doesn't include these consoles.  
Theere is a handy method for this in pandas called .isin() .  
If you create a list of values you want to keep then run the following line it will keep only the rows you want 
```python

  df=df[df[<column_of_interest>].isin(<list_of_wanted_values>)]
```
Now you try to keep only the following 4 consoles:

```text
["PS4", "XOne", "PC", "WiiU"]
```

<div class="hint">


```python
  consoles = ["PS4", "XOne", "PC", "WiiU"]
  df=df[df['platform'].isin(consoles)]

```
</div>

If you did it right you should be able to check your dataframe and check that only these 4 dataframes exist.