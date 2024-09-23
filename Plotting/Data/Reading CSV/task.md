To make a graph of the data we need to get the data into the code thanks to the library pandas that has never been easier. To get the data in we can use a pandas dataframe which is basically a fancy table.
The following line in python reads a csv from the input directory and creates a dataframe with it:
```python
 
 pd.read_csv(<inputdir>)
 
```
   
It's common practice to call the dataframe df so we can set this to df by simply using the following line :
```python
 
 df = pd.read_csv(<inputdir>)
 
```
    
We can see if everything works right by getting the head of the dataframe (first 5 rows) an printing it with the following line:
```python
   
print(df.head())
 
```
    
Now it's your turn to do something. In the main file get
<div class="hint">



```python
 
df = pd.read_csv("./dataset.csv")
print(df.head())

```
</div>
    
If you get it right the output should look something like this
![sample](../../../common/resources/images/head.png)