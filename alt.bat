@echo off

TITLE Select Steam account

taskkill.exe /F /IM steam.exe

set username="YOURALTUSERNAMEHERE"

reg add "HKCU\Software\Valve\Steam" /v AutoLoginUser /t REG_SZ /d %username% /f
reg add "HKCU\Software\Valve\Steam" /v RememberPassword /t REG_DWORD /d 1 /f
start steam://open/main

exit