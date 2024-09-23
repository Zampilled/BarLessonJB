Our graph is not perfect. It's a bit ugly but we can fix that with some quick steps.  
First by applying the seaborn theme with the following line:
```python
  
    sns.set_theme()
   
```
This will automatically make it look bette but the legend is stuck in the graph which makes it look ugly a quick fix to this is by first setting our plot to an ax.
This means we can alter details about it: 

```python
  
ax = sns.countplot(x='platform', hue='genre', data=df)
  
```

Then we can bring the legend with the following lines which just attach the box to the side of the graph and readjusts the margins:

```python

sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()

```

Try it yourself and adjust to your taste. I suggest you check out the [seaborn styling section](https://seaborn.pydata.org/tutorial/aesthetics.html) and find a style you like !