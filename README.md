# Practical Data Science

Repo for www.practialdatascience.org

This respository uses the `sphinx` document builder together with `nbconvert` to (mostly) convert jupyter notebooks into a static HTML website. 

It reads source material from the `source` folder (mostly jupyter notebooks, with a few `.rst` restructured text files (like the home page in `index.rst`), and when you run sphinx uses those to build an HTML site in `docs/html`, which is then hosted by github pages. 

## To Build

- Clone repository
- Install all relevant sphinx packages for converting notebooks to HTML:
    `conda install -c conda-forge sphinx nbsphinx recommonmark`
    `pip install sphinx_markdown_tables`
- cd to the root directory of repository.
- Run `sphinx-build source docs/html`

The site will be built into `docs/html`. 

You can open the site locally by double-clicking on `docs/index.html` (which just redirects to `docs/html/index.html`).  

Copyright Nicholas Eubank, 2021
