#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()  
driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account?trk=guest_homepage-basic_nav-header-signin")
time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("username")  

pword = driver.find_element(By.ID, "password")
pword.send_keys("password")        

driver.find_element(By.XPATH, "//button[@type='submit']").click()

#Entra no perfil
profile_urls = [
    "https://www.linkedin.com/in/vanessa-braganholo-111462308",
    "https://www.linkedin.com/in/tatiane-nogueira-rios-83301a30",
    "https://www.linkedin.com/in/ana-bazzan-1254b83",
    "https://www.linkedin.com/in/maria-cristina-ferreira-de-oliveira-01b6791a",
    "https://www.linkedin.com/in/marta-mattoso-12016a24",
    "https://www.linkedin.com/in/karinbecker",
    "https://www.linkedin.com/in/elizabeth-wanner-91607832",
    "https://www.linkedin.com/in/soraia-musse",
    "https://www.linkedin.com/in/aurora-pozo-b462032a",
    "https://www.linkedin.com/in/genaina-nunes-rodrigues-b194714",
    "https://www.linkedin.com/in/yoshiko-wakabayashi-49015b93",
    "https://www.linkedin.com/in/renata-reiser-8b15b3122",
    "https://www.linkedin.com/in/jussara-almeida-3312104",
    "https://www.linkedin.com/in/sabrina-marczak-18b7338",
    "https://www.linkedin.com/in/ana-carolina-lorena-06b1347",
    "https://www.linkedin.com/in/katia-felizardo-47853194",
    "https://www.linkedin.com/in/christiane-gresse-von-wangenheim-60659719",
    "https://www.linkedin.com/in/carla-freitas-8b7a242",
    "https://www.linkedin.com/in/luiza-mourelle-ab80ba8a",
    "https://www.linkedin.com/in/andreia-malucelli",
    "https://www.linkedin.com/in/crisgarcia",
    "https://www.linkedin.com/in/patricia-takako-endo-8bba69226",
    "https://www.linkedin.com/in/ahrcosta",
    "https://www.linkedin.com/in/nadia-nedjah-983275",
    "https://www.linkedin.com/in/viviane-moreira-ufrgs",
    "https://www.linkedin.com/in/carla-negri-lintzmayer",
    "https://www.linkedin.com/in/gisele-pappa",
    "https://www.linkedin.com/in/dr-olga-regina-pereira-bellon-6bbbbb154",
    "https://www.linkedin.com/in/claudia-linhares",
    "https://www.linkedin.com/in/teresa-ludermir-b6b85213",
    "https://www.linkedin.com/in/fabricia-roos-frantz-97a66a32",
    "https://www.linkedin.com/in/mirellammoro",
    "https://www.linkedin.com/in/maria-do-carmo-nicoletti-ab865a",
    "https://www.linkedin.com/in/elisa-yumi-nakagawa-757570272",
    "https://www.linkedin.com/in/judith-kelner-80523758",
    "https://www.linkedin.com/in/mariana-recamonde-mendoza",
    "https://www.linkedin.com/in/dianne-medeiros",
    "https://www.linkedin.com/in/sheilareinehr",
    "https://www.linkedin.com/in/avilasandra",
    "https://www.linkedin.com/in/solangerezende",
    "https://www.linkedin.com/in/lilian-berton-3a208824",
    "https://www.linkedin.com/in/simonedjb",
    "https://www.linkedin.com/in/raquel-c-de-melo-minardi-64a9815a",
    "https://www.linkedin.com/in/renata-souza-9690b350"
]



    
for profile_url in profile_urls:
        driver.get(profile_url)
        time.sleep(5)

        #Rola o perfil
        start = time.time()

        # will be used in the while loop
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            initialScroll = finalScroll
            finalScroll += 1000
            time.sleep(3)
            end = time.time()
            if round(end - start) > 20:
                break

        #Usando beautiful soup para localizar o container principal da introdução do perfil
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        intro = soup.find('div', {'class': 'mt2 relative'})
        print(intro)

        #INTRODUCAO
        #localizar Nome
        name_localizacao = intro.find("h1", {'class': 'text-heading-xlarge'})
        nome = name_localizacao.get_text().strip()
        #Localizar especificidade que está escrito abaixo do nome
        especif_localizacao = intro.find("div", {'class': 'text-body-medium'})
        apresentacao = especif_localizacao.get_text().strip() if especif_localizacao else "sem apresentação informada"
        #Localização
        local = intro.find("div", {'class':'WVsEYfFsGBlxEUYVuCIzjLuLSgfiEA mt2'}).find('span', {'class': 'text-body-small inline t-black--light break-words'})
        localidade = local.get_text().strip() if local else "sem localização informada"
        #print("nome: ", nome,
                #"\Apresentacao: ", apresentacao,
                #"\nLocalização: ", localidade)

       
    #Extraindo a formação academica

        education_data = []

        if driver.find_elements(By.ID, "navigation-index-see-all-education"):
            # Se o botão estiver presente, clique nele
            button = driver.find_element(By.ID, "navigation-index-see-all-education")
            driver.execute_script("arguments[0].click();", button)
            time.sleep(5)
            # Obtendo o HTML da página atual após clicar no botão
            html = driver.page_source
            # Usando BeautifulSoup para analisar o HTML
            soup = BeautifulSoup(html, 'html.parser')
            # Encontrando a seção de formação acadêmica
            education_section = soup.find('section', class_='artdeco-card pb3')
            print("--------------1---------------")
            print(education_section.prettify())

            # Encontrando todos os itens de formação acadêmica dentro da seção
            education_items = education_section.find_all('div', class_='FgUskDpLQihITyYLSeIpwrpzGcTtKeqbgsPU ytGwsyuVvZACisWRkrzCmHRyWEAorqVNbIY sNZVjoSAOLHIUipMiBynRTmauuJZJNeFFNhpPM')
            # Iterando sobre todos os itens de formação acadêmica e imprimindo as informações
            for education_item in education_items:
                try:
                    university_element = education_item.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold').find('span', {'class': 'visually-hidden'})
                    university = university_element.get_text(strip=True) if university_element else "sem universidade informada"
                except AttributeError:
                    university="universidade não informada"
                
                try:
                    education_element = education_item.find('span', class_='t-14 t-normal').find('span', {'class': 'visually-hidden'})
                    education = education_element.get_text(strip=True) if education_element else "sem especificação/curso informado"
                except AttributeError:
                    education="especificação/curso não informado"
                    
                try:
                    date_element = education_item.find('span', class_='t-14 t-normal t-black--light').find('span', {'class': 'visually-hidden'})
                    date = date_element.get_text(strip=True) if date_element else "sem data informada"
                except AttributeError:
                    date="data de formação não informada"
                    
                print("Universidade:", university, 
                        "\nEspecificação:", education, 
                        "\nData:", date,
                        "\n---------")

                education_data.append({"Universidade": university, "Especificação/curso": education, "Data de formação": date})


        else:
            all_h2_titles = soup.find_all('h2', {'class': 'pvs-header__title'})

            # Iterar sobre todas as ocorrências
            for h2_title in all_h2_titles:
                # Verificar se o texto "Formação acadêmica" está presente na tag h2
                if "Formação acadêmica" in h2_title.text.strip():
                    # Encontrar a seção pai da tag h2
                    education_section = h2_title.find_parent('section', {'class': 'artdeco-card pv-profile-card break-words mt2'})
                    print("--------------2---------------")
                    print(education_section.prettify())
                    # Verificar se a seção foi encontrada
                    if education_section:
                        # Encontrando todos os itens de formação acadêmica dentro da seção
                        education_items = education_section.find_all('div', {'class': 'FgUskDpLQihITyYLSeIpwrpzGcTtKeqbgsPU ytGwsyuVvZACisWRkrzCmHRyWEAorqVNbIY sNZVjoSAOLHIUipMiBynRTmauuJZJNeFFNhpPM'})

                        if education_items:
                            # Iterando sobre todos os itens de formação acadêmica e imprimindo as informações
                            for education_item in education_items:
                                try:
                                    university_element = education_item.find('div', {'class': 'display-flex align-items-center mr1 hoverable-link-text t-bold'}).find('span', {'class': 'visually-hidden'})
                                    university = university_element.get_text(strip=True) if university_element else None
                                except AttributeError:
                                    university="universidade não informada"
                                    
                                try:
                                    education_element = education_item.find('span', {'class':'t-14 t-normal'}).find('span', {'class': 'visually-hidden'})
                                    education = education_element.get_text(strip=True) if education_element else None
                                except AttributeError:
                                    education="especificação/curso não informado"
                                
                                try:
                                    date_element = education_item.find('span', {'class':'t-14 t-normal t-black--light'}).find('span', {'class': 'visually-hidden'})
                                    date = date_element.get_text(strip=True) if date_element else None
                                except AttributeError:
                                    date="data de formação não informada"

                                print("Universidade:", university, 
                                    "\nEspecificação/curso:", education, 
                                    "\nData de formação:", date,
                                    "\n---------")
                                education_data.append({"Universidade": university, "Especificação/curso": education, "Data de formação": date})
                        else:
                            print("Nenhuma informação de formação acadêmica encontrada.")
                    else:
                        print("Seção 'education' não encontrada ou está vazia.")
                    break  # Parar após encontrar a primeira ocorrência de "Formação acadêmica"

            else:
                print("Nenhuma ocorrência de 'Formação acadêmica' encontrada.")

        with open('PesquisadorasDeProdutividade.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Nome da pesquisadora', 'Resumo do perfil', 'Localização', 'Universidade', 'Especificação/curso', 'Data de formação']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


            # Escrever informações acadêmicas
            for education_info in education_data:
                row_data = {'Nome da pesquisadora': nome, 'Resumo do perfil': apresentacao, 'Localização': localidade}
                row_data.update(education_info)
                writer.writerow(row_data)
        print(f"As informações foram escritas no arquivo CSV.")
        time.sleep(3)

driver.quit()
    
    
    
    

