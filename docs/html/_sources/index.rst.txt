Hello!
======


*The course site for Duke MIDS Fall 2022 Practical Data Science (IDS 720) Course*

**If you are not a Duke Masters in Data Science student, please see** `this page <not_a_mids_student.ipynb>`_ **about how best to use this site!**

Data Science is an intrinsically applied field, and yet all too often students are taught the advanced math and statistics behind data science tools, but are left to fend for themselves when it comes to learning the tools we use to do data science on a day-to-day basis or how to manage actual projects. This course is designed to fill that gap.

Practical Data Science is a flipped-classroom, exercise and project-focused course. It is designed to give students practical experience manipulating and analyzing manipulating real (often messy, error ridden, and poorly documented) data using the full range of bread-and-butter Python data science tools (like the command line, git, python (especially numpy and pandas), jupyter notebooks, and more). By the end of the course, students will be able to:

- Manipulate and analyze data in any format, including cleaning, merging, and summarizing all standard tabular formats and levels of cleanliness, as well as large datasets and GIS data,
- Identify and resolve data issues using defensive programming practices,
- Setup and manage a data science programming environment on their own computers, including installing Python, managing packages with pip and conda, setting PATH variables, and working with VS Code,
- Collaborate with colleagues effectively using git and github,
- Plan and execute a full data science project from planning data manipulations through analysis and presentation of findings.



Syllabus
--------

`The full syllabus for this course can be downloaded here <https://github.com/nickeubank/practicaldatascience/raw/master/syllabus/Syllabus_PracticalDataScience.pdf>`_. Please note that this syllabus is subject to change up until the first day of class.


Class Schedule 
--------------

`The (tentative) Class Schedule can be found here <class_schedule.rst>`_

Questions or comments?
-----------------------

Please let me know! All source files (and underlying jupyter notebooks) for this site can be `found on github <https://github.com/nickeubank/practicaldatascience/>`_, and you can raise issues there by creating a new issue, or by emailing me at `nick@nickeubank.com <mailto:nick@nickeubank.com>`_. 

.. toctree:: 
   :maxdepth: 1
   :hidden:

   Class Schedule <class_schedule>
   Autograder Guidelines <autograder_guidelines>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: Environment Setup

   Setup Python and miniconda <00_setup_env/setup_python>
   Setup VS Code <00_setup_env/setup_vscode>
   Setup Command Line <00_setup_env/setup_augmented_commandline>
   Setup Jupyter <00_setup_env/jupyter_in_vscode>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: Command Line

   Command Line, Basics <10_commandline/command_line_part1>
   Command Line, Advanced <10_commandline/command_line_part2>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: Programming Concepts
   
   Python / R Differences <20_programming_concepts/python_v_r>
   Python: Vars v Objects <20_programming_concepts/vars_v_objects>
   Numbers in Computers <20_programming_concepts/ints_and_floats>
   Debugging <20_programming_concepts/10_debugging_principles>
   Good Notebooks <20_programming_concepts/writing_good_jupyter_notebooks>
   Defensive Programming <20_programming_concepts/defensive_programming>
   Workflow Management <20_programming_concepts/workflow>
   Backwards Design <20_programming_concepts/backwards_design>
   Getting Help Online <20_programming_concepts/getting_help>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: numpy

   Why numpy <30_numpy/10_vectors/10_why_numpy>
   Vectors <30_numpy/10_vectors/20_intro_to_vectors>
   Views and Copies <30_numpy/15_advanced_numpy_concepts/10_views_and_copies>
   Matrices <30_numpy/20_matrices/20_matrices>
   ND Arrays <30_numpy/30_ndarrays/40_nd_arrays>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: pandas

   Welcome to Pandas <40_pandas_basics/00_intro_to_pandas>
   Pandas Series <40_pandas_basics/10_pandas_series>
   Pandas DataFrames <40_pandas_basics/30_pandas_dataframes>
   Views and Copies in Pandas <40_views_and_copies_in_pandas>
  
.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: DS Concepts

   What is Big Data? <what_is_big_data>
   Working with Big Data <big_data_strategies>
   Understanding Performance <performance_understanding>
   Solving Performance Probs <performance_solutions>
   Parallel Computing <parallelism>
   Distributed Computing <distributed_computing>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: Git and Github

   Git and Github <git_and_github>
   Reviewing Code on Github <pr_review>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: GIS

   What is GIS? <gis_what_is_gis>
   Installing Geopandas <gis_setup_geopandas>
   Geopandas <gis_geopandas>
   Merging Spatial Data <gis_spatial_joins>
   Spatial Data Formats <gis_data>
   Spatial Projections <gis_projections>
   Managing Projections in Geopandas <gis_crs_geopandas>
   Mapping with Geopandas <gis_mapping>

.. toctree::
   :maxdepth: 2
   :hidden: 
   :caption: Other
   
   Buying a Data Science Computer <buying_datascience_computer>
   chatGPT and You <llms>
   Considering a PhD? <PhD_Advice>
   Not a MIDS Student? <not_a_mids_student>
   Cheat Sheets <cheatsheets>
