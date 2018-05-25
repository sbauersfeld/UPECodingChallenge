import requests
import json
import time

dead = True
letters = "eiastonrhlfcumdpgwybvkxjqz"
index = 0
first_guess = True
attempted_words = []
word_guess = ""
lives = 3
counter=0
while(1):
  if (dead):
    counter=0
    guesses=""
    word_guessed=""
    attempted_words=[]
    word_guess=""
    lives=3
    first_guess = True
    r1 = requests.get('http://upe.42069.fun/Ci4zv')
    index=0
    print(r1.status_code)
    j = r1.json()
    dead = False
  else:
    counter+=1
    '''json_string = '{"email": "sbauersfeld@g.ucla.edu"}'
    msg = json.loads(json_string)
    r = requests.post('http://upe.42069.fun/Ci4zv/reset', msg)
    print(r.json())'''
    while (letters[index] in guesses):
      index+=1
    next_guess = letters[index]
    length=0
    if (j['remaining_guesses'] == 1):
      attempted_words+=word_guessed
    item=""
    master_array=[]
    if ((not first_guess) and (j['remaining_guesses']  == 2 or j['remaining_guesses'] == 1) ):
      break_bool = False
      master_array=[]
      with open('newDict.txt') as f:
        f.seek(0, 0)
        lines = f.read().splitlines()
        group=[]
        cur_max=0
        count=0
        item=""
        lists = j['state'].split()
        L = len(lists)
        inc=0
        while(1):
          if(inc ==  L):
            break
          inc+=1
          if(break_bool):
            break
          cur_min=100
          item=""
          for item2 in lists:
            count=0
            for achar in item2:
              if (achar == '_'): 
                count+=1
            if (count!= 0 and count <= cur_min and item2 not in group):
              cur_min = count
              item=item2
            if (break_bool):
              break
          group.append(item)
          for word in lines:
            if (item == ""):
              break_bool = True
              break
            count = 0
            item.replace(",", "")
            length = len(item)
            if (len(word) == length and word not in attempted_words):
              k = 0
              while (k < length):
                if (item[k] != '_' and word[k] != item[k]):
                  break
                if (k == length - 1):
                  master_array.append(word)
                  break_bool=True
                k=k+1
    D = {}
    for word in master_array:
      a=0
      while (a < length):
        if (item[a] == '_' and word[a] not in guesses):
          if (word[a] not in D):
            D[word[a]] = 1
          else:
            D[word[a]]+=1
          break
        a=a+1
    max_count=0
    word_guessed = []
    for i in D.keys():
      if(D[i] > max_count and i in letters or (i in letters and D[i] == max_count and letters.find(i) < letters.find(next_guess))):
        max_count=D[i]
        next_guess=i
    for w in master_array:
      if (next_guess in w):
        word_guessed.append(w)
    guesses+=next_guess
    json_string = '{"guess": "' + next_guess + '"}'
    msg = json.loads(json_string)
    r = requests.post('http://upe.42069.fun/Ci4zv', msg)
    first_guess = False
    j = r.json()
    print(j)
    if (j['status'] == "DEAD" or j['status'] == "FREE"):
      dead = True
    time.sleep(1)
