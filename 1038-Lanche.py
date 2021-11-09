codproduto, quantidade = input().split(" ")
codproduto = eval(codproduto)
quantidade = eval(quantidade)
if (codproduto == 1):
    total = quantidade * 4
    print(f"Total: R$ {total:.2f}")
if (codproduto == 2):
    total = quantidade * 4.5
    print(f"Total: R$ {total:.2f}")
if (codproduto == 3):
    total = quantidade * 5
    print(f"Total: R$ {total:.2f}")
if (codproduto == 4):
    total = quantidade * 2
    print(f"Total: R$ {total:.2f}")
if (codproduto == 5):
    total = quantidade * 1.5
    print(f"Total: R$ {total:.2f}")
