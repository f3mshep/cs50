from nltk.tokenize import sent_tokenize
import pdb

def list_compare(list_a, list_b):
  """returns a list of all identical strings"""
  results = []
  string_hash = {}
  for substring in list_a:
    if not substring == '': 
      string_hash[substring] = True
  for substring in list_b:
    if string_hash[substring]:
      results.append(substring)
  return results

def lines(a, b):
  """Return lines in both a and b"""
  list_a = a.split("\n")
  list_b = b.split("\n")
  return list_compare(list_a, list_b)

def sentences(a, b):
  """Return sentences in both a and b"""
  list_a = sent_tokenize(a)
  list_b = sent_tokenize(b)
  return list_compare(list_a, list_b)

def substrings(a, b, n):
  """Return substrings of length n in both a and b"""
  list_a = splitter(a, n)
  list_b = splitter(b, n)
  return list_compare(list_a, list_b)

def splitter(string, length):
  results = []
  string = string.replace('\n','')
  for counter in range(len(string)):
    chunk = string[counter:counter + length]
    if len(chunk) == length:
      results.append(chunk)
  return results
