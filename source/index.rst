

Welcome to Practical Data Science!
==================================

*The course site for Duke MIDS Fall 2020 Practical Data Science Course*

**If you are not a Duke Masters in Data Science student, please see** `this page <not_a_mids_student.ipynb>`_ **about how best to use this site!**

Data Science is an intrinsically applied field, and yet all too often students are taught the advanced math and statistics behind data science tools, but are left to fend for themselves when it comes to learning the tools we use to do data science on a day-to-day basis or how to manage actual projects. This course is designed to fill that gap.

This course will be divided into two parts:

- **Part 1: Data Wrangling**: In Part 1 of this course, students will develop hands-on experience manipulating real world data using a range of data science tools (including the command line, python, jupyter, git, and github). In addition, students will also learn best practices for managing workflows, collaborating with peers, and using defensive programming techniques. This portion of the course will take up about 3/4 of the semester. 
- **Part 2: Answering Questions**: This course adopts the view that Data Science is about **answering important questions using quantitative data**. In Part 2 of this course, students will learn to develop data science projects that achieve this goal via backwards design, and learn tips for managing projects from inception to presentation of results.

The first portion of the course will provide students with extensive hands-on experience manipulating real (often messy, error ridden, and poorly documented) data using the a range of bread-and-butter data science tools (like the command line, git, python (especially numpy and pandas), jupyter notebooks, and more). The goal of these exercises is to ensure students are comfortable working with data in most any form. In addition to being of intrinsic value, developing these skills will also ensure that in advanced statistics or machine learning courses, students can focus on understanding the concepts being taught rather than having to split their attention between concepts and the nuts and bolts of data manipulation required to complete assignments.

The first portion of the course will culminate in students completing the full data manipulation and analysis component of a data science project (the goal of the project will be provided). This will include everything from gathering data from third parties, cleaning and merging different data sources, and analyzing the resultant data. These projects will be completed in teams using Git and Github to give students experience managing github working flows. 

In the second portion of the class, we will take a step back from the nuts and bolts of data manipulation and talk about how to approach the central task of data science: answering questions about the world. In particular, we'll discuss how to use backwards design to plan data science projects, how to refine questions to ensure they are answerable, how to evaluate whether you've actually answered the question you set out to answer, and how to pick the **most appropriate** data science tool based on the question you seek to answer (this will be a bit of preview of material we will engage with even more in `Unifying Data Science <http://www.unifyingdatascience.org>`_). 

This portion of the course will culminate in students picking a topic, developing an *answerable* question, thinking about what (in very concerte terms) an answer to that question would look like, figuring out what tools they would employ to generate that answer, and developing a plan for finding the data they would need to actually execute their project. 

`The full syllabus for this course can be downloaded here <https://github.com/nickeubank/practicaldatascience/raw/master/syllabus/Syllabus_PracticalDataScience.pdf>`_. Please note that this syllabus is subject to change up until the first day of class.


Covid-19 Accommodations
------------------------

This class is organized around having two (synchronous) class sessions every week. To accommodate the fact that, as a result of Covid-19, students are distributed across a wide range of time zones, once enrollment is complete we will conduct a survey of students to establish both student availability and time zones.  We will then select one or, if necessary, two times for each class session. If we need to pick two times for each class session, each student will be assigned to one of those two times and will be required to attend their assigned time each week. If possible, we will attempt to have class sessions on Tuesdays and Thursdays.

**Synchronous attendance at both of your assigned class sessions each week is required unless you are unable to participate synchronously due to extenuating circumstances (such as an internet connection that will not support synchronous participation).** If you feel you may not be able to attend the synchronous classes for some reason, please speak with me immediately.

`The (tentative) Class Schedule can be found here <class_schedule.rst>`_

Questions or comments?
-----------------------

Please let me know! All source files (and underlying jupyter notebooks) for this site can be `found on github <https://github.com/nickeubank/practicaldatascience/>`_, and you can raise issues there by creating a new issue, or by emailing me at `nick@nickeubank.com <mailto:nick@nickeubank.com>`_. 

.. toctree:: 
   :maxdepth: 1
   :hidden:

   CLASS SCHEDULE <class_schedule>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: PYTHON & PANDAS

   Setting Up Python <setup_environment>
   Managing Packages <managing_python_packages>
   Python / R Differences <python_v_r>
   Python: Vars v Objects <vars_v_objects>
   Numbers in Computers <ints_and_floats>
   Pandas 1: Series <pandas_series>
   Pandas 2: DataFrames <pandas_dataframes>
   Plotting, Basics <plotting_part1>
   Plotting, Advanced <plotting_part2>
   Pandas 3: Views <views_and_copies_in_pandas>
   Cleaning: Editing Values <cleaning_editingvalues>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: OTHER TOOLS

   Command Line, Basics <command_line_part1>
   Command Line, Advanced  <command_line_part2>
   Jupyter <jupyter>
   Git and Github <git_and_github>
   Parquet Format <parquet>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: CLOUD
   
   What Is The Cloud? <cloud_what_is_it>
   AzureML <cloud_azureml>
   Set Up Dask on AzureML <cloud_dask>
   More on Azure Storage <cloud_azurestorage>

.. toctree:: 
   :maxdepth: 2
   :hidden:
   :caption: SKILLS

   Getting Help Online <getting_help>
   Defensive Programming <defensive_programming>
   Workflow Management <workflow>
   What is Big Data? <what_is_big_data>
   Working with Big Data <big_data_strategies>
   Understanding Performance <performance_understanding>
   Solving Performance Probs <performance_solutions>
   Parallel Computing <parallelism>
   Distributed Computing <distributed_computing>

.. toctree::
   :maxdepth: 2
   :hidden: 
   :caption: OTHER
   
   Not a MIDS Student? <not_a_mids_student>
   Cheat Sheets <cheatsheets>
