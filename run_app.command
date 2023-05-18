#!/bin/bash
source /YourPathToConda/anaconda3/etc/profile.d/conda.sh 
conda activate [your ASR conda environment]
cd /your/app/path
streamlit run asr_app.py
