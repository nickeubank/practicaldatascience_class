# Practical Data Science

Repo for www.practialdatascience.org

This respository uses the `sphinx` document builder together with `nbconvert` to (mostly) convert jupyter notebooks into a static HTML website. 

It reads source material from the `source` folder (mostly jupyter notebooks, with a few `.rst` restructured text files (like the home page in `index.rst`), and when you run sphinx uses those to build an HTML site in `docs/html`, which is then hosted by github pages. 

Hello world!

## To Build

- Clone repository
- Install all relevant sphinx packages for converting notebooks to HTML:
    `conda install -c conda-forge sphinx nbsphinx recommonmark`
    `pip install sphinx_markdown_tables`
- cd to the root directory of repository.
- Run `sphinx-build source docs/html`

The site will be built into `docs/html`. 

You can also install `sphinx-autobuild` (`pip install sphinx-autobuild`), and from the root directory run `python3 -m sphinx_autobuild source docs/html`. This will create a process that watched the `source` folder, and any time it see changes, re-build the repo. If you're doing iterative development, it can be helpful to leave this running to auto-build after ever change so you can look at how your changes are working in your local browser. 

You can open the site locally by double-clicking on `docs/index.html` (which just redirects to `docs/html/index.html`).  

Copyright Nicholas Eubank, 2021
