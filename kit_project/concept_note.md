Introduction
============

The RapidSMS system for monitoring of WASH/CLTS is based on the health agents
that go out into the field, and collect data about the progress of CLTS in their
assigned locations. 

How it works
------------

The system will have the each reporter identified by his phone number in the system,
and associated with a group (NGO). Once the reporter goes out to the field, he will 
text in the data associated with that location which will then be recorded. These 
submissions will need to be approved by the local NGO manager through a web interface
before they are used in the report.

The local NGO is responsible for maintaining a log of their health reporters, their phone
numbers, and the locations that they will be reporting from. This should not be difficult
as the names and locations are already on file, only the sms numbers need to be added.

Problem
---------
Now, we need a way to identify the village that the worker is reporting from, because each
worker can report from a number of villages. For this the best way would be some sort
of a unique code for each village in the district. The worker texts in the village code and
the data for that village. The system then parses the location from the text message and 
registers the submission for that village. 

Currently the way kit is setup, it just parses the texts for indicators and associates the
location of the submission with the reporting location of the contact. What is needed is that
there is an attribute of the submission, which is its location. And this attribute needs to be
parsed from the message.

    Now one way i can see of doing that is maybe have one of the indicators/commands/keywords be the 
    name of the village where the health worker is reporting from. Then use the value of this
    indicator to populate the field for the village of the submission.

        
        maybe could try some sort of hackery because there is a location based on GPS that is 
        available in x-forms using ODK collect. Some maybe work around that and somehow allow
        the system to read the location from the text.


> OR

        Just pass the locations for now, and let the submission be associated with the location
        of the reporter, which will not be the village, but the NGO area or some level above
        the villages, or well, just dont have locations.
        Just let the data come in like that for now, and then use the data to work out where 
        the information came from. Maybe make it the job of the NGO manager to make sure that
        the spelling and stuff of the village is correct.

