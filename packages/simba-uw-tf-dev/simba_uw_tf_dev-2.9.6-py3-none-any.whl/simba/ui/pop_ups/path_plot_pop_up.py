__author__ = "Simon Nilsson"

import os
import threading
from copy import deepcopy
from tkinter import *
from typing import Union

from simba.mixins.config_reader import ConfigReader
from simba.mixins.pop_up_mixin import PopUpMixin
from simba.plotting.path_plotter import PathPlotterSingleCore
from simba.plotting.path_plotter_mp import PathPlotterMulticore
from simba.ui.tkinter_functions import (CreateLabelFrameWithIcon, DropDownMenu,
                                        Entry_Box, SimbaButton, SimbaCheckbox)
from simba.utils.checks import (check_if_string_value_is_valid_video_timestamp,
                                check_if_valid_rgb_str, check_int,
                                check_that_hhmmss_start_is_before_end)
from simba.utils.enums import Formats, Keys, Links
from simba.utils.errors import (FrameRangeError, NoFilesFoundError,
                                NoROIDataError)
from simba.utils.lookups import get_color_dict
from simba.utils.read_write import get_file_name_info_in_directory


class PathPlotPopUp(PopUpMixin, ConfigReader):
    def __init__(self, config_path: Union[str, os.PathLike]):
        ConfigReader.__init__(self, config_path=config_path, read_video_info=False)
        self.machine_results_files = get_file_name_info_in_directory(directory=self.machine_results_dir, file_type=self.file_type)
        self.outlier_corrected_files = get_file_name_info_in_directory(directory=self.outlier_corrected_dir, file_type=self.file_type)
        self.files_found = list(set(list(self.machine_results_files.keys()) + list(self.outlier_corrected_files.keys())))
        if len(self.files_found) == 0:
            raise NoFilesFoundError(msg=f'No data files found inside the {self.outlier_corrected_dir} or the {self.machine_results_dir} directory', source=self.__class__.__name__)
        PopUpMixin.__init__(self, title="CREATE PATH PLOTS", size=(550, 850), icon='path_2')
        self.resolution_options = deepcopy(self.resolutions)
        self.resolution_options.insert(0, "As input")
        self.bg_clr_options = deepcopy(list(self.colors_dict.keys()))
        self.animal_trace_clrs = deepcopy(list(self.colors_dict.keys()))
        self.bg_clr_options.extend(("Video - static frame", "Video - moving frames"))
        self.animal_trace_clrs.append("Custom")
        self.bg_opacity_options = [str(x) + "%" for x in range(10, 110, 10)]
        self.animal_cnt_options = list(range(1, self.animal_cnt + 1))
        self.custom_rgb_selections = {}

        self.style_settings_frm = CreateLabelFrameWithIcon(parent=self.main_frm, header="STYLE SETTINGS", icon_name=Keys.DOCUMENTATION.value, icon_link=Links.PATH_PLOTS.value)
        self.auto_compute_styles, self.autocompute_var = SimbaCheckbox(parent=self.style_settings_frm, txt="AUTO-COMPUTE STYLES", txt_img='system', cmd=self.enable_style_settings, val=True)
        self.max_prior_lines_dropdown = DropDownMenu(self.style_settings_frm, "Max prior lines:", ["Entire video", "Specify milliseconds"], "16", com=self.enable_entrybox_from_dropdown)
        self.max_lines_entry = Entry_Box(self.style_settings_frm, "Max prior lines (ms): ", "16", validation="numeric")
        self.resolution_dropdown = DropDownMenu(self.style_settings_frm, "Resolution:", self.resolution_options, "16")
        self.bg_clr_dropdown = DropDownMenu(self.style_settings_frm, "Background:", self.bg_clr_options, "16", com=lambda x: self.__activate_settings(choice=x))
        self.line_width = Entry_Box(self.style_settings_frm, "Line width: ", "16", validation="numeric")
        self.font_size = Entry_Box(self.style_settings_frm, "Font size: ", "16", validation="numeric")
        self.font_thickness = Entry_Box(self.style_settings_frm, "Font thickness: ", "16", validation="numeric")
        self.bg_opacity_dropdown = DropDownMenu(self.style_settings_frm, "Background opacity:", self.bg_opacity_options, "16")
        self.circle_size = Entry_Box(self.style_settings_frm, "Circle size: ", "16", validation="numeric")
        self.resolution_dropdown.setChoices(self.resolution_options[0])
        self.line_width.entry_set(val=6)
        self.bg_clr_dropdown.setChoices("White")
        self.circle_size.entry_set(val=20)
        self.font_size.entry_set(val=3)
        self.font_thickness.entry_set(val=2)
        self.max_prior_lines_dropdown.setChoices("Entire video")
        self.max_prior_lines_dropdown.disable()
        self.max_lines_entry.entry_set(2000)
        self.bg_opacity_dropdown.setChoices("100%")
        self.bg_opacity_dropdown.disable()
        self.resolution_dropdown.disable()
        self.line_width.set_state("disable")
        self.bg_clr_dropdown.disable()
        self.circle_size.set_state("disable")
        self.font_size.set_state("disable")
        self.max_lines_entry.set_state("disable")
        self.font_thickness.set_state("disable")

        self.body_parts_frm = LabelFrame(self.main_frm, text="CHOOSE BODY-PARTS", font=Formats.FONT_HEADER.value, pady=5, padx=5)
        self.number_of_animals_dropdown = DropDownMenu(self.body_parts_frm, "# Animals:", self.animal_cnt_options, "16", com=self.populate_body_parts_menu)
        self.number_of_animals_dropdown.setChoices(self.animal_cnt_options[0])

        self.video_slicing_frm = LabelFrame(self.main_frm, text="SEGMENTS", font=Formats.FONT_HEADER.value, pady=5, padx=5)
        self.slice_var = BooleanVar(value=False)
        self.video_start_time_entry = Entry_Box(self.video_slicing_frm, "Start time:", "16")
        self.video_end_time_entry = Entry_Box(self.video_slicing_frm, "End time:", "16")
        self.video_start_time_entry.entry_set("00:00:00")
        self.video_end_time_entry.entry_set("00:00:00")
        self.video_start_time_entry.set_state("disable")
        self.video_end_time_entry.set_state("disable")
        self.slice_cb = Checkbutton(
            self.video_slicing_frm,
            text="Plot ONLY defined time-segment",
            font=Formats.FONT_REGULAR.value,
            variable=self.slice_var,
            command=lambda: self.enable_entrybox_from_checkbox(
                check_box_var=self.slice_var,
                entry_boxes=[self.video_start_time_entry, self.video_end_time_entry],
            ),
        )
        self.slice_cb.grid(row=0, column=0, sticky=NW)
        self.video_start_time_entry.grid(row=1, column=0, sticky=NW)
        self.video_end_time_entry.grid(row=2, column=0, sticky=NW)

        self.clf_frm = LabelFrame(self.main_frm, text="CLASSIFICATION VISUALIZATION", font=Formats.FONT_HEADER.value, pady=5, padx=5)
        self.include_clf_locations_var = BooleanVar(value=False)

        self.include_clf_locations_cb = Checkbutton(self.clf_frm, text="INCLUDE CLASSIFICATION LOCATIONS", font=Formats.FONT_REGULAR.value, variable=self.include_clf_locations_var, command=self.populate_clf_location_data)
        self.include_clf_locations_cb.grid(row=0, sticky=NW)
        self.populate_clf_location_data()

        self.roi_frm = LabelFrame(self.main_frm, text="ROI VISUALIZATION", font=Formats.FONT_HEADER.value, pady=5, padx=5)
        roi_cb, self.roi_var = SimbaCheckbox(parent=self.roi_frm, txt='INCLUDE ROIs', txt_img='roi', val=False)



        self.populate_body_parts_menu(self.animal_cnt_options[0])
        self.settings_frm = LabelFrame(self.main_frm, text="VISUALIZATION SETTINGS", font=Formats.FONT_HEADER.value, pady=5, padx=5)
        self.multiprocessing_var = BooleanVar()

        path_frames_cb, self.path_frames_var = SimbaCheckbox(parent=self.settings_frm, txt='CREATE FRAMES', txt_img='frames')
        path_videos_cb, self.path_videos_var = SimbaCheckbox(parent=self.settings_frm, txt='CREATE VIDEOS', txt_img='video')
        path_last_frm_cb, self.path_last_frm_var = SimbaCheckbox(parent=self.settings_frm, txt='CREATE LAST FRAME', txt_img='finish', val=True)
        self.include_animal_names_cb, self.include_animal_names_var = SimbaCheckbox(parent=self.settings_frm, txt='INCLUDE ANIMAL NAMES', txt_img='id_card')

        self.multiprocess_cb = Checkbutton(
            self.settings_frm,
            text="Multiprocess videos (faster)",
            font=Formats.FONT_REGULAR.value,
            variable=self.multiprocessing_var,
            command=lambda: self.enable_dropdown_from_checkbox(
                check_box_var=self.multiprocessing_var,
                dropdown_menus=[self.multiprocess_dropdown],
            ),
        )
        self.multiprocess_dropdown = DropDownMenu(self.settings_frm, "CPU cores:", list(range(2, self.cpu_cnt)), "12")
        self.multiprocess_dropdown.setChoices(2)
        self.multiprocess_dropdown.disable()

        self.run_frm = LabelFrame( self.main_frm, text="RUN", font=Formats.FONT_HEADER.value, pady=5, padx=5, fg="black")
        self.run_single_video_frm = LabelFrame(self.run_frm, text="SINGLE VIDEO", font=Formats.FONT_HEADER.value, pady=5, padx=5, fg="black")
        self.run_single_video_btn = SimbaButton(parent=self.run_single_video_frm, txt='CREATE SINGLE VIDEO', img='rocket', txt_clr='blue', font=Formats.FONT_REGULAR.value, cmd=self.__create_path_plots, cmd_kwargs={'multiple_videos': False})

        self.single_video_dropdown = DropDownMenu( self.run_single_video_frm, "Video:", self.files_found, "12")
        self.single_video_dropdown.setChoices(self.files_found[0])
        self.run_multiple_videos = LabelFrame( self.run_frm, text="MULTIPLE VIDEO", font=Formats.FONT_HEADER.value, pady=5, padx=5, fg="black")
        self.run_multiple_video_btn = SimbaButton(parent=self.run_multiple_videos, txt=f"Create multiple videos ({len(self.files_found)} video(s) found)", font=Formats.FONT_REGULAR.value, img='rocket', txt_clr='blue', cmd=self.__create_path_plots, cmd_kwargs={'multiple_videos': True})

        self.style_settings_frm.grid(row=0, sticky=NW)
        self.auto_compute_styles.grid(row=0, sticky=NW)
        self.resolution_dropdown.grid(row=1, sticky=NW)
        self.max_prior_lines_dropdown.grid(row=2, sticky=NW)
        self.max_lines_entry.grid(row=3, sticky=NW)
        self.line_width.grid(row=4, sticky=NW)
        self.circle_size.grid(row=5, sticky=NW)
        self.font_size.grid(row=6, sticky=NW)
        self.font_thickness.grid(row=7, sticky=NW)
        self.bg_clr_dropdown.grid(row=8, sticky=NW)
        self.bg_opacity_dropdown.grid(row=9, sticky=NW)

        self.video_slicing_frm.grid(row=1, sticky=NW)
        self.clf_frm.grid(row=2, sticky=NW)

        self.roi_frm.grid(row=3, sticky=NW)
        roi_cb.grid(row=0, sticky=NW)

        self.body_parts_frm.grid(row=4, sticky=NW)
        self.number_of_animals_dropdown.grid(row=0, sticky=NW)

        self.settings_frm.grid(row=5, sticky=NW)
        path_frames_cb.grid(row=0, sticky=NW)
        path_videos_cb.grid(row=1, sticky=NW)
        path_last_frm_cb.grid(row=2, sticky=NW)
        self.include_animal_names_cb.grid(row=3, sticky=NW)
        self.multiprocess_cb.grid(row=4, column=0, sticky=NW)
        self.multiprocess_dropdown.grid(row=4, column=1, sticky=NW)

        self.run_frm.grid(row=6, sticky=NW)
        self.run_single_video_frm.grid(row=0, sticky=NW)
        self.run_single_video_btn.grid(row=0, column=0, sticky=NW)
        self.single_video_dropdown.grid(row=0, column=1, sticky=NW)

        self.run_multiple_videos.grid(row=1, sticky=NW)
        self.run_multiple_video_btn.grid(row=0, sticky=NW)

        self.main_frm.mainloop()

    def populate_body_parts_menu(self, choice):
        if hasattr(self, "bp_dropdowns"):
            for (k, v), (k2, v2) in zip(
                self.bp_dropdowns.items(), self.bp_colors.items()
            ):
                self.bp_dropdowns[k].destroy()
                self.bp_colors[k].destroy()
        for k, v in self.custom_rgb_selections.items():
            v.destroy()
        self.custom_rgb_selections = {}

        self.bp_dropdowns, self.bp_colors = {}, {}
        self.bp_row_idx = []
        for animal_cnt in range(int(self.number_of_animals_dropdown.getChoices())):
            self.bp_dropdowns[animal_cnt] = DropDownMenu(self.body_parts_frm, "Body-part {}:".format(str(animal_cnt + 1)), self.body_parts_lst, "16")
            self.bp_dropdowns[animal_cnt].setChoices(self.body_parts_lst[animal_cnt])
            self.bp_dropdowns[animal_cnt].grid(row=animal_cnt + 1, column=0, sticky=NW)
            self.bp_colors[animal_cnt] = DropDownMenu(self.body_parts_frm, "", self.animal_trace_clrs, "2", com=lambda x, k=animal_cnt: self.__set_custom_clrs(choice=x, row=k))
            self.bp_colors[animal_cnt].setChoices(list(self.colors_dict.keys())[animal_cnt])
            self.bp_colors[animal_cnt].grid(row=animal_cnt + 1, column=1, sticky=NW)

    def __activate_settings(self, choice: str):
        if choice == "Video - static frame" or choice == "Video - moving frames":
            self.bg_opacity_dropdown.enable()
        else:
            self.bg_opacity_dropdown.disable()
        if choice == "Video - static frame":
            self.static_frm_index_eb = Entry_Box(self.style_settings_frm, "Frame index: ", "10", validation="numeric")
            self.static_frm_index_eb.entry_set(val=1)
            self.static_frm_index_eb.grid(row=8, column=1, sticky=NW)
        else:
            if hasattr(self, "static_frm_index_eb"):
                self.static_frm_index_eb.destroy()

    def __set_custom_clrs(self, choice: str, row: int):
        if choice == "Custom":
            self.custom_rgb_selections[row] = Entry_Box(self.body_parts_frm, "RGB:", "5", entry_box_width=10)
            self.custom_rgb_selections[row].entry_set(val="255,0,0")
            self.custom_rgb_selections[row].grid(row=row + 1, column=3, sticky=NW)
        else:
            if row in self.custom_rgb_selections.keys():
                self.custom_rgb_selections[row].destroy()
                self.custom_rgb_selections.pop(row)

    def populate_clf_location_data(self):
        self.clf_name, self.clf_clr, self.clf_size = {}, {}, {}
        size_lst = list(range(1, 51))
        size_lst = ["Size: " + str(x) for x in size_lst]
        for clf_cnt, clf_name in enumerate(self.clf_names):
            self.clf_name[clf_cnt] = DropDownMenu(self.clf_frm, "Classifier {}:".format(str(clf_cnt + 1)), self.clf_names, "16")
            self.clf_name[clf_cnt].setChoices(self.clf_names[clf_cnt])
            self.clf_name[clf_cnt].grid(row=clf_cnt + 1, column=0, sticky=NW)

            self.clf_clr[clf_cnt] = DropDownMenu(self.clf_frm, "", list(self.colors_dict.keys()), "2")
            self.clf_clr[clf_cnt].setChoices(list(self.colors_dict.keys())[clf_cnt])
            self.clf_clr[clf_cnt].grid(row=clf_cnt + 1, column=1, sticky=NW)

            self.clf_size[clf_cnt] = DropDownMenu(self.clf_frm, "", size_lst, "2")
            self.clf_size[clf_cnt].setChoices(size_lst[15])
            self.clf_size[clf_cnt].grid(row=clf_cnt + 1, column=2, sticky=NW)

        self.enable_clf_location_settings()

    def enable_clf_location_settings(self):
        if self.include_clf_locations_var.get():
            for clf_cnt in self.clf_name.keys():
                self.clf_name[clf_cnt].enable()
                self.clf_clr[clf_cnt].enable()
                self.clf_size[clf_cnt].enable()
        else:
            for clf_cnt in self.clf_name.keys():
                self.clf_name[clf_cnt].disable()
                self.clf_clr[clf_cnt].disable()
                self.clf_size[clf_cnt].disable()

    def enable_entrybox_from_dropdown(self, dropdown_selection):
        if dropdown_selection == "Entire video":
            self.max_lines_entry.set_state("disable")
        else:
            self.max_lines_entry.set_state("normal")

    def enable_style_settings(self):
        if not self.autocompute_var.get():
            self.resolution_dropdown.enable()
            self.max_prior_lines_dropdown.enable()
            self.max_lines_entry.set_state("normal")
            self.line_width.set_state("normal")
            self.font_thickness.set_state("normal")
            self.circle_size.set_state("normal")
            self.font_size.set_state("normal")
            self.bg_clr_dropdown.enable()
            if self.bg_clr_dropdown.getChoices() == "Video":
                self.bg_opacity_dropdown.enable()
            self.enable_entrybox_from_dropdown(self.max_prior_lines_dropdown.getChoices())
        else:
            self.resolution_dropdown.disable()
            self.max_prior_lines_dropdown.disable()
            self.max_lines_entry.set_state("disable")
            self.font_thickness.set_state("disable")
            self.line_width.set_state("disable")
            self.circle_size.set_state("disable")
            self.font_size.set_state("disable")
            self.bg_clr_dropdown.disable()
            self.bg_opacity_dropdown.disable()

    def __create_path_plots(self, multiple_videos: bool):
        if self.autocompute_var.get():
            style_attr = None
        else:
            if self.resolution_dropdown.getChoices() != "As input":
                width = int(self.resolution_dropdown.getChoices().split("×")[0])
                height = int(self.resolution_dropdown.getChoices().split("×")[1])
            else:
                width, height = "As input", "As input"
            check_int(name="PATH LINE WIDTH", value=self.line_width.entry_get, min_value=1)
            check_int(name="PATH CIRCLE SIZE", value=self.circle_size.entry_get, min_value=1)
            check_int(name="PATH FONT SIZE", value=self.font_size.entry_get, min_value=1)
            check_int(name="FONT THICKNESS", value=self.font_thickness.entry_get, min_value=1)
            if self.bg_clr_dropdown.getChoices() == "Video - static frame":
                check_int(name="Static frame index", value=self.static_frm_index_eb.entry_get, min_value=0)
                bg_clr = {
                    "type": "static",
                    "opacity": int(
                        "".join(
                            c
                            for c in self.bg_opacity_dropdown.getChoices()
                            if c.isdigit()
                        )
                    ),
                    "frame_index": int(self.static_frm_index_eb.entry_get),
                }
            elif self.bg_clr_dropdown.getChoices() == "Video - moving frames":
                bg_clr = {
                    "type": "moving",
                    "opacity": int(
                        "".join(
                            c
                            for c in self.bg_opacity_dropdown.getChoices()
                            if c.isdigit()
                        )
                    ),
                }
            else:
                bg_clr = get_color_dict()[self.bg_clr_dropdown.getChoices()]

            style_attr = {"width": width,
                          "height": height,
                          "line width": int(self.line_width.entry_get),
                          "font size": int(self.font_size.entry_get),
                          "font thickness": int(self.font_thickness.entry_get),
                          "circle size": int(self.circle_size.entry_get),
                          "bg color": bg_clr,
                          "clf locations": self.include_clf_locations_var.get()}

            if self.max_prior_lines_dropdown.getChoices() == "Entire video":
                style_attr["max lines"] = "entire video"
            else:
                check_int( name="PATH MAX LINES", value=self.max_lines_entry.entry_get, min_value=1)
                style_attr["max lines"] = int(self.max_lines_entry.entry_get)

        animal_attr = {}
        for cnt, (key, value) in enumerate(self.bp_colors.items()):
            if cnt not in animal_attr.keys():
                animal_attr[cnt] = {}
            clr = value.getChoices()
            if clr == "Custom":
                clr = self.custom_rgb_selections[cnt].entry_get
                clr = check_if_valid_rgb_str(input=clr)
                animal_attr[cnt]["color"] = clr
            else:
                animal_attr[cnt]["color"] = get_color_dict()[value.getChoices()]
        for cnt, (key, value) in enumerate(self.bp_dropdowns.items()):
            if cnt not in animal_attr.keys():
                animal_attr[cnt] = {}
            animal_attr[cnt]["bp"] = value.getChoices()

        self.slicing = None
        if self.slice_var.get():
            check_if_string_value_is_valid_video_timestamp(value=self.video_start_time_entry.entry_get, name="Video slicing START TIME")
            check_if_string_value_is_valid_video_timestamp(value=self.video_end_time_entry.entry_get, name="Video slicing END TIME")
            if (self.video_start_time_entry.entry_get == self.video_end_time_entry.entry_get):
                raise FrameRangeError(msg="The sliced start and end times cannot be identical", source=self.__class__.__name__)
            check_that_hhmmss_start_is_before_end(start_time=self.video_start_time_entry.entry_get, end_time=self.video_end_time_entry.entry_get, name="SLICE TIME STAMPS")
            self.slicing = {"start_time": self.video_start_time_entry.entry_get, "end_time": self.video_end_time_entry.entry_get}

        clf_attr = None
        if self.include_clf_locations_var.get():
            if multiple_videos:
                if len(self.machine_results_paths) == 0:
                    raise NoFilesFoundError(msg=f'No DATA found in {self.machine_results_dir} directory. Un-check the classifier location checkbox, OR make sure the folder contains classification data.')
                else:
                    data_paths = list(self.machine_results_files.values())
            else:
                if self.single_video_dropdown.getChoices() not in self.machine_results_files.keys():
                    raise NoFilesFoundError(msg=f'No DATA found for video in {self.single_video_dropdown.getChoices()} in directory {self.machine_results_dir}. Un-check the classifier location checkbox, OR make sure the folder contains classification data for the video.')
                else:
                    data_paths = [self.machine_results_files[self.single_video_dropdown.getChoices()]]
            clf_attr = {}
            for cnt, (key, value) in enumerate(self.clf_name.items()):
                clf_attr[value.getChoices()] = {}
                clf_attr[value.getChoices()]["color"] = get_color_dict()[self.clf_clr[cnt].getChoices()]
                size = "".join(filter(str.isdigit, self.clf_size[cnt].getChoices()))
                clf_attr[value.getChoices()]["size"] = int(size)

        else:
            if multiple_videos:
                data_paths = list(self.outlier_corrected_files.values())
            else:
                data_paths = [self.outlier_corrected_files[self.single_video_dropdown.getChoices()]]

        if self.roi_var.get():
            if not os.path.isfile(self.roi_coordinates_path):
                raise NoROIDataError(msg=f'No SimBA ROI project data found. Expected at path {self.roi_coordinates_path}', source=self.__class__.__name__)

        if not self.multiprocessing_var.get():
            path_plotter = PathPlotterSingleCore(config_path=self.config_path,
                                                 frame_setting=self.path_frames_var.get(),
                                                 video_setting=self.path_videos_var.get(),
                                                 last_frame=self.path_last_frm_var.get(),
                                                 files_found=data_paths,
                                                 input_style_attr=style_attr,
                                                 print_animal_names=self.include_animal_names_var.get(),
                                                 animal_attr=animal_attr,
                                                 clf_attr=clf_attr,
                                                 slicing=self.slicing,
                                                 roi=self.roi_var.get())
        else:
            path_plotter = PathPlotterMulticore(config_path=self.config_path,
                                                frame_setting=self.path_frames_var.get(),
                                                video_setting=self.path_videos_var.get(),
                                                last_frame=self.path_last_frm_var.get(),
                                                files_found=data_paths,
                                                input_style_attr=style_attr,
                                                print_animal_names=self.include_animal_names_var.get(),
                                                animal_attr=animal_attr,
                                                clf_attr=clf_attr,
                                                cores=int(self.multiprocess_dropdown.getChoices()),
                                                slicing=self.slicing,
                                                roi=self.roi_var.get())

        threading.Thread(target=path_plotter.run()).start()



#_ = PathPlotPopUp(config_path=r"/Users/simon/Desktop/envs/simba/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini")

# _ = PathPlotPopUp(config_path='/Users/simon/Desktop/envs/simba/troubleshooting/beepboop174/project_folder/project_config.ini')

# _ = PathPlotPopUp(config_path='/Users/simon/Desktop/envs/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini')

# _ = PathPlotPopUp(config_path='/Users/simon/Desktop/envs/troubleshooting/dorian_2/project_folder/project_config.ini')
