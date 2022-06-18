from data import *

fig, ax = subplots(figsize=(11, 8))

suptitle("Пекін, Китай", size=18)
ax.set_title("Вологість", size=14)

days = [datetime.datetime(2022, 5, 26) + datetime.timedelta(days=k) for k in range(6)]
ax.pie(avrg_humid, labels=["{0:.2f}%".format(i) for i in avrg_humid], shadow=True,
       explode=[0.12 if day.weekday() == 5 or day.weekday() == 6 else 0 for day in days])

ax.legend([i.strftime("%A").capitalize() for i in days], bbox_to_anchor=(1.2, 1.0))

show()
