import os
import re
import csv
import math
import traceback
from tracemalloc import start
from turtle import fillcolor
from openpyxl import Workbook

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from PIL import Image
import tifffile
import AutoStatLib

import settings as s

# Defaults:

# save synchronization test plots to check
# sync of stim and recording
# and provide detailed errors traceback
DEBUG = True

# min percent of successfully generated AP for ROI to consider it responsive
BINARIZATION_RESP_THRESHOLD = 0.29

# gaussian_filter sigma for derivatives calculation, to reduce noise and artifacts
# standard in ImageJ is 1.0
DERIVATIVES_SIGMA = 2.3

# Adjust the sampling interval to account for the
# clock synchronization of the microscope's hardware and PC
# Coefficient estimated experimentally
# -0.0031556459008686036  more precise
# -0.0029183722446345     old one estimation
# -0.00313                compromise
SYNC_COEF = -0.0028

# lag in frames to calculate derivatives, to avoid artifacts at the edges of epochs
DERIVATIVES_FRAME_LAG = -2

CALCULATIONS_SUBFOLDER_NAME = "_CALCULATIONS_auto_"
DERIVATIVES_SUBFOLDER_NAME = "_DERIVATIVES_auto_"
SUMMARY_SUBFOLDER_NAME = "_SUMMARY_auto__"

postprocessing_summary = True

# bugs:
# 1. on st1 in V_stack traces plots delay +10s when plotting red X (binarization calculated right)
# 2. when multiprocessing does not load bins and vshifts again
#        To solve use regex where string is 'MASK FOR ANY ENDING HERE'


class Helpers:

    def frame_to_sec(self, frame: int) -> float:
        """Convert frame to timestamp (start of frame)."""
        out = frame / self.fps if frame <= self.n_frames else self.s_movie_duration
        return out

    def sec_to_frame(self, timestamp: float) -> int:
        """Convert timestamp to frame (floor rounding)."""
        if timestamp < 0:
            raise ValueError("Timestamp must be non-negative")

        out = (
            math.floor(timestamp * self.fps)
            if timestamp <= self.s_movie_duration
            else self.n_frames
        )

        return out

    def save_tiff(self, output_path, data, metadata={}):

        # output = Image.fromarray(data)
        # output.save(output_path, save_all=True,
        #             compression="tiff_deflate",
        #             tiffinfo=metadata)

        # does not work for some reasons:
        # if data.ndim == 3 else np.array([data]).astype(np.float32)
        img = data.astype(np.float32)
        tifffile.imwrite(
            output_path, img, imagej=True, compression="zlib", metadata=metadata
        )

    def transpose(self, matrix):
        rows = len(matrix)
        cols = max(len(row) for row in matrix)

        # use internal numpy method if ndarray for optimization
        if isinstance(matrix, np.ndarray):
            transposed = matrix.T
        else:
            transposed = [[None] * rows for _ in range(cols)]

            for i in range(rows):
                for j in range(len(matrix[i])):
                    transposed[j][i] = matrix[i][j]

        return transposed

    def transpose_autoballance(self, data):
        # Determine the maximum length of any row
        max_len = max(len(row) for row in data)
        # Fill shorter rows with None to make all rows equal in length
        balanced_data = tuple(list(row) + [None] * (max_len - len(row)) for row in data)
        # Transpose the matrix
        data_t = tuple(
            tuple(balanced_data[j][i] for j in range(len(balanced_data)))
            for i in range(max_len)
        )
        return data_t

    def csv_write(self, data, csv_path, csv_file, filename_suffix, subdir=False):

        if subdir:
            os.makedirs(csv_path + csv_file + filename_suffix + "/", exist_ok=True)
            path = "{0}{1}{2}/{2}.csv".format(
                csv_path,
                csv_file,
                filename_suffix,
            )

        else:
            path = "{0}/{2}.csv".format(
                csv_path,
                csv_file,
                filename_suffix,
            )

        with open(path, "w") as f:

            writer = csv.writer(
                f,
                delimiter=",",
                lineterminator="\r",
            )
            for row in data:
                writer.writerow(row)

    def filter_list(self, list, bin, replace=True, replace_with=None):
        if replace == True:
            output = [value if bin[i] else replace_with for i, value in enumerate(list)]
        else:
            output = [value for value, keep in zip(list, bin) if keep]

        return output

    def plot_traces(
        self,
        x,
        cols,
        events,
        savename,
        offset=0,
        figsize=(15, 5),
        alpha=None,
        dpi=200,
        linewidth=0.5,
        linecolor="k",
        fillcolor="g",
        avg_linecolor="r",
        event_linecolor="g",
        event_linestyle=":",
    ):

        x = np.array(x)

        plt.figure(figsize=figsize, dpi=dpi)
        # plt.style.use("ggplot")

        # set alpha based on number of columns,
        # so that the more columns,
        # the more transparent each line
        if not alpha:
            n_cols = len(cols)
            alpha = 3 / n_cols

        if alpha > 1:
            alpha = 1

        # Plot each trace
        for i, col in enumerate(cols):
            plt.plot(x, col, color=linecolor, linewidth=linewidth, alpha=alpha)

        plt.plot(
            x,
            np.mean(cols, axis=0),
            color=avg_linecolor,
            linewidth=linewidth * 3,
            alpha=1,
        )

        for event in events:
            if isinstance(event, int) or isinstance(event, float):
                plt.axvline(
                    event,
                    color=event_linecolor,
                    linestyle=event_linestyle,
                    linewidth=linewidth * 0.5,
                    zorder=1,
                )
            elif isinstance(event, list) or isinstance(event, tuple):
                plt.fill_between(
                    x,
                    y1=np.max(cols),
                    y2=np.min(cols),
                    where=(x >= event[0]) & (x <= event[-1]),
                    color=fillcolor,
                    edgecolor="none",
                    alpha=0.4,
                    zorder=0,
                )
            else:
                pass

        # plt.suptitle(TITLE)
        # plt.xlabel('Time, s')
        # plt.ylabel("Amplitude + Offset")

        plt.tight_layout()

        # Save the combined figure

        if isinstance(savename, str):
            plt.savefig(savename, transparent=False)
        elif isinstance(savename, list) or isinstance(savename, tuple):
            for name in savename:
                plt.savefig(name, transparent=False)
        else:
            self.logging("!!!    Fail: invalid savename type        ", type(savename))

        plt.close()


class Logging:

    def __init__(
        self,
    ):
        self.log = " \n"

    def logging(self, *args, **kwargs):
        message = " ".join(map(str, args))
        self.log += "\n" + message


class TracesCalc(Logging):

    def file_finder(self, pattern, nonrecursive=False):
        files_list = []  # To store the paths of .txt files

        # Walk through the directory and its subdirectories
        for root, _, files in os.walk(self.path):
            for filename in files:
                if re.search(pattern, filename):
                    files_list.append(
                        [root if root[-1] == "/" else root + "/", filename[:-4]]
                    )

            if nonrecursive:
                break

        return files_list

    def file_lister(self, pattern, nonrecursive=False):
        files = []

        if os.path.isdir(self.path):
            files.extend(self.file_finder(pattern, nonrecursive))
        else:
            self.logging("!!!    Fail: invalid path        ", self.path)

        return files

    def find_time_index(self, content, time):
        content = (float(i) - time for i in list(zip(*content))[0])
        diffs = [abs(i) for i in content]
        index = diffs.index(min(diffs))

        return index

    def data_normalize(self, content, start, zero):
        content_normalized = []

        for column in content:
            baseline = column[start:zero]
            baseline_sum = sum((float(cell) for cell in baseline))
            baseline_len = len(baseline)
            mean = baseline_sum / baseline_len if baseline_len and baseline else 0

            column_normalized = [
                (float(cell) - mean) / mean if mean else 0 for cell in column
            ]  # ΔF/F₀
            # column_normalized = [float(cell)/mean if mean else 1 for cell in column]   # ΔF/F

            content_normalized.append(column_normalized)

        return content_normalized

    def csv_cutter(self, content):
        timeline_zero = (float(i) - self.s_trig_time for i in list(zip(*content))[0])

        start = (
            self.find_time_index(content, self.s_trig_time - self.time_before_trig)
            if self.time_before_trig
            else None
        )

        start_bl = (
            self.find_time_index(content, self.s_trig_time - self.baseline_duraton)
            if self.baseline_duraton
            else start
        )

        zero = self.find_time_index(content, self.s_trig_time)

        end = (
            self.find_time_index(content, self.s_trig_time + self.time_after_trig)
            if self.time_after_trig
            else None
        )

        content = list(zip(*content))[1:]
        content[:0] = [timeline_zero]

        if self.relative_values:
            content[1:] = self.data_normalize(content[1:], start_bl, zero)

        csv_output = list(zip(*content))[start:end]
        csv_output_np = np.array(csv_output)

        return csv_output_np

    def csv_transform(
        self,
        content_raw,
    ):

        mean_col = self.mean_col_order  # order of "Mean" col in measurments
        n_cols = self.cols_per_roi  # n of measurments for each ROI

        first_col = (str(i * self.spf) for i in range(len(content_raw)))
        content = list(zip(*content_raw))[mean_col::n_cols]
        content[:0] = [first_col]
        content = list(zip(*content))[1:]

        return content

    def csv_read(self, csv_path, csv_file):

        with open(csv_path + csv_file + ".csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            content_raw = tuple(reader)

        return content_raw

    def calculate_ampl_auc_bin(self, start_bl, end_bl, start, end):

        matrix = np.array(self.transpose(self.csv_matrix))

        # Extract time vector and data traces
        x = matrix[0]
        traces = matrix[1:]

        # Indices for baseline and signal periods
        bl_indices = np.where((x >= start_bl) & (x <= end_bl))[0]
        sig_indices = np.where((x >= start) & (x <= end))[0]
        whole_step_indices = np.where((x >= start_bl) & (x <= end))[0]

        # Lists to store peak amplitudes and AUCs for each trace
        ampl_list = []
        auc_list = []
        bin_list = []
        raw_line_list = [x[whole_step_indices] - start]

        for trace in traces:
            # Calculate baseline
            baseline = np.mean(trace[bl_indices])
            # Baseline correction
            corrected_trace = trace - baseline
            # Peak amplitude in signal period
            ampl = np.max(corrected_trace[sig_indices])
            ampl_list.append(ampl)
            # AUC in signal period
            auc = np.trapezoid(corrected_trace[sig_indices], x[sig_indices])
            auc_list.append(auc)
            # biarization
            bin_list.append(ampl > self.sigmas_treshold * np.std(trace[bl_indices]))

            raw_line_list.append(corrected_trace[whole_step_indices])

            # Debug plot
            # self.logging(ampl > self.sigmas_treshold *
            #                 np.std(trace[bl_indices]))
            # plt.plot(corrected_trace[whole_step_indices])
            # plt.show()
            # plt.close()

        # Calculate mean amplitude and AUC across all traces
        ampl_mean_of_rois = np.mean(ampl_list)
        auc_mean_of_rois = np.mean(auc_list)

        return (
            ampl_mean_of_rois,
            ampl_list,
            auc_mean_of_rois,
            auc_list,
            bin_list,
            raw_line_list,
        )

    def calc_traces_sequence(self, i):

        delay = self.s_step_duration * i
        (
            ampl_mean_of_rois_by_epoch,
            ampl_list_each_by_roi,
            auc_mean_of_rois_by_epoch,
            auc_list_each_by_roi,
            bin_list_each_by_roi,
            raw_line_list,
        ) = [
            [
                self.calculate_ampl_auc_bin(
                    (i * self.s_epoch_duration) + delay - self.s_step_duration / 2,
                    (i * self.s_epoch_duration) + delay,
                    (i * self.s_epoch_duration) + delay,
                    (i * self.s_epoch_duration) + delay + self.s_step_duration / 2,
                )[j]
                for i in range(self.start_from_epoch, self.n_epochs)
            ]
            for j in range(6)
        ]

        ampl_list_each_by_epoch = self.transpose(ampl_list_each_by_roi)
        auc_list_each_by_epoch = self.transpose(auc_list_each_by_roi)
        bin_list_each_by_epoch = self.transpose(bin_list_each_by_roi)
        ampl_mean_of_epochs_by_rois = [
            np.mean(epoch) for epoch in ampl_list_each_by_epoch
        ]
        auc_mean_of_epochs_by_rois = [
            np.mean(epoch) for epoch in auc_list_each_by_epoch
        ]

        return (
            ampl_mean_of_rois_by_epoch,
            ampl_mean_of_epochs_by_rois,
            ampl_list_each_by_roi,
            ampl_list_each_by_epoch,
            auc_mean_of_rois_by_epoch,
            auc_mean_of_epochs_by_rois,
            auc_list_each_by_roi,
            auc_list_each_by_epoch,
            bin_list_each_by_epoch,
            raw_line_list,
        )

    def detailed_stats(self, csv_path, csv_file, output_dir):

        # create unique id for each calculation unit (trigger)
        # unit_id = self.file_path + '%' + str(self.trig_number)
        unit_id = (
            csv_path + csv_file + "$" + str(self.trig_number) + "$" + self.output_suffix
        )

        s1s2 = False
        s1 = False
        s2 = False
        self.group_names = []
        for i, (sp1, sp2) in enumerate(zip(self.drs_pattern[0], self.drs_pattern[1])):
            match (sp1, sp2):
                case (1, 1):
                    (
                        s1s2_ampl_mean_of_rois_by_epoch,
                        s1s2_ampl_mean_of_epochs_by_rois,
                        s1s2_ampl_list_each_by_roi,
                        s1s2_ampl_list_each_by_epoch,
                        s1s2_auc_mean_of_rois_by_epoch,
                        s1s2_auc_mean_of_epochs_by_rois,
                        s1s2_auc_list_each_by_roi,
                        s1s2_auc_list_each_by_epoch,
                        s1s2_bin_list_each_by_epoch,
                        s1s2_raw_line_list,
                    ) = self.calc_traces_sequence(i)
                    self.s1s2_delay = i * self.s_step_duration
                    s1s2 = True
                    s1s2_order = i
                    self.group_names.append(self.stim_1_name + "&" + self.stim_2_name)
                case (1, 0):
                    (
                        s1_ampl_mean_of_rois_by_epoch,
                        s1_ampl_mean_of_epochs_by_rois,
                        s1_ampl_list_each_by_roi,
                        s1_ampl_list_each_by_epoch,
                        s1_auc_mean_of_rois_by_epoch,
                        s1_auc_mean_of_epochs_by_rois,
                        s1_auc_list_each_by_roi,
                        s1_auc_list_each_by_epoch,
                        s1_bin_list_each_by_epoch,
                        s1_raw_line_list,
                    ) = self.calc_traces_sequence(i)
                    self.s1_delay = i * self.s_step_duration
                    s1 = True
                    s1_order = i
                    self.group_names.append(self.stim_1_name)
                case (0, 1):
                    (
                        s2_ampl_mean_of_rois_by_epoch,
                        s2_ampl_mean_of_epochs_by_rois,
                        s2_ampl_list_each_by_roi,
                        s2_ampl_list_each_by_epoch,
                        s2_auc_mean_of_rois_by_epoch,
                        s2_auc_mean_of_epochs_by_rois,
                        s2_auc_list_each_by_roi,
                        s2_auc_list_each_by_epoch,
                        s2_bin_list_each_by_epoch,
                        s2_raw_line_list,
                    ) = self.calc_traces_sequence(i)
                    self.s2_delay = i * self.s_step_duration
                    s2 = True
                    s2_order = i
                    self.group_names.append(self.stim_2_name)
                case (0, 0):
                    pass
                case (None, None):
                    pass
                # responses_each_by_roi, responses_each_by_epoch = self.calc_traces_sequence(i)

        # Check is there both stim or only one to avoid errs
        # Огидна конструкція, потім переробити

        if s1s2:
            st1_ampl_mean_of_epochs_by_rois = s1s2_ampl_mean_of_epochs_by_rois
            st2_ampl_mean_of_epochs_by_rois = s2_ampl_mean_of_epochs_by_rois
            st1_auc_mean_of_epochs_by_rois = s1s2_auc_mean_of_epochs_by_rois
            st2_auc_mean_of_epochs_by_rois = s2_auc_mean_of_epochs_by_rois

        if not s1s2 and not s1:
            ampl_s2_to_s1s2_ratio_mean_of_epochs_by_rois = np.array(
                [0.001] * len(s2_ampl_mean_of_epochs_by_rois)
            )
            ampl_s2_to_s1s2_ratio_rois_by_epoch = np.array(
                [[0.001] for _ in range(len(s2_ampl_list_each_by_epoch))]
            )
            s1s2_ampl_mean_of_epochs_by_rois = np.array(
                [0.001] * len(s2_auc_mean_of_epochs_by_rois)
            )
            s1s2_ampl_list_each_by_epoch = np.array([[0.001] * self.n_epochs])

            auc_s2_to_s1s2_ratio_mean_of_epochs_by_rois = np.array(
                [0.001] * len(s2_auc_mean_of_epochs_by_rois)
            )
            auc_s2_to_s1s2_ratio_rois_by_epoch = np.array(
                [[0.001] for _ in range(len(s2_auc_list_each_by_epoch))]
            )
            s1s2_auc_mean_of_epochs_by_rois = np.array(
                [0.001] * len(s2_auc_mean_of_epochs_by_rois)
            )
            s1s2_auc_list_each_by_epoch = np.array([[0.001] * self.n_epochs])

        if s1s2 and not s1:
            st1_ampl_mean_of_epochs_by_rois = s1s2_ampl_mean_of_epochs_by_rois
            st2_ampl_mean_of_epochs_by_rois = s2_ampl_mean_of_epochs_by_rois

            ampl_st2_to_st1_ratio_mean_of_epochs_by_rois = np.array(
                s2_ampl_mean_of_epochs_by_rois
            ) / np.array(s1s2_ampl_mean_of_epochs_by_rois)
            ampl_st2_to_st1_ratio_rois_by_epoch = np.array(
                s2_ampl_list_each_by_epoch
            ) / np.array(s1s2_ampl_list_each_by_epoch)

            st1_auc_mean_of_epochs_by_rois = s1s2_auc_mean_of_epochs_by_rois
            st2_auc_mean_of_epochs_by_rois = s2_auc_mean_of_epochs_by_rois

            auc_st2_to_st1_ratio_mean_of_epochs_by_rois = np.array(
                s2_auc_mean_of_epochs_by_rois
            ) / np.array(s1s2_auc_mean_of_epochs_by_rois)
            auc_st2_to_st1_ratio_rois_by_epoch = np.array(
                s2_auc_list_each_by_epoch
            ) / np.array(s1s2_auc_list_each_by_epoch)

        if s1 and not s1s2:
            st1_ampl_mean_of_epochs_by_rois = s1_ampl_mean_of_epochs_by_rois
            st2_ampl_mean_of_epochs_by_rois = s2_ampl_mean_of_epochs_by_rois

            ampl_st2_to_st1_ratio_mean_of_epochs_by_rois = np.array(
                s2_ampl_mean_of_epochs_by_rois
            ) / np.array(s1_ampl_mean_of_epochs_by_rois)
            ampl_st2_to_st1_ratio_rois_by_epoch = np.array(
                s2_ampl_list_each_by_epoch
            ) / np.array(s1_ampl_list_each_by_epoch)

            st1_auc_mean_of_epochs_by_rois = s1_auc_mean_of_epochs_by_rois
            st2_auc_mean_of_epochs_by_rois = s2_auc_mean_of_epochs_by_rois

            auc_st2_to_st1_ratio_mean_of_epochs_by_rois = np.array(
                s2_auc_mean_of_epochs_by_rois
            ) / np.array(s1_auc_mean_of_epochs_by_rois)
            auc_st2_to_st1_ratio_rois_by_epoch = np.array(
                s2_auc_list_each_by_epoch
            ) / np.array(s1_auc_list_each_by_epoch)

        # Binarization:

        if not s1s2 and not s1:
            s1s2_bin_list_each_by_epoch = s2_bin_list_each_by_epoch
            s1_bin_list_each_by_epoch = s2_bin_list_each_by_epoch
        if not s1s2 and s1:
            s1s2_bin_list_each_by_epoch = s1_bin_list_each_by_epoch
        if not s1 and s1s2:
            s1_bin_list_each_by_epoch = s1s2_bin_list_each_by_epoch

        if len(self.group_names) == 1:
            self.group_names.insert(0, "_")

        if not s1 and s1s2:
            st1_bin_summary_by_rois = [
                sum(i) / len(i) > BINARIZATION_RESP_THRESHOLD
                for i in s1s2_bin_list_each_by_epoch
            ]
        if not s1s2 and s1:
            st1_bin_summary_by_rois = [
                sum(i) / len(i) > BINARIZATION_RESP_THRESHOLD
                for i in s1_bin_list_each_by_epoch
            ]
        st2_bin_summary_by_rois = [
            sum(i) / len(i) > BINARIZATION_RESP_THRESHOLD
            for i in s2_bin_list_each_by_epoch
        ]

        # save binarization for the next calculations
        load_unitid = (
            csv_path
            + csv_file
            + "$"
            + str(self.SD_filter_of_trig - 1)
            + "$"
            + "MASK FOR ANY ENDING HERE"
        )
        current_filter = [
            st1_bin_summary_by_rois,
            st1_bin_summary_by_rois,
            st2_bin_summary_by_rois,
        ]

        if self.SD_filter_of_trig and load_unitid in self.filters:
            filter = self.filters[load_unitid]
        else:
            filter = current_filter

        self.filters_return |= {unit_id: current_filter}

        # save responses Ampl and AUC for the next calculations
        amps = [
            st1_ampl_mean_of_epochs_by_rois,
            st1_ampl_mean_of_epochs_by_rois,
            st2_ampl_mean_of_epochs_by_rois,
        ]

        aucs = [
            st1_auc_mean_of_epochs_by_rois,
            st1_auc_mean_of_epochs_by_rois,
            st2_auc_mean_of_epochs_by_rois,
        ]

        self.ampls_return |= {unit_id: amps}
        self.aucs_return |= {unit_id: aucs}

        self.plot_s2_to_s1s2_ratio_rois_by_epoch(
            1 / ampl_st2_to_st1_ratio_rois_by_epoch,
            "{0}{1}/_rois_by_epoch_{3}_to_{2}_{4}_ratio_auto_.png".format(
                csv_path,
                output_dir,
                self.group_names[0],
                self.group_names[1],
                self.output_suffix,
            ),
        )

        # csv file of #1#2 and #2 amplitudes by rois epochs average
        header = [self.group_names[0], self.group_names[1], "ratio col1/col2"]

        # CSV summary Amplitude

        self.csv_write(
            [
                [
                    "Unfiltered",
                    "",
                    "",
                    "",
                    "",
                    "Filtered by {} SD of {}".format(
                        self.sigmas_treshold, self.group_names[1]
                    ),
                    "",
                    "",
                    "",
                    "",
                    "Filtered by {} SD of {}".format(
                        self.sigmas_treshold, self.group_names[0]
                    ),
                ],
                header + [""] * 2 + header + [""] * 2 + header,
                *self.transpose(
                    [
                        st1_ampl_mean_of_epochs_by_rois,
                        st2_ampl_mean_of_epochs_by_rois,
                        1 / ampl_st2_to_st1_ratio_mean_of_epochs_by_rois,
                        "",
                        "",
                        self.filter_list(st1_ampl_mean_of_epochs_by_rois, filter[2]),
                        self.filter_list(st2_ampl_mean_of_epochs_by_rois, filter[2]),
                        self.filter_list(
                            1 / ampl_st2_to_st1_ratio_mean_of_epochs_by_rois, filter[2]
                        ),
                        "",
                        "",
                        self.filter_list(st1_ampl_mean_of_epochs_by_rois, filter[1]),
                        self.filter_list(st2_ampl_mean_of_epochs_by_rois, filter[1]),
                        self.filter_list(
                            1 / ampl_st2_to_st1_ratio_mean_of_epochs_by_rois, filter[1]
                        ),
                    ]
                ),
            ],
            csv_path + output_dir,
            output_dir,
            "_by_rois_mean_of_epochs_{0}_and_{1}_ampl_{2}_auto_".format(
                self.group_names[0], self.group_names[1], self.output_suffix
            ),
        )

        # CSV summary AUC
        self.csv_write(
            [
                [
                    "Unfiltered",
                    "",
                    "",
                    "",
                    "",
                    "Filtered by {} SD of {}".format(
                        self.sigmas_treshold, self.group_names[1]
                    ),
                    "",
                    "",
                    "",
                    "",
                    "Filtered by {} SD of {}".format(
                        self.sigmas_treshold, self.group_names[0]
                    ),
                ],
                header + [""] * 2 + header + [""] * 2 + header,
                *self.transpose(
                    [
                        st1_auc_mean_of_epochs_by_rois,
                        st2_auc_mean_of_epochs_by_rois,
                        1 / auc_st2_to_st1_ratio_mean_of_epochs_by_rois,
                        "",
                        "",
                        self.filter_list(st1_auc_mean_of_epochs_by_rois, filter[2]),
                        self.filter_list(st2_auc_mean_of_epochs_by_rois, filter[2]),
                        self.filter_list(
                            1 / auc_st2_to_st1_ratio_mean_of_epochs_by_rois, filter[2]
                        ),
                        "",
                        "",
                        self.filter_list(st1_auc_mean_of_epochs_by_rois, filter[1]),
                        self.filter_list(st2_auc_mean_of_epochs_by_rois, filter[1]),
                        self.filter_list(
                            1 / auc_st2_to_st1_ratio_mean_of_epochs_by_rois, filter[1]
                        ),
                    ]
                ),
            ],
            csv_path + output_dir,
            output_dir,
            "_by_rois_mean_of_epochs_{0}_and_{1}_auc_{2}_auto_".format(
                self.group_names[0], self.group_names[1], self.output_suffix
            ),
        )

        # plot_s1s2_s2_roi_stats AUC for all rois
        self.plot_s1s2_s2_roi_stats(
            self.filter_list(st1_auc_mean_of_epochs_by_rois, filter[2], replace=False),
            self.filter_list(st2_auc_mean_of_epochs_by_rois, filter[2], replace=False),
            "{0}{1}/_by_rois_{2}_{3}_{4}_auc_auto_.png".format(
                csv_path,
                output_dir,
                self.group_names[0],
                self.group_names[1],
                self.output_suffix,
            ),
            paired=True,
            y_label="AUC",
            Groups_Name=[self.group_names[0], self.group_names[1]],
        )

        # plot_s1s2_s2_roi_stats Ampl for all rois
        self.plot_s1s2_s2_roi_stats(
            self.filter_list(st1_ampl_mean_of_epochs_by_rois, filter[2], replace=False),
            self.filter_list(st2_ampl_mean_of_epochs_by_rois, filter[2], replace=False),
            "{0}{1}/_by_rois_{2}_{3}_{4}_ampl_auto_.png".format(
                csv_path,
                output_dir,
                self.group_names[0],
                self.group_names[1],
                self.output_suffix,
            ),
            paired=True,
            y_label="ΔF/F₀",
            Groups_Name=[self.group_names[0], self.group_names[1]],
        )

        # plot_s1s2_s2_roi_stats for each roi during timeline
        if s1s2 and s2:
            for i in range(len(s1s2_ampl_list_each_by_epoch)):
                self.plot_s1s2_s2_roi_stats(
                    s1s2_ampl_list_each_by_epoch[i],
                    s2_ampl_list_each_by_epoch[i],
                    "{0}{1}/_roi{2}_{3}{4}_{4}_{5}_ampl_auto_.png".format(
                        csv_path,
                        output_dir,
                        i + 1,
                        self.stim_1_name,
                        self.stim_2_name,
                        self.output_suffix,
                    ),
                    paired=True,
                    y_label=f"ΔF/F₀        ROI {i+1}",
                    Groups_Name=[
                        "{}+{}".format(self.stim_1_name, self.stim_2_name),
                        self.stim_2_name,
                    ],
                )

        # save vertical shift for the next calculations
        load_vshift = (
            csv_path
            + csv_file
            + "$"
            + str(self.vertical_shift_of_trig - 1)
            + "$"
            + "MASK FOR ANY ENDING HERE"
        )
        if self.vertical_shift_of_trig and load_vshift in self.v_shifts:
            self.vertical_shift = self.v_shifts[load_vshift]
        if not self.vertical_shift or self.vertical_shift == 0:
            vertical_shift = np.amax(s2_ampl_list_each_by_roi)
        else:
            vertical_shift = self.vertical_shift

        self.v_shifts_return |= {unit_id: vertical_shift}

        # CSV all traces in timeframe
        matrix = self.csv_matrix[
            int(
                (
                    (self.start_from_epoch)
                    * self.s_step_duration
                    * self.n_steps_per_epoch
                )
                / self.spf
            ) : int(
                (
                    (self.start_from_epoch + self.n_epochs + 1)
                    * self.s_step_duration
                    * self.n_steps_per_epoch
                )
                / self.spf
            )
        ]
        matrix_T = self.transpose(matrix)

        # save them to CSV
        self.csv_write(
            matrix,
            csv_path + output_dir,
            output_dir,
            "_full_traces_raw_{0}_and_{1}_ampl_{2}_auto_".format(
                self.group_names[0], self.group_names[1], self.output_suffix
            ),
        )

        # plot them all (slows script down)
        self.plot_traces(
            matrix_T[0],
            matrix_T[1:],
            [],
            csv_path
            + output_dir
            + "/"
            + "_full_traces_raw_{0}_and_{1}_ampl_{2}_auto_.png".format(
                self.group_names[0], self.group_names[1], self.output_suffix
            ),
            linewidth=0.5,
            dpi=400,
        )

        # plot debug graph to check time sync
        if DEBUG:
            start = (
                self.start_from_epoch * self.s_step_duration * self.n_steps_per_epoch
            )
            end = start + self.s_step_duration
            start_frame = int(
                (
                    (self.start_from_epoch)
                    * self.s_step_duration
                    * self.n_steps_per_epoch
                )
                / self.spf
            )
            end_frame = int(
                (
                    (self.start_from_epoch + 1.5)
                    * self.s_step_duration
                    * self.n_steps_per_epoch
                )
                / self.spf
            )

            chunk = self.csv_matrix[start_frame:end_frame]
            chunk_T = self.transpose(chunk)
            self.plot_traces(
                chunk_T[0],
                chunk_T[1:],
                [start, end],
                csv_path
                + output_dir
                + "/"
                + "debug_Synchronization_{}.png".format(self.output_suffix),
                linewidth=0.5,
                alpha=0.8,
                event_linecolor="magenta",
                avg_linecolor="darkcyan",
                dpi=400,
            )

        # plot_stacked_traces all togather
        for i in self.group_names:
            os.makedirs(
                csv_path
                + output_dir
                + "/_by_rois_traces_bin_{0}_{1}_auto_".format(i, self.output_suffix),
                exist_ok=True,
            )

        self.plot_stacked_traces(
            np.array(matrix_T[0])
            - ((self.start_from_epoch) * self.s_step_duration * self.n_steps_per_epoch),
            matrix_T[:],
            s1s2_bin_list_each_by_epoch,
            st1_bin_summary_by_rois,
            "{0}{1}/_by_rois_traces_bin_{2}_{3}_auto_/_full_traces_stacked_by_rois_auto_.png".format(
                csv_path, output_dir, self.group_names[0], self.output_suffix
            ),
            vertical_shift=vertical_shift,
            delay=0,
        )
        self.plot_stacked_traces(
            np.array(matrix_T[0])
            - ((self.start_from_epoch) * self.s_step_duration * self.n_steps_per_epoch),
            matrix_T[:],
            s2_bin_list_each_by_epoch,
            st2_bin_summary_by_rois,
            "{0}{1}/_by_rois_traces_bin_{2}_{3}_auto_/_full_traces_stacked_by_rois_auto_.png".format(
                csv_path, output_dir, self.group_names[1], self.output_suffix
            ),
            vertical_shift=vertical_shift,
            delay=self.s2_delay,
        )

        # plot_stacked_traces by groups
        chunk_size = 20
        for pos in range(0, len(self.csv_matrix[0]) - 1, chunk_size):
            self.plot_stacked_traces(
                np.array(matrix_T[0])
                - (
                    (self.start_from_epoch)
                    * self.s_step_duration
                    * self.n_steps_per_epoch
                ),
                matrix_T[pos : pos + chunk_size + 1],
                s1s2_bin_list_each_by_epoch[pos : pos + chunk_size + 1],
                st1_bin_summary_by_rois[pos : pos + chunk_size + 1],
                "{0}{1}/_by_rois_traces_bin_{2}_{5}_auto_/_full_traces_stacked_by_rois_{3}-{4}_{5}_auto_.png".format(
                    csv_path,
                    output_dir,
                    self.group_names[0],
                    pos + 1,
                    pos + chunk_size,
                    self.output_suffix,
                ),
                vertical_shift=vertical_shift,
                delay=self.s2_delay,
            )
        for pos in range(0, len(self.csv_matrix[0]) - 1, chunk_size):
            self.plot_stacked_traces(
                np.array(matrix_T[0])
                - (
                    (self.start_from_epoch)
                    * self.s_step_duration
                    * self.n_steps_per_epoch
                ),
                matrix_T[pos : pos + chunk_size + 1],
                s2_bin_list_each_by_epoch[pos : pos + chunk_size + 1],
                st2_bin_summary_by_rois[pos : pos + chunk_size + 1],
                "{0}{1}/_by_rois_traces_bin_{2}_{5}_auto_/_full_traces_stacked_by_rois_{3}-{4}_{5}_auto_.png".format(
                    csv_path,
                    output_dir,
                    self.group_names[1],
                    pos + 1,
                    pos + chunk_size,
                    self.output_suffix,
                ),
                vertical_shift=vertical_shift,
                delay=self.s2_delay,
            )

        # plot_traces_by_rois
        # for i in range(len(s1s2_raw_line_list)):
        #     self.plot_traces_by_rois(s1s2_raw_line_list[i],
        #                              s2_raw_line_list[i],
        #                              '{0}{1}/_epoch{2}_AC_C_traces_auto_.png'.format(csv_path, output_dir[:], i+self.start_from_epoch))

        # plot_heatmaps
        self.plot_heatmap(
            matrix_T[:],
            "{0}{1}/_by_rois__heatmap_bin_{2}_{3}_auto_.png".format(
                csv_path, output_dir, self.group_names[0], self.output_suffix
            ),
            s1s2_bin_list_each_by_epoch,
            st1_bin_summary_by_rois,
            delay=0,
        )
        self.plot_heatmap(
            matrix_T[:],
            "{0}{1}/_by_rois__heatmap_bin_{2}_{3}_auto_.png".format(
                csv_path, output_dir, self.group_names[1], self.output_suffix
            ),
            s2_bin_list_each_by_epoch,
            st2_bin_summary_by_rois,
            delay=self.s2_delay,
        )
        self.plot_heatmap(
            matrix_T[:],
            "{0}{1}/_by_rois__heatmap_auto_{2}.png".format(
                csv_path, output_dir, self.output_suffix
            ),
            delay=self.s2_delay,
        )

    def plot_s2_to_s1s2_ratio_rois_by_epoch(self, array, path):

        # Create the plot
        plt.figure(figsize=(15, 10))  # Set the figure size to 10x15 inches
        x = list(range(1, len(array[0]) + 1))

        for roi in array:
            plt.plot(x, roi, marker="o", linestyle="-", color="k")

        plt.title(
            "{1} to {0}+{1} resp amplitude ratio by time".format(
                self.stim_1_name, self.stim_2_name
            )
        )
        plt.xlabel("epoch")
        plt.ylabel(
            "{1} to {0}+{1} resp amplitude ratio".format(
                self.stim_1_name, self.stim_2_name
            )
        )
        plt.savefig(path)
        plt.close()

    def plot_s1s2_s2_roi_stats(
        self, group1, group2, path, paired=True, y_label="", Groups_Name=[]
    ):

        data = [group1, group2]

        # set the parameters:
        paired = True  # is groups dependend or not
        tails = 2  # two-tailed or one-tailed result

        # initiate the analysis
        analysis = AutoStatLib.StatisticalAnalysis(
            data,
            paired=paired,
            tails=tails,
            verbose=False,
            groups_name=Groups_Name,
        )

        analysis.RunWilcoxon()
        results = analysis.GetResult()

        if "p_value_exact" in results:
            plot = AutoStatLib.StatPlots.BarStatPlot(
                data,
                **results,
                y_label=y_label,
                figure_scale_factor=0.8,
                figure_h=4,
                figure_w=0,
            )
        else:
            plot = AutoStatLib.StatPlots.BarStatPlot(data, dependent=True)
        plot.plot()
        plot.save(path)
        plot.close()

    def plot_traces_by_rois(self, array1, array2, path):
        plt.figure()

        # Plot lines from the first array in black
        x = array1[0]
        for y in array1[1:]:
            plt.plot(x, y, "k-", alpha=0.5)

        # Plot lines from the second array in red
        x = array2[0]
        for y in array2[1:]:
            plt.plot(x, y, "r-", alpha=0.5)

        plt.savefig(path)
        plt.close()

    def plot_stacked_traces(
        self, x, array, bin, bin_summary_by_rois, path, vertical_shift=1, delay=0
    ):
        plt.figure(figsize=(10, 10))

        for i, y in enumerate(array[1:]):
            color = "g-" if bin_summary_by_rois[i] else "k-"
            vertical_shifted_y = [val + i * vertical_shift for val in y]
            plt.plot(x, vertical_shifted_y, color, linewidth=0.7, alpha=1)

            plt.plot(
                [
                    (
                        j * self.s_step_duration * self.n_steps_per_epoch + delay
                        if bin[i][j]
                        else None
                    )
                    for j, dot in enumerate(bin[i])
                ],
                [i * vertical_shift] * len((bin[i])),
                "rx",
            )

        # Set y-tick labels divided by vertical_shift, starting from 1, and rounded to integers
        ax = plt.gca()
        # y_ticks = ax.get_yticks()
        # ax.set_yticks(y_ticks)
        # ax.set_yticklabels([f'{int(round(y / vertical_shift + 1))}' for y in y_ticks])

        # Remove y-axis ticks
        ax.set_yticks([])

        ax.errorbar(
            -15,
            -0.5,
            yerr=0.5,
            fmt="none",
            capsize=4,
            ecolor="k",
            linewidth=2,
            zorder=3,
        )

        plt.text(
            -15, -1.0, "1 ΔF/F₀", horizontalalignment="center", verticalalignment="top"
        )

        for i, y in enumerate(array[1:]):
            plt.text(
                -20,
                (i * vertical_shift),
                f"{i+1}",
                horizontalalignment="center",
                verticalalignment="bottom",
            )

        # Save the plot as plot.png
        plt.tight_layout()
        plt.savefig(path, transparent=False)
        plt.close()

    def plot_heatmap(self, matrix, path, bin=[], bin_summary_by_rois=[], delay=0):
        array = np.array(matrix[1:])  # Exclude the x-axis row
        array = array[::-1]  # reverse matrix along y axis
        x = np.array(matrix[0])  # x-axis values

        # Create the heatmap
        plt.figure(figsize=(14, 10))
        plt.imshow(
            array,
            aspect="auto",
            cmap="magma",
            interpolation="nearest",
            origin="upper",
            extent=[x[0], x[-1], len(array), 0],
        )
        plt.colorbar(label="ΔF/F₀")

        # Overlay bin events
        if bin and bin_summary_by_rois:
            for i in range(len(array)):
                if bin_summary_by_rois[i]:
                    plt.plot(
                        min(x) - 5, len(array) - i - 0.5, "wo", markeredgecolor="g"
                    )
                for j, dot in enumerate(bin[i]):
                    if dot:
                        event_x = (
                            j * self.s_step_duration * self.n_steps_per_epoch
                            + delay
                            + min(x)
                        )
                        plt.plot(
                            event_x, len(array) - i - 0.5, "wx", markeredgecolor="g"
                        )

        # plt.xlabel('Time')
        # plt.ylabel('ROIs')
        plt.tight_layout()
        plt.savefig(path)
        plt.close()

    def csv_process(self, detailed_stats=True):
        csv_list = []
        csv_list.extend(
            self.file_lister(
                r"^" + re.escape(self.file_nosuffix) + r".*\.csv$", nonrecursive=True
            )
        )

        if csv_list:

            for i, [csv_path, csv_file] in enumerate(csv_list):
                content_raw = self.csv_read(csv_path, csv_file)
                content = self.csv_transform(content_raw)

                # For multievent movies:
                # for i, event in enumerate(self.events):
                #     csv_output = self.csv_cutter(content, *event)
                #     try:
                #         self.csv_write(csv_output, csv_path, csv_file)
                #     except PermissionError:
                #         self.logging('       File actually opened:')
                #         continue

                self.csv_matrix = self.csv_cutter(content)
                try:
                    self.csv_write(
                        self.csv_matrix,
                        csv_path,
                        csv_file + ".csv",
                        CALCULATIONS_SUBFOLDER_NAME + self.output_suffix,
                        subdir=True,
                    )
                except PermissionError as e:
                    self.logging("       File actually opened:" + repr(e))
                    continue

                if detailed_stats:
                    self.detailed_stats(
                        csv_path,
                        csv_file,
                        csv_file
                        + ".csv"
                        + CALCULATIONS_SUBFOLDER_NAME
                        + self.output_suffix,
                    )

            result = "***    Done: {} csv files for      {}".format(
                len(csv_list), self.file_path
            )

        else:
            result = "---    Skip: no csv files for      {}".format(self.file_path)

        csv_list = None
        self.logging(result)
        return result


class DerivativesCalc(Helpers, Logging):

    def compute_gaussian_derivatives(self, image_stack, start, end, sigma):

        # Compute derivatives along z-axis
        dz = gaussian_filter(image_stack[start:end], sigma=sigma, order=[1, 0, 0])

        return dz

    def process_tiff_stack(self, start, end):

        assert (
            end - start >= 2
        ), "!!! Error: {} - Too small interval to differentiate between frames {} and {}. ".format(
            self.file_path, start, end
        )
        assert start > 0, "!!! Error: Set the correct timing"
        assert end < self.n_frames, "!!! Error: Timing is out of movie duration"

        # self.logging("Frames ", start, ":", end)

        # Initialize a list to store the derivative images
        derivatives = self.compute_gaussian_derivatives(
            self.img, start, end, DERIVATIVES_SIGMA
        )

        # Average the derivatives to create a single image
        output_derivative = np.mean(np.maximum(derivatives, 0), axis=0)

        return output_derivative

    def average_sequence_responses(self, s_step_shift):

        sequence_stack = []
        for i in range(self.start_from_epoch, self.n_epochs + self.start_from_epoch):
            start = self.sec_to_frame(
                self.s_trig_time + (i * self.s_epoch_duration) + s_step_shift
            )
            end = self.sec_to_frame(
                self.s_trig_time
                + (i * self.s_epoch_duration)
                + s_step_shift
                + self.s_resp_duration
            )

            # Adjust for derivatives frame lag
            start += DERIVATIVES_FRAME_LAG
            end += DERIVATIVES_FRAME_LAG

            sequence_stack.append(self.process_tiff_stack(start, end))
            self.derivatives_frames_log.append((start, end))

        self.result = np.average(sequence_stack, axis=0)

    def calc_sequence(self, i, filename_ending):

        s_step_shift = self.s_step_duration * i
        self.average_sequence_responses(s_step_shift)

        metadata = {
            "axes": "YX",
            "min": 0,
            "max": np.max(self.result),
            " DERIVATIVES_SIGMA": DERIVATIVES_SIGMA,
        }

        self.save_tiff(
            os.path.join(
                self.path,
                self.file + DERIVATIVES_SUBFOLDER_NAME + self.output_suffix,
                filename_ending,
            ),
            self.result,
            metadata=metadata,
        )

    def derivatives_calculate(
        self,
    ):

        stims_overlap_png = True
        stims_overlap_tif = True
        ratio_heatmap = True
        stims_substracted = True
        stims_substracted_diff = True

        self.derivatives_frames_log = []

        os.makedirs(
            self.file_path + DERIVATIVES_SUBFOLDER_NAME + self.output_suffix + "/",
            exist_ok=True,
        )

        # Open the TIFF image stack
        # rewrite self.n_frames to get actual length of the stack, not just a number from metadata
        self.img = tifffile.imread(self.file_path)
        self.n_frames = len(self.img)

        s1s2_name_ending = "_DERIVATIVES_auto_{}&{}_{}.tif".format(
            self.stim_1_name, self.stim_2_name, self.output_suffix
        )
        s1_name_ending = "_DERIVATIVES_auto_{}_{}.tif".format(
            self.stim_1_name, self.output_suffix
        )
        s2_name_ending = "_DERIVATIVES_auto_{}_{}.tif".format(
            self.stim_2_name, self.output_suffix
        )

        for i, (A, C) in enumerate(zip(self.drs_pattern[0], self.drs_pattern[1])):
            match (A, C):
                case (1, 1):
                    self.logging(
                        f"Sequence {self.stim_1_name}+{self.stim_2_name} done!"
                    )
                    self.calc_sequence(i, s1s2_name_ending)
                case (1, 0):
                    self.logging(f"Sequence {self.stim_1_name} done!")
                    self.calc_sequence(i, s1_name_ending)
                case (0, 1):
                    self.logging(f"Sequence {self.stim_2_name} done!")
                    self.calc_sequence(i, s2_name_ending)
                case (0, 0):
                    pass
                case (None, None):
                    self.calc_sequence(i, "DERIVATIVES_auto_.tif")

        self.logging(
            f"Taken {self.n_epochs} epochs: {self.start_from_epoch + 1} to {self.n_epochs + self.start_from_epoch}\n"
        )

        if DEBUG:

            x = [i for i in range(self.n_frames)]
            y = [np.mean(np.mean(self.img, axis=1), axis=1)]

            last_epoch_time = (
                self.s_trig_time
                + (self.start_from_epoch + self.n_epochs - 1) * self.s_epoch_duration
            )
            start = self.sec_to_frame(last_epoch_time - self.s_step_duration)
            end = self.sec_to_frame(last_epoch_time + self.s_step_duration * 2)
            yf = [np.mean(np.mean(self.img, axis=1)[start:end], axis=1)]

            lines1 = [
                [i for i in range(*sorted(self.derivatives_frames_log)[j])]
                for j in range(len(self.derivatives_frames_log))
            ]
            lines1 = np.array(lines1).flatten()

            events1 = self.derivatives_frames_log.copy()
            events1.extend(lines1.tolist())

            lines2 = [
                [i for i in range(*sorted(self.derivatives_frames_log)[-j])]
                for j in range(1, self.n_steps_per_epoch + 1)
            ]
            lines2 = np.array(lines2).flatten()

            events2 = sorted(self.derivatives_frames_log)[
                -self.n_steps_per_epoch :
            ].copy()
            events2.extend(lines2.tolist())

            self.plot_traces(
                x,
                y,
                events1,
                f"{self.path}/{self.file}{DERIVATIVES_SUBFOLDER_NAME}{self.output_suffix}/debug_selected_epoch.svg",
                linewidth=0.05,
                fillcolor="magenta",
                event_linecolor="w",
                event_linestyle="-",
                avg_linecolor="darkcyan",
                alpha=1,
                dpi=800,
            )

            self.plot_traces(
                x,
                y,
                self.derivatives_frames_log,
                f"{self.path}/{self.file}{DERIVATIVES_SUBFOLDER_NAME}{self.output_suffix}/debug_selected_epoch.png",
                linewidth=0.5,
                fillcolor="magenta",
                event_linecolor="w",
                event_linestyle="-",
                avg_linecolor="darkcyan",
                alpha=1,
                dpi=100,
            )

            self.plot_traces(
                x[start:end],
                yf,
                events2,
                f"{self.path}/{self.file}{DERIVATIVES_SUBFOLDER_NAME}{self.output_suffix}/debug_synchronization.png",
                linewidth=0.5,
                fillcolor="magenta",
                event_linecolor="w",
                event_linestyle="-",
                avg_linecolor="darkcyan",
                alpha=1,
                dpi=150,
            )

        # Different stims - differrent colors
        merger_s1s2_s2 = TifDerivativeProcess(
            os.path.join(
                self.path, self.file + DERIVATIVES_SUBFOLDER_NAME + self.output_suffix
            ),
            s1s2_name_ending,
            s2_name_ending,
            s1s2_name_ending,
            "_{2}_{1}-green_{0}&{1}-magenta_auto.tif".format(
                self.stim_1_name, self.stim_2_name, self.output_suffix
            ),
            self.stim_1_name,
            self.stim_2_name,
            self.output_suffix,
            ratio_heatmap=ratio_heatmap,
            stims_overlap_png=stims_overlap_png,
            stims_overlap_tif=stims_overlap_tif,
            stims_substracted=False,
            stims_substracted_diff=False,
        )

        merger_s1s2_s2.process_directory()
        del merger_s1s2_s2

        # Different stims - differrent colors
        # merger_s1_s2 = TifDerivativeProcess(
        #     os.path.join(
        #         self.path, self.file + DERIVATIVES_SUBFOLDER_NAME + self.output_suffix
        #     ),
        #     s2_name_ending,
        #     s1_name_ending,
        #     s1_name_ending,
        #     "_{2}_{1}-red_{0}-cyan_auto.tif".format(
        #         self.stim_1_name, self.stim_2_name, self.output_suffix
        #     ),
        #     self.stim_1_name,
        #     self.stim_2_name,
        #     self.output_suffix,
        #     ratio_heatmap=ratio_heatmap,
        #     stims_overlap_png=stims_overlap_png,
        #     stims_overlap_tif=stims_overlap_tif,
        #     stims_substracted=stims_substracted,
        #     stims_substracted_diff=stims_substracted_diff,
        # )

        # merger_s1_s2.process_directory()
        # del merger_s1_s2


class Movie(DerivativesCalc, TracesCalc, Logging):

    def __init__(
        self,
        file_path,
        working_dir,
        output_suffix,
        resp_duration,
        drs_pattern,
        step_duration,
        n_epochs,
        start_from_epoch,
        trig_number,
        time_before_trig,
        time_after_trig,
        baseline_duraton,
        relative_values,
        mean_col_order,
        cols_per_roi,
        stim_1_name,
        stim_2_name,
        sigmas_treshold,
        vertical_shift,
        vertical_shift_of_trig,
        SD_filter_of_trig,
        v_shifts={},
        filters={},
        **misc,
    ):

        self.file_path = working_dir + file_path
        self.path = os.path.split(self.file_path)[0]
        self.file = os.path.split(self.file_path)[1]
        self.filename_suffix, self.file_nosuffix = self.__calculate_suffix_and_nosuffix(
            self.file_path
        )
        self.output_suffix = output_suffix

        self.sigmas_treshold = sigmas_treshold
        self.vertical_shift = vertical_shift
        self.vertical_shift_of_trig = vertical_shift_of_trig
        self.SD_filter_of_trig = SD_filter_of_trig

        self.relative_values = relative_values
        self.mean_col_order = mean_col_order
        self.cols_per_roi = cols_per_roi

        self.stim_1_name = stim_1_name
        self.stim_2_name = stim_2_name

        self.result = None
        self.n_frames = None

        # Movie timings

        Parser = MetadataParser()
        self.events, self.spf, self.s_movie_duration, self.n_frames = Parser.Parse(
            self.path, self.file_nosuffix
        )

        self.trig_number = trig_number - 1
        self.event = self.events[self.trig_number]
        self.event_name = self.events[self.trig_number][0]
        self.s_trig_time = self.events[self.trig_number][1]

        self.spf += self.spf * SYNC_COEF
        self.fps = 1 / self.spf

        self.s_resp_duration = resp_duration
        self.drs_pattern = drs_pattern
        self.s_step_duration = step_duration
        self.n_steps_per_epoch = len(self.drs_pattern[0])
        self.n_epochs = n_epochs
        self.start_from_epoch = start_from_epoch if start_from_epoch != 0 else 1
        self.start_from_epoch -= 1

        self.s_epoch_duration = self.s_step_duration * self.n_steps_per_epoch

        self.time_before_trig = time_before_trig
        self.time_after_trig = time_after_trig
        self.baseline_duraton = baseline_duraton

        # cache and return

        self.v_shifts = v_shifts
        self.filters = filters

        self.v_shifts_return = {}
        self.filters_return = {}
        self.ampls_return = {}
        self.aucs_return = {}

        Logging.__init__(
            self,
        )

        self.logging(
            "\nFile: {} \nMovie duration: {} \nn frames: {} \nSampling interval, s: {} \nTrigger time, s: {}".format(
                self.file_path,
                self.s_movie_duration,
                self.n_frames,
                self.spf,
                self.s_trig_time,
            )
        )

    def __calculate_suffix_and_nosuffix(self, file_full_path):
        # Get the directory from the given file's full path

        file_full_path = os.path.abspath(
            os.path.normpath(os.path.splitext(file_full_path)[0])
        )

        dir_path = os.path.dirname(file_full_path)
        # Get the given file's name
        given_file = os.path.basename(file_full_path)

        # List all .txt files in the directory
        txt_files = [
            os.path.abspath(os.path.normpath(os.path.join(dir_path, f)))
            for f in os.listdir(dir_path)
            if f.endswith(".txt")
        ]

        assert (
            txt_files
        ), f"!!! Error: No .txt metadata file found in directory {dir_path}."

        # Find the longest common prefix among the given file and txt files
        common_prefixes = [
            os.path.commonprefix([file_full_path, txt_file]) for txt_file in txt_files
        ]

        file_nosuffix_with_path = max(common_prefixes, key=len).rstrip("_")

        # Remove the directory path from the common prefix
        file_nosuffix = os.path.basename(file_nosuffix_with_path)

        # Determine the suffix from the given file
        filename_suffix = os.path.basename(
            file_full_path[len(file_nosuffix_with_path) :]
        )

        return filename_suffix, file_nosuffix


class TifDerivativeProcess(Helpers):

    def __init__(
        self,
        dir,
        red_name_ending,
        green_name_ending,
        blue_name_ending,
        output_name_ending,
        stim_1_name,
        stim_2_name,
        output_suffix,
        ratio_heatmap=True,
        stims_overlap_png=True,
        stims_overlap_tif=True,
        stims_substracted=True,
        stims_substracted_diff=True,
    ):
        self.dir = dir
        self.red_name_ending = red_name_ending
        self.green_name_ending = green_name_ending
        self.blue_name_ending = blue_name_ending
        self.output_name_ending = output_name_ending
        self.stim_1_name = stim_1_name
        self.stim_2_name = stim_2_name
        self.output_suffix = output_suffix

        self.ratio_heatmap = ratio_heatmap
        self.stims_overlap_png = stims_overlap_png
        self.stims_overlap_tif = stims_overlap_tif
        self.stims_substracted = stims_substracted
        self.stims_substracted_diff = stims_substracted_diff

    def __make_png(self, channels, output_filename):
        for i in range(3 - len(channels)):
            channels.append(np.zeros_like(channels[0]))

        channels = np.array(channels)
        rgb_array_normalized = np.stack(
            [
                (channel - channels.min()) / (channels.max() - channels.min())
                for channel in channels
            ],
            axis=-1,
        )
        rgb_image = Image.fromarray((rgb_array_normalized * 255).astype("uint8"), "RGB")
        try:
            rgb_image.save(output_filename)
        except PermissionError as e:
            pass
            print("PermissionError:", e)

    def __process_derivative_images(
        self,
        red_channel_path,
        green_channel_path,
        blue_channel_path,
        output_path,
    ):
        channels = []

        if red_channel_path:
            red_channel = Image.open(red_channel_path)
            red_array = np.array(red_channel).astype(np.float32)
            channels.append(red_array)

        if green_channel_path:
            green_channel = Image.open(green_channel_path)
            green_array = np.array(green_channel).astype(np.float32)
            channels.append(green_array)

        if blue_channel_path:
            blue_channel = Image.open(blue_channel_path)
            blue_array = np.array(blue_channel)
            channels.append(blue_array)

        # Stack the arrays along the first axis to create a multi-channel image
        multi_channel_array = np.stack(channels, axis=0)

        # Save the multi-channel image in ImageJ format
        if self.stims_overlap_tif:
            try:
                self.save_tiff(
                    output_path + "stims_overlap" + self.output_name_ending,
                    multi_channel_array,
                    metadata={"axes": "CYX", "mode": "composite"},
                )
            except PermissionError as e:
                pass
                print("PermissionError:", e)

        # Save the image as a PNG file
        if self.stims_overlap_png:
            self.__make_png(
                multi_channel_array,
                output_path + "stims_overlap" + self.output_name_ending[:-4] + ".png",
            )

        # make heatmap and save as a PNG file
        if self.ratio_heatmap:
            self.__create_ratio_heatmap(channels, output_path, matplotlib_graph=True)

        # Crerating Stims Substracted images
        if self.stims_substracted:
            self.__create_substracted_image(
                channels[:2:1], output_path, self.stim_1_name, color="darkcyan"
            )
            self.__create_substracted_image(
                channels[1::-1], output_path, self.stim_2_name, color="darkred"
            )

        # Crerating stims Diff image
        if self.stims_substracted_diff:
            self.__create_diff_image(channels[:2], output_path)

    def __create_ratio_heatmap(self, channels, output_path, matplotlib_graph=False):
        # Crerating Heatmap
        # Calculate the ratio image if red and green channels are available
        if len(channels) >= 2:
            image = np.divide(
                channels[1],
                channels[0],
                out=np.zeros_like(channels[0]),
                where=channels[0] != 0,
            )
            image = np.clip(image, 0, np.max(image))

            # Save the ratio image as a single-frame TIFF file with inferno LUT metadata
            output_filename = output_path + "ratio_of_inhibition" + "_heatmap.tif"

            metadata = {
                "axes": "YX",
                "min": 1,
                "max": 4,  # np.max(image) * 0.73
            }

            try:
                # tifffile.imwrite(output_filename, image.astype(np.float32), imagej=True, metadata=metadata)
                self.save_tiff(output_filename, image, metadata=metadata)
                # self.logging(f"Created heatmap image: {output_filename}")

            except PermissionError as e:
                print("PermissionError:", e)

            if matplotlib_graph:
                # Save the ratio image as a heatmap in PNG format using matplotlib
                image = np.clip(image, 1, 4)
                output_filename = output_path + "ratio_of_inhibition" + "_heatmap.png"
                enlarged_shape = (int(image.shape[1] * 1.0), int(image.shape[0] * 1.0))
                fig, ax = plt.subplots(
                    figsize=(enlarged_shape[0] / 100, enlarged_shape[1] / 100), dpi=165
                )

                ax.imshow(
                    image, cmap="inferno", interpolation="bicubic", extent=[0, 1, 0, 1]
                )
                ax.set_position([0.02, 0.02, 0.98, 0.98])
                ax.axis("off")
                fig.patch.set_facecolor("white")
                cbar = plt.colorbar(
                    ax.imshow(
                        image,
                        cmap="inferno",
                        interpolation="bicubic",
                        extent=[0, 1, 0, 1],
                    ),
                    ax=ax,
                )
                cbar.set_label("C to A+C responses ratio", rotation=90, labelpad=5)
                plt.savefig(output_filename, bbox_inches="tight", pad_inches=0)
                plt.close()

    def __create_substracted_image(
        self, channels, output_path, stim, color="k", bins=1024, histogram_xlim=7
    ):
        # Crerating Substracted images
        # Calculate the substraction image if red and green channels are available
        # then set up min pixel values to 0
        if len(channels) >= 2:
            image = np.subtract(channels[1], channels[0])
            image = np.clip(image, 0, np.max(image))

            # Get the name of that directory of experiment day
            two_up_path = os.path.dirname(os.path.dirname(output_path))
            directory_name = os.path.basename(two_up_path)

            # Save the ratio image as a single-frame TIFF file with inferno LUT metadata
            output_filename = (
                output_path
                + "resp_to_stim_"
                + stim
                + "_"
                + self.output_suffix
                + "_"
                + directory_name
                + "_"
                + ".tif"
            )

            metadata = {
                "axes": "YX",
                "min": 0,
                "max": 50,  # np.max(image)
            }

            try:
                # tifffile.imwrite(output_filename, image.astype(np.float32), imagej=True, metadata=metadata)
                self.save_tiff(output_filename, image, metadata=metadata)
                # self.logging(f"Created heatmap image: {output_filename}")

                # Flatten for histogram
                values = image.flatten()
                values = values[values > 0]

                # Build histogram
                # plt.style.use('ggplot')
                fig, ax = plt.subplots(dpi=90, figsize=(3, 3))
                ax.hist(values, bins=bins, color=color)
                ax.set_xlim(0, histogram_xlim)
                ax.set_xlabel("Resp. Intensity \nto Stim " + stim + self.output_suffix)

                # Create histogram filename
                dirname = os.path.dirname(output_filename)
                basename = os.path.basename(output_filename)
                stem, _ = os.path.splitext(basename)
                hist_filename = os.path.join(dirname, stem + "_histogram.png")

                # Save PNG
                fig.savefig(hist_filename, bbox_inches="tight")
                plt.close(fig)

            except PermissionError as e:
                print("PermissionError:", e)

    def __create_diff_image(self, channels, output_path):
        # Crerating Diff image
        # Calculate the substraction image if red and green channels are available
        # then set up min pixel values to 0
        # and merge them into single diff img
        if len(channels) >= 2:
            image1 = np.subtract(channels[0], channels[1])
            image1 = np.clip(image1, 0, np.max(image1))

            image2 = np.subtract(channels[1], channels[0])
            image2 = np.clip(image2, 0, np.max(image2))

            channels = [image1, image2, image2]
            multi_channel_array = np.stack(channels, axis=0)

            # Save the ratio image as a single-frame TIFF file with inferno LUT metadata
            output_filename = (
                output_path
                + "diff_between_"
                + self.stim_2_name
                + "-red_"
                + self.stim_1_name
                + "-cyan_"
                + self.output_suffix
                + ".tif"
            )

            metadata = {
                "axes": "CYX",
                "mode": "composite",
                "min": 0,
                "max": 50,  # np.max(image)
            }

            try:
                # tifffile.imwrite(output_filename, image.astype(np.float32), imagej=True, metadata=metadata)
                self.save_tiff(output_filename, multi_channel_array, metadata=metadata)
                # self.logging(f"Created heatmap image: {output_filename}")

            except PermissionError as e:
                print("PermissionError:", e)

            self.__make_png(
                multi_channel_array,
                output_path
                + "diff_between_"
                + self.stim_2_name
                + "-red_"
                + self.stim_1_name
                + "-cyan_"
                + self.output_suffix
                + ".png",
            )

    def process_directory(
        self,
    ):
        for root, _, files in os.walk(self.dir):
            red_files = [f for f in files if f.endswith(self.red_name_ending)]
            green_files = [f for f in files if f.endswith(self.green_name_ending)]

            for red_file in red_files:
                base_name = red_file[: -len(self.red_name_ending)]
                matching_green_file = base_name + self.green_name_ending
                matching_blue_file = base_name + self.blue_name_ending

                if matching_green_file in green_files:
                    red_path = (
                        os.path.join(root, red_file) if self.red_name_ending else None
                    )
                    green_path = (
                        os.path.join(root, matching_green_file)
                        if self.green_name_ending
                        else None
                    )
                    blue_path = (
                        os.path.join(root, matching_blue_file)
                        if self.blue_name_ending
                        else None
                    )
                    output_path = os.path.join(root, base_name)

                    self.__process_derivative_images(
                        red_path, green_path, blue_path, output_path
                    )
                    # self.logging("\nCreated hyperstack image: {}".format(output_path))


class MetadataParser:

    def Parse(self, path, file):

        with open("{}/{}.txt".format(path, file), "r") as file:

            trigger = '"[Event '
            strings = file.readlines()

            string = strings[12]
            if not string.startswith('"T Dimension"'):
                raise ValueError

            n_slides = int(re.findall(r'\	"([^[]*), ', string)[0])
            t_duration = float(re.findall(r"- ([^[]*)\ \[", string)[0])
            t_resolution = t_duration / n_slides

            events = [
                (strings[i + 1][18:-2], float(strings[i + 2][15:-6]) / 1000)
                for i, line in enumerate(strings)
                if trigger in line
            ]

        return events, t_resolution, t_duration, n_slides


class PostprocessingSummary(Helpers):

    def __init__(
        self,
    ):
        pass

    def reformat_dict(self, data, col=1):
        from collections import defaultdict

        grouped = defaultdict(list)

        for key, value in data.items():
            name, order_str, suffix = key.split("$")
            order = int(order_str)
            # insert suffix as a name of column in summary
            if value[0][0] != suffix:
                value[0].insert(0, suffix)
            if value[1][0] != suffix:
                value[1].insert(0, suffix)
            if value[2][0] != suffix:
                value[2].insert(0, suffix)

            grouped[name].append((order, value))

        # Sort by the integer order and extract only the lists
        reformatted = {
            name: [v[col] for _, v in sorted(values, key=lambda x: x[0])]
            for name, values in grouped.items()
        }

        return reformatted

    def save_dict_to_xlsx_files(self, data, suffix=""):
        """
        Takes a dict where each key is a file path (.xlsx)
        and each value is a list of lists representing columns.
        Writes each value into a separate Excel file.
        Empty lists or zeros produce empty columns.
        """
        for filepath, columns in data.items():

            wb = Workbook()
            ws = wb.active
            ws.title = "Data"

            # Find max column height
            max_len = max(
                (len(col) for col in columns if isinstance(col, list)), default=0
            )

            for col_idx, col_data in enumerate(columns, start=1):
                if not isinstance(col_data, list):
                    continue
                for row_idx in range(max_len):
                    # Fill only if valid non-empty/nonzero
                    if row_idx < len(col_data):
                        val = col_data[row_idx]
                        # if val.size == 0:
                        #     continue
                        ws.cell(row=row_idx + 1, column=col_idx, value=val)

            savepath = "{0}.csv{2}/{1}{3}.xlsx".format(
                filepath,
                os.path.dirname(filepath).split("/")[-1],
                SUMMARY_SUBFOLDER_NAME,
                suffix,
            )
            # Ensure directory exists
            os.makedirs(os.path.dirname(savepath), exist_ok=True)

            wb.save(savepath)
            print(f"✅ Summary Saved ", savepath)


def worker(
    item,
    run_derivatives_calculation,
    run_traces_calculation,
    v_shifts={},
    filters={},
    ampls={},
    aucs={},
):

    movie = Movie(item[0], **item[1], v_shifts=v_shifts, filters=filters)

    e1 = ""
    if run_derivatives_calculation:
        try:
            movie.derivatives_calculate()
        except Exception as e:
            e1 = repr(e)
            if DEBUG:
                print(traceback.format_exc())
            pass

    e2 = ""
    if run_traces_calculation:
        try:
            movie.csv_process()
        except Exception as e:
            e2 = repr(e)
            if DEBUG:
                print(traceback.format_exc())
            pass

    # get some results to use them in the next calculations as params
    vertical_shifts = movie.v_shifts_return
    filters = movie.filters_return
    ampls = movie.ampls_return
    suffix = movie.output_suffix
    # aucs = movie.aucs_return

    print(movie.log)

    del movie
    return vertical_shifts, [filters, ampls], item[0] + "_" + suffix, e1, e2


def generate_postprocessing_summary(output):

    bins = {}
    amps = {}
    for i in output:
        bins.update(i[1][0])
        amps.update(i[1][1])

    summary = PostprocessingSummary()
    bins_st1 = summary.reformat_dict(bins, col=1)
    bins_st2 = summary.reformat_dict(bins, col=2)
    amps_st1 = summary.reformat_dict(amps, col=1)
    amps_st2 = summary.reformat_dict(amps, col=2)

    amps_filtered1_st1 = {}
    amps_filtered1_st2 = {}
    amps_filtered2_st1 = {}
    amps_filtered2_st2 = {}
    amps_filtered3_st1 = {}
    amps_filtered3_st2 = {}

    h = Helpers()

    for key, value in bins_st1.items():
        amps_filtered1_st1[key] = [
            h.filter_list(i, bins_st1[key][0], replace=True, replace_with="")
            for i in amps_st1[key]
        ]
    for key, value in bins_st2.items():
        amps_filtered1_st2[key] = [
            h.filter_list(i, bins_st2[key][0], replace=True, replace_with="")
            for i in amps_st2[key]
        ]

    for key, value in bins_st1.items():
        amps_filtered2_st1[key] = [
            h.filter_list(
                i,
                np.logical_and(
                    np.array(bins_st1[key][0], dtype=np.bool_),
                    np.array(bins_st1[key][1], dtype=np.bool_),
                ),
                replace=True,
                replace_with="",
            )
            for i in amps_st1[key]
        ]

    for key, value in bins_st2.items():
        amps_filtered2_st2[key] = [
            h.filter_list(
                i,
                np.logical_and(
                    np.array(bins_st2[key][0], dtype=np.bool_),
                    np.array(bins_st2[key][1], dtype=np.bool_),
                ),
                replace=True,
                replace_with="",
            )
            for i in amps_st2[key]
        ]

    for key, value in bins_st1.items():
        amps_filtered3_st1[key] = [
            h.filter_list(
                i,
                np.logical_and(
                    np.array(bins_st1[key][1], dtype=np.bool_),
                    np.array(bins_st1[key][2], dtype=np.bool_),
                ),
                replace=True,
                replace_with="",
            )
            for i in amps_st1[key]
        ]

    for key, value in bins_st2.items():
        amps_filtered3_st2[key] = [
            h.filter_list(
                i,
                np.logical_and(
                    np.array(bins_st2[key][1], dtype=np.bool_),
                    np.array(bins_st2[key][2], dtype=np.bool_),
                ),
                replace=True,
                replace_with="",
            )
            for i in amps_st2[key]
        ]

    # create summary xlsx
    table_st1 = {}
    table_st2 = {}
    for key, value in bins_st1.items():
        table_st1[key] = (
            bins_st1[key]
            + [""]
            + amps_st1[key]
            + ["1 only (roi responded to):"]
            + amps_filtered1_st1[key]
            + ["1 AND 2 (roi responded to):"]
            + amps_filtered2_st1[key]
            + ["2 AND 3 (roi responded to):"]
            + amps_filtered3_st1[key]
        )
        table_st2[key] = (
            bins_st2[key]
            + [""]
            + amps_st2[key]
            + ["1 only (roi responded to):"]
            + amps_filtered1_st2[key]
            + ["1 AND 2 (roi responded to):"]
            + amps_filtered2_st2[key]
            + ["2 AND 3 (roi responded to):"]
            + amps_filtered3_st2[key]
        )

    summary.save_dict_to_xlsx_files(table_st1, suffix="_stim1_summary")
    summary.save_dict_to_xlsx_files(table_st2, suffix="_stim2_summary")

    # statistical analysis and plotting
    def statplot(data, key, suffix, groups_name, plot_title="", test="wilcoxon"):
        analysis = AutoStatLib.StatisticalAnalysis(
            data,
            paired=True,
            tails=2,
            popmean=0,
            posthoc=True,
            verbose=False,
            groups_name=groups_name,
        )
        if test == "friedman":
            analysis.RunFriedman()
        else:
            analysis.RunWilcoxon()
        results = analysis.GetResult()

        if "Samples" in results:
            if test == "friedman":
                plot = AutoStatLib.StatPlots.SwarmStatPlot(
                    results["Samples"],
                    **results,
                    y_label="Amplitude, ΔF/F₀",
                    plot_title=plot_title,
                    print_p_label=False,
                    print_stars=False,
                )
            else:
                plot = AutoStatLib.StatPlots.BarStatPlot(
                    results["Samples"],
                    **results,
                    y_label="Amplitude, ΔF/F₀",
                    plot_title=plot_title,
                    print_p_label=True,
                )
            plot.plot()

            savepath = "{0}.csv{2}/{1}{3}.png".format(
                key, os.path.dirname(key).split("/")[-1], SUMMARY_SUBFOLDER_NAME, suffix
            )

            plot.save(savepath)
            print(f"📈 Graph Saved ", savepath)
            plot.close()

        del analysis

    for key in table_st1.keys():

        data_f1_st1 = amps_filtered1_st1[key]
        statplot(
            data_f1_st1,
            key,
            "_stim1_summary_rois_1_all",
            plot_title="ROIs responded in Ctrl",
            test="friedman",
            groups_name=[i[0] for i in data_f1_st1],
        )
        statplot(
            data_f1_st1[:2],
            key,
            "_stim1_summary_rois_1",
            plot_title="ROIs in Ctrl",
            groups_name=[i[0] for i in data_f1_st1[:2]],
        )

        data_f2_st1 = amps_filtered2_st1[key]
        statplot(
            data_f2_st1,
            key,
            "_stim1_summary_rois_1&2_all",
            plot_title="ROIs responded in Ctrl and CNO",
            test="friedman",
            groups_name=[i[0] for i in data_f2_st1],
        )
        statplot(
            data_f2_st1[:2],
            key,
            "_stim1_summary_rois_1&2",
            plot_title="ROIs in Ctrl & CNO",
            groups_name=[i[0] for i in data_f2_st1[:2]],
        )

        # data_f3_st1 = amps_filtered3_st1[key]
        # statplot(data_f3_st1, key, '_stim1_summary_rois_2&3_all', plot_title='ROIs responded in CNO and Dyn', test='friedman',
        #          groups_name=[i[0] for i in data_f3_st1])
        # statplot(data_f3_st1[:2], key, '_stim1_summary_rois_2&3', plot_title='ROIs in CNO & Dyn',
        #          groups_name=[i[0] for i in data_f3_st1[:2]])

    for key in table_st2.keys():

        data_f1_st2 = amps_filtered1_st2[key]
        statplot(
            data_f1_st2,
            key,
            "_stim2_summary_rois_1_all",
            plot_title="ROIs responded in Ctrl",
            test="friedman",
            groups_name=[i[0] for i in data_f1_st2],
        )
        statplot(
            data_f1_st2[:2],
            key,
            "_stim2_summary_rois_1",
            plot_title="ROIs in Ctrl",
            groups_name=[i[0] for i in data_f1_st2[:2]],
        )

        data_f2_st2 = amps_filtered2_st2[key]
        statplot(
            data_f2_st2,
            key,
            "_stim2_summary_rois_1&2_all",
            plot_title="ROIs responded in Ctrl and CNO",
            test="friedman",
            groups_name=[i[0] for i in data_f2_st2],
        )
        statplot(
            data_f2_st2[:2],
            key,
            "_stim2_summary_rois_1&2",
            plot_title="ROIs in Ctrl & CNO",
            groups_name=[i[0] for i in data_f2_st2[:2]],
        )

        # data_f3_st2 = amps_filtered3_st2[key]
        # statplot(data_f3_st2, key, '_stim2_summary_rois_2&3_all', plot_title='ROIs responded in CNO and Dyn', test='friedman',
        #          groups_name=[i[0] for i in data_f3_st2])
        # statplot(data_f3_st2[:2], key, '_stim1_summary_rois_2&3', plot_title='ROIs in CNO & Dyn',
        #          groups_name=[i[0] for i in data_f3_st2[:2]])


def main(
    working_dir=s.working_dir,
    to_do_list=s.to_do_list,
    run_derivatives_calculation=s.run_derivatives_calculation,
    run_traces_calculation=s.run_traces_calculation,
    resp_duration=s.resp_duration,
    step_duration=s.step_duration,
    n_epochs=s.n_epochs,
    drs_pattern=s.drs_pattern,
    stim_1_name=s.stim_1_name,
    stim_2_name=s.stim_2_name,
    relative_values=s.relative_values,
    mean_col_order=s.mean_col_order,
    cols_per_roi=s.cols_per_roi,
    time_before_trig=s.time_before_trig,
    baseline_duraton=s.baseline_duraton,
    sigmas_treshold=s.sigmas_treshold,
    vertical_shift=s.vertical_shift,
    vertical_shift_of_trig=s.vertical_shift_of_trig,
    SD_filter_of_trig=s.SD_filter_of_trig,
    time_after_trig=s.time_after_trig,
    multiprocessing=s.multiprocessing,
    processes_limit=s.processes_limit,
):

    for item in to_do_list:

        # setting default parameters if they are missing in the to_do_list
        item[1].setdefault("output_suffix", "")
        item[1].setdefault("working_dir", working_dir)
        item[1].setdefault("resp_duration", resp_duration)
        item[1].setdefault("drs_pattern", drs_pattern)
        item[1].setdefault("step_duration", step_duration)
        item[1].setdefault("n_epochs", n_epochs)
        item[1].setdefault("start_from_epoch", 1)
        item[1].setdefault("trig_number", 1)
        item[1].setdefault("time_before_trig", time_before_trig)
        item[1].setdefault("time_after_trig", time_after_trig)
        item[1].setdefault("baseline_duraton", baseline_duraton)
        item[1].setdefault("relative_values", relative_values)
        item[1].setdefault("mean_col_order", mean_col_order)
        item[1].setdefault("cols_per_roi", cols_per_roi)
        item[1].setdefault("stim_1_name", stim_1_name)
        item[1].setdefault("stim_2_name", stim_2_name)
        item[1].setdefault("sigmas_treshold", sigmas_treshold)
        item[1].setdefault("vertical_shift", vertical_shift)
        item[1].setdefault("vertical_shift_of_trig", vertical_shift_of_trig)
        item[1].setdefault("SD_filter_of_trig", SD_filter_of_trig)

    if multiprocessing:
        import multiprocessing as mp

        cores = mp.cpu_count()  # CPU cores count
        jobs = len(to_do_list)  # jobs to do count

        if processes_limit == 0:
            processes_limit = 1000

        threads = min(cores - 2, jobs, processes_limit)
        try:
            pool = mp.Pool(threads)
        except ValueError:
            print("No one file listed, there is nothing to do.")
            return 0

        v_shifts = {}
        filters = {}

        def spread_jobs(jobs):
            processes = [
                pool.apply_async(
                    worker,
                    args=(
                        item,
                        run_derivatives_calculation,
                        run_traces_calculation,
                        v_shifts,
                        filters,
                    ),
                )
                for item in jobs
            ]
            output = [p.get() for p in processes]
            return output

        print("\nParallel processing mode activated:")
        print("Please, ensure if you have enough RAM for multiprocessing.")
        print(
            'If processing went wrong, please, use "processes_limit" option in the settings.py'
        )
        print(
            "{0} cpu cores per queue of {1} files found, pool of {2} processes created.".format(
                cores, jobs, threads
            )
        )
        print("\nJob started...\n")

        # separating the jobs that have to be done first,
        # because they do not use the results of the previous calculations
        do_first = [
            i
            for i in to_do_list
            if not (i[1]["vertical_shift_of_trig"] or i[1]["SD_filter_of_trig"])
        ]
        do_second = [
            i
            for i in to_do_list
            if (i[1]["vertical_shift_of_trig"] or i[1]["SD_filter_of_trig"])
        ]

        output = spread_jobs(do_first)

        for i in output:
            v_shifts.update(i[0])
            filters.update(i[1][0])

        output.extend(spread_jobs(do_second))

        errors = [
            [
                i[2] + ":\n",
                "derivatives : " + i[3] + "\n",
                "calculations:   " + i[4] + "\n",
                "\n",
            ]
            for i in output
            if (i[3] or i[4])
        ]
        msg = (
            [item for sublist in errors for item in sublist]
            if errors
            else ["✅ --no errors--\n"]
        )

        print("\n\nAll done! ✨ 🍰 ✨\n")
        print("Errors: \n")
        print(*msg)

    else:
        output = []
        for item in to_do_list:
            v_shifts = {}
            filters = {}
            output.append(
                worker(
                    item,
                    run_derivatives_calculation,
                    run_traces_calculation,
                    v_shifts,
                    filters,
                )
            )
            v_shifts = output[-1][0]
            filters = output[-1][1][0]
            # ampls = output[-1][1][1]
            # aucs = output[-1][1][2]

            if output[-1][3]:
                print(output[-1][3])
            if output[-1][4]:
                print(output[-1][4])

        print("\n\nAll done! ✨ 🍰 ✨\n")

    if postprocessing_summary and run_traces_calculation:
        try:
            generate_postprocessing_summary(output)
        except IndexError as e:
            print(
                "Postprocesssing: Index error - only one timeframe in a boundle so there is nothing to compare"
            )


if __name__ == "__main__":
    print("Set the parameters in the launcher file and run it to execute the script")
