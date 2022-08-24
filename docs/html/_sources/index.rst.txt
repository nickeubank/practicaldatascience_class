Hello!
======


*The course site for Duke MIDS Fall 2021 Practical Data Science (IDS 720) Course*

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
   Topic List <topic_list>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: Environment Setup

   Setup Python and miniconda <setup_python>
   Setup VS Code <setup_vscode>
   Setup Command Line <setup_augmented_commandline>
   Setup Jupyter <jupyter>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: Basic Tools

   Command Line, Basics <command_line_part1>
   Command Line, Advanced <command_line_part2>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: Python & Pandas
   
   Python / R Differences <python_v_r>
   Python: Vars v Objects <vars_v_objects>
   Numbers in Computers <ints_and_floats>
   Pandas 1: Series <pandas_series>
   Pandas 2: DataFrames <pandas_dataframes>
   Plotting, Basics <plotting_altair_part1>
   Plotting, Advanced <plotting_altair_part2>
   Pandas 3: Views <views_and_copies_in_pandas>
   Cleaning: Editing Values <cleaning_editingvalues>
   Parquet Format <parquet>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: DS Concepts

   Defensive Programming <defensive_programming>
   Workflow Management <workflow>
   Backwards Design <backwards_design>
   Getting Help Online <getting_help>
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
   
   Buying a Data Science Computer <buying_datascience_computer.ipynb>
   Not a MIDS Student? <not_a_mids_student>
   Cheat Sheets <cheatsheets>
