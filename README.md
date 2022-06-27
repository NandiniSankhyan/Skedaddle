# Skedaddle (Conversational Interfaces)

## App Description
It is a text-based intelligent chatbot which will help international people in completing the necessary formalities before and after they enter Germany. For now, we are restricting it to Bayreuth. 

## Key Features
- Conversational User Interface: To ensure a touch of personalization by engaging users with one-on-one conversations, maintaining a natural-communication tone, and by being good at interactive communication to ensure users feel like they're talking to a reliable, smart source.
- User should be able to select the items on checklist and get a text-based chatbot response and to be able to ask related queries and get responses in a conversation manner.
- Detailed information on topics like: Blocked account, Travel and Public Health Insurance, City registration etc.

## Install Rasa & spaCy

The installation might take several minutes, since rasa depends on libraries, such as tensorflow.

For the tutorial we need a conda environment with `pip` available to install Rasa:

1. Create a new environemnt: `conda create -n week4 python=3.8`
2. Activate the environment: `source activate week4`
3. Install pip: `conda install pip`
4. Install Rasa: `pip3 install rasa==2.5.0 --use-deprecated=legacy-resolver`
5. Install spaCy: `conda install -c conda-forge spacy`
5.1 Install English embeddings, e.g.: `python -m spacy download en_core_web_md`

You are all done with installing Rasa & spaCy. See how to use Rasa from the command line interface on: https://rasa.com/docs/rasa/command-line-interface

Rasa depends on numpy 1.18.5. In case you are getting an error, re-install numpy `pip install numpy==1.18.5`

### There are newer Rasa versions available
We will use Rasa version 2.5.0 to run the project properly yet there is already version 3.0 released.

### Run Rasa

1. Change directory to rasa `cd rasa`
2. Run `rasa run actions`
3. Open a second terminal, change directory to rasa (as in step 1), and run:
   1. `rasa shell` to try out the conversation in the shell
   2. `rasa run --enable-api --cors "*"` to run the Rasa API

Note: Our Rasa model will not work without the Rasa Action Server running since we use custom Actions.
# skedaddle
