# LOG CREATOR

### Udacity ND Back End Developer

-----------------------------

This code analyzes a database with more than one and a half million logs of a news articles website, and answer some questions about it, like:

1. What are the three most popular articles of all time?
2. Who are the authors of most popular articles of all time?
3. On what days more than 1% of requests resulted in errors?

This is a simple PostgreSQL + Python log creator for a sample database provide by Udacity.

## Preparing

* You may have installed the [Virtual Machine](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html).
* To configure the Virtual Machine you can clone this [repository](https://github.com/udacity/fullstack-nanodegree-vm) and run `vagrant up` inside vagrant folder.
* After all is ok, run `vagrant ssh` to log into Linux VM

## Running this project

* First, you may unpack newsdata.zip and `psql -d news -f newsdata.sql` to install the database on VM.
* Then, locate the folder where log_creator.py was clone and run `python log_creator.py` to view logs.
