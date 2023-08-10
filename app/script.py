from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

def realizar_solicitud():
    options = webdriver.ChromeOptions()#crear una instancia 
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get('https://www.eliteperfumes.cl/collections/para-el')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    #links = soup.select("ul.ipc-metadata-list li div.ipc-metadata-list-summary-item__c div div div.ipc-title a")
    title_elements = soup.select(".productitem--title")
    price_elements = soup.select(".price__current")

    title_elements = title_elements[:10]
    price_elements = price_elements[:10]

    list = {}

    for items in range(len(title_elements)):
        title = title_elements[items].text.strip()
        price = price_elements[items].text.strip()
        list[title] = price

    print(list)
    driver.quit()

def solicitud_pricio_oferta():
    options = webdriver.ChromeOptions()#crear una instancia 
    options.add_argument("--start-maximized")# Maximizar la ventana del navegador

    driver = webdriver.Chrome(options=options)

    driver.get('https://www.eliteperfumes.cl/collections/para-el')#cambiar ip de la pagina a rascar

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    links = soup.select(".productitem--title a")#seleccionar el nombre del producto que posea un href
    first10 = links[:4]

    productos = []

    for anchor in first10:
        driver.get('https://www.eliteperfumes.cl/' + anchor['href'])
        print(anchor.text)

        ahorro = driver.find_element(By.CLASS_NAME, 'product__badge').text#ingresando a la oferta
        price = driver.find_element(By.CLASS_NAME, 'money').text #ingresando a precio original
        productos.append({
            "name": anchor.text,
            "price": price,
            "oferta": ahorro,
        })
        time.sleep(3)

    df = pd.DataFrame(productos)

    ruta_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

    if not os.path.exists(ruta_data):
        os.makedirs(ruta_data)

    ruta_csv = os.path.join(ruta_data, 'perfumes_men_eliteperfumes.csv')

    df.to_csv(ruta_csv, index=False)
    driver.quit()


solicitud_pricio_oferta()