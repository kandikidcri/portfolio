cls
@echo on
echo
echo
@echo off
cls
echo Exiting..
rem Clear
cls
rem Dont show the output of this to the user.
@echo off
set /p MsgPrompt=Hey Sexy, press any key to launch the python simple web server on your local machine at http://127.0.0.1:5000/...
cls
rem Show the output of this to the user.
@echo on
cls
echo
echo
@echo off
cls
rem Init simple python dev web server.
py server.py
cls
@echo on
echo Exiting.
echo Exiting..
echo Exiting...
cls
echo 0