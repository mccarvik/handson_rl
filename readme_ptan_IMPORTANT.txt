A LOT of changes needed to the PTAN library to get it going

- need to copy and paste ignite module from github: https://github.com/Shmuma/ptan/blob/master/ptan/ignite.py
- need to edit a bunch of reset() functions to reset()[0] to remove the unnecessary info return
- need to add a "trunc" var to a bunch of step functions