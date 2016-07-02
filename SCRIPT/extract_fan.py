
path_utenti_costanti = "../OUTPUT/muse/utenti_costanti.csv"
path_ascolti_muse = "../OUTPUT/muse/user_listenings_distribution_muse.csv"
path_ascolti_utenti_costanti_muse = "../OUTPUT/muse/ascolti_utenti_costanti_muse.csv"

file_utenti_costanti = open(path_utenti_costanti,'r')
file_ascolti_muse = open(path_ascolti_muse,'r')
file_ascolti_utenti_costanti_muse = open(path_ascolti_utenti_costanti_muse,'w')

artist_fans = []                # utenti costanti
artist_listeners = []           # utenti che hanno ascoltato muse almeno 10 volte

for l in file_utenti_costanti:
    artist_fans.append(l.rstrip())

file_utenti_costanti.close()

count = 0
file_ascolti_utenti_costanti_muse.write(file_ascolti_muse.readline())

for l in file_ascolti_muse:
    if count > 0:   # per saltare la prima riga
        record_list = l.rstrip().split(',')
        # print record_list
        if record_list[0] in artist_fans:
            file_ascolti_utenti_costanti_muse.write(l)
    count += 1

file_ascolti_muse.close()
file_ascolti_utenti_costanti_muse.close()