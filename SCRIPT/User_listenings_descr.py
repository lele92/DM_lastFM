import pandas as pd
import time
import datetime
import matplotlib.pyplot as plt
from collections import Counter
import random

def load_csv(input_filename):
    return pd.read_csv("../OUTPUT/"+input_filename, skipinitialspace=True, delimiter=",", error_bad_lines=False)

def to_millis(date_str):
    return time.mktime(datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").timetuple())

def to_year_week(date_str):
    date_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    week_str = str(date_time.isocalendar()[1])
    if len(week_str) == 1:
        week_str = "0"+week_str

    return str(date_time.strftime("%Y")) + "/" + week_str


def create_user_listenings_descr(user_listenings_millis):
    out_file = open("../OUTPUT/user_listenings_descr.csv", "w")
    out_file.write("user_id,first_listening,last_listening,time_span,time_span_days\n")

    for key in user_listenings_millis:
        time_span = user_listenings_millis[key][-1] - user_listenings_millis[key][0]
        time_span_days = int(time_span / 86400)
        out_file.write(str(key) + "," + str(user_listenings_millis[key][0]) + "," + str(
            user_listenings_millis[key][-1]) + "," + str(time_span) + "," + str(time_span_days) + "\n")

    out_file.close()

def plot_user_distribution(g_data, out=None):
    print g_data
    g_data = sorted(g_data.iteritems(), key=lambda (k, v): k)
    x_axis = []
    y_axis = []
    genres_label = []
    count = 1
    for key, value in g_data:
        x_axis.append(count)
        y_axis.append(value)
        genres_label.append(key)
        count += 1

    plt.bar(x_axis, y_axis, align='center', color="b", alpha=0.5)
    plt.xticks(x_axis, genres_label, rotation='vertical')
    # plt.title(title)
    plt.tick_params(axis='x', labelsize=9)
    plt.tick_params(axis='y', labelsize=9)
    plt.xlim([+0, len(x_axis)+1])
    # plt.ylim([-10, 105])
    plt.gca().yaxis.grid(True)
    if (out):
        plt.savefig(out, bbox_inches="tight")
    plt.show()

def create_user_listenings_week_count(user_listenings_week):
    out_file = open("../OUTPUT/user_listenings_week_count.csv", "w")
    out_file.write("user_id,week_year,listening_count\n")
    user_listenings_week_count = {}
    for user in user_listenings_week:
        user_week_listenings_list = user_listenings_week[user]
        user_listenings_week_count[user] = dict(Counter(user_week_listenings_list))
        # per scrivere su file le triple user,week,count
        dict_user = sorted(user_listenings_week_count[user].iteritems(), key=lambda (k, v): k)
        for week,value in dict_user:
            out_file.write(str(user)+","+str(week)+","+str(value)+"\n")
    out_file.close()

def load_listenings_genre_merged():
    # 1.leggere CSV e caricare in dataframe
    df = load_csv('listenings_genre_merged.csv')

    # 2.groupby e conversione in millis
    grouped_users = df.groupby('user_id')   # groupBy per user_id
    user_listenings_millis = {}
    user_listenings_week = {}


    # per ogni utente (user_id) nel dataframe groupBy, aggiungo all'oggetto user_obj una lista del tipo: user_id:lista ordinata (dal primo all'ultimo) degli ascolti in millis
    # tot_sum = 0
    for key, row in grouped_users:
        user_listenings_millis[key] = sorted([to_millis(date) for date in row['date']])
        user_listenings_week[key] = sorted([to_year_week(date) for date in row['date']])
        # tot_sum += len(user_listenings_millis[key])
    # print tot_sum

    return user_listenings_millis,user_listenings_week


def load_user_listenings_week_count():
    user_listenings_week_count = {}
    df = load_csv("user_listenings_week_count.csv")
    grouped_users = df.groupby('user_id')
    for key, user_week in grouped_users:
        user_listenings_week_count[key] = {}
        user_dict = {}
        for index,row in user_week.iterrows():
            user_dict[row['week_year']] = int(row['listening_count'])
        user_listenings_week_count[key] = dict(sorted(user_dict.iteritems(), key=lambda (k, v): k))
    return user_listenings_week_count


def plot_random_user_listenings_week_count(user_listenings_week_count):
    random_user_list = []
    for i in range(50):
        random_user_list.append(random.choice(user_listenings_week_count.keys()))

    for i in random_user_list:
        print sum(user_listenings_week_count[i].values())
        plot_user_distribution(user_listenings_week_count[i], out="../PLOT/RandomUserPlots/" + str(i) + ".jpg")


# user_listenings_millis, user_listenings_week = load_listenings_genre_merged()

# create_user_listenings_descr(user_listenings_millis)

# create_user_listenings_week_count(user_listenings_week)

# user_listenings_week_count = load_user_listenings_week_count()
# print user_listenings_week_count['epic_discord']

# plot_random_user_listenings_week_count(user_listenings_week_count)