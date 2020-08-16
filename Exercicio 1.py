def remove_repetidos(lista):

    clone_lista = sorted(lista[:])
    
    for a in range(len(clone_lista)):
        
        if a == len(clone_lista)-1:
            return clone_lista
        
        else:
            for b in range(len(clone_lista)):
                
                if clone_lista[a] == clone_lista[a+1]:
                    del clone_lista[a+1]
                else:
                    break
            
