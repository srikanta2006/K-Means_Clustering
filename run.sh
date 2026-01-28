#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  K-Means Clustering - Wholesale Customer Segmentation     ║"
echo "║  Quick Start                                               ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

pip install -r requirements.txt

echo ""
echo "🚀 Starting Streamlit app..."
echo "Opening at: http://localhost:8501"
echo ""

streamlit run streamlit_app.py
