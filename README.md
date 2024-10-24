# SimplyPy

Creating a python library to ease the use of few redundant functons that I use everyday. 

Source: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

At first the testing myfuction via test_myfunction.py did not work due to pytest not being installed. 

```bash
pip install --upgrade pytest
```
Check installation worked or not. 
```bash
python -c "import sys; print(sys.version)"
python -c "import pytest; print(pytest.__version__)"
```
After installing pytest, the test_myfunction.py worked. 