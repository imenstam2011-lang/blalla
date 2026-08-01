@echo off
cd /d "%~dp0"
REM Download the official Napse logo into public/napse-logo.png
"%~dp0\scripts\download_logo.py"
if exist public\napse-logo.png (
	echo Updated public\napse-logo.png
) else (
	echo Failed to update public\napse-logo.png
)
