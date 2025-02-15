@echo off
color 0B
setlocal EnableDelayedExpansion

echo So...this is a project that basically is done by 2 random ass devs for fun.
echo This is also used for installing libraries for python.
echo You will need Python to use this.

echo Python Installing in 2 Seconds.

timeout /t 2 >nul

winget install python --disable-interactivity

echo Python install checked!

pip install pygame
REM pip install 

timeout /t 2 >nul

BouncingSped.py

echo All done installing!

pause 
