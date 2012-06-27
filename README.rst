--------------------------------------
--------------------------------------
RapidSMS Madagascar - WASH monitoring
--------------------------------------
--------------------------------------


reports -> the survey with indicators

groups -> NGO's

the managers for each NGO are given online id's, wherein they
can access and edit the submissions belonging to their
NGO (group) only

The managers need to approve the messages as they come in

The central admin can generate a report once they see that all
the messages are approved.

The messages have the following format

Ex.   CLTS    101               600             AMBD            SAH        4 5 10 9 5 2 1
     KEYWORD REGION-NUM-CODE COMMUNE-NUM-CODE FOKONTANY-CODE VILLAGE-CODE INDICATOR VALUES 
     
The health-workers know the region and commune codes already, and now we need a way to codify the fokontany and villages.
One option would be to create numeric codes for all of these, but that would take time, be very hard to
train the health workers in, and also be prone to frequent errors that the NGO Manager would then need to fix. This
could in turn act as a deterrent for the manager, causing him to not want to go in and approve the messages. Hence, 
I recommend the use of symbolic codes for the villages and fokontany that are created from the names of the original
locations, and can be easily distributed with the training card, and are easier than numeric codes to teach the 
health workers. 
The batch of codes for Saint-Marie has been created.


Installation
============

The following is a step-by-step process for installing the development indicator
collection kit on an Ubuntu machine.

Virtual Environment
--------------------
If you're installing the collection kit on a machine with other python applications,
you'll likely want to create a "Virtual Environment" to install all dependencies.  This
keeps the copy of python in /usr clean, and also keeps you from having to run
sudo to install every dependency.  From a terminal, you'll run the following commands:

::

    sudo apt-get install python-virtualenv
    
    cd /path/to/your/virtual/environments/

    mkdir virtual_environments

    cd virtual_environments

    virtualenv --no-site-packages kit

    source kit/bin/activate

Downloading the source
----------------------
Second, you'll need the application source itself.  Unfortunately, for now, this
required a clone directly from github (rather than a download or pip install).  Check
this README on github for updates to the install process.  From a terminal, run:

::

    cd /path/to/your/projects/

    git clone git://github.com/daveycrockett/kit.git

    cd kit
    
    git submodule init
    
    git submodule update

Configuring the application
---------------------------
Once you've downloaded kit, you'll need to install kit's requirements:

    cd kit

    pip install -r requirements.pip

Run the usual database initialization steps:

    python manage.py syncdb

    python manage.py migrate

And now you should be ready to run the server:

    python manage.py runserver

Dashboard
=========
When you navigate to http://localhost:8000, you'll be walked through the process of
initializing the system to collect data.  This involves uploading locations (these
aren't GPS coordinates, but rather a tree of locations for aggregating information),
users (those reporting information), reports (SMS reports and XForms) and indicators 
(individual pieces of data to be collected). 
