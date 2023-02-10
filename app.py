# =========================================================================================
# /*
# APP NAME: Mission Name Marauder - NSA CodeName Generator
# APP URI: https://franklinmedia.com.au/apps/mission-name-marauder/
# AUTHOR: Z3r0_K3lv1n
# AUTHOR URI: https://franklinmedia.com.au/z3r0-k3lv1n
# DESCRIPTION: "Mission Name Marauder is an app that generates clever and catchy codenames for covert operations.
# With a total of 1376 adjectives and 7984 nouns to choose from, this app has the potential to generate a staggering
# 11,124,544 unique combinations. Simply run the app and it will generate a new codename for you, ensuring that no two
# codenames are the same. The app also maintains a list of used codenames, so you don't have to worry about
# accidentally using the same codename twice. Whether you're a member of the intelligence community or just a fan of
# secret agents and covert operations, Mission Name Marauder has you covered!"
# TAGS: Python, codenames, covert operations, secret missions, adjectives, nouns, unique combinations, random
# generation, used codenames, intelligence community, secret agents, word lists, naming tool, titler, generator,
# composer, marauder, classified documents, heist, swiper, caper creator
# VERSION: 1.1
# LICENSE: Franklin Media Australia Pty Ltd - Private Use Copyright License
# LICENSE URI: https://www.franklinmedia.com.au/licenses/
# COPYRIGHT LICENSE FOR PRIVATE USE ONLY
# This license allows for the use of the copyrighted material in perpetuity for private use only. The copyright holder,
# Franklin Media Australia Pty Ltd, reserves all rights for commercial use of the material.
# By accepting this license, the user agrees not to use the material for any commercial purposes, including but not
# limited to, selling or distributing the material in any form. The user also agrees not to modify or alter the
# material in any way.
# This license is non-transferable and any unauthorised use of the material will be considered a violation of
# copyright law.
# The copyright holder reserves the right to terminate this license at any time for any reason.
# This license is governed by the laws of Australia, and any disputes arising from this license shall be resolved in
# the courts of Australia.
# By accepting this license, the user acknowledges and agrees to the terms and conditions outlined above.
# */
# =========================================================================================

import os
import random
import english_adjectives
import english_nouns

adjectives = english_adjectives.english_adjectives
nouns = english_nouns.english_nouns
total_nouns = len(nouns)
total_adjectives = len(adjectives)
notice = f"The total number of adjectives in the adjectives list is: {total_adjectives}.\nThe total number of " \
         f"nouns in the nouns list is: {total_nouns}."
print(notice)


def read_used_codenames():
    """Reads the set of used codenames from a file and returns it"""
    if not os.path.exists('used_codenames.txt'):  # if the file does not exist
        return set()  # return an empty set
    with open('used_codenames.txt', 'r') as f:
        used_codenames = set(line.strip() for line in f)
    return used_codenames


def write_used_codenames(used_codenames):
    """Writes the set of used codenames to a file"""
    with open('used_codenames.txt', 'w') as f:
        for codename in used_codenames:
            f.write(codename + '\n')


def generate_codename():
    used_codenames = read_used_codenames()  # read the set of used codenames from the file
    codename = random.choice(adjectives) + " " + random.choice(nouns)
    while codename in used_codenames:  # while the generated codename has already been used
        codename = random.choice(adjectives) + " " + random.choice(nouns)  # generate a new codename
    used_codenames.add(codename)  # add the new codename to the set of used codenames
    write_used_codenames(used_codenames)  # write the updated set of used codenames to the file
    return codename


codename = generate_codename()
print(codename)
