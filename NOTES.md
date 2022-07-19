# Lecture Notes

1. lets write a simple library to return how cute an animal is

2. we can call this function from a python shell:
```bash
python
```
```python
from determine import determine_cuteness
determine_cuteness("Maja")
determine_cuteness("otter")
determine_cuteness("giraffe")
```

3. what if we want to make this callable from other scripts in other
   locations??
    1. module
    2. setup.py
    3. __init__.py

4. we can now install and use it in other places
```bash
pip install determine-cuteness
python
```
```python
from determine_cuteness import determine_cuteness
determine_cuteness("Maja")
determine_cuteness("otter")
determine_cuteness("giraffe")
```

5. hmm maybe we should add tests.
```bash
pip install pytest
pytest determine-cuteness
```

6. or maybe make this callable directly in the command line...
   ... this is a lot of stuff... there has to be a better way.
   https://github.com/evamaxfield/cookiecutter-py-package

7. what is linting, formating, typing ???

8. lets push this to github so that others can contribute

9. can we automate testing??

10. lets publish this so others can install it??

11. docs??

---

1. linting, formating, and typing is a must
2. dependencies are important to track and manage
3. most stable repos have a contributing guide
    1. commit often, commit small

---

1. cdp-scrapers has a lot of bots
2. if we wanted to try out one of your current scrapers right now
   we would need to clone your fork, install it, install the dependencies,
   run the correct file??
3. most CI systems (the automated testing) have extra features that we can overload
   cdp-scrapers has bots!