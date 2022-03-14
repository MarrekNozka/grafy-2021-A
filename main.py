#!/usr/bin/env python3
# Soubor:  main.py
# Datum:   14.03.2022 08:41
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha: tvorba grafů
########################################################################################
import pylab as pl
from pylab import linspace, pi, plot, sin, cos, show

f = 50  # Hz

# časová osa
t = linspace(0, 50e-3, 300)
# napětí
u = cos(2 * pi * f * t + 0)
# proud
i = cos(2 * pi * f * t + pi / 3)
# výkon
p = u * i

pl.figure(1)
plot(t, u, ":", label=u"elektrické napětí", c="#fe2364")
plot(t, i, "--", label=u"elektrický proud")
plot(t, p, "-", label=u"elektrický výkon", c="green")

pl.grid(True)
pl.legend()
pl.title("Výkon střídavého proudu")
pl.xlabel("t [s]")
pl.ylabel("u [V],i [A], p [W]")

# limity osy x a y
pl.xlim([0, 50e-3])
pl.ylim(-1.1, 2)
pl.ylim()

pl.figure(2)
# dva řádky, jeden sloupec, pořadí 1
pl.subplot(2, 1, 1)
pl.title("řádek 1")
plot(t, u, ":", label=u"elektrické napětí", c="#fe2364")
plot(t, i, "--", label=u"elektrický proud")

# dva řádky, jeden sloupec, pořadí 2
pl.subplot(2, 1, 2)
pl.title("řádek 2222")
plot(t, p, "-", label=u"elektrický výkon", c="green")


pl.show()
