import linecache
import json
import time

def linearSearch(lines, word):
#   with open(filename) as f:
   for line in lines:
      if line.rstrip() == word:
         return word

   return ""

def binarySearch(lines, word):
   return recBinSearch(lines, word, 0, len(lines))

# https://stackoverflow.com/a/850962
def bufcount(filename):
    f = open(filename)
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.read # loop optimization

    buf = read_f(buf_size)
    while buf:
        lines += buf.count('\n')
        buf = read_f(buf_size)

    return lines

def recBinSearch(lines, word, start, end):
   if start > end:
      return ""

   middle = (start + end) // 2
#   check = linecache.getline(file, middle)
   check = lines[middle]

   if word == check:
      return check

   if word > check:
      return recBinSearch(lines, word, start, middle)

   if word < check:
      return recBinSearch(lines, word, middle, start)

def treeSearch(word, tree):

#   tFile = open(dictFile)
#   tJson = tFile.read()
#   tree = {"word": False}
#   tree["next"] = json.loads(tJson)

   check = getNextLetter(word, tree)
   if check[-1] == "!":
      result = check[:len(check)-2]
      if result == word:
         return result
      else:
         return ""
   else:
      return ""

def getNextLetter(letters, dict):
   if letters[0] in dict["next"].keys() and len(letters) > 1:
      # print(letters[0])
      # sleep(1)
      next = getNextLetter(letters[1:], dict)

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
   dictFile = "words_alpha.txt"
   treeFile = "dict.json"
   outFile = "results.txt"

   tFile = open(treeFile)
   tJson = tFile.read()
   tree = {"word": False}
   tree["next"] = json.loads(tJson)

   with open(dictFile) as f:
      lines = f.readlines()
      for line in lines:
         word = line.rstrip()

         linearStart = time.perf_counter_ns()
         linearResult = linearSearch(lines, word)
         linearEnd = time.perf_counter_ns()

         binStart = time.perf_counter_ns()
         binResult = binarySearch(lines, word)
         binEnd = time.perf_counter_ns()

         treeStart = time.perf_counter_ns()
         treeResult = treeSearch(word, tree)
         treeEnd = time.perf_counter_ns()

         linearTime = linearEnd - linearStart
         binTime = binEnd - binStart
         treeTime = treeEnd - treeStart

         output = f"{word},{linearTime},{binTime},{treeTime}\n"
         print(output)
         with open(outFile, "a") as out:
            out.write(output)

if __name__ == "__main__":
   main()
