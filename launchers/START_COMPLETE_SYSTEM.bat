@echo off
title BRAHMA COMPLETE SYSTEM

echo =====================================
echo STARTING BRAHMA SCAN FULL
echo =====================================

start "" "C:\BRAHMA_SCAN_FULL\launchers\START_WATCHDOG.bat"

timeout /t 3 >nul

start "" "C:\BRAHMA_SCAN_FULL\launchers\START_BRAHMA_FULL.bat"

exit