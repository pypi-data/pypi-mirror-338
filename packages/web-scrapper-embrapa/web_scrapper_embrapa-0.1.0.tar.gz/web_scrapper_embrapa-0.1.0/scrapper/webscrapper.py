import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

def scrapper(project_dir):
    # Definir diretório onde os arquivos serão salvos
    download_dir = project_dir + "PythonProject/data/raw"  # Altere para o caminho desejado

    # Configurar as preferências do Chrome para baixar os arquivos automaticamente
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,  # Define o diretório de download
        "download.prompt_for_download": False,  # Não pedir confirmação para baixar
        "download.directory_upgrade": True,  # Atualizar o diretório se necessário
        "safebrowsing.enabled": True  # Permitir downloads seguros
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless")  # Executa sem abrir o navegador (opcional)

    # Configurar o driver
    chrome_driver_path = "/Users/tiagoribeiro/PycharmProjects/PythonProject/.venv/bin/chromedriver"  # Caminho correto
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Listas de abas e sub-opções
    abas = ['02', '03', '04', '05', '06']
    sub_opcao = ['01', '02', '03', '04']
    sub_opcao2 = ['01', '02', '03', '04', '05']

    # Loop para acessar cada aba e baixar os arquivos
    for aba in abas:
        urls = []  # Lista de URLs a serem processadas nesta iteração

        if aba in ['02', '04']:
            urls.append(f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_{aba}")
        elif aba in ['03', '06']:
            urls = [f"http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_{opcao}&opcao=opt_{aba}" for opcao in sub_opcao]
        else:
            urls = [f"http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_{opcao}&opcao=opt_{aba}" for opcao in sub_opcao2]

        # Processa cada URL gerada
        for url in urls:
            print(f"Iniciando download: {url}")

            driver.get(url)
            time.sleep(5)  # Tempo para carregar a página

            # Tenta clicar no botão de download
            try:
                download_button = driver.find_element(By.CLASS_NAME, "footer_content")  # Ajuste conforme o site
                ActionChains(driver).move_to_element(download_button).click().perform()
                print(f"✔ Download iniciado! Arquivo salvo em {download_dir}")
            except Exception as e:
                print(f"⚠ Erro ao clicar no botão: {e}")

            time.sleep(10)  # Aguarda o download finalizar

    # Fecha o navegador após todos os downloads
    driver.quit()
    return

project_dir = "/Users/tiagoribeiro/PycharmProjects/"

scrapper(project_dir)
