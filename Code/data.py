import numpy as np   


####################################################
# Produit A x pour la matrice de la partie 1
def produit1(x,ddata):
    alpha, h = ddata
    prodx = x * 0.0
    
    n = len(prodx)
    for i in range(n):
        if i == 0:
            prodx[i] = (2 + alpha * h ** 2) * x[i] - x[i + 1]
        elif i == n - 1:
            prodx[i] = - x[i - 1] + (2 + alpha * h ** 2) * x[i]
        else:
            prodx[i] = - x[i - 1] + (2 + alpha * h ** 2) * x[i] - x[i + 1]
    
    return prodx
####################################################


####################################################
# Produit M^{-1} x pour la matrice de la partie 1
def diag1(x,ddata):    
    alpha,h = ddata
    res = x * 0.

    res = (1 / (2 + alpha * h ** 2)) * x
    
    return res
####################################################



    
####################################################
# Produit M^{-1} x pour la partie 2 (image)        
def diagImg(x,ddata):    
    mask,regu,Nx,Ny = ddata
    diagg = x*0.
    diagg += mask.reshape(-1)
    diagg += regu * 4.0 
    return x/diagg
####################################################



####################################################
# Produit A x pour la matrice de la partie 2 (image)    
def produitImg(x,ddata):
    mask,regu,Nx,Ny = ddata
    xxImg = x.reshape(Nx,Ny)
    
    newImg = x.reshape(Nx,Ny)
    imgres = laplace(xxImg)
            
    newImg = mask * xxImg + regu * laplace(xxImg)
    
    return newImg.reshape(-1)  
####################################################      
    
####################################################      
# Calcul du Laplacien discret partie 2 (image)    
def laplace(img):
    imgres = img*4.0 # Ici img est une matrice de taille Nx x Ny
    
    Nx = len(img)
    Ny = len(img[0])
    l,c = imgres.shape
    
    imgres[1:l-1,1:c-1] = 4*img[1:l-1, 1:c-1] - img[0:l-2,1:c-1] - img[1:l-1,0:c-2] - img[2:l,1:c-1] - img[1:l-1,2:c]
    
    
    return imgres
####################################################          
