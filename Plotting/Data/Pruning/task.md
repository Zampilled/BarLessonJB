There is more info then needed right now in our dataframe and the clock is ticking. (Another slack message from our boss).  
We actually only need two columns from our dataframe for this graph the platform one and the genre one.  
We can drop the rest of columns using the following method
```python
df.drop()
```

In this method the first argument is what to drop (the name of the columns).
Then we need to say which axis to drop (for columns it's 1)
Then to do it inplace we need to set inplace to True:

```python
df.drop([<column_names>], axis=1, inplace=True)
```

The columns we need to drop are the following:

```text
["name", "year_of_release", "publisher", "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales", "critic_score", "critic_count", "user_score", "user_count", "developer", "rating"]
```

You can then print the head again to make sure you're only left with the platform and genre column

<div class="hint">


```python
    df.drop(["name", "year_of_release", "publisher", "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales",
             "critic_score", "critic_count", "user_score", "user_count", "developer", "rating"
             ], axis=1, inplace=True)

    print(df.head())
```
</div>

If you get it right it should look something like the following:

![prune](../../../common/resources/images/prune.png)
