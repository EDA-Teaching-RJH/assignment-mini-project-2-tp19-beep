## Collectors Vault - Project reflection
**Assignment 2**: Mini Project 2

**Module** Code: EENG4101

**Name**: Tyler Procope

**Email**: tp19@kent.ac.uk

For this project I created a program called **Collectors Vault**. 
The goal of this program is to allow the user to manage their collection of toys and collectibles from the 2000s and 2010s. 

*The program allows users to:* 
- View their collection
- Add new collectibles 
- Remove collectibles 
- Search the Collection 
- Update collectible information 
- Count the number of collectibles
- Display a random collectible

The collectibles are saved in a .txt file so that any collectibles add or uodated will be available the next time the program runs, and that items deleted will also be permanently deleted. 

I went about the project step by step. I first built the basic menu system that allows the user to choose different actions such as viewing and adding items. 

After that I implemented the functions that manage the collection, such as adding, removing, searching and updating collectibles. 

Once the main features were working, I added validation features to make sure that the user cannot implement incorrect data. For exmaple IDs must have five digits, years must be four digits and prices should be valid numbers. 

I Finally organised the program into multiple python files for easier understanding. 

This project uses classes to rpresent collectibles. The "*Collectible*" class stores infromation such as brand, name, price, rarity and ID. I also creates a subclass called "*Doll*" that inherits from "*Collectible*". This demonstrates inheritance in **Object-Oriented Programming**. 

Python **libraries** were also used. "*sys.argv*" is used to greet the user if a name is passed when running the script, "*random*" is used to select a random collectible, and "*re*" is used to work with **regular expressions** for input validation. Using these **libraries** lets the program use python functions. A "*lambda*" function is used when displaying the collection to sort collectibles by Brand

**Regular expressions** are used to validate user input. For example, the program checks that IDs are are exactly five digits long, that years are exactly four digits long and that prices are valid numbers. This ensures that incorrect data cannot be stored. 

The program also saves collectible data in a file called "*collection.txt*". This uses **File input and output** through the functions, "*load_collection()*" and "*save_collection()*", that read and write data to this file so that the collection is saved whenever the program runs. 

**Testing** was implemented using "*pytest*". A seperate file called, "*test_vaultlib.py*", contains test that check the functions for IDs, prices and years. This ensure the acceptance of valid inputs and rejection of invalid inputs.

One challenge was making sure that user input was properly validated. without validation incorrect data could easily go undetected. Another challenge faced was the organisation of the program using multiple files and trying to understand how the functions and classes could be imported correctly. Ultimately however, I found using several files to work more effectvley than having sevral large ones as it kept the space organised and allowed me to spot mistakes easily. 

This project furthered my understanding of **OOP**, **Regex**, **File I/O** and **Testing**. It also taught me how to organise a program into multiple files and understand *pytests*. 

In the future i hope to better understand and improve this project by supporting additional collectibles, store data using .csv files, add morre advances search options and create a more polished user interface. 

