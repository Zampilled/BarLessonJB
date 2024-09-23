Python is a truly horrible langauge which is why it's my favorite one.  
Most projects rely on a list of dependencies which is in the three digits or more.  
While there exists new python managers I believe in the tried and test mehod of putting them all in a text file.  
pip is the main package instillation tool for python and anything can be installed with the following command:

```bash
pip install <name>
```

Once you install the dependencies you need you can create the text file with a command like:

```bash
pip freeze -> requirements.txt
```

Also to install all dependencies from one of these text files the following command is used:  

```bash
pip install -r <file_name.txt>
```

Pycharm will automatically create a virtual environment in which all dependencies are encapsulated to a specific project.
