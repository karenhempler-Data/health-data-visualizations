import matplotlib.pyplot as plt
import numpy as np

# 1. Tidslinje (X-aksen)
aar = ['-3', '-2', '-1', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 2. Dine data i DKK (Y-aksen)
plwh_dkk = [9624, 15395, 8235, 11528, 3494, 3554, 4965, 9265, 6473, 8496, 14148, 17881]
non_hiv_dkk = [1254, 2232, 2494, 2337, 2038, 2867, 3128, 1777, 1762, 1956, 1613, 3046]

# 3. Opsæt grafens størrelse og kvalitet (dpi)
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
x = np.arange(len(aar))

# 4. Tegn linjerne (Rød for HIV/PLWH, Blå for Kontrolgruppe/Non-HIV)
ax.plot(x, plwh_dkk, marker='o', linewidth=2.5, color='#d62728', label='Hiv-smittede (PLWH)', zorder=3)
ax.plot(x, non_hiv_dkk, marker='s', linewidth=2.5, color='#1f77b4', label='Kontrolgruppe (Non-HIV)', zorder=3)

# 5. Indsæt den stiplede lodrette linje for diagnosetidspunktet
ax.axvline(x=2.5, color='#7f7f7f', linestyle='--', linewidth=1.5, zorder=2)

# Tekst placeret pænt over linjerne med en hvid baggrundsboks for at undgå overlap
ax.text(2.6, 16800, 'Diagnose / Match tidspunkt', color='#555555', fontsize=9.5, fontweight='bold',
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.85, pad=2))

# 6. Titler og aksetekster
ax.set_title('Gennemsnitlige årlige psykiatriomkostninger per person (DKK)', fontsize=13, fontweight='bold', pad=18)
ax.set_xlabel('År før og efter hiv-diagnose / match', fontsize=11, labelpad=10)
ax.set_ylabel('Omkostninger i danske kroner (kr.)', fontsize=11, labelpad=10)

# 7. Finpudsning af akser, grid og layout
ax.set_xticks(x)
ax.set_xticklabels(aar)
ax.set_ylim(0, 20000)

# Fjern top- og højre-rammen for et mere rent og professionelt udtryk
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Gør de resterende rammer lidt mere afdæmpede i farven
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')

ax.grid(True, linestyle=':', alpha=0.5, zorder=1)
ax.legend(fontsize=10.5, loc='upper left', frameon=True, facecolor='white', edgecolor='#e5e5e5')

# Sikrer at intet bliver skåret af i kanten, når grafen gemmes
plt.tight_layout()
plt.show()
