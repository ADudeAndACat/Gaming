@echo off
rem Test runner batch file for Windows
echo Running Gaming package tests...
set PYTHONPATH=%PYTHONPATH%;%~dp0
python run_tests.py
