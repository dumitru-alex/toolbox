@echo off 
@IF EXIST "%~dp0\zowe_plugins_uninstall.py" (
  call "%~dp0\zowe_plugins_uninstall.py"
) ELSE (
  echo "File `zowe_plugins_uninstall.py` not found!"
)