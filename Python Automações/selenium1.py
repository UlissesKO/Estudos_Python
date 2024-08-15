from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


servico = Service(ChromeDriverManager().install()) #vai instalar o driver certo pra versao do navegador
navegador = webdriver.Chrome(service=servico)  #ta dizendo qual o navegador

a = 0

while a < 10:

    #vai acessar o link q colocar no parenteses
    navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSf1XuFXN0EMyAcUgPKXkUfnFHQUak7J-U-qycC4IUuyjOz91Q/viewform?usp=sf_link")

    #vai procurar elemento pelo xpath no navegador
    navegador.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Ana")
    #a função send_keys() serve pra escrever alguma coisa no elemento selecionado

    navegador.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("ana@gmail.com")

    navegador.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    #click() serve pra clicar

    a += 1
