# funciones_auxiliares.py

def printear_mapa(mapa, n, m, alpha=500):
    
    for i in range(n):
        for j in range(m):
            if mapa[i, j] - 1000 >= -alpha:
                print("🔥", end=" ")
            elif mapa[i, j] < alpha:
                print("🌲", end=" ")
            else:
                print(int(mapa[i, j]), end=" ")
        print()
    print("\n")


def printear_un_ejemplo(X_test, Y_test, Y_pred, tamaño, index=0):

    tx, ty = tamaño
    print("Condiciones iniciales:")
    print(f"Viento: {X_test[index][2:5]} Tiempo transcurrido: {X_test[index][5]}")
    print("\n")
    print("Mapa Inicial:\n")
    printear_mapa(X_test[index][6:].reshape(tx, ty), tx, ty)
    print("Mapa Final:\n")
    printear_mapa(Y_test[index].reshape(tx, ty), tx, ty)
    print("Mapa Predicho:\n")
    printear_mapa(Y_pred[index].reshape(tx, ty), tx, ty)