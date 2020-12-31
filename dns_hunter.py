#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import socket, time, sys, os
os.system('clear')

print('\033[35m'+'''
\n\n\n
                    ████████▄  ███▄▄▄▄      ▄████████                     
                    ███   ▀███ ███▀▀▀██▄   ███    ███                     
                    ███    ███ ███   ███   ███    █▀                      
                    ███    ███ ███   ███   ███                            
                    ███    ███ ███   ███ ▀███████████                     
                    ███    ███ ███   ███          ███                     
                    ███   ▄███ ███   ███    ▄█    ███                     
                    ████████▀   ▀█   █▀   ▄████████▀                      
                                                                          
   ▄█    █▄    ███    █▄  ███▄▄▄▄       ███        ▄████████    ▄████████ 
  ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
  ███    ███   ███    ███ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
 ▄███▄▄▄▄███▄▄ ███    ███ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀▀███▀  ███    ███ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ███   ███    ███ ███   ███     ███       ███    █▄  ▀███████████ 
  ███    ███   ███    ███ ███   ███     ███       ███    ███   ███    ███ 
  ███    █▀    ████████▀   ▀█   █▀     ▄████▀     ██████████   ███    ███ 
                                                               ███    ███                 

                       (programador: carlosadrianosj)
            (Ferramenta criada para enumeração de servidores DNS)
\n\n\n\
''')

#verifica se o programa foi executado em modo root
permissão_do_usuario = os.geteuid()
if permissão_do_usuario == 1000:
      print("              Este programa precisa ser executado em modo ROOT!!")
      time.sleep(0.5)
      print("              Este programa precisa ser executado em modo ROOT!!")
      time.sleep(0.5)
      print("              Este programa precisa ser executado em modo ROOT!!")
      time.sleep(0.5)
      print("                  Exemplo: sudo python3 dns_hunter.py\n\n\n\n")
      time.sleep(0.5)
      os._exit()
elif permissão_do_usuario == 0:
      pass

#coleta do alvo
dominio  = input("Digite seu alvo | (Ex: google.com): ")

#faz a leitura do dns_bruteforce.txt, tenta pingar no alvo com a pesquisa do arquivo, se positivo, printa na tela,
#se não, continua a lista 
with open("dns_bruteforce.txt", "r") as arquivo:
    dns_bruteforce = arquivo.readlines()
for nome in dns_bruteforce:
    DNS = nome.strip("\n") + "." + dominio
    try:
        print("#| " + DNS + ": " + socket.gethostbyname(DNS))
        
    except socket.gaierror:
        pass
print("\n\nEnumeração feita com sucesso!!")
    
