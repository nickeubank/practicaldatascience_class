# Modifying Subsets of Vectors

The subsetting logic from the previous reading isn't just for extracting subsets of vectors to analyze—it's also useful for modifying vectors. The idea is that instead of keeping elements that meet a logical condition or occur at a specific index, we can change them!

For example, let's consider the vector with the salaries of everyone in my company. Suppose we wanted to give a raise to one of our workers—the person earning $80,000—how would we correct that mistake without re-creating the full vector?

The answer is that we can fix it using indexing or a logical statement **on the left side of the assignment operator** to specify that we're only trying to assign new values to a subset of the entries in an array.

To illustrate, let's work through the example of trying to edit a single entry in a vector of salaries, increasing the salary of the fourth employee (who earns 80,000 dollars) to 90,000 dollars:
