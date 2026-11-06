#Author: Alexander Al Dahhan
#Date: November 6th, 2026
#Collaborators: https://mimo.org/glossary/python/list-count
#Assignment: Hash table


import csv
import time


class movieNode:
    def __init__(self, line):
        self.movie_name = line[0]
        self.genre = line[1]
        self.release_date = line[2]
        self.director = line[3]
        self.revenue = line[4]
        self.rating = line[5]
        self.min_duration = line[6]
        self.production_company = line[7]
        self.quote = line[8]


def hashFunction1(stringData):
    #weak hash function that will 100% cause collisions
    if stringData == "":
        return 0
    return ord(stringData[0])/13


def hashFunction2(stringData):
    #stronger hash function that should cause less collissions
    index = 0
    for letter in stringData:
        index = ord(letter)/11
    return index


def hashFunction3(stringData):
    #polynomial hash function
    index = 0
    for letter in stringData:
        index = index * (7 * ord(letter))
    return index


def hashFunction4(stringData):
    #stronger polynomial hash function
    index = 0
    for letter in stringData:
        index = index * ord(letter)/31
    return index


def hashFunction5(stringData):
    #mix of both polynomial hash functions
    index = 0
    for letter in stringData:
        index = index * 37 + ord(letter)
    return index


if __name__ == "__main__":
    def main():
        hashFunction = hashFunction1

        method = "linear" #"linked"

        movies = []

        with open("MOCK_DATA.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            for row in reader:
                if len(row) >= 9:
                    movies.append(movieNode(row))

        print("Movies loaded:", len(movies))

        size = int(len(movies)) + 1

        titleTable = [None] * size
        quoteTable = [None] * size

        titleCollisions = 0
        quoteCollisions = 0

        #-------------------------MOVIE TITLE-----------------------------
        startTime = time.time()

        for movie in movies:

            index = hashFunction(movie.movie_name) % size

            if method == "linked":

                if titleTable[index] is None:
                    titleTable[index] = []
                else:
                    titleCollisions += 1

                titleTable[index].append(movie)

            else:

                while titleTable[index] is not None:
                    titleCollisions += 1
                    index = (index + 1) % size

                titleTable[index] = movie

        titleTime = time.time() - startTime

        #----------------------------------------------MOVIE QUOTE-------------------------
        startTime = time.time()

        for movie in movies:

            index = hashFunction(movie.quote) % size

            if method == "linked":

                if quoteTable[index] is None:
                    quoteTable[index] = []
                else:
                    quoteCollisions += 1

                quoteTable[index].append(movie)

            else:

                while quoteTable[index] is not None:
                    quoteCollisions += 1
                    index = (index + 1) % size

                quoteTable[index] = movie

        quoteTime = time.time() - startTime

        titleWasted = titleTable.count(None)
        quoteWasted = quoteTable.count(None)


        #===========================================================================
        print("\n==HASH TABLE RESULTS==")
        print("Hash Function: hashfunction1")
        print("Collision Method:", method)
        print("Table Size:", size)

        print("\nMOVIE TITLE")
        print("Collisions:", titleCollisions)
        print("Wasted Space:", titleWasted)
        print("Construction Time:", titleTime, "seconds")

        print("\nMOVIE QUOTE")
        print("Collisions:", quoteCollisions)
        print("Wasted Space:", quoteWasted)
        print("Construction Time:", quoteTime, 6, "seconds")

