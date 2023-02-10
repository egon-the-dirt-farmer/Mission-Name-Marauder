# Technical Documentation for Mission Name Marauder - NSA Codename Generator
Mission Name Marauder is a NSA style codename generator that allows the user to generate clever and catchy codenames for covert operations. It offers a possible 11,124,544 unique combinations.


## Introduction
"Mission Name Marauder is an app that generates clever and catchy codenames for covert operations.
With a total of 1376 adjectives and 7984 nouns to choose from, this app has the potential to generate a staggering
11,124,544 unique combinations. Simply run the app and it will generate a new codename for you, ensuring that no two
codenames are the same. The app also maintains a list of used codenames, so you don't have to worry about
accidentally using the same codename twice. Whether you're a member of the intelligence community or just a fan of
secret agents and covert operations, Mission Name Marauder has you covered!"

## Requirements
In order to use MNM, you will need the following:

* Python 3.x installed on your system
* Required Python libraries: os, random
* Import the english_nouns and english_adjectives modules

## How it Works
Mission Name Marauder uses two python lists of English Nouns and Adjectives to generate unique two-word names in the style of an NSA mission name 
generator.
It uses the random python library to choose these randomly after reading the list of used codenames in the usedcodenames.txt file. 

## The app has the following main functions:
* read_used_codenames() - reads the list of codenames in used_codenames.txt.
* generate_codename() - generates a new codename by randomly selecting a word from each of the lists of English words and joining them together 
and assigning them to a variable.
* write_used_codenames() - each time a codename is generated it writes it to the list of used codenames.


## Technical Details
* The app uses the python random library to randomly choose index locations within the lists of words.
* The app uses the python os library to create a path for the used_codenames.txt file if it doesn't already exist.
* The app uses open function to write the name generated to the used_codenames.txt file

## License
Mission Name Marauder is privately licensed by Franklin Media Australia Pty Ltd for non-commercial use only. You may use the software for personal 
or internal business purposes, but you may not distribute, sell, or use it for any commercial purpose without the express written permission of 
Franklin Media Australia Pty Ltd. By using Mission name Marauder, you agree to be bound by the terms of the Franklin Media Australia Pty Ltd - 
Private Use Copyright License. 

Please note that this software is provided "as is" without warranty of any kind, express or implied. Franklin Media Australia Pty Ltd shall not be 
liable for any damages arising from the use of this software. If you have any questions or concerns about the license for New Swizard, please comment 
to the Franklin Media Australia programmers through their GitHub Repository.
