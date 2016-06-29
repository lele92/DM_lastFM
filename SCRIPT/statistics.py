import matplotlib.pyplot as plt
import pandas as pd


def histogram(x, y, xlabel=None, ylabel=None, title=None, out=None, highlight=None):
    plt.bar(range(len(x)), y, color='b', alpha=0.6, linewidth=0, align='center')

    # if highlight is not None:
    #     barlist[highlight].set_color('r')
    #     rect = barlist[highlight]
    #     height = rect.get_height()
    #     width = rect.get_width()
    #     plt.text(rect.get_x() + width/2., height+1, "%.2f%%" % float(height), ha='center', va='center')

    plt.xticks(range(len(x)), x, ha='center', va='top', rotation='vertical')
    plt.tick_params(axis='y', labelsize='x-small')
    plt.xlim([-1, len(x)])
    plt.ylim([0, y[0]+((y[0]/100)*10)])
    # plt.axis('auto')
    # plt.title(title)
    plt.gca().yaxis.grid(True)


    if xlabel != None and ylabel != None:
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    if out == None:
        plt.show()
    else:
        plt.savefig("../PLOT/" + out + ".jpg")
        plt.show()


def load_csv(input_filename):
    return pd.read_csv("../OUTPUT/"+input_filename, skipinitialspace=True, delimiter=",", error_bad_lines=False)


def obj_hist(obj, xlabel=None, ylabel=None, title=None, out=None):
    y = []
    for i in obj:
        y.append(i)
    histogram(obj.keys(), y, xlabel, ylabel, title, out)


df = load_csv('prova.csv')
df['track_artist'] = df['track'] + "\n(" + df['artist'] + ")"

# print df.describe()

# genre_count = df['genre'].value_counts()[:10]
# print genre_count
# obj_hist(genre_count, xlabel="Genre", ylabel="count", title="Genre distribution", out='Genre_distribution')
#
# artist_count = df['artist'].value_counts()[:10]
# print artist_count
# obj_hist(artist_count, xlabel="Artist", ylabel="count", title="Artist distribution", out='Artist_distribution')
#
# track_count = df['track_artist'].value_counts()[:10]
# print track_count
# obj_hist(track_count, xlabel="Track", ylabel="count", title="Track distribution", out='Track_distribution')





