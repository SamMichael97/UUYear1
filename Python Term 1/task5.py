#Produce a sample file bank_accounts.txt, that contains a list of at least 10 sample account numbers that
#follow a 7-digit format 501xxxx (were you replace xxxx with unique numbers for each account), comma
#separated from a corresponding account balance (£) e.g.

# Ac No, Balance (£)
#5015687, 24400
#5014875, 13580

#Write a program that reads the contents of the file (using appropriate file I/O code) into a 2-dimensional
#list/array. The program should request the user to enter, via the command line interface, a charge account
#number before the program checks whether the number is valid by searching for it in the 2d list. If the
#account number is found in the list, the program should display an output message indicating the number
#is valid and return the account balance. If the account number is not found in the list, the program should

#display a message indicating the number is invalid and offer the user a further attempt to enter a correct
#number. E,g.
#>> Enter an account number: 5015687
#>> Account 5015687 found.

def main():
    account_list = []
    balance_list = []
    bank_file = open('bank_accounts.txt', 'r')
    read = bank_file.readlines()

    for line in read:
        split_list = line.split(",")
        account_list.append(split_list[0].rstrip('\n'))
        balance_list.append(split_list[1].rstrip('\n'))

    del account_list[0]
    del balance_list[0]
    int_account_list = list(map(int, account_list))
    listoflists = [int_account_list, balance_list]

    print(listoflists)

    search = int(input('Please enter the account number that you are looking for'))
    try:
        index = int_account_list.index(search)
        for i in listoflists:
            print(i[index])
    except:
        print('Account not found')

main()

    #I/O and search

    #search = int(input('Please enter the account number that you are looking for'))

    #found = False
    #if search in account_list:
        #print('Yo Mr White the account has been found, bitch')
    #else:
        #print('that shit is gone man')

