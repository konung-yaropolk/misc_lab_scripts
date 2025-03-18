import random
from math import comb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.colors as color


class Helpers():

    def colors_to_rgba(self, colors, alpha=0.35):
        rgba_colors = []
        for col in colors:
            rgba = list(mcolors.to_rgba(col))
            rgba[3] = alpha
            rgba_colors.append(tuple(rgba))
        return rgba_colors

    def get_colors(self):
        # If a colormap is provided, use it; else generate one with n_groups colors.
        if self.colormap:
            colors_edge = [c if color.is_color_like(
                c) else 'k' for c in self.colormap]
            colors_fill = self.colors_to_rgba(colors_edge)
        else:
            n_colors = 9  # len(self.data_groups)
            cmap = plt.get_cmap('Set1')
            colors_edge = [cmap(i / n_colors) for i in range(n_colors)]
            colors_edge.insert(0, 'k')
            colors_fill = self.colors_to_rgba(colors_edge)
        return colors_edge, colors_fill

    def make_p_value_printed(self, p) -> str:
        if p is not None:
            if p > 0.99:
                return 'p>0.99'
            elif p >= 0.01:
                return f'p={p:.2g}'
            elif p >= 0.001:
                return f'p={p:.2g}'
            elif p >= 0.0001:
                return f'p={p:.1g}'
            elif p < 0.0001:
                return 'p<0.0001'
            else:
                return 'N/A'
        return 'N/A'

    def make_stars(self, p) -> int:
        if p is not None:
            if p < 0.0001:
                return 4
            if p < 0.001:
                return 3
            elif p < 0.01:
                return 2
            elif p < 0.05:
                return 1
            else:
                return 0
        return 0

    def make_stars_printed(self, n) -> str:
        return '*' * n if n else 'ns'

    def transpose(self, data):
        return list(map(list, zip(*data)))


class BaseStatPlot(Helpers):

    def __init__(self,
                 data_groups,
                 p=1,
                 testname='',
                 dependent=False,
                 plot_title='',
                 x_label='',
                 y_label='',
                 print_x_labels=True,
                 x_manual_tick_labels=None,
                 posthoc_matrix=[],
                 colormap=None,
                 **kwargs):
        self.data_groups = data_groups
        self.n_groups = len(self.data_groups)
        self.p = p
        self.testname = testname
        self.posthoc_matrix = posthoc_matrix
        self.n_significance_bars = 1
        self.dependent = dependent
        self.plot_title = plot_title
        self.x_label = x_label
        self.y_label = y_label
        self.print_x_labels = print_x_labels

        #  sd sem mean and median calculation if they are not provided
        self.mean = [
            np.mean(self.data_groups[i]).item() for i in range(self.n_groups)]
        self.median = [
            np.median(self.data_groups[i]).item() for i in range(self.n_groups)]
        self.sd = [
            np.std(self.data_groups[i]).item() for i in range(self.n_groups)]
        self.sem = [np.std(self.data_groups[i]).item() / np.sqrt(len(self.data_groups[i])).item()
                    for i in range(self.n_groups)]

        self.n = [len(i) for i in self.data_groups]
        self.p_printed = self.make_p_value_printed(self.p)
        self.stars_printed = self.make_stars_printed(self.make_stars(self.p))

        self.x_manual_tick_labels = x_manual_tick_labels if x_manual_tick_labels is not None else [
            '']

        self.colormap = colormap if colormap is not None and colormap != [
            ''] else []
        self.colors_edge, self.colors_fill = self.get_colors()

        self.y_max = max([max(data) for data in self.data_groups])

    def setup_figure(self, ):
        fig, ax = plt.subplots(figsize=(0.5 + 0.9 * self.n_groups, 4))
        return fig, ax

    def add_scatter(self, ax,
                    color='k',
                    alpha=0.5,
                    marker='o',
                    linewidth=1,
                    zorder=1):
        # Generate x jitter pool.
        spread_pool = []  # storing x positions of data points
        for i, data in enumerate(self.data_groups):
            spread = tuple(random.uniform(-.10, .10) for _ in data)
            spread_pool.append(tuple(i + s for s in spread))

        for i, data in enumerate(self.transpose(self.data_groups)):
            # Plot individual data points with x jitter.
            ax.plot(self.transpose(spread_pool)[i], data,
                    color=color,
                    alpha=alpha,
                    marker=marker,
                    linewidth=linewidth,
                    # Connect the data points if desired.
                    linestyle='-' if self.dependent else '',
                    zorder=zorder)

    def add_errorbar_sd(self, ax, x,
                        capsize=8,
                        ecolor='r',
                        linewidth=2,
                        zorder=3):
        # Add error bars
        ax.errorbar(x, self.mean[x],
                    yerr=self.sd[x],
                    fmt='none',
                    capsize=capsize,
                    ecolor=ecolor,
                    linewidth=linewidth,
                    zorder=zorder)

    def add_errorbar_sem(self, ax, x,
                         capsize=8,
                         ecolor='r',
                         linewidth=2,
                         zorder=3):
        # Add error bars
        ax.errorbar(x, self.mean[x],
                    yerr=self.sem[x],
                    fmt='none',
                    capsize=capsize,
                    ecolor=ecolor,
                    linewidth=linewidth,
                    zorder=zorder)

    def add_mean_marker(self, ax, x,
                        marker='_',
                        markerfacecolor='#00000000',
                        markeredgecolor='r',
                        markersize=16,
                        markeredgewidth=1):
        # Overlay mean marker
        ax.plot(x, self.mean[x],
                marker=marker,
                markerfacecolor=markerfacecolor,
                markeredgecolor=markeredgecolor,
                markersize=markersize,
                markeredgewidth=markeredgewidth)

    def add_median_marker(self, ax, x,
                          marker='x',
                          markerfacecolor='#00000000',
                          markeredgecolor='r',
                          markersize=10,
                          markeredgewidth=1):
        # Overlay median marker
        ax.plot(x, self.median[x],
                marker=marker,
                markerfacecolor=markerfacecolor,
                markeredgecolor=markeredgecolor,
                markersize=markersize,
                markeredgewidth=markeredgewidth)

    def axes_formatting(self, ax, linewidth=2):
        # Remove all spines except left.
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.spines['left'].set_visible(True)
        ax.xaxis.set_visible(bool(self.x_label or self.print_x_labels))
        plt.tight_layout()

        # Set x ticks and labels.
        if self.print_x_labels:
            plt.subplots_adjust(bottom=0.11)
            if self.x_manual_tick_labels != ['']:
                ax.set_xticks(range(self.n_groups))
                ax.set_xticklabels([self.x_manual_tick_labels[i % len(self.x_manual_tick_labels)]
                                    for i in range(self.n_groups)])
            else:
                ax.set_xticks(range(self.n_groups))
                ax.set_xticklabels(['Group {}'.format(i + 1)
                                   for i in range(self.n_groups)], fontweight='regular', fontsize=8)
        else:
            plt.subplots_adjust(bottom=0.08)
            ax.tick_params(axis='x', which='both',
                           labeltop=False, labelbottom=False)

        # Additional formatting.
        for ytick in ax.get_yticklabels():
            ytick.set_fontweight('bold')
        ax.tick_params(width=linewidth)
        ax.xaxis.set_tick_params(labelsize=10)
        ax.yaxis.set_tick_params(labelsize=12)
        ax.spines['left'].set_linewidth(linewidth)
        ax.tick_params(axis='y', which='both',
                       length=linewidth * 2, width=linewidth)
        ax.tick_params(axis='x', which='both', length=0)

    def add_significance_bars(self, ax, linewidth=2, capsize=0.01, col='k', label=''):
        '''label can be "p", "s", "both"'''

        self.n_significance_bars = comb(
            self.n_groups, 2) if self.n_groups > 2 else 1
        posthoc_matrix_printed = [[self.make_p_value_printed(element) for element in row]
                                  for row in self.posthoc_matrix] if self.posthoc_matrix else []
        posthoc_matrix_stars = [[self.make_stars_printed(self.make_stars(element)) for element in row]
                                for row in self.posthoc_matrix] if self.posthoc_matrix else []

        def draw_bar(p, stars, order=0, x1=0, x2=self.n_groups-1, capsize=capsize, linewidth=linewidth, col=col, label=label):
            if label == 'p':
                vspace = capsize+0.03
                label = '{}'.format(p)
            elif label == 's':
                vspace = capsize+0.03
                label = '{}'.format(stars)
            else:
                vspace = capsize+0.06
                label = '{}\n{}'.format(p, stars)

            # Draw significance bar connecting first and last group.
            y, h = ((1.05 + (order*vspace)) *
                    self.y_max), capsize * self.y_max
            ax.plot([x1, x1, x2, x2], [y, y + h, y + h, y],
                    lw=linewidth, c=col)

            ax.text((x1 + x2) * 0.5, y + h, label,
                    ha='center', va='bottom', color=col, fontweight='bold', fontsize=8)

        def bar(x1, x2, o):
            draw_bar(
                posthoc_matrix_printed[x1][x2], posthoc_matrix_stars[x1][x2], order=o, x1=x1, x2=x2)

        # def generate_pairs(matrix_len):
        #     count = 0
        #     for i in range(matrix_len):
        #         for j in range(i + 1, matrix_len):
        #             bar(i, j, count)
        #             count += i + j + 1

        # matrix_length = len(self.posthoc_matrix)
        # generate_pairs(matrix_length)

        # for i in range(len(self.data_groups)):
        #     for j in range(len(self.data_groups)):
        #         bar(j, 1, 0)

        if not self.posthoc_matrix:
            draw_bar(self.p_printed, self.stars_printed)
        elif len(self.posthoc_matrix) == 3:
            bar(0, 1, 0)
            bar(1, 2, 1)
            bar(0, 2, 3)
        elif len(self.posthoc_matrix) == 4:
            bar(0, 1, 0)
            bar(2, 3, 0)
            bar(1, 2, 1)

            bar(0, 2, 3)
            bar(1, 3, 5)

            bar(0, 3, 7)

        elif len(self.posthoc_matrix) == 5:

            bar(0, 1, 0)
            bar(2, 3, 0)
            bar(1, 2, 1)
            bar(3, 4, 1)

            bar(0, 2, 4)
            bar(2, 4, 5)
            bar(1, 3, 8)

            bar(0, 3, 11)
            bar(1, 4, 14)

            bar(0, 4, 17)

        else:
            draw_bar(self.p_printed, self.stars_printed)

    def add_titles_and_labels(self, fig, ax):
        if self.plot_title:
            ax.set_title(self.plot_title, fontsize=12, fontweight='bold')
        if self.x_label:
            ax.set_xlabel(self.x_label, fontsize=10, fontweight='bold')
        if self.y_label:
            ax.set_ylabel(self.y_label, fontsize=10, fontweight='bold')
        fig.text(0.95, 0.0,
                 '{}\nn={}'.format(self.testname,
                                   str(self.n)[1:-1] if not self.dependent else str(self.n[0])),
                 ha='right', va='bottom', fontsize=8, fontweight='regular')

    def show(self):
        plt.show()

    def save(self, path):
        plt.savefig(path)

    def plot(self):
        # Abstract method—each subclass must implement its own plot method.
        raise NotImplementedError(
            "Please implement the plot() method in the subclass.")


class BarStatPlot(BaseStatPlot):
    def plot(self):
        fig, ax = self.setup_figure()
        linewidth = 2

        for x, data in enumerate(self.data_groups):

            # Plot bar for mean with standard deviation error bars.
            ax.bar(x, self.mean[x],
                   width=0.75,
                   edgecolor=self.colors_edge[x % len(self.colors_edge)],
                   facecolor=self.colors_fill[x % len(self.colors_fill)],
                   fill=True,
                   linewidth=linewidth,
                   zorder=1)

            # Overlay errbars, and markers.
            self.add_median_marker(ax, x)
            self.add_mean_marker(ax, x)
            self.add_errorbar_sd(ax, x)

        self.add_scatter(ax)
        self.add_significance_bars(ax, linewidth)
        self.add_titles_and_labels(fig, ax)
        self.axes_formatting(ax, linewidth)


class ViolinStatPlot(BaseStatPlot):
    '''
        Violin plot, for adjusting see
        https://matplotlib.org/stable/gallery/statistics/customized_violin.html#sphx-glr-gallery-statistics-customized-violin-py
        https://medium.com/@mohammadaryayi/anything-about-violin-plots-in-matplotlib-ffd58a62bbb5

        Kernel Density Estimation (violin shape prediction approach)
        https://scikit-learn.org/stable/modules/density.html
    '''

    def plot(self):
        fig, ax = self.setup_figure()
        linewidth = 2

        for x, data in enumerate(self.data_groups):

            # Create a violin plot for this group.
            vp = ax.violinplot(data, positions=[x], widths=0.85, vert=True,
                               showmeans=True, showmedians=True, showextrema=True,
                               points=200, bw_method=0.1)
            for pc in vp['bodies']:
                pc.set_facecolor(self.colors_fill[x % len(self.colors_fill)])
                pc.set_edgecolor(self.colors_edge[x % len(self.colors_edge)])
                pc.set_linewidth(linewidth)

            # Overlay errbars, scatter and markers.
            self.add_median_marker(ax, x)
            self.add_mean_marker(ax, x)
            # self.add_errorbar_sd(ax, x)

        self.add_scatter(ax)
        self.add_significance_bars(ax, linewidth)
        self.add_titles_and_labels(fig, ax)
        self.axes_formatting(ax, linewidth)


class ScatterStatPlot(BaseStatPlot):
    def plot(self):
        fig, ax = self.setup_figure()
        linewidth = 2

        for x, data in enumerate(self.data_groups):

            # Overlay errbars, and markers.
            self.add_median_marker(ax, x)
            self.add_mean_marker(ax, x)
            self.add_errorbar_sd(ax, x)

        self.add_scatter(ax)
        self.add_significance_bars(ax, linewidth)
        self.add_titles_and_labels(fig, ax)
        self.axes_formatting(ax, linewidth)
