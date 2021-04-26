import speedtest
import csv

servers = [14612]
#https://help.speedtest.net/hc/en-us/articles/360038679354-How-does-Speedtest-measure-my-network-speeds
threads = 16

s = speedtest.Speedtest()

try:
    s.get_servers(servers)
except:
    s.get_closest_servers()
    s.get_best_server()

s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()
#print(results_dict)

arquivo_relatorio = 'speedtest.csv'

try:
    file = open(arquivo_relatorio, 'x', encoding='UTF8')
    file.close()
    
    with open(arquivo_relatorio, 'w', newline='', encoding='UTF8') as f:
        w = csv.DictWriter(f, results_dict.keys())
        w.writeheader()
        w.writerow(results_dict)
    
except IOError:
    with open(arquivo_relatorio, 'a', newline='', encoding='UTF8') as f:
        w = csv.DictWriter(f, results_dict.keys())
        w.writerow(results_dict)
