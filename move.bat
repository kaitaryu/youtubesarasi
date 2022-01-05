@echo off
cd /d %~dp0
call .venv/Scripts/activate
python main.py 1> log.txt 2> error.txt
deactivate
