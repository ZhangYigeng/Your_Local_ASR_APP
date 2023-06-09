# Your local automatic speech recognition (ASR) APP 🎙️

An out-of-the-box automatic speech recognition (ASR) application, designed to run on your local browser. 

This is 100% free 🆓 and your data remains completely secure - **No data is uploaded to the cloud!**

**This project is mainly developed by ChatGPT (GPT-4 Browsing version) under human supervision.**

## 🚀 Getting Started 

### Prerequisites 

The following dependencies are required:

- Python 3.9
- OpenAI whisper
- Streamlit

### Installation

#### MacOS as example (very similar steps for Windows and Linux):

1. **Anaconda**

   Install Anaconda by following the instructions on the [official website](https://www.anaconda.com/download).

2. **Conda Environment**

   Create and activate a new Conda environment:

   ```bash
   conda create -n myenv python=3.9
   conda activate myenv
   ```
3. **OpenAI Whisper**

   Install OpenAI Whisper using pip:

   ```bash
   pip install openai-whisper
   ```
4. **FFmpeg**

   Install FFmpeg on MacOS using Homebrew. 
   
   If you do not have Homebrew installed, you can do so from the [official website](https://brew.sh/).

   ```bash
   brew install ffmpeg
   ```
5. **Streamlit**

   Install Streamlit using pip:
   
   ```bash
   pip install streamlit
   ```
6. **Download the files or Git clone this repo on your machine**

   Only ```asr_app.py``` and ```run_app.command``` are necessary.

7. **Set the Correct Path in the .command file**

   Modify the ```run_app.command``` file (or modify it to any shell script) to set the correct path to your application. Grant it appropriate access privileges:
   ```bash
   chmod u+x run_app.command
   ```
   
8. **Run the App**

   Double-click the ```run_app.command``` file to start the application.

9. **Follow the webpage and upload your .mp3 audio file**

   And start transcribing!


That's it! Enjoy transcribing your audio files securely on your local browser! 🎉
