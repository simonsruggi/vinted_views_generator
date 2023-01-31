import threading, requests, time, random, os

print('Please input Vinted link')

vinted_link = input()

lock = threading.Lock()

print('How many threads do you want to run?')

threads = int(input())

ctr = 0

class utils():

    def safe_print(thread_id, arg):

        lock.acquire()

        print("[Thread "+str(thread_id)+"]", arg)

        lock.release()

    def loadproxy():
        
        proxylist = []

        try:

            proxydirectory = os.path.dirname(__file__) + '/proxies.txt'

            with open(proxydirectory,'r') as f:

                tmp = f.read().split('\n')

            for n in range(0, len(tmp)):
                if ':' in tmp[n]:
                    temp = tmp[n]
                    temp = temp.split(':')
                    try:
                        proxie = temp[2] + ':' + temp[3] + '@' + temp[0] + ':' + temp[1]
                    except:
                        proxie = temp[0] + ':' + temp[1]

                    proxylist.append(proxie)

            px = random.choice(proxylist)

            proxy = {
                'http':'http://{}'.format(px),
                'https':'https://{}'.format(px)
            }

            return proxy

        except Exception as e:
            
            return None

class vinted():

    def main(thread_id):

        session = requests.Session()

        session.proxies = utils.loadproxy()

        global ctr

        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }
        while True:
            
            try:

                r = session.get(vinted_link, headers = headers)
                
                if r.status_code == 200:
                    ctr += 1

                    utils.safe_print(thread_id,"Added 1 view to product {} Total views added: {}".format(vinted_link,ctr))
                    
                    time.sleep(1)

                elif r.status_code == 429:

                    utils.safe_print(thread_id,"Ip address rate limited {}".format(vinted_link,ctr))

                    if session.proxies != None:

                        session.proxies = utils.loadproxy() # change proxy if one is rate limited
                    
                    else:

                        time.sleep(5)

                else:
                    
                    utils.safe_print(thread_id,"Error {}".format(r.status_code))

                    time.sleep(3)
            except Exception as e:

                
                utils.safe_print(thread_id,"Request failed, retrying {}".format(r.status_code))

                time.sleep(2)

def runthreads():

    for i in range(0, threads):
        try:
            threading.Thread(target = vinted.main, args=[i,]).start()
        except:
            time.sleep(1)
            pass

runthreads()