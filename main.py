import os
import openai
import pinecone
import time
import sys
import importlib.util
sys.path.insert(0, './scripts')
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from pydub import effects

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def main_menu():
    print("*************************************")
    print("*Welcome to the  Aetherius Main Menu*")
    print("*           Version  0.04           *")
    print("*************************************")
    print("*  Please give a star on github and *")
    print("* share with friends if you wish to *")
    print("*     see continued development!    *")
    print("*  It helps keep  me motivated lol  *")
    print("*************************************")
    print("* Type [Exit] after making a choice *")
    print("*     to return to this screen!     *")
    print("*************************************")
    # Get a list of all the files in the folder
    files = os.listdir('scripts')
    # Filter out only the .py files 
    scripts = [file for file in files if file.endswith('.py')]
    # Print the menu options
    for i, script in enumerate(scripts):
        # Replace underscores with spaces
        script_name = script[:-3].replace('_', ' ')
        print(f"{i+1}. {script_name}")
    # Get the user's choice
    choice = int(input("Enter your choice: "))
    # Make sure the choice is valid
    if 1 <= choice <= len(scripts):
        # Get the chosen script
        script = scripts[choice-1]
        # Remove the .py extension to get the module name
        module_name = script[:-3]
        # Import the module
        spec = importlib.util.spec_from_file_location(module_name, f"scripts/{script}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Call the function with the same name as the module
        function = getattr(module, module_name)
        function()
    else:
        print("Invalid choice")


if __name__ == '__main__':
#    key = input("Enter OpenAi API KEY:")
#   openai.api_key = key
    openai.api_key = open_file('api_keys/key_openai.txt')
    pinecone.init(api_key=open_file('api_keys/key_pinecone.txt'), environment=open_file('api_keys/key_pinecone_env.txt'))
    vdb = pinecone.Index("aetherius")
    if not os.path.exists('nexus/implicit_short_term_memory_nexus'):
        os.makedirs('nexus/implicit_short_term_memory_nexus')
    if not os.path.exists('nexus/explicit_short_term_memory_nexus'):
        os.makedirs('nexus/explicit_short_term_memory_nexus')
    if not os.path.exists('nexus/explicit_long_term_memory_nexus'):
        os.makedirs('nexus/explicit_long_term_memory_nexus')
    if not os.path.exists('nexus/implicit_long_term_memory_nexus'):
        os.makedirs('nexus/implicit_long_term_memory_nexus')
    if not os.path.exists('nexus/episodic_memory_nexus'):
        os.makedirs('nexus/episodic_memory_nexus')
    if not os.path.exists('nexus/flashbulb_memory_nexus'):
        os.makedirs('nexus/flashbulb_memory_nexus')
    if not os.path.exists('nexus/heuristics_nexus'):
        os.makedirs('nexus/heuristics_nexus')
    if not os.path.exists('nexus/cadence_nexus'):
        os.makedirs('nexus/cadence_nexus')
    if not os.path.exists('logs/complete_chat_logs'):
        os.makedirs('logs/complete_chat_logs')
    if not os.path.exists('logs/final_response_logs'):
        os.makedirs('logs/final_response_logs')
    if not os.path.exists('logs/inner_monologue_logs'):
        os.makedirs('logs/inner_monologue_logs')
    if not os.path.exists('logs/intuition_logs'):
        os.makedirs('logs/intuition_logs')
    while True:
        main_menu()
        continue
