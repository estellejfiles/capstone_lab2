# create new author class
class Author:
    # class takes name as an argument
    def __init__(self, name):
        # name and books list are the two instance variables for the object
        self.name = name
        self.books = []

    # publish method takes book title as an argument
    def publish (self, title):
        # check for duplicates of title given as argument
        if title not in self.books:
            # if the title given is not in the list, add the title to the list
            self.books.append(title)
        else:
            # if the title is already in the list, print a message to user
            print(f'The book "{title}" is already published by this author.')

    # method to create string representation of the object
    def __str__(self):
        # join together books in list into string by commas
        # if that attempt returns false (means there are no books in list) returns separate string
        book_list = ', '.join(self.books) or 'No books published yet.'
        # returns author's name and book list as the string
        return f'{self.name}: {book_list}'

# main function
def main():
    # add author and their books (will not add duplicates due to check in def publish)
    jane_austen = Author('Jane Austen')
    jane_austen.publish('Pride and Prejudice')
    jane_austen.publish('Sense and Sensibility')
    jane_austen.publish('Pride and Prejudice')
    # print string representation with author's name and book list to user
    print(jane_austen)

    # add author and use .publish to add books
    marissa_meyer = Author('Marissa Meyer')
    marissa_meyer.publish('Cinder')
    marissa_meyer.publish('Heartless')
    marissa_meyer.publish('Cinder')
    marissa_meyer.publish('Renegades')
    # print string representation with name and book list
    print(marissa_meyer)

main()