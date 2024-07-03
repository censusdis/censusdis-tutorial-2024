## Objective

The objective of this tutorial is to give attendees immediately applicable skills they can use 
to work with U.S. Census data in Python. The presentation is filled with both practical knowledge 
and examples of best practices for both basic and advanced use cases.

U.S. Census data can be difficult to wrangle, even though vast quantities of it are available via a 
web API. Data sets and variables can be difficult to locate, and geographic hierarchies can be hard 
to manage. Something as simple as querying data for all the census tracts in a metropolitan area that 
crosses state lines can be non-trivial. The [censusdis](https://github.com/censusdis/censusdis) 
package that we will introduce in this tutorial manages this complexity behind a simple interface 
that makes it easy to bring the full set of data and maps the U.S. Census Bureau provides into a 
Python environment.

Armed with a working knowledge of [censusdis](https://github.com/censusdis/censusdis), attendees 
will be able to spend less time wrangling data and more time answering research questions.

## Format

This tutorial will consist of a series of lessons, each 15-20 minutes in length. Each lesson
will be followed by an interactive exercise where attendees will get a chance to write some
code using the concepts they just learned. Solutions will be provided.

After the lessons and exercises, attendees will break into groups of 2-4 and work on 
one of several available projects. These projects will require attendees to apply several
of the techniques they learned in the lessons and practiced in the exercises to answer
a research question using U.S. Census data. 

Finally, at the end of the session, attendees will have a chance to present the work
they did on their chosen project to the entire group.

For more details, see the outline below.

## Materials

Tutorial materials can be found in GitHub at https://github.com/censusdis/censusdis-tutorial-2024.

This tutorial is an extended, updated, and more interactive version of a 90 minute tutorial  presented at 
[PyData Seattle 23](https://www.youtube.com/watch?v=3vyC7ON0Tvg)

## Environment Setup

We will be using [Nebari](https://docs.google.com/document/d/11YWMZKW6Y4tXnMs3Jekc1S7BQWTR6THZazDaq3WoNxw/edit#heading=h.wtozhevy8waj), 
an open source data science platform designed to quickly set up and deploy 
an opinionated JupyterHub distribution, with built-in integrations and features for collaboration.

Setup is simple and takes 10-15 minutes. **We encourage participants to set up their environment in advance of the 
start of the tutorial.**

Details on how to set up Nebari for this tutorial can be found in the `README.md` file of the tutorial's 
GitHub repository, found at 
[https://github.com/censusdis/censusdis-tutorial-2024](https://github.com/censusdis/censusdis-tutorial-2024).
 
## Prerequisites

Attendees are expected to have a basic working knowledge of Python. Some experience with Pandas is 
helpful but not strictly required. No prior knowledge of the U.S. Census data model is required.