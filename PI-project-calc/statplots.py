import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.colors as color


class BaseStatPlot:

    def __init__(self,
                 data_groups,
                 p=1,
                 stars='ns',
                 sd=None,
                 mean=None,
                 median=None,
                 testname='',
                 n=0,
                 dependent=False,
                 plot_title='',
                 x_label='',
                 y_label='',
                 print_x_labels=True,
                 x_manual_tick_labels=None,
                 colormap=None):
        self.data_groups = data_groups
        self.p = p
        self.stars = stars
        # add here sd sem mean and median calculation if they are not provided
        self.sd = sd if sd is not None else [0] * len(data_groups)
        self.mean = mean if mean is not None else [0] * len(data_groups)
        self.median = median if median is not None else [0] * len(data_groups)
        self.testname = testname
        self.n = n
        self.dependent = dependent
        self.plot_title = plot_title
        self.x_label = x_label
        self.y_label = y_label
        self.print_x_labels = print_x_labels
        self.x_manual_tick_labels = x_manual_tick_labels if x_manual_tick_labels is not None else [
            '']
        self.colormap = colormap if colormap is not None and colormap != [
            ''] else []
        self.colors_edge, self.colors_fill = self.get_colors()

    def colors_to_rgba(self, colors, alpha=0.35):
        rgba_colors = []
        for col in colors:
            rgba = list(mcolors.to_rgba(col))
            rgba[3] = alpha  # Set the alpha value.
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

    def setup_figure(self, n_groups):
        fig, ax = plt.subplots(figsize=(0.5 + 0.9 * n_groups, 4))
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

    def add_errorbar(self, ax, x,
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

    def axes_formatting(self, ax, n_groups, linewidth=2):
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
                ax.set_xticks(range(n_groups))
                ax.set_xticklabels([self.x_manual_tick_labels[i % len(self.x_manual_tick_labels)]
                                    for i in range(n_groups)])
            else:
                ax.set_xticks(range(n_groups))
                ax.set_xticklabels(['Group {}'.format(i + 1)
                                   for i in range(n_groups)])
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

    def add_significance_bar(self, ax, n_groups, linewidth=2):
        # Draw significance bar connecting first and last group.
        y_range = max([max(data) for data in self.data_groups])
        x1, x2 = 0, n_groups - 1
        y, h, col = 1.05 * y_range, 0.05 * y_range, 'k'
        ax.plot([x1, x1, x2, x2], [y, y + h, y + h, y],
                lw=linewidth, c=col)
        ax.text((x1 + x2) * 0.5, y + h,
                '{}\n{}'.format(self.p, self.stars),
                ha='center', va='bottom', color=col, fontweight='bold')

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
                 ha='right', va='bottom', fontsize=8, fontweight='bold')

    def transpose(self, data):
        return list(map(list, zip(*data)))

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
        n_groups = len(self.data_groups)
        fig, ax = self.setup_figure(n_groups)
        linewidth = 2

        for x, data in enumerate(self.data_groups):

            # Plot bar for mean with standard deviation error bars.
            ax.bar(x, self.mean[x],
                   # yerr=self.sd[i],
                   width=0.75,
                   capsize=8,
                   ecolor='r',
                   edgecolor=self.colors_edge[x % len(self.colors_edge)],
                   facecolor=self.colors_fill[x % len(self.colors_fill)],
                   fill=True,
                   linewidth=linewidth,
                   zorder=1)

            # Overlay errbars, and markers.
            self.add_median_marker(ax, x)
            self.add_mean_marker(ax, x)
            self.add_errorbar(ax, x)

        self.add_scatter(ax)
        self.add_significance_bar(ax, n_groups, linewidth)
        self.add_titles_and_labels(fig, ax)
        self.axes_formatting(ax, n_groups, linewidth)


class ViolinStatPlot(BaseStatPlot):
    '''
        Violin plot, for adjusting see
        https://matplotlib.org/stable/gallery/statistics/customized_violin.html#sphx-glr-gallery-statistics-customized-violin-py

        Kernel Density Estimation (violin shape prediction approach)
        https://scikit-learn.org/stable/modules/density.html
    '''

    def plot(self):
        n_groups = len(self.data_groups)
        fig, ax = self.setup_figure(n_groups)
        linewidth = 2

        for x, data in enumerate(self.data_groups):

            # Create a violin plot for this group.
            vp = ax.violinplot(data, positions=[x], widths=0.85, vert=True,
                               showmeans=True, showmedians=True, showextrema=True,
                               points=200, bw_method='silverman')
            for pc in vp['bodies']:
                pc.set_facecolor(self.colors_fill[x % len(self.colors_fill)])
                pc.set_edgecolor(self.colors_edge[x % len(self.colors_edge)])
                pc.set_linewidth(linewidth)

            # Overlay errbars, scatter and markers.
            self.add_median_marker(ax, x)
            self.add_mean_marker(ax, x)
            # self.add_errorbar(ax, x)

        self.add_scatter(ax)
        self.add_significance_bar(ax, n_groups, linewidth)
        self.add_titles_and_labels(fig, ax)
        self.axes_formatting(ax, n_groups, linewidth)
