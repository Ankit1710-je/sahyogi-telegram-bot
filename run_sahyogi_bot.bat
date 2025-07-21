@echo off
echo ===============================
echo  Sahyogi GitHub Auto-Push Bot
echo ===============================

REM Set your Git user info (optional if already set globally)
git config user.name "Ankit1710-je"
git config user.email "ankitje10@gmail.com"

REM Navigate to your Git repo folder
cd /d "D:\FINAL sahyogi_bot_final_cleaned\Github\sahyogi_bot_render_ready"

REM Stage all changes
git add .

REM Commit with a timestamp message
setlocal enabledelayedexpansion
for /f %%i in ('powershell -Command "Get-Date -Format \"yyyy-MM-dd HH:mm:ss\" "') do set timestamp=%%i
git commit -m "Auto update on !timestamp!"

REM Push to GitHub
git push origin master

echo.
echo ✅ All changes pushed to GitHub successfully!
pause
<PLACEHOLDER>