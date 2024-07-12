from matplotlib_venn import venn3_unweighted, venn3_circles
import matplotlib.pyplot as plt

# Define set sizes
total = 121
set1 = 5
set2 = 0
set3 = 23
intersection12 = 1
intersection13 = 29
intersection23 = 10
intersection123 = 52

sets = (set1, set2, intersection12, set3, intersection13, intersection23, intersection123)


v = venn3_unweighted(subsets=sets, set_labels=('ASP', 'CIM', 'Capsaicin'), set_colors=('g', 'b', 'r'), alpha=0.4, subset_label_formatter=lambda x: str(x) + "\n" + f"{(x/total):1.0%}")
c = venn3_circles(subsets=(1,1,1,1,1,1,1), linestyle='dashed', linewidth=1, color="black", alpha=1.0)

#plt.title('C-stimulation responding Boutons', fontname='')
plt.show()
#plt.savefig(f'plot_venn_C_boutons.png')
