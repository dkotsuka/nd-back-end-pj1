# LOG CREATOR

This is a simple PostgreSQL + Python log creator for a sample database.
The database is provide by Udacity in Back End Developer's course.

## Preparing

You may have installed the [Virtual Machine](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html).
To configure the Virtual Machine you can clone this [repository](https://github.com/udacity/fullstack-nanodegree-vm) and run `vagrant up` inside vagrant folder.
After all is ok, run `vagrant ssh` to log into Linux VM

## Running this project

First, you may unpack newsdata.zip and `psql -d news -f newsdata.sql` to install the database on VM.
Then, locate the folder where log_creator.py was clone and run `python log_creator.py` to view logs.
