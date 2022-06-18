from data import *

fig, ax = subplots(figsize=(11, 7))

title("Пекін, Китай", size=18, loc="left")

ax.set_xlabel("Дата", size=18)
ax.set_ylabel("Температура (°C)", size=18)

ax.xaxis.set_minor_locator(HourLocator(byhour=[2, 8, 14, 20]))
ax.xaxis.set_minor_formatter(DateFormatter("%H:%M"))
ax.tick_params(axis='x', which='minor', labelsize=7, rotation=20)
ax.tick_params(axis='x', which='major', labelsize=10, rotation=0, pad=20)

ax.axis([dates[0] - datetime.timedelta(hours=2),
         dates[len(dates)-1] + datetime.timedelta(hours=2),
         20, 41])

ax.plot(dates, [x for sub in temperature for x in sub], "r-", label="Реальна")
ax.plot(dates, [x for sub in real_feel_temp for x in sub], "g--", label="Як відчувається")

ax.grid(which='major', linewidth=0.8)
ax.grid(which='minor', linestyle=':', linewidth=0.5)

ax.legend()

show()
