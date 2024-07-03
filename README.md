# censusdis-tutorial-2024

This repository contains notebooks to accompany the [SciPy 24](https://www.scipy2024.scipy.org/) tutorial 
[Working with U.S. Census Data in Python: Discovery, Analysis, and Visualization
](https://cfp.scipy.org/2024/talk/BTG9U3/). 

## When and Where

This tutorial will be held live on July 9th, 2024 from 1:30 to 5:30 pm in 
[Room 315](https://tacomaconventioncenter.org/floor-plan-capacities) of the 
[Tacoma Convention Center](https://www.google.com/maps/place/Greater+Tacoma+Convention+Center/@47.2485675,-122.4415581,17z/data=!3m2!4b1!5s0x5490557439af7381:0xf34f9f35c5114bb4!4m6!3m5!1s0x549055744d668161:0xe464395e6d5c8dd5!8m2!3d47.2485639!4d-122.4389778!16s%2Fm%2F04797gw?entry=ttu).
Tickets for this and other tutorials are available at [https://ti.to/scipy/scipy2024](https://ti.to/scipy/scipy2024).
We look forward to seeing you there.

## Environment Setup (Nebari)

Thanks to [Quantsight](https://quansight.com/), all participants have access to a web-based Nebari Jupyter notebook environment 
with everything they need for this tutorial pre-installed. 

**We strongly encourage attendees to set up their environment prior to attending.** 
Creating an account and setting up your own environment only takes about 10 minutes.
But if anything goes wrong it is easier to debug it before the tutorial starts than 
while it is going on.

To set up your environment, please follow the 
[Quantsight Nebari instructions](https://docs.google.com/document/d/11YWMZKW6Y4tXnMs3Jekc1S7BQWTR6THZazDaq3WoNxw/edit?pli=1#heading=h.iiycnjuxtvzz) 
with the following additional details:

- In step 0, the coupon code you should use is {FILL-IN-CODE}.

- In step 2, choose a medium instance.

- In step 3, we will be using Option 2. The repository URL to clone is https://github.com/censusdis/censusdis-tutorial-2024.git

- Once you have cloned the repository, click through in the Jupyter left-nav to 
  `/censusdis-tutorial-2024/Lessons/Lesson 0 Introduction.ipynb` and run all the cells.

- If you are asked to choose a kernel. Choose `us-census-data-tutorial`.

- We will start here when the tutorial begins. See you there!

## Environment Setup (Local)

If you prefer to set up the tutorial environment locally on your laptop, you can do so.
We assume you have a fresh local virtual environment running Python 3.9 or higher and 
`git`.

In your virtual env, install `censusdis`, the main package we will use in the tutorial.

```shell
pip install censusdis
```

Next, install jupyterlab so we can run the notebooks.

```shell
pip install jupyterlab
```

Now checkout the tutorial code using

```shell
git clone https://github.com/censusdis/censusdis-tutorial-2024.git
cd censusdis-tutorial-2024 
ls Lessons 
```

You should see the lesson notebooks as follows:

```
Lesson 0 Introduction.ipynb     Lesson 3 Variables.ipynb
Lesson 1 Basic Queries.ipynb    Lesson 4 Query Filters.ipynb
Lesson 2 Maps.ipynb             Lesson 5 Advanced Geography.ipynb
```

Now start Jupyter with

```shell
jupyter-lab &
```

This should start the server and open a browser pointing to it. The window will look
something like this:

![Jupyter lab running in a browser](./images/jupyter-local.png)

You are now ready to go. Bring your laptop to the tutorial and we will jump right in.
