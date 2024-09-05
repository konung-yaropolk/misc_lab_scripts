from matplotlib_venn import venn3, venn3_unweighted, venn3_circles
import matplotlib.pyplot as plt
import os

# Define set sizes
total = 58
set1 = 12
set2 = 1
set3 = 3
intersection12 = 7
intersection13 = 6
intersection23 = 4
intersection123 = 18


OUTPUT = 'venn_demo.svg'
SCALED = True
PARAMS = {

'subsets': (set1, set2, intersection12, set3, intersection13, intersection23, intersection123),
'set_labels': ('ASP 7663', 'CIM 0216', 'Capsaicin'),
'set_colors': ('g', 'b', 'r'),
'alpha': 0.4,
'subset_label_formatter': lambda x: str(x) + "\n" + f"{(x/total):1.0%}",

}





if SCALED:
    v = venn3(**PARAMS)
else:
    PARAMS['subsets'] = (1,1,1,1,1,1,1)    # for unweighted diagram mode
    v = venn3_unweighted(**PARAMS)
c = venn3_circles(subsets=PARAMS['subsets'], linestyle='--', linewidth=1, color="black", alpha=1.0)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, OUTPUT)
print('Saved as: ', file_path)

#plt.title('Your Title', fontname='')
plt.savefig(file_path)
plt.show()
