from data import *

fig, [ax1, ax2] = subplots(2, 1, figsize=(11, 14))
fig.tight_layout(pad=4)

suptitle("Пекін, Китай", size=18)

# === AX1 ===

ax1.set_xlabel("Дата", size=18)
ax1.set_ylabel("Температура (°C)", size=18)

ax1.xaxis.set_minor_locator(HourLocator(byhour=[2, 8, 14, 20]))
ax1.xaxis.set_minor_formatter(DateFormatter("%H:%M"))
ax1.tick_params(axis='x', which='minor', labelsize=7, rotation=20)
ax1.tick_params(axis='x', which='major', labelsize=10, rotation=0, pad=20)

ax1.axis([dates[0] - datetime.timedelta(hours=2),
         dates[len(dates) - 1] + datetime.timedelta(hours=2),
         20, 41])

ax1.plot(dates, [x for sub in temperature for x in sub], "r-", label="Реальна")

ax1.grid(which='major', linewidth=0.8)
ax1.grid(which='minor', linestyle=':', linewidth=0.5)

ax1.legend()

# === AX2 ===

ax2.set_xlabel("Дата", size=18)
ax2.set_ylabel("Температура (°C)", size=18)

ax2.xaxis.set_minor_locator(HourLocator(byhour=[2, 8, 14, 20]))
ax2.xaxis.set_minor_formatter(DateFormatter("%H:%M"))
ax2.tick_params(axis='x', which='minor', labelsize=7, rotation=20)
ax2.tick_params(axis='x', which='major', labelsize=10, rotation=0, pad=20)

ax2.axis([dates[0] - datetime.timedelta(hours=2),
          dates[len(dates) - 1] + datetime.timedelta(hours=2),
          20, 41])

ax2.plot(dates, [x for sub in real_feel_temp for x in sub], "g--", label="Як відчувається")

ax2.grid(which='major', linewidth=0.8)
ax2.grid(which='minor', linestyle=':', linewidth=0.5)

ax2.legend()

show()
