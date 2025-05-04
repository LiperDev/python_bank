import time

def temporizador(tempo):
    match (tempo):
        case 1:
            time.sleep(2)
        case 2:
            time.sleep(4)
        case 3:
            time.sleep(6)
        case _:
            print("Valor inválido!")
