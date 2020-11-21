from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path="/home/pamela/Downloads/chromedriver")

    def login (self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        campo_usuario= driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)

    @staticmethod
    def digite_como_uma_pessoa (frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comente_na_foto (self):
        driver = self.driver
        driver.get("") #link da publicação de que deseja comentar
        try:
            u1 = ["", " ", ""] #lista de usuários que serão marcados nos comentários


            driver.find_element_by_class_name('Ypffh').click()
            campo_comentario = driver.find_element_by_class_name('Ypffh')
            time.sleep(random.randint(2,5))
            self.digite_como_uma_pessoa(u1, campo_comentario)
           # time.sleep(random.randint(45, 60))
            time.sleep(60)
            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
            time.sleep(5)
            
            
        except Exception as e:
            print(e)

bot = InstagramBot("", "") # colocar o usuário primeiro, e depois a senha
bot.login()
time.sleep(8)
while True:
    bot.comente_na_foto()
    time.sleep(25)
