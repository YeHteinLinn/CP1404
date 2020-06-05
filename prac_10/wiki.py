import wikipedia


def main():
    search_on_wiki = input("Enter the search phrase or page title:")
    while search_on_wiki != "":
        print(wikipedia.summary(search_on_wiki))
        search_on_wiki = input("Enter the search phrase or page title:")


if __name__ == '__main__':
    main()
