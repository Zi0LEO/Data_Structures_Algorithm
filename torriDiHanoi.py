h = 0

def moveDisk(X, Y):
    global h
    h = h + 1
    print(str(h) + ") Muovi un disco da " + str(X) + " a " + str(Y))

def hanoi(n, start, destination, aux):
    if n > 0:
        hanoi(n-1, start, aux, destination)  #2T(n - 1) + 1
    #prendo tutti i dischi ad eccezione del più grande dal primo anello e li sposto verso l'anello di ausilio
        moveDisk(start, destination) #O(1)
    #muovo il disco più grande dall'anello iniziale a quello finale
        hanoi(n - 1, aux, destination, start) #2T(n - 1) + 1
    #Sposto la torre che ho formato sull'anello di ausilio a quella di destinazione finale

#Thanoi = O(2^n), calcolo fatto su quaderno
#Shanoi = O(n)

hanoi(3, "A", "B", "C")