from datetime import datetime
import os
from random import randint
import time
import json
from venv import create

class Monkey:
   def __init__(self):
      self.alphabet = "abcdefghijklmnopqrstuvwxyz"
      self.count = 0

   def pressKey(self):
      num = randint(0, len(self.alphabet) - 1)
      self.count += 1
      return self.alphabet[num]

def getNextLetter(letters, dict):
   if letters[0] in dict["next"].keys():
      # print(letters[0])
      # sleep(1)
      next = getNextLetter(letters[1:], dict["next"][letters[0]])

      if next == "?":
         if dict["word"] == True:
            return "!"
         else:
            return "?"
      else:
         return letters[0] + next

   else:
      # print("DICT WORD: ", dict["word"])
      # print(dict)
      if dict["word"]:
         return "!"
      else:
         return "?"

def main():
   monkey = Monkey()
   i = 0
   letters = ""
   while i < 20:
      letters += monkey.pressKey()
      i += 1

   print(letters)

   # letter = Letter()

   f = open("dict_test.json")
   dict = json.loads(f.read())
   f.close()

   filename = "words1.txt"
   fileCtr = 1

   while True:
      if letters[0] in dict.keys():
         lett = dict[letters[0]]
         word = letters[0] + getNextLetter(letters[1:], lett)
         if word[-1] == "!" and len(word) > 4: # Only save valid words with at least 4 letters
            with open(filename, "a") as f:
               f.write(word[:len(word) - 1] + "," + str(monkey.count) + "," + str(datetime.now().time()) + "\n")
            monkey.count = 0

      letters = letters[1:] + monkey.pressKey()
      print(letters)

      if os.path.exists(filename):
         if os.path.getsize(filename) > 1000000:
            fileCtr += 1
            filename = "words" + str(fileCtr) + ".txt"

if __name__ == "__main__":
   main()
