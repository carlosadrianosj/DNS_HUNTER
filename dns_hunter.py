import logging
import os
from queue import Queue
from threading import Thread
from time import time
from lib_hunter import Hunter
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
hunter = Hunter()

class HeartBeatWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue


    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            target_domain, domain_in_bruteforce = self.queue.get()
            try:
                print(hunter.heartbeat(target_domain, domain_in_bruteforce))
            except Exception as e:
                logging.info(e)
            finally:
                self.queue.task_done()


def main():
    print(hunter.get_banner())
    print('Checking Permissions')
    time.sleep(5)
    if not hunter.is_root():
        for i in range(5):
            print("              Este programa precisa ser executado em modo ROOT!!")
        os._exit(0)
    domain_target = hunter.get_user_parameters("Digite seu alvo | (Ex: google.com): ")
    cores_for_parallelism = hunter.get_user_parameters("digite a quantidade de nucleos de processamento para uso de paralelismo | (Ex: 8):")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    wordlist = os.path.join(base_dir, 'dns_bruteforce.txt')

    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    with open(wordlist, "r") as arquivo:
        dns_bruteforce = arquivo.readlines()

    for x in range(int(cores_for_parallelism)):
        worker = HeartBeatWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
        # Put the tasks into the queue as a tuple

    for domain in dns_bruteforce:
        try:
            logger.info('Queueing {}'.format(domain))
            queue.put((domain_target, domain))
        except Exception as e:
            print(e)
    queue.join()
    pass

if __name__ == '__main__':
    main()