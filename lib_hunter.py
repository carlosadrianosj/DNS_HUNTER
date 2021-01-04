#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import socket, os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Hunter:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.wordlist = os.path.join(self.base_dir, 'dns_bruteforce.txt')
        self.banner = os.path.join(self.base_dir, 'banner.txt')

    def get_banner(self):
        os.system('clear')
        with open(self.banner, 'r') as banner:
            return '\033[35m'+ banner.read()

    def is_root(self):
        permissao_do_usuario = os.geteuid()
        if permissao_do_usuario != 0:
            return True
        return False

    def get_user_parameters(self, explanation):
        return input(explanation)

    def heartbeat(self, target_domain, dominio_in_bruteforce):
        for nome in dominio_in_bruteforce:
            DNS = nome.strip("\n") + "." + target_domain
            try:
                print("#| " + DNS + ": " + socket.gethostbyname(DNS))
                with open('dns_hunter_result.txt', 'a') as output:
                    output.write("#| " + DNS + ": " + socket.gethostbyname(DNS))

            except socket.gaierror:
                pass
        return ("\n\nEnumeração feita com sucesso!!")


if __name__ == '__main__':
    hunt = Hunter()
    print(hunt.hunt())


