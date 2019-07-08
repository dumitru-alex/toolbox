@echo off 
@IF EXIST "%~dp0\backup_staged_files.py" (
  call "%~dp0\backup_staged_files.py"
) ELSE (
  echo "File `backup_staged_files.py` not found!"
)