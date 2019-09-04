
def create_trans_file(file):
    f = open(file)

    lines = f.readlines()
    transactions = []
    for line in lines:
        if "<TRNAMT>" in line:
            start_index = line.find("<TRNAMT>")+8
            end_index = line.find("<FITID>")

            transaction = line[start_index:end_index]

            transactions.append(transaction)
    
    f.close()

    f = open("income_list.txt", "w")
    for transaction in transactions:
        if(float(transaction) >= 0):
            f.write(transaction+"\n")
    f.close()

    f = open("outcome_list.txt", "w")
    for transaction in transactions:
        if(float(transaction) < 0):
            f.write(transaction[1:]+"\n")
    f.close()


def main():
    create_trans_file("./cibc.ofx")


if __name__ == "__main__":
    main()