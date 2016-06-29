__author__ = 'Trappola'


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import datetime
import pandas as pd
import matplotlib.pyplot as plt


def plot_user_distribution(g_data, out):
    g_data = sorted(g_data.iteritems(), key=lambda (k, v): k)[-14:]
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
    plt.savefig(out, bbox_inches="tight")
    plt.show()


def extraxt_year_from_string_date(string_date):
    print string_date
    date_object = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")
    print date_object.millis
    sys.exit()


def load_csv(input_filename):
    return pd.read_csv("../OUTPUT/"+input_filename, skipinitialspace=True, delimiter=",", error_bad_lines=False)


# 8 Describe
df = load_csv("listenings_genre_merged.csv")
# print df.describe()
groupby = df.groupby(df['user_id'])
# for name, group in groupby:
    # print str(name) + " " + str(len(group))
    # if name == "000Silenced":
    #     print str(name) + " " + str(len(group))


# df = load_csv("prova.csv")
# df['datetime'] = pd.to_datetime(df['date'])
# df['year'], df['month'], df['week'] = df['datetime'].dt.year, df['datetime'].dt.month, df['datetime'].dt.week
# # df['year_true'] = df['year'].map(lambda x: (x.year-2005)*53 + x.isocalendar()[1])
# # print df
# groupby = df.groupby(df['year'])
# # groupby = df.groupby(df['year']).map(lambda x: (x.year-2005)*53 + x.isocalendar()[1]))
# # # print groupby.describe()
# #
# # #
# year_dict = {}
# # # out_year_frequency = open("../OUTPUT/year_frequency.csv", "w")
# for name, group in groupby:
#     # print str(name) + " " + str(len(group))
#     print group
#     year_dict[int(name)] = len(group)
#     for index, row in group.iterrows():
#         print index
#         print row["artist"]
#         # print cazzo
#         sys.exit()
#     # res = "%s,%s\n" % (name, len(group))
#     # out_year_frequency.write("%s" % res.encode('utf-8'))
# # out_year_frequency.close()
# print year_dict
# # # # print sorted(year_dict.iteritems(), key=lambda (k, v): k)[-1:]
# # # plot_user_distribution(year_dict, "../PLOT/time_listenings_distribution_v2.jpg")
