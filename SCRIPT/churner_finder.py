# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def plot_user_tot_and_artist_distribution(g_data, title=None, out=None):
    # print g_data
    # g_data = sorted(g_data.iteritems(), key=lambda (k, v): k)
    x_axis = []
    y_axis_tot = []
    y_axis_artist = []
    genres_label = []
    count = 1
    for key, value in g_data:
        # print str(key)+": "+str(value)
        x_axis.append(count)
        y_axis_tot.append(value['num_ascolti_totali'])
        y_axis_artist.append(value['num_ascolti_artista'])
        genres_label.append(key)
        count += 1

    plt.bar(x_axis, y_axis_tot, align='center', color="b", alpha=0.5)
    plt.bar(x_axis, y_axis_artist, align='center', color="r", alpha=0.5)
    plt.xticks(x_axis, genres_label, rotation='vertical')
    plt.title(title)
    plt.tick_params(axis='x', labelsize=9)
    plt.tick_params(axis='y', labelsize=9)
    plt.xlim([+0, len(x_axis) + 1])
    # plt.ylim([-10, 105])
    plt.gca().yaxis.grid(True)
    if (out):
        plt.savefig(out, bbox_inches="tight")
    # plt.show()
    plt.close()

# se ha < MIN_LISTENINGS_LAST_THREE_WEEK ascolto/i muse nelle ultime 3 settimane =>  churner
# return true => churner
# return false => not churner
def pass_last_three_weeks_test(fan, MIN_LISTENINGS_LAST_THREE_WEEK):
    return fan[-1][1]['num_ascolti_artista'] + fan[-2][1]['num_ascolti_artista'] + fan[-3][1]['num_ascolti_artista'] < MIN_LISTENINGS_LAST_THREE_WEEK

# se ha un buco di almeno 3 settimane dopo l'ultimo ascolto => churner
# return true  => churner
# return false => not churner
def pass_three_week_test(fan):
    return fan[-1][1]['num_ascolti_artista'] + fan[-2][1]['num_ascolti_artista'] + fan[-3][1]['num_ascolti_artista'] == 0


# se ha avuto meno di THRESHOLD_LISTENINGS ascolti nelle ultime 2 settimane di ascolti (presenti nel dataset) => churner
# return true  => churner
# return false => not churner
def pass_less_than_threshold_listenings_last_two_weeks_test(fan, THRESHOLD_LISTENINGS):
    return fan[-1][1]['num_ascolti_artista'] + fan[-2][1]['num_ascolti_artista'] <= THRESHOLD_LISTENINGS


# se ha una quota di ascolti muse (#artist/#totale) < di una certa soglia => NOT churner
# return true  => churner
# return false => not churner
def pass_quota_artist_less_than_threshold(fan, THRESHOLD_QUOTA_TOT):
    sum_ascolti = 0
    sum_ascolti_artista = 0
    for i in fan:
        sum_ascolti += i[1]['num_ascolti_totali']

    for i in fan:
        sum_ascolti_artista += i[1]['num_ascolti_artista']

    # print float(sum_ascolti_artista)/float(sum_ascolti)
    return float(sum_ascolti_artista)/float(sum_ascolti) < THRESHOLD_QUOTA_TOT

# se ha una quota media di ascolti muse nelle ultime due settimane <= di una certa soglia => churner
# return true  => churner
# return false => NOT churner
def pass_last_two_weeks_quota_test(fan, THRESHOLD_QUOTA_TWO_WEEKS):
    # print fan
    ascolti_last = fan[-1][1]['num_ascolti_totali']
    ascolti_artista_last = fan[-1][1]['num_ascolti_artista']
    ascolti_second_last = fan[-2][1]['num_ascolti_totali']
    ascolti_artista_second_last = fan[-2][1]['num_ascolti_artista']

    last_week_quota = float(ascolti_artista_last) / float(ascolti_last)
    second_last_week_quota = float(ascolti_artista_second_last) / float(ascolti_second_last)

    # print last_week_quota
    # print second_last_week_quota
    # print (last_week_quota + second_last_week_quota)/2
    # print (last_week_quota + second_last_week_quota)/2 < THRESHOLD_QUOTA_TWO_WEEKS
    return (last_week_quota + second_last_week_quota)/2 <= THRESHOLD_QUOTA_TWO_WEEKS

# se ha ascoltato l'artista (almeno un ascolto settimanale) >= THRESHOLD_QUOTA_ARTIST_WEEKS delle settimane in cui ha ascoltato in generale => NOT churner
# return true  => NOT churner
# return false => churner
def pass_quota_artist_weeks_test(fan, THRESHOLD_QUOTA_ARTIST_WEEKS):
    weeks_artist_count = 0
    weeks_count = 0
    for i in fan:
        weeks_count += 1
        if int(i[1]['num_ascolti_artista']) > 0:
            weeks_artist_count += 1
        # print i
    # print weeks_count
    # print weeks_artist_count
    # print float(weeks_artist_count)/float(weeks_count)
    return float(weeks_artist_count)/float(weeks_count) >= THRESHOLD_QUOTA_ARTIST_WEEKS

# se ha quota ascolti ultime 3 settimane (somma, non media quote) <= THRESHOLD_QUOTA_LAST_THREE_WEEKS => churner
# return true  => churner
# return false => NOT churner
def pass_less_than_quota_last_three_weeks(fan, THRESHOLD_QUOTA_LAST_THREE_WEEKS):
    sum_ascolti_artista = int(fan[-1][1]['num_ascolti_artista']) + int(fan[-2][1]['num_ascolti_artista']) + int(fan[-3][1]['num_ascolti_artista'])
    sum_ascolti_totali = int(fan[-1][1]['num_ascolti_totali']) + int(fan[-2][1]['num_ascolti_totali']) + int(fan[-3][1]['num_ascolti_totali'])

    return float(sum_ascolti_artista)/float(sum_ascolti_totali) <= THRESHOLD_QUOTA_LAST_THREE_WEEKS
def create_fans_dict(file_ascolti_utenti_costanti_muse, excluded_fans_list):
    fans_dict = {}
    count = 0
    for l in file_ascolti_utenti_costanti_muse:
        if count > 0:  # per saltare la prima riga
            fan_list = l.rstrip().split(',')
            if str(fan_list[0]) not in excluded_fans_list:
                if not str(fan_list[0]) in fans_dict.keys():
                    fans_dict[str(fan_list[0])] = {}

                fans_dict[str(fan_list[0])][str(fan_list[1])] = {
                        'num_ascolti_totali': int(fan_list[2]),
                        'num_ascolti_artista': int(fan_list[3])
                    }
        count += 1

    for fan in fans_dict:
        fans_dict[fan] = sorted(fans_dict[fan].iteritems(), key=lambda (k, v): k)

    return fans_dict


path_ascolti_utenti_costanti_muse = "../OUTPUT/muse/ascolti_utenti_costanti_muse.csv"
path_ascolti_utenti_costanti_muse_churning = "../OUTPUT/muse/ascolti_utenti_costanti_muse_churning.csv"
path_churning_plot = "../PLOT/ChurningPlot/"
path_excluded_fans = "../OUTPUT/muse/wrong_users_muse.txt"

file_ascolti_utenti_costanti_muse = open(path_ascolti_utenti_costanti_muse,'r')
file_churning = open(path_ascolti_utenti_costanti_muse_churning,'w')
file_excluded_fans = open(path_excluded_fans,'r')

MIN_LISTENINGS_LAST_THREE_WEEKS = 3
THRESHOLD_LISTENINGS = 3
THRESHOLD_QUOTA_TOT = 0.10
THRESHOLD_QUOTA_TWO_WEEKS = THRESHOLD_QUOTA_TOT + 0.10 # deve essere maggiore di THRESHOLD_QUOTA_TOT
THRESHOLD_QUOTA_ARTIST_WEEKS = 0.65
THRESHOLD_QUOTA_LAST_THREE_WEEKS = 0.15

excluded_fans_list = []
for l in file_excluded_fans:
    excluded_fans_list.append(str(l.rstrip()))

fans_dict = create_fans_dict(file_ascolti_utenti_costanti_muse, excluded_fans_list)


count = 1
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_e = 0
count_f = 0


file_churning.write("id,churn,reason\n")
# fans = 218 utenti costanti
for fan in fans_dict:
    print str(count) + " ==> " + str(fan)
    count += 1
    churning_level = 0
    fan_str_churner = str(fan) + ",1"       # 1 = churner
    fan_str_not_churner = str(fan) + ",0"    # 0 = not churner

    if pass_three_week_test(fans_dict[fan]):        # se ha un buco di almeno 3 settimane dopo l'ultimo ascolto => churner
        count_a += 1
        plot_user_tot_and_artist_distribution(fans_dict[fan],
                                              title="A - [CHURNER] buco di almeno 3 settimane dopo l'ultimo ascolto",
                                              out=path_churning_plot + str(fan) + ".jpg")
        print "\tA - [CHURNER] buco di almeno 3 settimane dopo l'ultimo ascolto"
        file_churning.write(fan_str_churner+",A - [CHURNER] buco di almeno 3 settimane dopo l'ultimo ascolto\n")
    else:
        if pass_last_three_weeks_test(fans_dict[fan],MIN_LISTENINGS_LAST_THREE_WEEKS):  # se ha < MIN_LISTENINGS_LAST_THREE_WEEKS ascolti muse nelle ultime 3 settimane => churner
            count_b += 1
            plot_user_tot_and_artist_distribution(fans_dict[fan],
                                                  title="B - [CHURNER] ascolto/i artista nelle ultime 3 settimane <" + str(MIN_LISTENINGS_LAST_THREE_WEEKS),
                                                  out=path_churning_plot + str(fan) + ".jpg")
            print "\tB - [CHURNER] ascolto/i artista nelle ultime 3 settimane <" + str(MIN_LISTENINGS_LAST_THREE_WEEKS)  # file_churning.write(fan_str_not_churner)
            file_churning.write(fan_str_churner+",B - [CHURNER] ascolto/i artista nelle ultime 3 settimane <" + str(MIN_LISTENINGS_LAST_THREE_WEEKS)+"\n")
        else:
            if pass_quota_artist_weeks_test(fans_dict[fan], THRESHOLD_QUOTA_ARTIST_WEEKS):   # se ha ascoltato l'artista (almeno un ascolto settimanale) >= THRESHOLD_QUOTA_ARTIST_WEEKS delle settimane in cui ha ascoltato in generale => NOT churner
                count_c += 1
                plot_user_tot_and_artist_distribution(fans_dict[fan],
                                                      title="C - [NOT CHURNER] quota settimane ascolto artista >= "+str(THRESHOLD_QUOTA_ARTIST_WEEKS),
                                                      out=path_churning_plot + str(fan) + ".jpg")
                print "\tC - [NOT CHURNER] quota settimane ascolto artista >= "+str(THRESHOLD_QUOTA_ARTIST_WEEKS)
                file_churning.write(fan_str_not_churner+",C - [NOT CHURNER] quota settimane ascolto artista >= "+str(THRESHOLD_QUOTA_ARTIST_WEEKS)+"\n")
            else:
                if pass_less_than_quota_last_three_weeks(fans_dict[fan], THRESHOLD_QUOTA_LAST_THREE_WEEKS): # se ha quota ascolti ultime 3 settimane <= THRESHOLD_QUOTA_LAST_THREE_WEEKS => churner
                    count_d += 1
                    plot_user_tot_and_artist_distribution(fans_dict[fan],
                                                          title="D - [CHURNER] quota ascolti artista ultime 3 settimane <= " + str(THRESHOLD_QUOTA_LAST_THREE_WEEKS),
                                                          out=path_churning_plot + str(fan) + ".jpg")
                    print "\tD - [CHURNER] quota ascolti artista ultime 3 settimane <= " + str(THRESHOLD_QUOTA_LAST_THREE_WEEKS)
                    file_churning.write(fan_str_churner+",D - [CHURNER] quota ascolti artista ultime 3 settimane <= " + str(THRESHOLD_QUOTA_LAST_THREE_WEEKS)+"\n")
                else:
                    count_e += 1
                    plot_user_tot_and_artist_distribution(fans_dict[fan],
                                                          title="E - [NOT CHURNER] quota ascolti artista ultime 3 settimane > " + str(THRESHOLD_QUOTA_LAST_THREE_WEEKS),
                                                          out=path_churning_plot + str(fan) + ".jpg")
                    print "\tE - [NOT CHURNER] quota ascolti artista ultime 3 settimane > " + str(THRESHOLD_QUOTA_LAST_THREE_WEEKS)
                    file_churning.write(fan_str_not_churner+",E - [NOT CHURNER] quota ascolti artista ultime 3 settimane > " + str(THRESHOLD_QUOTA_LAST_THREE_WEEKS)+"\n")

file_churning.close()

                # if pass_less_than_threshold_listenings_last_two_weeks_test(fans_dict[fan], THRESHOLD_LISTENINGS):   # se ha avuto meno di THRESHOLD_LISTENINGS ascolti nelle ultime 2 settimane di ascolti (presenti nel dataset) => churner
                #     count_c += 1
                #     plot_user_tot_and_artist_distribution(fans_dict[fan],
                #                                           title="C - [CHURNER] meno di "+str(THRESHOLD_LISTENINGS)+" ascolti artista nelle ultime due settimane",
                #                                           out=path_churning_plot + str(fan) + ".jpg")
                #     print "\tC - [CHURNER] meno di "+str(THRESHOLD_LISTENINGS)+" ascolti artista nelle ultime due settimane" # file_churning.write(fan_str_churner)
                # else:
                #     if pass_quota_artist_less_than_threshold(fans_dict[fan], THRESHOLD_QUOTA_TOT) :       # se ha una quota di ascolti muse (#artist/#totale) < di una certa soglia => churner
                #         count_d += 1    #     file_churning.write(fan_str_not_churner)
                #         plot_user_tot_and_artist_distribution(fans_dict[fan],
                #                                               title="D - [CHURNER] quota ascolti artista < "+str(THRESHOLD_QUOTA_TOT),
                #                                               out=path_churning_plot + str(fan) + ".jpg")
                #         print "\tD - [CHURNER] quota ascolti artista < "+str(THRESHOLD_QUOTA_TOT)
                #     else:
                #         if pass_last_two_weeks_quota_test(fans_dict[fan], THRESHOLD_QUOTA_TWO_WEEKS):       # se ha una quota media di ascolti muse nelle ultime due settimane <= di una certa soglia => churner
                #             count_e += 1
                #             plot_user_tot_and_artist_distribution(fans_dict[fan],
                #                                                   title="E - [CHURNER] quota ascolti artista ultime due settimane <= "+str(THRESHOLD_QUOTA_TWO_WEEKS),
                #                                                   out=path_churning_plot + str(fan) + ".jpg")
                #             print "\tE - [CHURNER] quota ascolti artista ultime due settimane <= "+str(THRESHOLD_QUOTA_TWO_WEEKS)  # file_churning.write(fan_str_churner)
                #         else:               # se ha una quota media di ascolti muse nelle ultime due settimane >= di una certa soglia => NOT churner
                #             count_f += 1
                #             plot_user_tot_and_artist_distribution(fans_dict[fan],
                #                                                   title="F - [NOT CHURNER] quota ascolti artista ultime due settimane >= " + str(THRESHOLD_QUOTA_TWO_WEEKS),
                #                                                   out=path_churning_plot + str(fan) + ".jpg")
                #             print "\tF - [NOT CHURNER] quota ascolti artista ultime due settimane >= " + str(THRESHOLD_QUOTA_TWO_WEEKS)
                #             # file_churning.write(fan_str_not_churner)


print "\nA - [CHURNER] buco di almeno 3 settimane dopo l'ultimo ascolto: " + str(count_a)
print "B - [CHURNER] ascolto/i artista nelle ultime 3 settimane <" + str(MIN_LISTENINGS_LAST_THREE_WEEKS) + ": "+ str(count_b)
print "C - [NOT CHURNER] quota settimane ascolto artista >= "+str(THRESHOLD_QUOTA_ARTIST_WEEKS) + ": "+ str(count_c)
print "D - [CHURNER] quota ascolti artista ultime 3 settimane <= " + str(THRESHOLD_QUOTA_LAST_THREE_WEEKS) + ": "+ str(count_d)
print "E - [NOT CHURNER] quota ascolti artista ultime 3 settimane > " + str(THRESHOLD_QUOTA_LAST_THREE_WEEKS) + ": "+ str(count_e)
print "tot: " + str(count_a + count_b + count_c + count_d + count_e)