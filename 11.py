def main():
    names = input().split()
    n = int(input())
    payers = []
    amounts = []
    count = 0ㄆ
    while True:
        if count == n:
            break
        payer, amount = input().split()
        payers.append(payer)
        amounts.append(int(amount))
        count += 1
    paid = build_paid(names, payers, amounts)
    share = get_share(paid)
    balance = get_balance(paid, share)
    report = make_report(balance)
    print(f"每人分攤：{share} 元")
    for line in report:
        print(line)

if __name__ == "__main__":
    main()