import matplotlib.pyplot as plt
import numpy as np

# 1. Tidslinje (X-aksen)
aar = ['-3', '-2', '-1', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 2. Dine præcise data i DKK (Y-aksen)
plwh_dkk = [23764, 26430, 49216, 110661, 47663, 44273, 40033, 45102, 49283, 46625, 43855, 41981]
non_hiv_dkk = [10885, 12058, 13991, 14342, 14402, 16306, 15709, 15447, 15007, 17269, 15096, 16380]

# 3. Opsæt grafens størrelse og kvalitet (dpi)
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
x = np.arange(len(aar))

# 4. Tegn linjerne (Rød for HIV/PLWH, Blå for Kontrolgruppe/Non-HIV) med lagstyring (zorder)
ax.plot(x, plwh_dkk, marker='o', linewidth=2.5, color='#d62728', label='Hiv-smittede (PLWH)', zorder=3)
ax.plot(x, non_hiv_dkk, marker='s', linewidth=2.5, color='#1f77b4', label='Kontrolgruppe (Non-HIV)', zorder=3)

# 5. Indsæt den stiplede lodrette linje for diagnosetidspunktet
ax.axvline(x=2.5, color='#7f7f7f', linestyle='--', linewidth=1.5, zorder=2)

# FORBEDRING: Rykket en smule ned (y=95000), så den ikke støder ind i signaturforklaringen
ax.text(2.6, 95000, 'Diagnose / Match tidspunkt', color='#555555', fontsize=9.5, fontweight='bold',
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.85, pad=2))

# 6. Titler og aksetekster
ax.set_title('Gennemsnitlige årlige samlede omkostninger per person (DKK)', fontsize=13, fontweight='bold', pad=18)
ax.set_xlabel('År før og efter hiv-diagnose / match', fontsize=11, labelpad=10)
ax.set_ylabel('Omkostninger i danske kroner (kr.)', fontsize=11, labelpad=10)

# 7. Finpudsning af akser, grid og layout
ax.set_xticks(x)
ax.set_xticklabels(aar)

# FORBEDRING: Ændret bunden til 0, så den blå linje ikke klemmer sig helt ned i bunden
ax.set_ylim(0, 130000)

# FORBEDRING: Tilføjer tusindtalsseparator (f.eks. 100.000 i stedet for 100000) med dansk punktum
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)).replace(",", ".")))

# FORBEDRING: Fjern top- og højre-rammen for det åbne, moderne look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')

ax.grid(True, linestyle=':', alpha=0.5, zorder=1)
ax.legend(fontsize=10.5, loc='upper left', frameon=True, facecolor='white', edgecolor='#e5e5e5')

# Sikrer at intet bliver skåret af i kanten, når grafen gemmes
plt.tight_layout()
plt.show()
