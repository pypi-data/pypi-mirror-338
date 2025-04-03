"""
BactoWidget is a jupyter widget for bacterial colony growth image analysis.
"""

from pathlib import Path
from typing import Optional, Union, Literal

import ipywidgets
from ipywidgets import (
    VBox,
    HBox,
    IntSlider,
    FloatSlider,
    FloatLogSlider,
    Button,
    ToggleButton,
    ToggleButtons,
    Layout,
    Dropdown,
)

import numpy as np
from PIL import Image

from bactovision.canvas_widget import CanvasWidget
from bactovision.image_processing import (
    segment_by_thresholding,
    preprocess_image,
    working_preprocessing,
    get_summary_metrics,
)


class BactoWidget(VBox):
    """
    BactoWidget is a jupyter widget for bacterial colony growth image analysis.

    Attributes:
        original_img: numpy array of the original image.
        mask: numpy array of the mask.

    Methods:
        get_metrics: get the metrics of the image after the annotation.
        cut_img: cut the image to the region of interest.
        apply_auto_annotation: apply auto annotation to the image.
    """

    def __init__(self, img: Union[np.ndarray, str, Path], mask: Optional[np.ndarray] = None):
        """
        Initialize the BactoWidget.

        Args:
            img: image to be analyzed, numpy array or path to image file.
            mask: numpy array of `mask` - an annotation with the same shape as the image,
                where the pixels with value 1 correspond to the bacterial colony, and 0
                otherwise. Optional, default is None.
        """
        # load image
        if isinstance(img, (str, Path)):
            img = np.array(Image.open(img))

        assert isinstance(img, np.ndarray), "img should be a numpy array or a path to an image"
        assert img.ndim == 3, "img should be a 3D array"

        # save original image
        self.original_img = np.array(img)

        self._saved_mask = mask
        self._prev_draw_btn_state = 'Off'

        # init all widgets
        self.draw_mode_btns = ToggleButtons(
            options=['Off', 'Add', 'Erase'], disable=False, description='Manual annotation:'
        )

        layout_dict = dict(
            display='flex', flex_flow='column', align_items='stretch', style={'description_width': 'initial'},
            layout=Layout(width='auto')
        )

        self.brush_size_slider = FloatSlider(5, min=1, max=20, description='brush size', **layout_dict)
        self.hide_annotation_btn = ToggleButton(value=False, description='Hide annotation', **layout_dict)
        self.canvas_widget = CanvasWidget()
        self.threshold_slider = FloatSlider(1., min=0.01, max=2, step=0.001, description='Brightness threshold',
                                            continuous_update=False, **layout_dict)
        self.small_object_size = FloatSlider(1., min=0.1, max=3., step=0.01, description='Smallest size',
                                             continuous_update=False, **layout_dict)
        self.annotate_btn = Button(value=False, description='Apply auto', **layout_dict)
        self.clahe_btn = ToggleButton(value=False, description='Apply CLAHE', **layout_dict)
        self.clahe_limit_slider = FloatLogSlider(
            200, min=1, max=4, description='CLAHE limit', continuous_update=False, **layout_dict)

        self.subtract_background_btn = ToggleButton(value=False, description='Subtract background', **layout_dict)

        self.cmap_down = Dropdown(
            options=['YlGnBu', 'gray', 'viridis', 'cividis', 'plasma'], value='YlGnBu', description='Colormap',
        )

        # grid
        self.hide_grid_btn = ToggleButton(value=False, description='Hide grid', **layout_dict)
        self.change_grid_btn = ToggleButton(value=False, description='Adjust grid', **layout_dict)

        self.x_grid_size_slider = IntSlider(self.canvas_widget.grid_num_x, 1, 15, description='Horizontal grid size',
                                            **layout_dict)
        self.y_grid_size_slider = IntSlider(self.canvas_widget.grid_num_y, 1, 15, description='Vertical grid size',
                                            **layout_dict)
        self.top_pad_slider = IntSlider(self.canvas_widget.pad_top, 0, 200, **layout_dict)
        self.bottom_pad_slider = IntSlider(self.canvas_widget.pad_bottom, 0, 200, **layout_dict)
        self.right_pad_slider = IntSlider(self.canvas_widget.pad_right, 0, 200, **layout_dict)
        self.left_pad_slider = IntSlider(self.canvas_widget.pad_left, 0, 200, **layout_dict)

        self.control_widgets = [
            self.draw_mode_btns, self.brush_size_slider, self.threshold_slider, self.small_object_size,
            self.annotate_btn,
        ]

        # set data
        self._preprocessed_img = preprocess_image(self.cut_img(self.original_img))

        if mask is None:
            mask = np.zeros_like(self._preprocessed_img)

        self._set_image(self._preprocessed_img)
        self.canvas_widget.set_annotation(mask)

        # init connections
        self.init_connections()

        # layout

        frame_layout = Layout(
            border='1px solid gray',  # Add a solid border to create the frame
            padding='2px',  # Add some padding inside the frame
            margin='2px',  # Add some margin outside the frame
            width='auto',  # Adjust width
            height='auto'  # Adjust height based on content
        )

        fixed_frame_layout = Layout(
            border='1px solid gray',  # Add a solid border to create the frame
            padding='2px',  # Add some padding inside the frame
            margin='2px',  # Add some margin outside the frame
            width='50%',  # Adjust width
            height='auto'  # Adjust height based on content
        )

        self.grid_widgets = VBox([
            HBox([self.change_grid_btn, self.hide_grid_btn, ]),
            self.x_grid_size_slider,
            self.y_grid_size_slider,
        ], layout=frame_layout)

        self.contrast_widgets = VBox([
            self.clahe_btn,
            self.clahe_limit_slider,
            self.subtract_background_btn,
            self.cmap_down,
        ], layout=frame_layout)

        self.manual_annotation_widgets = VBox([
            self.draw_mode_btns,
            self.brush_size_slider,
        ], layout=frame_layout)

        self.auto_annotation_widgets = VBox([
            HBox([self.annotate_btn, self.hide_annotation_btn]),
            self.threshold_slider,
            self.small_object_size,
        ], layout=frame_layout)

        preprocessing_column = VBox([
            self.grid_widgets,
            self.contrast_widgets,
        ], layout=fixed_frame_layout)

        annotation_column = VBox([
            self.manual_annotation_widgets,
            self.auto_annotation_widgets,
        ], layout=fixed_frame_layout)

        control_panel = HBox([preprocessing_column, annotation_column])

        super().__init__([control_panel, self.canvas_widget])

    def get_metrics(
            self, 
            brightness_mode: Literal['luminance', 'luminance-inverse', 'red', 'green', 'blue'] = 'luminance-inverse'
        ):
        """
        Get the metrics of the image after the annotation.

        Args:
            brightness_mode: mode to calculate the brightness,
                one of 'luminance', 'luminance-inverse', 'red', 'green', 'blue'.
                Default is 'luminance-inverse' used in the paper.
        """
        return get_summary_metrics(
            self.cut_img(self.original_img),
            self.mask,
            grid_x=self.canvas_widget.grid_num_x,
            grid_y=self.canvas_widget.grid_num_y,
            mode=brightness_mode,
        )

    def cut_img(self, img: np.ndarray) -> np.ndarray:
        w = self.canvas_widget
        top, bottom, left, right = map(lambda x: int(round(x)), (w.pad_top, w.pad_bottom, w.pad_left, w.pad_right))
        img = img[bottom:-top, left: - right]
        return img

    def apply_auto_annotation(self, *args):
        # self.annotate_btn.description = str(btn.value)
        t = self.threshold_slider.value
        s = self.small_object_size.value
        self.disable_widgets()

        processed_img, mask = segment_by_thresholding(self._preprocessed_img, t, s)

        self._saved_mask = mask
        self.canvas_widget.set_annotation(mask)
        self.disable_widgets(False)

    def _set_image(self, img=None):
        if img is None:
            img = self._preprocessed_img
        self.canvas_widget.set_image(img, cmap=self.cmap_down.value)

    def _update_image_view(self, *args):
        self._set_image()

    def disable_widgets(self, value: bool = True):
        for widget in self.control_widgets + [self.hide_annotation_btn, self.clahe_btn]:
            widget.disabled = value

    def _hide_annotation_clicked(self, *args):
        hide = self.hide_annotation_btn.value

        if hide:
            self.hide_annotation_btn.description = 'Show annotation'
            self._prev_draw_btn_state = self.draw_mode_btns.value
            self.draw_mode_btns.value = 'Off'

            self._saved_mask = self.mask

            for widget in self.control_widgets:
                widget.disabled = True

            self.canvas_widget.set_annotation(np.zeros_like(self._saved_mask))
        else:
            self.hide_annotation_btn.description = 'Hide annotation'

            for widget in self.control_widgets:
                widget.disabled = False
            self.draw_mode_btns.value = self._prev_draw_btn_state

            self.canvas_widget.set_annotation(self._saved_mask)

    def _update_preprocessed_image(self, *args):
        use_clahe = self.clahe_btn.value
        clahe_limit = self.clahe_limit_slider.value
        subtract_background = self.subtract_background_btn.value

        self._preprocessed_img = working_preprocessing(
            self.cut_img(self.original_img), use_clahe=use_clahe, clahe_limit=clahe_limit,
            subtract_background=subtract_background,
        )

        self._set_image(self._preprocessed_img)

    def _change_grid_btn_clicked(self, *args):
        change_grid_mode = self.change_grid_btn.value
        self.canvas_widget.change_grid = change_grid_mode

        if change_grid_mode:
            self._set_image(self.original_img)
        else:
            self._update_preprocessed_image()

    @property
    def mask(self):
        mask = self.canvas_widget.get_annotation()
        mask = mask.sum(-1)
        mask[mask > 0] = 1.
        return mask

    def init_connections(self):
        # connect widgets
        self.clahe_btn.observe(self._update_preprocessed_image, 'value')
        self.clahe_limit_slider.observe(self._update_preprocessed_image, 'value')
        self.subtract_background_btn.observe(self._update_preprocessed_image, 'value')
        self.cmap_down.observe(self._update_image_view, 'value')

        self.annotate_btn.on_click(self.apply_auto_annotation)
        self.hide_annotation_btn.observe(self._hide_annotation_clicked, 'value')
        self.threshold_slider.observe(self.apply_auto_annotation, 'value')
        self.small_object_size.observe(self.apply_auto_annotation, 'value')
        self.change_grid_btn.observe(self._change_grid_btn_clicked, 'value')

        # link properties
        ipywidgets.link((self.draw_mode_btns, 'value'), (self.canvas_widget, 'mode'))
        ipywidgets.link((self.brush_size_slider, 'value'), (self.canvas_widget, 'brush_size'))
        ipywidgets.link((self.x_grid_size_slider, 'value'), (self.canvas_widget, 'grid_num_x'))
        ipywidgets.link((self.y_grid_size_slider, 'value'), (self.canvas_widget, 'grid_num_y'))
        ipywidgets.link((self.top_pad_slider, 'value'), (self.canvas_widget, 'pad_top'))
        ipywidgets.link((self.bottom_pad_slider, 'value'), (self.canvas_widget, 'pad_bottom'))

        ipywidgets.link((self.right_pad_slider, 'value'), (self.canvas_widget, 'pad_right'))
        ipywidgets.link((self.left_pad_slider, 'value'), (self.canvas_widget, 'pad_left'))
        ipywidgets.link((self.hide_grid_btn, 'value'), (self.canvas_widget, 'hide_grid'))
