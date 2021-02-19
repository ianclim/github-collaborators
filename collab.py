#!/usr/bin/env python3
"""
Module Docstring
"""
import requests

__author__ = "Ian Lim"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    """ repo_path structure: {organization}/{repo name}"""
    #array1 = []

    with open('projects.txt', 'r') as f:
        for line in f.readlines():
            #array1.append(line)

            #repo_path = "facebook/react"
            repo_path = line

            total = 0
            counter = 0
            while True:
                res = requests.get(
                    "https://api.github.com/repos/" + repo_path + "/contributors",
                    params={'per_page': 100, 'anon': 'true', 'page': counter}
                )
                if len(res.json()) == 0:
                    break
                else:
                    total += len(res.json())
                    counter += 1

            print("Total number of contributors for repo path: ", repo_path, "is", total)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()