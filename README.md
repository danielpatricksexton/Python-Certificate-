
## Code Challenges for Python01

## 1. Palindrome - easy

### Write a function that checks if a given word is a palindrome

#### solution:


```python
def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome("hannah"))

```

* is_palindrome takes an argument and checks to see if the argument is equal to the argument reversed from the last character.

* We check "hannah" and return True

## 2. Merge Names - Easy

### When passed two arrays of names, it will return an array containing the names that appear in either or both arrays. The returned array should have no duplicates.

#### solution:


```python

def unique_names(names1, names2):
    return list(set(names1 + names2))


names1 = ["Jim", "Bob", "John", "Bill"]
names2 = ["Pat", "Mike", "Bob", "Bob", "Pat"]


print(unique_names(names1, names2))

```

* set() will remove iterable items from our list and covert to a dictionary of unique items

* with list() we convert the unique items from a dictionary back to a list

## 3. Ice Cream Machine - medium

### Implement the IceCreamMachine's scoops so that it returns all combinations of one ingredient and one topping.

#### solution:


```python

class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings


    def scoops(self):
        list = []
        for i in self.ingredients:
            for t in self.toppings:
                list.append([i, t])
        return list


machine = IceCreamMachine(['vanilla', 'chocolate'], ['chocolate sauce'])
print(machine.scoops())

```

* We start with a local variable blank list in our scoops() method.

* Using a for loop we iterate through our ingredients (i)

* We use a nested for loop to append our toppings (t) to each ingredient (i) and return our list

## 4. File Owners - medium

### Implement a group_by_owners function that accepts a dictionary containing the file owner name for each file name.

### Return a dictionary containing a list of file names for each owner name, in any order.

#### solution:


```python

def group_by_owners(files):
    new_dict = {}
    for pair in files.items():
        if pair[1] not in new_dict.keys():
            new_dict[pair[1]] = []

        new_dict[pair[1]].append(pair[0])

    return new_dict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))

```

* We start with a local variable new_dict, an empty dictionary

* Using for loop we iterate through the dictionary keys and values

* as we loop through our keys and values we check to see which value our key has been asigned to

* We switch our keys and values by appending our key pairs to its asigned value

## 5. Songs - hard

### Implement a function is_repeating_playlist that returns true if a playlist is reapeating or false if it is not.

#### solution:


```python

class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        songs = set()
        next_song = self
        while next_song:
            if next_song.name in songs:
                return True
            else:
                songs.add(next_song.name)
                next_song = next_song.next or None

        return False


first = Song('Hello')
second = Song('Eye of the tiger')
third = Song('Third Eye')

first.next_song(second);
second.next_song(third);
third.next_song(first)

print(first.is_repeating_playlist())
#returns True

```

* Starting with a while we return True as long as the playlist is repeating

* if our local variable of self.name (song name) is in songs (our set) we return True

* But if our set does not repeat we use an add function to add an unplayed song go to the next song
"# pythoncert" 
"# pythoncert" 
"# pythoncert" 
"# pythoncert" 
