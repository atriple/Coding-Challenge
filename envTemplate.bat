rem This is used for quick Python Environment Activation.
rem This file is just template, the actual batch to my actual path will be ignored by git.

@echo off

set BACK_PATH=%CD%
echo %BACK_PATH%

rem go to directory to the list of python environment
cd ...

rem Just showing list of the available python env
dir /d

rem Input name of environment/dir that you choose
set /p UserInputPath=Choose the Environment: 
cd %UserInputPath%\Scripts
call activate

cd %BACK_PATH%
echo Activation Success!