from data import *

fig, ax = subplots(figsize=(11, 8))

title("Пекін, Китай", size=18, loc="left")

ax.set_xlabel("Дата", size=18)
ax.set_ylabel("Швидкість повітря (м/с)", size=18)

ax.xaxis.set_minor_locator(HourLocator(byhour=[2, 5, 8, 11, 14, 17, 20, 23]))
ax.xaxis.set_minor_formatter(DateFormatter("%H:%M"))
ax.tick_params(axis='x', which='minor', labelsize=7, rotation=80)
ax.tick_params(axis='x', which='major', labelsize=10, rotation=0, pad=30)

ax.axis([dates[0] - datetime.timedelta(hours=2),
         dates[len(dates) - 1] + datetime.timedelta(hours=2),
         0, 12])

ax.grid(axis="x", which="major", linewidth=0.8)

bar(dates, [x for sub in wind_speed for x in sub], width=0.11)

show()
