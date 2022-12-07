#string data analyst
#accurencies of each letter

def main():
    
    return count_string('hello')

def count_string(chain= str):

    chain_lst = []
    count_letters = []

    for i in chain:
        if i not in chain_lst:
            chain_lst.append(i)

    for j in chain_lst:
        count_letters.append(chain.count(j))
    
    return list(zip(chain_lst, count_letters))


if __name__ == '__main__':
    x = main()
    print(x)