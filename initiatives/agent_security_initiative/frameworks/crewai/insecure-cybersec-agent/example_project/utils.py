import os
import pickle


def run_system_command(command):
    os.system(command)  

def load_user_data(filepath):
    with open(filepath, "rb") as file:
        return pickle.load(file) 
