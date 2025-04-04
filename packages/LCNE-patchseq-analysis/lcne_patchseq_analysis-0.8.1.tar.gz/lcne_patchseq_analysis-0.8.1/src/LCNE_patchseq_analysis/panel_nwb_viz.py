"""
Panel-based visualization tool for navigating and visualizing patch-seq NWB files.

To start the app, run:
panel serve panel_nwb_viz.py --dev --allow-websocket-origin=codeocean.allenneuraldynamics.org
"""

import matplotlib.pyplot as plt
import numpy as np
import panel as pn
import param

from LCNE_patchseq_analysis.data_util.metadata import load_ephys_metadata
from LCNE_patchseq_analysis.data_util.nwb import PatchSeqNWB


class PatchSeqNWBApp(param.Parameterized):
    """
    Object-Oriented Panel App for navigating NWB files.
    Encapsulates metadata loading, sweep visualization, and cell selection.
    """

    class DataHolder(param.Parameterized):
        ephys_roi_id = param.String(default="")

    def __init__(self):
        # Holder for currently selected cell ID.
        self.data_holder = PatchSeqNWBApp.DataHolder()

        # Load and prepare metadata.
        self.df_meta = load_ephys_metadata()
        self.df_meta = self.df_meta.rename(
            columns={col: col.replace("_tab_master", "") for col in self.df_meta.columns}
        ).sort_values(["injection region"])
        self.cell_key = [
            "Date",
            "jem-id_cell_specimen",
            "ephys_roi_id",
            "ephys_qc",
            "LC_targeting",
            "injection region",
        ]

        # Create the cell selector panel once.
        self.cell_selector_panel = self.create_cell_selector_panel()

    @staticmethod
    def update_plot(raw, sweep):
        """
        Extracts a slice of data from the NWB file and returns a matplotlib figure.
        """
        trace = raw.get_raw_trace(sweep)
        stimulus = raw.get_stimulus(sweep)
        time = np.arange(len(trace)) * raw.dt_ms

        fig, ax = plt.subplots(2, 1, figsize=(6, 4), gridspec_kw={"height_ratios": [3, 1]})
        ax[0].plot(time, trace)
        ax[0].set_title(f"Sweep number {sweep}")
        ax[0].set(ylabel="Vm (mV)")

        ax[1].plot(time, stimulus)
        ax[1].set(xlabel="Time (ms)", ylabel="I (pA)")
        ax[0].label_outer()

        plt.close(fig)  # Prevent duplicate display in Panel.
        return fig

    @staticmethod
    def highlight_selected_rows(row, highlight_subset, color, fields=None):
        """
        Highlight rows based on a subset of values.
        If fields is None, highlight the entire row.
        """
        style = [""] * len(row)
        if row["sweep_number"] in highlight_subset:
            if fields is None:
                return [f"background-color: {color}"] * len(row)
            else:
                for field in fields:
                    style[list(row.keys()).index(field)] = f"background-color: {color}"
        return style

    @staticmethod
    def get_qc_message(sweep, df_sweeps):
        """Return a QC message based on sweep data."""
        if sweep not in df_sweeps["sweep_number"].values:
            return "<span style='color:red;'>Sweep number not found in the jsons!</span>"
        if sweep in df_sweeps.query("passed != passed")["sweep_number"].values:
            return "<span style='background:salmon;'>Sweep terminated by the experimenter!</span>"
        if sweep in df_sweeps.query("passed == False")["sweep_number"].values:
            return (
                f"<span style='background:yellow;'>Sweep failed QC! "
                f"({df_sweeps[df_sweeps.sweep_number == sweep].reasons.iloc[0][0]})</span>"
            )
        return "<span style='background:lightgreen;'>Sweep passed QC!</span>"

    def create_sweep_panel(self, ephys_roi_id=""):
        """
        Builds and returns the sweep visualization panel for a single cell.
        """
        if ephys_roi_id == "":
            return pn.pane.Markdown("Please select a cell from the table above.")

        # Load the NWB file for the selected cell.
        raw_this_cell = PatchSeqNWB(ephys_roi_id=ephys_roi_id)

        # Create a slider widget to navigate sweeps.
        slider = pn.widgets.IntSlider(
            name="Sweep number", start=0, end=raw_this_cell.n_sweeps - 1, value=0
        )
        # Bind the slider to the plotting function.
        plot_panel = pn.bind(
            PatchSeqNWBApp.update_plot, raw=raw_this_cell, sweep=slider.param.value
        )
        mpl_pane = pn.pane.Matplotlib(plot_panel, dpi=400, width=600, height=400)

        # Build a Tabulator for sweep metadata.
        tab_sweeps = pn.widgets.Tabulator(
            raw_this_cell.df_sweeps[
                [
                    "sweep_number",
                    "stimulus_code_ext",
                    "stimulus_name",
                    "stimulus_amplitude",
                    "passed",
                    "num_spikes",
                    "stimulus_start_time",
                    "stimulus_duration",
                    "tags",
                    "reasons",
                    "stimulus_code",
                ]
            ],
            hidden_columns=["stimulus_code"],
            selectable=1,
            disabled=True,  # Not editable
            frozen_columns=["sweep_number"],
            header_filters=True,
            show_index=False,
            height=700,
            width=1000,
            groupby=["stimulus_code"],
            stylesheets=[":host .tabulator {font-size: 12px;}"],
        )

        # Apply conditional row highlighting.
        tab_sweeps.style.apply(
            PatchSeqNWBApp.highlight_selected_rows,
            highlight_subset=raw_this_cell.df_sweeps.query("passed == True")[
                "sweep_number"
            ].tolist(),
            color="lightgreen",
            fields=["passed"],
            axis=1,
        ).apply(
            PatchSeqNWBApp.highlight_selected_rows,
            highlight_subset=raw_this_cell.df_sweeps.query("passed != passed")[
                "sweep_number"
            ].tolist(),
            color="salmon",
            fields=["passed"],
            axis=1,
        ).apply(
            PatchSeqNWBApp.highlight_selected_rows,
            highlight_subset=raw_this_cell.df_sweeps.query("passed == False")[
                "sweep_number"
            ].tolist(),
            color="yellow",
            fields=["passed"],
            axis=1,
        ).apply(
            PatchSeqNWBApp.highlight_selected_rows,
            highlight_subset=raw_this_cell.df_sweeps.query("num_spikes > 0")[
                "sweep_number"
            ].tolist(),
            color="lightgreen",
            fields=["num_spikes"],
            axis=1,
        )

        # --- Two-Way Synchronization between Slider and Table ---
        def update_slider_from_table(event):
            """Update slider when table selection changes."""
            if event.new:
                selected_index = event.new[0]
                new_sweep = raw_this_cell.df_sweeps.loc[selected_index, "sweep_number"]
                slider.value = new_sweep

        tab_sweeps.param.watch(update_slider_from_table, "selection")

        def update_table_selection(event):
            """Update table selection when slider value changes."""
            new_val = event.new
            row_index = raw_this_cell.df_sweeps.index[
                raw_this_cell.df_sweeps["sweep_number"] == new_val
            ].tolist()
            tab_sweeps.selection = row_index

        slider.param.watch(update_table_selection, "value")
        # --- End Synchronization ---

        # Build a reactive QC message panel.
        sweep_msg = pn.bind(
            PatchSeqNWBApp.get_qc_message,
            sweep=slider.param.value,
            df_sweeps=raw_this_cell.df_sweeps,
        )
        sweep_msg_panel = pn.pane.Markdown(sweep_msg, width=600, height=30)

        return pn.Row(
            pn.Column(
                pn.pane.Markdown(f"# {ephys_roi_id}"),
                pn.pane.Markdown("Use the slider to navigate through the sweeps in the NWB file."),
                pn.Column(slider, sweep_msg_panel, mpl_pane),
            ),
            pn.Column(
                pn.pane.Markdown("## Metadata from jsons"),
                tab_sweeps,
            ),
        )

    def create_cell_selector_panel(self):
        """
        Builds and returns the cell selector panel that displays metadata.
        """
        # MultiSelect widget to choose additional columns.
        cols = list(self.df_meta.columns)
        cols.sort()
        selectable_cols = [col for col in cols if col not in self.cell_key]
        col_selector = pn.widgets.MultiSelect(
            name="Add Columns to show",
            options=selectable_cols,
            value=[],  # start with no additional columns
            height=500,
        )

        def add_df_meta_col(selected_columns):
            return self.df_meta[self.cell_key + selected_columns]

        filtered_df_meta = pn.bind(add_df_meta_col, col_selector)
        tab_df_meta = pn.widgets.Tabulator(
            filtered_df_meta,
            selectable=1,
            disabled=True,  # Not editable
            frozen_columns=self.cell_key,
            groupby=["injection region"],
            header_filters=True,
            show_index=False,
            height=500,
            width=1300,
            pagination=None,
            stylesheets=[":host .tabulator {font-size: 12px;}"],
        )

        # When a row is selected, update the current cell (ephys_roi_id).
        def update_sweep_view_from_table(event):
            if event.new:
                selected_index = event.new[0]
                self.data_holder.ephys_roi_id = str(
                    int(self.df_meta.iloc[selected_index]["ephys_roi_id"])
                )

        tab_df_meta.param.watch(update_sweep_view_from_table, "selection")

        cell_selector_panel = pn.Row(
            pn.Column(
                pn.pane.Markdown("## Cell selector"),
                pn.pane.Markdown(f"### Total LC-NE patch-seq cells: {len(self.df_meta)}"),
                width=400,
            ),
            col_selector,
            tab_df_meta,
        )
        return cell_selector_panel

    def main_layout(self):
        """
        Constructs the full application layout.
        """
        pn.config.throttled = False
        pane_cell_selector = self.cell_selector_panel

        # Bind the sweep panel to the current cell selection.
        pane_one_cell = pn.bind(
            self.create_sweep_panel, ephys_roi_id=self.data_holder.param.ephys_roi_id
        )

        layout = pn.Column(
            pn.pane.Markdown("# Patch-seq Ephys Data Navigator\n"),
            pane_cell_selector,
            pn.layout.Divider(),
            pane_one_cell,
        )
        return layout


app = PatchSeqNWBApp()
layout = app.main_layout()
layout.servable()
