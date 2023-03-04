@echo off

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

if not exist input (
    echo Creating input directory...
    mkdir input
)

if not exist output (
    echo Creating output directory...
    mkdir output
)

echo Activating virtual environment...
call venv\Scripts\activate

python main.py