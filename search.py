from random import randint
from dict import Letter
import json
from time import sleep

class Monkey:
   def __init__(self):
      self.alphabet = "abcdefghijklmnopqrstuvwxyz"

   def pressKey(self):
      num = randint(0, len(self.alphabet) - 1)
      return self.alphabet[num]

def getNextLetter(letters, dict):
   if letters[0] in dict["next"].keys():
      print(letters[0])
      sleep(1)
      return letters[0] + getNextLetter(letters[1:], dict["next"][letters[0]])
   elif "\n" in dict["next"].keys():
      return "!" 
   else:
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

   letter = Letter()

   f = open("dict.json")
   dict = json.loads(f.read())
   f.close()

   while True:
      if letters[0] in dict.keys():
         lett = dict[letters[0]]
         word = letters[0] + getNextLetter(letters[1:], lett)
         #if word[-1] == "!":
         print(word)

      letters = letters[1:] + monkey.pressKey()
      print(letters)

if __name__ == "__main__":
   main()
