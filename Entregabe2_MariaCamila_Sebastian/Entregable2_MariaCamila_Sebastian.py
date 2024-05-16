import cv2 
import numpy as np
import matplotlib.pyplot as plt
import os
import pydicom

def conteoImagen(ruta):
    imagen=cv2.imread(ruta)
    img=cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB) 
    gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    mid=np.mean(gris)
    Umb,imgB=cv2.threshold(gris,mid,255,cv2.THRESH_BINARY) 
    kernel = np.ones((5,5),np.uint8) 
    eros=cv2.erode(imgB,kernel,iterations = 7)
    dilata=cv2.dilate(eros,kernel,iterations = 7)
    elem,mask=cv2.connectedComponents(dilata)
    plt.figure(figsize=(15,8),facecolor="lightblue")
    plt.subplot(2,2,1)
    plt.imshow(img, cmap='gray')
    plt.title("IMAGEN ORIGINAL")
    plt.subplot(2,2,2)
    plt.imshow(gris, cmap='gray')
    plt.title("IMAGEN EN ESCALA DE GRISES")
    plt.subplot(2,2,3)
    plt.imshow(imgB, cmap='gray')
    plt.title("IMAGEN BINARIZADA")
    plt.subplot(2,2,4)
    plt.imshow(dilata, cmap="gray")
    plt.title("IMAGEN TRANSFORMACIONES MORFOLÓGICAS")
    print(f">>>>> ESTA IMAGEN TIENE {elem-1} CÉLULAS <<<<<")
    plt.show()

def cargar_imagen(rutadi):
    archivo_dicom = [file for file in os.listdir(rutadi) if file.endswith(".dcm")]
    archivo_dicom.sort()
    imagenes_dicom = [pydicom.dcmread(os.path.join(rutadi,file))for file in archivo_dicom]
    return imagenes_dicom

def mostrar_imagen(imagendi):
    fig = plt.figure()
    while True:
        for imagen in imagendi:
            plt.imshow(imagen.pixel_array, cmap=plt.cm.gray)
            plt.title("Imagen Dicom")
            plt.axis("off")
            plt.pause(0.5)
            plt.clf()
            
        
        for imagen in imagendi[::-1]:
            plt.imshow(imagen.pixel_array, cmap=plt.cm.gray)
            plt.title("Imagen dicom")
            plt.axis("off")
            plt.pause(0.5)
            plt.clf()
            

while True:
    print("*****BIENVENID@ AL SISTEMA GESTIÓN DE ARCHIVOS CON CV2 Y PYDICOM")
    menu=int(input("""Marque según lo que desee hacer:
               1.Conteo de células de una imagen
               2.Visualizar una a una las imagenes médicas de un archivo DICOM
               3.salir 
                   >>>> """))
    if menu == 1:
        ruta=input("Registra la ruta de la imagen para el conteo >>> ")
        conteoImagen(ruta)

    elif menu == 2:
        rutadi=input("Registra la ruta del archivo DICOM para la visualización >>> ")
        imagendi = cargar_imagen(rutadi)
        mostrar_imagen(imagendi)
    
    elif menu == 3:
        break

    else:
        print("¡¡¡Ingreso una opción incorrecta, inténtelo de nuevo!!!")
        continue
    