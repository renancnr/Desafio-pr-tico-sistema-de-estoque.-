
import threading
import time

estoque = 5
lock = threading.Lock()


def comprar(cliente):
    global estoque

    with lock:
        if estoque > 0:
            print(cliente, "encontrou", estoque, "unidade(s)")
            time.sleep(0.5)
            estoque -= 1
            print(cliente, "comprou. Restam:", estoque)
        else:
            print(cliente, "não conseguiu comprar: estoque esgotado")


clientes = []

for i in range(1, 9):
    t = threading.Thread(
        target=comprar,
        args=(f"Cliente {i}",)
    )
    clientes.append(t)
    t.start()

for t in clientes:
    t.join()

print("Estoque final:", estoque)
