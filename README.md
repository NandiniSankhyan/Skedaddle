# Skedaddle (Conversational Interfaces)

## App Description
It is a text-based intelligent chatbot which will help international people in completing the necessary formalities before and after they enter Germany. For now, we are restricting it to Bayreuth. 

## Key Features
- Conversational User Interface: To ensure a touch of personalization by engaging users with one-on-one conversations, maintaining a natural-communication tone, and by being good at interactive communication to ensure users feel like they're talking to a reliable, smart source.
- User should be able to select the items on checklist and get a text-based chatbot response and to be able to ask related queries and get responses in a conversation manner.
- Detailed information on topics like: Blocked account, Travel and Public Health Insurance, City registration etc.

## Install Rasa

The installation might take several minutes, since rasa depends on libraries, such as tensorflow.

For the project we nee python3.7 virtual environment available to install Rasa:

1. Create a new environemnt: `python3.7 -m venv env `
2. Activate the environment: `source env/bin/activate `
3. Upgrade setuptools : `pip3 install --upgrade setuptools`
4. Upgrade pip : `pip3 install --upgrade pip`
5. Install Rasa: `pip install rasa=3.0.0`


You are all done with installing Rasa. See how to use Rasa from the command line interface on: https://rasa.com/docs/rasa/command-line-interface

Rasa depends on numpy 1.19.5. In case you are getting an error, re-install numpy `pip install numpy==1.19.5`

### There are newer Rasa versions available
We will use Rasa version 3.0.0 to run the project.

### Run Rasa

1. Change directory to rasa `cd rasa`
2. Run `rasa run actions`
3. Open a second terminal, change directory to rasa (as in step 1), and run:
   1. `rasa shell` to try out the conversation in the shell
   2. `rasa run --enable-api --cors "*"` to run the Rasa API

Note: Our Rasa model will not work without the Rasa Action Server running since we use custom Actions.
# skedaddle
