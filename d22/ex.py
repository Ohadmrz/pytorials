import string


class AlphabetIterator:

    class InvalidLetter(Exception):
        pass

    def __init__(self, char: str):
        if char.isalpha() and len(char) == 1:
            self._char = char
            self._abc = string.ascii_lowercase \
                if self._char.islower() \
                else string.ascii_uppercase
        else:
            raise self.InvalidLetter()

    def __iter__(self):
        self._idx = self._abc.index(self._char)
        return self

    def __next__(self):
        if self._idx < len(self._abc):
            ret_val = self._abc[self._idx]
            self._idx += 1
            return ret_val
        else:
            raise StopIteration()


if __name__ == '__main__':
    while True:
        l = input("Insert letter: ")
        try:
            ai = AlphabetIterator(l)
            # print(ai)
            # for letter in ai:
            #     print(letter, end=" ")
            print(list(ai))
            # new_list = []
            # for letter in ai:
            #     new_list.append(letter)
            # print(new_list)
            break
        except AlphabetIterator.InvalidLetter:
            print("Not a letter, try again!")
