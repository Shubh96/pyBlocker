# pyBlocker
[pyBlocker](https://github.com/Shubh96/pyBlocker) is a simple python application, using which people can block the websites that they want. The major use of this application can be to set work hours and include those website in the block list which are distracting or time eating in nature and one wishes not to use those during the work hours. The application can be made to run in the background the steps for which have been described below.

## Dependencies
As a dependency, this application uses only the `datetime` and `time` modules in python, other than that, the built-in task scheduler in Windows OS has been used to set the application to run as a background process so it can begin at start-up and continue to run.

## Code insights
In order for this code to run, we need to use the `hosts` file which is stored in the location `C:\Windows\System32\drivers\etc` for windows users and in the location `\etc` for Linux and Mac users.

- In the initial few lines the code is self explanatory where we have made lists to store the websites to be blocked and some variables to store the website to redirect to which is necessarily the `localhost` or `127.0.0.1`.
- We define the variables `socialWebsiteStart` and `socialWebsiteEnd` as in the code, to mark the beginning and end hours for when the websites should be blocked and when not.
- As we want this code to run always so we start an infinite loop inside which we check for the condition whether the current time lies between the hours when the websites have to be blocked.

- If yes, then we open the hosts file using `with  open(hostsLocation, "r+") as  file` inside which we first check whether the websites to be blocked are already existent or not, if not then we write then to the hosts file using `write` method else we ignore.
- Now, if the current time is not between the blocking hours then we read the file line by line, and check if the websites to block are present in a particular line. If it is present then we don't write that line to the file else we write that line.

## Enhancements
As of now this code has been developed to be working only for one work hour, further enhancements will be made to enable the code to work in multiple work hours as per the requirement of the users. Further work would be done soon.