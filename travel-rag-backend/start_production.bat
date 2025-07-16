@echo off
echo =============================================
echo Travel RAG Backend - Production Launcher
echo =============================================

cd /d "d:\KR\Flutter\Projects\travel_rag_app\travel-rag-backend"

echo.
echo Current directory: %CD%
echo.

echo Checking backend files...
python check_backend.py

echo.
echo Starting PRODUCTION backend (NOT debug version)...
echo You should see: "Travel RAG Backend with Chat History Context"
echo If you see "TEST RESPONSE" messages, press Ctrl+C and check the file!
echo.

python travel_rag_backend.py

pause
