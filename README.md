# `base_library`

A copy-and-pasteable base set of files, tests, and so on that allow quick setup of new libraries.

Contains:
- A top-level package with a `tests` folder.
- A `test_project` folder from which tests and the Django server are run.
- A base user factory (using `django.contrib.auth.get_user_model`) and a `RequestTestCase` derived from it.
- A makefile that handles tests, migrations and running a server.

There are a number of `TODO`s in this project that mark the holes that will most commonly need to be filled in.  Searching for the string `TODO` (not as a whole word) should find them all.
- `TODO_PACKAGE_NAME` - replace this string everywhere with the name of the top-level package of your library.
- `TODO_PROJECT_NAME` - replace this string everywhere with the name of the repository.
- `setup.py` has a `TODO` in the description field and a `TODO_DEV_STATUS` in the `classifier` field.  The latter needs to be one of the seven Trove development status options, which are listed at the bottom.
- `requirements.txt` may need updating to use latest versions of dependencies.
- `LICENSE` has a `TODO_CURRENT_YEAR` slot in the copyright line that will need to be filled in. The licence supplied is the 2-Clause BSD licence, which is currently the one we use for open-source projects at time of writing.  Change, remove or update it as necessary if that isn't right for the project you're building.

`.travis.yml` and `setup.py` contain some configuration and description that may need fine-tuning.  At time of writing, this project "supports" Python 2.7, 3.4 and 3.5 - update the Trove classifiers (in `setup.py`) and Travis environment config as necessary.

Once that is done, check whether you need any particular component and delete it if necessary.

After setup, make sure to do the following:
- This base library doesn't install Django for you, so in order to run it you'll need to manually install whichever version of Django you need.
- Activate the library on Travis (then make a push to the repository).
- Replace this readme with information about your project.


### Trove

These are the Trove development status options, for filling in the `TODO_DEV_STATUS` in `setup.py`.  Choose one:

```
Development Status :: 1 - Planning
Development Status :: 2 - Pre-Alpha
Development Status :: 3 - Alpha
Development Status :: 4 - Beta
Development Status :: 5 - Production/Stable
Development Status :: 6 - Mature
Development Status :: 7 - Inactive
```

The full list of Trove classifiers can be found at [pypi.python.org](https://pypi.python.org/pypi?:action=list_classifiers).