#!/usr/bin/env python
# coding: utf-8

# In[7]:


#importo le librerie necessarie
import re
import requests
from bs4 import BeautifulSoup


# In[8]:


#salvo l'url della pagina profilo del giocatore, in questo caso Lautaro Martinez
url = "https://www.transfermarkt.it/lautaro-martinez/profil/spieler/406625"


# In[9]:


#ottengo l'id giocatore
player_id = url.split('/')[-1] # mi da il valore dopo l'ultimo slash
player_id


# In[10]:


#salvo l'headers ottenuto tramite whatsmybrowser.com
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


# In[11]:


#risposta
response = requests.get(url, headers=headers)


# In[12]:


#stato risposta
response.status_code # Quando un server invia lo status code 200, comunica al client che la richiesta 
                     # è stata ricevuta con successo e fornisce in risposta il contenuto richiesto


# In[13]:


soup = BeautifulSoup(response.content, "html.parser")


# In[15]:


#ottengo nome e cognome del giocatore
nome_giocatore = soup.select_one('h1[class="data-header__headline-wrapper"]')
nome_giocatore


# In[16]:


#ottengo la sola stringa per nome e cognome del giocatore
nome_giocatore = soup.select_one('h1[class="data-header__headline-wrapper"]').text.split('\n')[-1].strip()
nome_giocatore


# In[18]:


#ottengo il numero del giocatore
numero_giocatore = soup.select_one('span[class="data-header__shirt-number"]')
numero_giocatore


# In[40]:


#ottengo la sola stringa contenente il numero del giocatore
numero_giocatore = soup.select_one('span[class="data-header__shirt-number"]').text.replace('#', '').strip()
numero_giocatore


# In[41]:


#trasformo la stringa in un intero
int(numero_giocatore)


# In[20]:


#ottengo la scadenza del contratto utilizzando le regex tramite regex101.com
scadenza_contratto_giocatore = re.search("(30/giu/2026).*", str(soup))
scadenza_contratto_giocatore


# In[46]:


#prendo solo la stringa cotenente la data che mi serve
scadenza_contratto_giocatore = re.search("(30/giu/2026).*", str(soup)).group(1)
scadenza_contratto_giocatore


# In[58]:


#ottengo il valore del giocatore
valore_giocatore = soup.select_one('a[href="/lautaro-martinez/marktwertverlauf/spieler/406625"]').text
valore_giocatore


# In[ ]:




