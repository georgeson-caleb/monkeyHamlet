import jsons

class Letter:
   def __init__(self):
      self.word = False
      self.next = dict()

def main():
   f = open("english-words/words_alpha.txt")
   words = f.readlines()
   f.close()
   dict = Letter()
   for word in words:
      print(word)
      curLett = dict
      ctr = 0
      length = len(word) - 1
      for lett in word:
         if lett not in curLett.next.keys():
            curLett.next.update({lett: Letter()})

         if ctr == length:
            curLett.next[lett].word = True

         curLett = curLett.next[lett]

         ctr += 1

   f = open("dict_test.json", "w")
   f.write(jsons.dumps(dict.next))
   f.close()


if __name__ == "__main__":
   main()
