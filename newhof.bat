@echo off
echo Remember to create a folder to store all my files!

set /p dir="Input the full directory where you want to store your HOF: "
copy "main.exe" "%dir%"
copy "read.exe" "%dir%"
cd "%dir%"

set /p hofName="Enter the HOF file name you want to create: "
type nul > %hofName%.hof
type nul > busstoplist.txt
mkdir 6words
mkdir 8words

set /p open="Do you want to start the HOF creator now? [Y/N]: "

if %open%==Y start "%dir%" main.exe