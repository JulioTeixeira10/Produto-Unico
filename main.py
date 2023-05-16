import requests
from configparser import ConfigParser
import xml.etree.ElementTree as ET
import urllib.parse
from errortreatment import tratamento
import time

#Diretório de dados
dirDados = "C:\\Bancamais\\Fastcommerce\\DadosLoja"

#Diretório de XML
dirXML = "C:\\Bancamais\\Fastcommerce\\XMLs\\XMLProdUni\\xml.txt"

#Administração do arquivo .cfg
configobject = ConfigParser()
configobject.read(f"{dirDados}\\StoreData.cfg")
STOREINFO = configobject["STOREINFO"]
StoreName = STOREINFO["StoreName"]
StoreID = STOREINFO["StoreID"]
Username = STOREINFO["Username"]
password = STOREINFO["password"]

#Script para trazer e codificar o XML para a URL
xmlrecord = open(f'{dirXML}','r').read()

root = ET.fromstring(xmlrecord)
for record in root.findall('Record'):
    CodProd2 = record.find("Field[@Name='CodProd']").attrib['Value']

xmlcoded = urllib.parse.quote(xmlrecord)

#Request
url = "https://www.rumo.com.br/sistema/adm/APILogon.asp"
payload= (f"""StoreName={StoreName}&StoreID={StoreID}&Username={Username}&
            method=ProductManagement&password={password}&XMLRecords={xmlcoded}""")
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.request("POST", url, headers=headers, data=payload)
checkresponse = response.text

#Tratamento de erro da primeira request
tratamento(checkresponse)

#Pega o dia atual
datetime = time.strftime("%d/%m/%Y")

#Codificação da data para a URL
DataInicial = datetime + " 00:00:01"
DataInicialEncoded = urllib.parse.quote(DataInicial)
DataFinal = datetime + " 23:59:59"
DataFinalEncoded = urllib.parse.quote(DataFinal)

#Request
payload= (f"""StoreName={StoreName}&StoreID={StoreID}&Username={Username}&
        method=ReportView&password={password}&ObjectID=89&Fields=IDProduto, Ref.&Par5={DataInicialEncoded}&Par6={DataFinalEncoded}""")
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.request("POST", url, headers=headers, data=payload)


xmlstring = response.text

#Pega o XML e procura o ID do produto
root = ET.fromstring(xmlstring)
for record in root.findall('Record'):
    CodProd1 = record.find("Field[@Name='Ref.']").attrib['Value']
    id_produto = record.find("Field[@Name='IDProduto']").attrib['Value']
    if CodProd1 == CodProd2:
        id_produtoFinal = id_produto
        break

#Escreve o ID do produto no arquivo
with open("C:\\Bancamais\\Fastcommerce\\DadosLoja\\id_produto.txt","w+") as f:
    f.write(id_produtoFinal)
    f.close()