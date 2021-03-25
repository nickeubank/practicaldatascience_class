# Practical Data Science

Repo for www.practialdatascience.org

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
