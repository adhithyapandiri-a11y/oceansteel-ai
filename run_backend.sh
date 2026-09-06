#!/bin/bash
echo "=========================================================="
echo " Starting OceanSteel AI - SIH 2026 (SIH262006)"
echo " Maritime-to-Inland Decision Support & TLC Optimizer"
echo "=========================================================="

cd backend
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
