# -*- coding: utf-8 -*-
# Copyright (c) Alibaba, Inc. and its affiliates.
import copy
import datetime
import json
import os
import random
import time
from collections import OrderedDict

from tqdm import tqdm

import decord
import gradio as gr
import torch
import yaml
from scepter.modules.utils.directory import get_md5
from scepter.modules.utils.file_system import FS
from scepter.modules.utils.import_utils import get_dirname
from scepter.studio.self_train.scripts.trainer import TrainManager
from scepter.studio.self_train.self_train_ui.component_names import \
    TrainerUIName
from scepter.studio.self_train.utils.config_parser import (
    get_default, get_values_by_model, get_values_by_model_version,
    get_values_by_model_version_tuner)
from scepter.studio.utils.uibase import UIBase


def print_memory_status(is_debug):
    if not is_debug:
        nvi_info = os.popen('nvidia-smi').read()
        gpu_mem = nvi_info.split('\n')[9].split('|')[2].split('/')[0].strip()
    else:
        gpu_mem = 0
    return gpu_mem


def is_basic_or_container_type(obj):
    basic_and_container_types = (int, float, str, bool, complex, list, tuple,
                                 dict, set)
    return isinstance(obj, basic_and_container_types)


refresh_symbol = '\U0001f504'  # 🔄


def get_work_name(model, version, tuner):
    model_prefix = f'Swift@{model}@{version}@{tuner}'
    return model_prefix + '@' + '{0:%Y%m%d%H%M%S%f}'.format(
        datetime.datetime.now()) + ''.join(
            [str(random.randint(1, 10)) for i in range(3)])


def judge_tuner_visible(tuner_name):
    lora_visible = tuner_name in ['LORA', 'TEXT_LORA']
    text_lora_visible = tuner_name in ['TEXT_SCE']
    sce_visible = tuner_name in ['SCE', 'TEXT_SCE']
    return lora_visible, text_lora_visible, sce_visible


def update_tuner_cfg(tuner_name, tuner_cfg, **kwargs):
    update_info = {}
    if tuner_name in ['LORA', 'TEXT_LORA']:
        update_info = {
            'LORA_ALPHA': kwargs['lora_alpha'],
            'R': kwargs['lora_rank']
        }
    elif tuner_name == 'SCE' or (tuner_name == 'TEXT_SCE'
                                 and tuner_cfg['NAME'] == 'SwiftSCETuning'):
        update_info = {'DOWN_RATIO': kwargs['sce_ratio']}
    elif tuner_name == 'TEXT_SCE' and tuner_cfg['NAME'] == 'SwiftLoRA':
        update_info = {
            'LORA_ALPHA': kwargs['text_lora_alpha'],
            'R': kwargs['text_lora_rank']
        }
    tuner_cfg.update(update_info)
    return tuner_cfg


class TrainerUI(UIBase):
    def __init__(self, cfg, all_cfg_value, is_debug=False, language='en'):
        self.BASE_CFG_VALUE = all_cfg_value
        self.para_data = get_default(self.BASE_CFG_VALUE)
        self.train_para_data = cfg.TRAIN_PARAS
        self.run_script = os.path.join(os.path.dirname(get_dirname()),
                                       cfg.SCRIPT_DIR, 'run_task.py')
        self.work_dir_pre, _ = FS.map_to_local(cfg.WORK_DIR)
        self.is_debug = is_debug
        self.current_train_model = None
        self.trainer_ins = TrainManager(self.run_script, self.work_dir_pre)
        self.component_names = TrainerUIName(language=language)
        self.save_file_local_path = cfg.SAVE_FILE_LOCAL_PATH

        self.h_level_dict = {}
        for hw_tuple in self.train_para_data.RESOLUTIONS.get('VALUES', []):
            h, w = hw_tuple
            if h not in self.h_level_dict:
                self.h_level_dict[h] = []
            self.h_level_dict[h].append(w)
        self.h_level_dict = OrderedDict(
            sorted(self.h_level_dict.items(),
                   key=lambda x: int(x[0]),
                   reverse=False))

    def create_ui(self):
        with gr.Group():
            with gr.Row(variant='panel', equal_height=True):
                with gr.Column(scale=1, min_width=0, variant='panel'):
                    gr.Markdown(self.component_names.user_direction)
                    with gr.Group():
                        gr.Markdown(self.component_names.train_data)
                        self.data_source = gr.Dropdown(
                            choices=self.component_names.data_source_choices,
                            value=self.component_names.data_source_value,
                            label=self.component_names.data_source_name,
                            interactive=True)
                        self.data_type = gr.Dropdown(
                            choices=[
                                self.component_names.data_type_map[key] for key
                                in self.component_names.data_type_choices
                            ],
                            value=self.component_names.data_type_map[
                                self.component_names.data_type_value],
                            label=self.component_names.data_type_name,
                            interactive=True)
                        self.ori_data_name = gr.Textbox(
                            label=self.component_names.ori_data_name,
                            max_lines=1,
                            placeholder=self.component_names.ori_data_name,
                            interactive=True)
                        self.ms_data_name = gr.Textbox(
                            label=' or '.join(
                                self.component_names.data_source_choices),
                            max_lines=1,
                            placeholder=self.component_names.
                            ms_data_name_place_hold,
                            visible=True,
                            interactive=True)
                        with gr.Group(visible=False) as self.ms_data_box:
                            with gr.Row():
                                self.ms_data_space = gr.Textbox(
                                    label=self.component_names.ms_data_space,
                                    max_lines=1)
                                self.ms_data_subname = gr.Textbox(
                                    label=self.component_names.ms_data_subname,
                                    value='default',
                                    max_lines=1)
                    with gr.Group():
                        gr.Markdown(self.component_names.eval_data)
                        self.eval_prompts = gr.Dropdown(
                            value=None,
                            choices=self.train_para_data.get(
                                'EVAL_PROMPTS', []),
                            label=self.component_names.eval_prompts,
                            interactive=True,
                            multiselect=True,
                            allow_custom_value=True,
                            max_choices=20)
                        # self.task = gr.Radio(
                        #     choices=self.component_names.task_choices,
                        #     label=self.component_names.task,
                        #     value=self.component_names.task_choices[0],
                        #     interactive=False)
                        self.eval_image = gr.Image(
                            label=self.component_names.eval_image,
                            type='pil',
                            sources=['upload'],
                            interactive=False,
                            visible=False)
                with gr.Column(scale=2, min_width=0, variant='panel'):
                    gr.Markdown(self.component_names.training_block)
                    with gr.Group():
                        gr.Markdown(self.component_names.model_param)
                        with gr.Row():
                            self.base_model = gr.Dropdown(
                                choices=self.para_data.get(
                                    'model_choices', []),
                                value=self.para_data.get('model_default', ''),
                                label=self.component_names.base_model,
                                interactive=True)
                            self.base_model_revision = gr.Dropdown(
                                choices=self.para_data.get(
                                    'version_choices', []),
                                value=self.para_data.get(
                                    'version_default', ''),
                                label=self.component_names.base_model_revision,
                                interactive=True)
                    with gr.Group():
                        gr.Markdown(self.component_names.tuner_param)
                        # with gr.Column(scale=1, min_width=0):
                        if 'TUNER' in self.para_data:
                            lora_visible, text_lora_visible, sce_visible = judge_tuner_visible(
                                self.para_data['TUNER'])
                        else:
                            lora_visible, text_lora_visible, sce_visible = False, False, False
                        with gr.Row():
                            self.tuner_name = gr.Dropdown(
                                choices=self.para_data.get(
                                    'tuner_choices', []),
                                value=self.para_data.get('tuner_default', ''),
                                label=self.component_names.tuner_name,
                                interactive=True)
                        with gr.Row():
                            with gr.Row(
                                    visible=lora_visible) as self.lora_param:
                                self.lora_alpha = gr.Number(
                                    label='LoRA Alpha',
                                    value=self.para_data.get('lora_alpha', 4),
                                    interactive=True)
                                self.lora_rank = gr.Number(
                                    label='LoRA Rank',
                                    value=self.para_data.get('lora_rank', 4),
                                    interactive=True)
                            with gr.Row(visible=text_lora_visible
                                        ) as self.text_lora_param:
                                self.text_lora_alpha = gr.Number(
                                    label='Text LoRA Alpha',
                                    value=self.para_data.get(
                                        'text_lora_alpha', 4),
                                    interactive=True)
                                self.text_lora_rank = gr.Number(
                                    label='Text LoRA Rank',
                                    value=self.para_data.get(
                                        'text_lora_rank', 4),
                                    interactive=True)
                                self.sce_ratio = gr.Slider(
                                    label='SCE Ratio',
                                    minimum=0.2,
                                    maximum=2.0,
                                    step=0.1,
                                    value=self.para_data.get('sce_ratio', 1.0),
                                    interactive=True,
                                    visible=sce_visible)
                    with gr.Group():
                        gr.Markdown(self.component_names.resolution_param)
                        with gr.Row(equal_height=True):
                            self.resolution_height = gr.Dropdown(
                                choices=list(self.h_level_dict.keys()),
                                value=self.para_data.get('RESOLUTION',
                                                         1024)[0],
                                label=self.component_names.resolution_height,
                                allow_custom_value=True,
                                interactive=True)
                            self.resolution_width = gr.Dropdown(
                                choices=self.h_level_dict[
                                    self.resolution_height.value],
                                value=self.para_data.get('RESOLUTION',
                                                         1024)[1],
                                label=self.component_names.resolution_width,
                                allow_custom_value=True,
                                interactive=True)
                            self.enable_resolution_bucket = gr.Checkbox(
                                value=False,
                                container=True,
                                interactive=True,
                                label=self.component_names.
                                enable_resolution_bucket,
                                info=self.component_names.
                                enable_resolution_bucket_ins)
                        with gr.Column(visible=self.enable_resolution_bucket.
                                       value) as self.resolution_bucket_param:
                            with gr.Row():
                                self.min_bucket_resolution = gr.Number(
                                    label=self.component_names.
                                    min_bucket_resolution,
                                    value=self.para_data.get(
                                        'min_bucket_resolution', 256),
                                    interactive=True)
                                self.max_bucket_resolution = gr.Number(
                                    label=self.component_names.
                                    max_bucket_resolution,
                                    value=self.para_data.get(
                                        'max_bucket_resolution', 1024),
                                    interactive=True)
                            with gr.Row(equal_height=True):
                                self.bucket_resolution_steps = gr.Number(
                                    label=self.component_names.
                                    bucket_resolution_steps,
                                    value=self.para_data.get(
                                        'bucket_resolution_steps', 64),
                                    interactive=True)
                                with gr.Group():
                                    self.bucket_no_upscale = gr.Checkbox(
                                        value=False,
                                        container=True,
                                        interactive=True,
                                        label=self.component_names.
                                        bucket_no_upscale,
                                        info=self.component_names.
                                        bucket_no_upscale_ins)
                    with gr.Group():
                        gr.Markdown(self.component_names.base_param)
                        with gr.Row():
                            self.train_epoch = gr.Number(
                                label=self.component_names.train_epoch,
                                value=self.para_data.get('EPOCHS', 10),
                                precision=0,
                                interactive=True)
                            self.learning_rate = gr.Number(
                                label=self.component_names.learning_rate,
                                value=self.para_data.get(
                                    'LEARNING_RATE', 0.0001),
                                interactive=True)

                        with gr.Row():
                            self.save_interval = gr.Number(
                                label=self.component_names.save_interval,
                                value=self.para_data.get('SAVE_INTERVAL', 10),
                                precision=0,
                                interactive=True)
                            self.train_batch_size = gr.Number(
                                label=self.component_names.train_batch_size,
                                value=self.para_data.get(
                                    'TRAIN_BATCH_SIZE', 4),
                                precision=0,
                                interactive=True)

                        with gr.Row():
                            self.accumulate_step = gr.Number(
                                label=self.component_names.accumulate_step,
                                value=self.para_data.get('ACCUMULATE_STEP', 1),
                                precision=0,
                                interactive=True)
                            self.gpus = gr.Dropdown(
                                choices=list(range(torch.cuda.device_count())),
                                value=list(range(torch.cuda.device_count())),
                                label=self.component_names.gpus,
                                multiselect=True,
                                interactive=True)

                        with gr.Row():
                            self.prompt_prefix = gr.Text(
                                label=self.component_names.prompt_prefix,
                                value=self.para_data.get('TRAIN_PREFIX', ''))
                            self.replace_keywords = gr.Text(
                                label=self.component_names.replace_keywords,
                                value='')
            with gr.Row(variant='panel', equal_height=True):
                with gr.Group():
                    with gr.Row(variant='panel', equal_height=True):
                        gr.Markdown(self.component_names.work_name)
                    with gr.Row(variant='panel', equal_height=True):
                        with gr.Column(scale=6, min_width=0):
                            self.work_name = gr.Text(value=None,
                                                     container=False,
                                                     interactive=False)
                        with gr.Column(scale=2, min_width=0):
                            self.work_name_button = gr.Button(
                                value=refresh_symbol, size='lg')

            with gr.Row(variant='panel', visible=False, equal_height=True):
                with gr.Column(scale=2, min_width=0):
                    self.push_to_hub = gr.Checkbox(
                        label=self.component_names.push_to_hub,
                        value=False,
                        visible=False)

            with gr.Row(variant='panel', equal_height=True):
                self.examples = gr.Examples(
                    examples=[
                        [
                            self.component_names.data_source_choices[0],
                            self.component_names.data_type_map[
                                self.component_names.data_type_value],
                            '',
                            'https://www.modelscope.cn/api/v1/models/iic/scepter/repo?Revision=master&FilePath=datasets/3D_example_csv.zip',  # noqa
                            '3D_example_csv',
                            ''
                        ],
                        [
                            self.component_names.data_source_choices[1],
                            self.component_names.data_type_map[
                                self.component_names.data_type_value], 'damo',
                            'style_custom_dataset', 'style_custom_dataset',
                            '3D'
                        ],
                        [
                            self.component_names.data_source_choices[2],
                            self.component_names.data_type_map[
                                self.component_names.data_type_value_video],
                            '',
                            'https://modelscope.cn/models/iic/scepter/resolve/master/datasets/video_example.txt',   # noqa
                            'video_example_txt',
                            ''
                        ]
                    ],
                    inputs=[
                        self.data_source, self.data_type, self.ms_data_space,
                        self.ms_data_name, self.ori_data_name,
                        self.ms_data_subname
                    ])
            with gr.Row(variant='panel', equal_height=True):
                self.training_button = gr.Button()

    def get_trans_dataset_type(self, dataset_type):
        reverse_data_type = {
            v: k
            for k, v in self.component_names.data_type_map.items()
        }
        trans_dataset_type = reverse_data_type[dataset_type]
        return trans_dataset_type

    def set_callbacks(self, inference_ui, manager):
        def change_data_source(data_source):
            if data_source in [
                    self.component_names.data_source_choices[0],
                    self.component_names.data_source_choices[2]
            ]:
                return gr.Group(visible=False)
            elif data_source == self.component_names.data_source_choices[1]:
                return gr.Group(visible=True)

        self.data_source.change(fn=change_data_source,
                                inputs=[self.data_source],
                                outputs=[self.ms_data_box],
                                queue=False)

        def change_data_type(data_type):
            data_type_key = self.get_trans_dataset_type(data_type)
            if data_type_key in self.component_names.data_task_map and self.component_names.data_task_map[
                    data_type_key] is not None:
                return self.component_names.data_task_map[data_type_key]
            else:
                return self.para_data.get('model_default', '')  # gr.Dropdown()

        self.data_type.change(fn=change_data_type,
                              inputs=[self.data_type],
                              outputs=[self.base_model],
                              queue=False)

        self.work_name_button.click(fn=get_work_name,
                                    inputs=[
                                        self.base_model,
                                        self.base_model_revision,
                                        self.tuner_name
                                    ],
                                    outputs=[self.work_name],
                                    queue=False)

        # def change_eval_image_by_task(task):
        #     # ret_data.get('EVAL_PROMPTS', eval_prompts)
        #     visible = True if task == 'Image Editing' else False
        #     return gr.Image(interactive=visible, visible=visible), \
        #         gr.Dropdown(choices=, multiselect=False)
        # self.task.change(fn=change_eval_image_by_task,
        #                  inputs=[self.task],
        #                  outputs=[self.eval_image],
        #                  queue=False)

        def change_train_value_by_model(base_model):
            '''
                Changes to the base model will affect the training parameters,
                and it is best to define the related default values in the YAML.
                Training Iterations:
                Learning Rate:
                Training Prefix Used:
                Training Batch Size:
                Supported Resolutions:
                Supported Fine-tuning Methods:
                Supported Fine-tuning Methods:
                Prefix for Saved Model:
            '''
            ret_data = get_values_by_model(self.BASE_CFG_VALUE, base_model)
            task = ret_data.get('TASK', 'Text2Image')
            is_edit = task == 'Image Editing'
            eval_prompts = [] if is_edit else self.train_para_data.get(
                'EVAL_PROMPTS', [])
            eval_prompts = ret_data.get('EVAL_PROMPTS', eval_prompts)

            return ret_data.get('EPOCHS', 10), \
                ret_data.get('LEARNING_RATE', 0.0001), \
                ret_data.get('SAVE_INTERVAL', 10), \
                ret_data.get('TRAIN_BATCH_SIZE', 4), \
                ret_data.get('TRAIN_PREFIX', ''), \
                gr.Dropdown(value=ret_data.get('version_default', ''), choices=ret_data.get('version_choices', []),
                            interactive=True), \
                gr.Dropdown(value=ret_data.get('tuner_default', ''), choices=ret_data.get('tuner_choices', []),
                            interactive=True), \
                gr.Dropdown(value=ret_data.get('RESOLUTION', 1024)[0],
                            choices=list(self.h_level_dict.keys()),
                            interactive=True), \
                gr.Dropdown(value=ret_data.get('RESOLUTION', 1024)[1],
                            choices=self.h_level_dict[ret_data.get('RESOLUTION', 1024)[0]],
                            interactive=True), \
                gr.Image(visible=is_edit, interactive=is_edit, value=None), \
                gr.Dropdown(choices=eval_prompts, multiselect=not is_edit)
            # gr.Dropdown(value=task)

        self.base_model.change(
            fn=change_train_value_by_model,
            inputs=[self.base_model],
            outputs=[
                self.train_epoch,
                self.learning_rate,
                self.save_interval,
                self.train_batch_size,
                self.prompt_prefix,
                self.base_model_revision,
                self.tuner_name,
                self.resolution_height,
                self.resolution_width,
                self.eval_image,
                self.eval_prompts,
                # self.task
            ],
            queue=False)

        #
        def change_train_value_by_model_version(base_model,
                                                base_model_revision):
            '''
                Changes to the base model will affect the training parameters,
                and it is best to define the related default values in the YAML.
                Training Iterations:
                Learning Rate:
                Training Prefix Used:
                Training Batch Size:
                Supported Resolutions:
                Supported Fine-tuning Methods:
                Supported Fine-tuning Methods:
                Prefix for Saved Model:
            '''
            ret_data = get_values_by_model_version(self.BASE_CFG_VALUE,
                                                   base_model,
                                                   base_model_revision)
            return ret_data.get('EPOCHS', 10), \
                ret_data.get('LEARNING_RATE', 0.0001), \
                ret_data.get('SAVE_INTERVAL', 10), \
                ret_data.get('TRAIN_BATCH_SIZE', 4), \
                ret_data.get('TRAIN_PREFIX', ''), \
                gr.Dropdown(value=ret_data.get('tuner_default', ''),
                            choices=ret_data.get('tuner_choices', []),
                            interactive=True), \
                gr.Dropdown(value=ret_data.get('RESOLUTION', 1024)[0],
                            choices=list(self.h_level_dict.keys()),
                            interactive=True), \
                gr.Dropdown(value=ret_data.get('RESOLUTION', 1024)[1],
                            choices=self.h_level_dict[ret_data.get('RESOLUTION', 1024)[0]],
                            interactive=True)

        #
        self.base_model_revision.change(
            fn=change_train_value_by_model_version,
            inputs=[self.base_model, self.base_model_revision],
            outputs=[
                self.train_epoch, self.learning_rate, self.save_interval,
                self.train_batch_size, self.prompt_prefix, self.tuner_name,
                self.resolution_height, self.resolution_width
            ],
            queue=False)

        #
        def change_train_value_by_model_version_tuner(base_model,
                                                      base_model_revision,
                                                      tuner_name):
            '''
                Changes to the base model will affect the training parameters,
                and it is best to define the related default values in the YAML.
                Training Iterations:
                Learning Rate:
                Training Prefix Used:
                Training Batch Size:
                Supported Resolutions:
                Supported Fine-tuning Methods:
                Supported Fine-tuning Methods:
                Prefix for Saved Model:
            '''
            ret_data = get_values_by_model_version_tuner(
                self.BASE_CFG_VALUE, base_model, base_model_revision,
                tuner_name)
            lora_visible, text_lora_visible, sce_visible = judge_tuner_visible(
                tuner_name)
            return ret_data.get('EPOCHS', 10), \
                ret_data.get('LEARNING_RATE', 0.0001), \
                ret_data.get('SAVE_INTERVAL', 10), \
                ret_data.get('TRAIN_BATCH_SIZE', 4), \
                ret_data.get('TRAIN_PREFIX', ''), \
                gr.Dropdown(value=ret_data.get('RESOLUTION', 1024)[0],
                            choices=list(self.h_level_dict.keys()),
                            interactive=True), \
                gr.Dropdown(value=ret_data.get('RESOLUTION', 1024)[1],
                            choices=self.h_level_dict[ret_data.get('RESOLUTION', 1024)[0]],
                            interactive=True), \
                gr.Row.update(visible=lora_visible), \
                gr.Row.update(visible=text_lora_visible), \
                gr.Row.update(visible=sce_visible)

        #
        self.tuner_name.change(fn=change_train_value_by_model_version_tuner,
                               inputs=[
                                   self.base_model, self.base_model_revision,
                                   self.tuner_name
                               ],
                               outputs=[
                                   self.train_epoch, self.learning_rate,
                                   self.save_interval, self.train_batch_size,
                                   self.prompt_prefix, self.resolution_height,
                                   self.resolution_width, self.lora_param,
                                   self.text_lora_param, self.sce_ratio
                               ],
                               queue=False)

        def change_resolution(h):
            if h not in self.h_level_dict:
                return gr.Dropdown()
            all_choices = self.h_level_dict[h]
            default = all_choices[0]
            return gr.Dropdown(choices=all_choices, value=default)

        self.resolution_height.change(change_resolution,
                                      inputs=[self.resolution_height],
                                      outputs=[self.resolution_width],
                                      queue=False)

        def change_resolution_bucket(evt: gr.SelectData):
            is_selected = evt.selected
            return (
                gr.update(
                    label=self.component_names.resolution_height_max if
                    is_selected else self.component_names.resolution_height),
                gr.update(
                    label=self.component_names.resolution_width_max
                    if is_selected else self.component_names.resolution_width),
                gr.update(visible=is_selected))

        self.enable_resolution_bucket.select(change_resolution_bucket,
                                             inputs=[],
                                             outputs=[
                                                 self.resolution_height,
                                                 self.resolution_width,
                                                 self.resolution_bucket_param
                                             ],
                                             queue=False)

        def run_train(work_name, data_source, data_type, ori_data_name,
                      ms_data_space, ms_data_name, ms_data_subname, base_model,
                      base_model_revision, tuner_name, resolution_height,
                      resolution_width, train_epoch, learning_rate,
                      save_interval, train_batch_size, prompt_prefix,
                      replace_keywords, push_to_hub, eval_prompts, eval_image,
                      lora_alpha, lora_rank, text_lora_alpha, text_lora_rank,
                      sce_ratio, enable_resolution_bucket,
                      min_bucket_resolution, max_bucket_resolution,
                      bucket_resolution_steps, bucket_no_upscale,
                      accumulate_step, gpus, user_name):
            # Check Cuda
            if not torch.cuda.is_available() and not self.is_debug:
                raise gr.Error(self.component_names.training_err1)

            if work_name == 'custom' or work_name is None or work_name == '':
                raise gr.Error(self.component_names.training_err4)
            work_dir = os.path.join(self.work_dir_pre, work_name)

            self.current_train_model = work_name
            if os.path.exists(work_dir) or os.path.exists(
                    f'.flag/{work_name}.tmp'):
                raise gr.Error(self.component_names.training_err4)
            else:
                os.makedirs(work_dir)
            os.makedirs('.flag', exist_ok=True)
            with open(f'.flag/{work_name}.tmp', 'w') as f:
                f.write('new line.')
            # save params
            exclude_keys = ['exclude_keys', 'ms_data_name']
            with open(os.path.join(work_dir, 'params.json'), 'w') as f_out:
                json.dump(
                    {
                        key: val
                        for key, val in locals().items()
                        if is_basic_or_container_type(val)
                        and key not in exclude_keys
                    },
                    f_out,
                    ensure_ascii=False)

            if push_to_hub:
                model_id = work_name
                model_id = model_id.replace('@', '-')
                hub_model_id = f'scepter/{model_id}'
            else:
                hub_model_id = ''

            # Check Instance Valid
            if ms_data_name is None:
                raise gr.Error(self.component_names.training_err3)

            def prepare_train_image_data(data_cfg):
                data_cfg['BATCH_SIZE'] = int(train_batch_size)
                data_cfg['PROMPT_PREFIX'] = prompt_prefix
                data_cfg['REPLACE_KEYWORDS'] = replace_keywords
                if 'TRANSFORMS' in data_cfg:
                    for trans in data_cfg['TRANSFORMS']:
                        if trans['NAME'] in [
                                'Resize', 'FlexibleResize', 'CenterCrop',
                                'FlexibleCenterCrop'
                        ]:
                            trans['SIZE'] = [
                                int(resolution_height),
                                int(resolution_width)
                            ]
                if data_source in self.component_names.data_source_choices:
                    if ms_data_name.startswith(
                            'http') or ms_data_name.endswith('zip'):
                        work_data_dir = os.path.join(work_dir, 'data')
                        if not os.path.exists(work_data_dir):
                            os.makedirs(work_data_dir)
                        ms_data_http_zip_path = ms_data_name
                        ms_data_local_name = ms_data_name.split(
                            '/')[-1].replace('.zip', '')
                        ms_data_local_zip_path = os.path.join(
                            work_data_dir,
                            ms_data_name.split('/')[-1])
                        ms_data_local_file_path = os.path.join(
                            work_data_dir, ms_data_local_name)
                        if not os.path.exists(ms_data_local_file_path):
                            if ms_data_http_zip_path.startswith('http'):
                                os.system(
                                    f"wget '{ms_data_http_zip_path}' -O '{ms_data_local_zip_path}'"
                                )
                            elif os.path.exists(ms_data_http_zip_path):
                                ms_data_local_zip_path = ms_data_http_zip_path
                            else:
                                raise gr.Error(
                                    self.component_names.training_err6)
                            print(
                                f"unzip -o '{ms_data_local_zip_path}' -d '{work_data_dir}'"
                            )
                            os.system(
                                f"unzip -o '{ms_data_local_zip_path}' -d '{work_data_dir}'"
                            )
                        data_cfg['MS_DATASET_NAME'] = ms_data_local_file_path
                        data_cfg['MS_DATASET_NAMESPACE'] = ''
                        data_cfg['MS_DATASET_SUBNAME'] = ''
                        data_cfg['MS_REMAP_PATH'] = ms_data_local_file_path
                        data_cfg['MS_REMAP_KEYS'] = None
                    elif (os.path.exists(ms_data_name) and os.path.exists(
                            os.path.join(ms_data_name, 'train.csv'))
                          and os.path.exists(
                              os.path.join(ms_data_name, 'images'))):
                        data_cfg['MS_DATASET_NAME'] = ms_data_name
                        data_cfg['MS_DATASET_NAMESPACE'] = ''
                        data_cfg['MS_DATASET_SUBNAME'] = ''
                        data_cfg['MS_REMAP_PATH'] = ms_data_name
                        data_cfg['MS_REMAP_KEYS'] = None
                    else:
                        data_cfg['MS_DATASET_NAME'] = ms_data_name
                        data_cfg['MS_DATASET_NAMESPACE'] = ms_data_space
                        data_cfg['MS_DATASET_SUBNAME'] = ms_data_subname
                        if ms_data_name == 'style_custom_dataset':
                            data_cfg['MS_REMAP_KEYS'] = {
                                'Image:FILE': 'Target:FILE'
                            }
                        elif ms_data_name == 'lora-stable-diffusion-finetune':
                            data_cfg['MS_REMAP_KEYS'] = {'Text': 'Prompt'}
                        else:
                            data_cfg['MS_REMAP_KEYS'] = None
                    data_cfg['OUTPUT_SIZE'] = [
                        int(resolution_height),
                        int(resolution_width)
                    ]
                    if enable_resolution_bucket:
                        local_data_dir = data_cfg['MS_DATASET_NAME']
                        local_file_list = os.path.join(local_data_dir,
                                                       'file.txt')
                        data_num = sum(1 for line in open(local_file_list))
                        if os.path.exists(local_data_dir) and os.path.exists(
                                local_file_list):
                            data_cfg.update({
                                'NAME':
                                'ImageTextPairDataset'
                                if data_cfg['NAME'] == 'ImageTextPairMSDataset'
                                else data_cfg['NAME'],
                                'ENABLE_RESOLUTION_BUCKET':
                                enable_resolution_bucket,
                                'SAMPLER': {
                                    'NAME':
                                    'ResolutionBatchSampler',
                                    'DATA_FILE':
                                    local_file_list,
                                    'FIELDS':
                                    ['img_path', 'width', 'height', 'prompt'],
                                    'DELIMITER':
                                    '#;#',
                                    'MAX_RESO': [
                                        int(resolution_width),
                                        int(resolution_height)
                                    ],
                                    'MIN_BUCKET_RESO':
                                    int(min_bucket_resolution),
                                    'MAX_BUCKET_RESO':
                                    int(max_bucket_resolution),
                                    'BUCKET_RESO_STEPS':
                                    int(bucket_resolution_steps),
                                    'BUCKET_NO_UPSCALE':
                                    bucket_no_upscale
                                },
                                'DATA_NUM':
                                data_num
                            })
                            if 'TRANSFORMS' in data_cfg:
                                for trans in data_cfg['TRANSFORMS']:
                                    if trans['NAME'] == 'Select':
                                        trans['META_KEYS'] = [
                                            'img_path', 'image_size'
                                        ]
                        else:
                            raise Exception(
                                'Cannot find right data format for resolution_bucket'
                            )

                return data_cfg

            def prepare_train_video_data(data_cfg):
                if ms_data_name.startswith('http') and (
                        '.txt' in ms_data_name or '.csv' in ms_data_name):
                    data_name = get_data_from_list()
                else:
                    data_name = os.path.join(ms_data_name, 'file.txt')

                data_cfg['BATCH_SIZE'] = int(train_batch_size)
                data_cfg['PROMPT_PREFIX'] = prompt_prefix
                if data_cfg['NAME'] in ['VideoGenDataset']:
                    data_cfg['SAMPLER']['SUB_SAMPLERS'][0][
                        'PATH_PREFIX'] = os.path.dirname(data_name)
                    data_cfg['SAMPLER']['SUB_SAMPLERS'][0][
                        'INDEX_FILE'] = data_name
                elif data_cfg['NAME'] in ['VideoGenDatasetOTF']:
                    data_cfg['PATH_PREFIX'] = os.path.dirname(data_name)
                    data_cfg['DATA_FILE'] = data_name
                else:
                    raise Exception('Unsupported data type {}'.format(
                        data_cfg['NAME']))
                return data_cfg

            def get_data_from_list():
                file_list = []
                file = FS.get_from(ms_data_name)
                with FS.get_from(file) as local_path:
                    with open(local_path, 'r') as f:
                        for line in tqdm(f):
                            line = line.strip()
                            if line == '':
                                continue
                            try:
                                src_video_path, caption = line.split('#;#', 1)
                            except Exception:
                                try:
                                    src_video_path, caption = line.split(
                                        ',', 1)
                                except Exception:
                                    raise gr.Error(
                                        self.component_names.illegal_data_err)
                            relative_path = os.path.join(
                                'videos',
                                f'{get_md5(src_video_path)[:18]}_{int(time.time())}.mp4'
                            )
                            video_path = os.path.join(
                                self.save_file_local_path, ori_data_name,
                                relative_path)
                            local_path = FS.get_from(src_video_path,
                                                     local_path=video_path)
                            video_reader = decord.VideoReader(local_path)
                            w = video_reader[0].shape[1]
                            h = video_reader[0].shape[0]
                            file_list.append('{}#;#{}#;#{}#;#{}\n'.format(
                                relative_path, w, h, caption))
                local_save_file_list = os.path.join(self.save_file_local_path,
                                                    ori_data_name, 'file.txt')
                directory = os.path.dirname(local_save_file_list)
                os.makedirs(directory, exist_ok=True)
                FS.delete_object(file)
                with open(local_save_file_list, 'w') as f:
                    f.writelines(file_list)
                return local_save_file_list

            def prepare_eval_data(data_cfg):
                data_cfg['PROMPT_PREFIX'] = prompt_prefix
                data_cfg['IMAGE_SIZE'] = [
                    int(resolution_height),
                    int(resolution_width)
                ]
                if eval_image is not None:
                    ep = eval_prompts
                    ep = '' if ep is None else ep
                    ep = ep[0] if isinstance(ep, list) else ep

                    eval_image_path = os.path.join(work_dir, 'eval_image.jpg')
                    with FS.put_to(eval_image_path) as local_file:
                        eval_image.save(local_file)
                    data_cfg['PROMPT_DATA'] = [ep + '#;#' + eval_image_path]
                    data_cfg['FIELDS'] = ['prompt', 'src_path']
                else:
                    data_cfg['PROMPT_DATA'] = eval_prompts
                return data_cfg

            def prepare_train_config():
                cfg_file = os.path.join(work_dir, 'train.yaml')
                current_model_info = self.BASE_CFG_VALUE[base_model][
                    base_model_revision]
                modify_para = current_model_info['modify_para']
                cfg = copy.deepcopy(current_model_info['config_value'])
                if isinstance(modify_para, dict) and tuner_name in modify_para:
                    modify_c = modify_para[tuner_name]
                    if isinstance(modify_c, dict) and 'TRAIN' in modify_c:
                        train_modify_c = modify_c['TRAIN']
                        if isinstance(train_modify_c, dict):
                            for key, val in train_modify_c.items():
                                cache_value = [cfg]
                                c_k_list = key.split('.')
                                for idx, c_k in enumerate(c_k_list):
                                    if c_k.strip() == '':
                                        continue
                                    cache_value.append(
                                        copy.deepcopy(cache_value[idx][c_k]))
                                current_val = copy.deepcopy(val)
                                for c_k, v in zip(c_k_list[::-1],
                                                  cache_value[:-1][::-1]):
                                    v[c_k] = current_val
                                    current_val = v
                                cfg = current_val
                # update config
                cfg['SOLVER']['WORK_DIR'] = work_dir
                # cfg['SOLVER']['OPTIMIZER']['LEARNING_RATE'] = float(
                #     learning_rate * 640 / int(train_batch_size))
                cfg['SOLVER']['OPTIMIZER']['LEARNING_RATE'] = float(
                    learning_rate)
                cfg['SOLVER']['MAX_EPOCHS'] = int(train_epoch)
                cfg['SOLVER']['TRAIN_DATA']['BATCH_SIZE'] = int(
                    train_batch_size)
                if 'TUNER' in cfg['SOLVER']:
                    tuner_cfg_list = current_model_info['tuner_para'][
                        tuner_name] if isinstance(
                            current_model_info['tuner_para'],
                            dict) and tuner_name in current_model_info[
                                'tuner_para'] else None
                    if tuner_cfg_list is not None:
                        tuner_params = dict(
                            lora_alpha=int(lora_alpha),
                            lora_rank=int(lora_rank),
                            text_lora_alpha=int(text_lora_alpha),
                            text_lora_rank=int(text_lora_rank),
                            sce_ratio=sce_ratio)
                        tuner_cfg_list = [
                            update_tuner_cfg(tuner_name, tuner_cfg,
                                             **tuner_params)
                            for tuner_cfg in tuner_cfg_list
                        ]
                    cfg['SOLVER']['TUNER'] = tuner_cfg_list

                if cfg['SOLVER']['TRAIN_DATA']['NAME'] in [
                        'VideoGenDataset', 'VideoGenDatasetOTF'
                ]:
                    cfg['SOLVER']['TRAIN_DATA'] = prepare_train_video_data(
                        cfg['SOLVER']['TRAIN_DATA'])
                else:
                    cfg['SOLVER']['TRAIN_DATA'] = prepare_train_image_data(
                        cfg['SOLVER']['TRAIN_DATA'])
                if eval_prompts is not None and len(eval_prompts) > 0:
                    cfg['SOLVER']['EVAL_DATA'] = prepare_eval_data(
                        cfg['SOLVER']['EVAL_DATA'])
                else:
                    cfg['SOLVER'].pop('EVAL_DATA')
                if 'SAMPLE_ARGS' in cfg[
                        'SOLVER'] and not enable_resolution_bucket:
                    cfg['SOLVER']['SAMPLE_ARGS']['IMAGE_SIZE'] = [
                        int(resolution_height),
                        int(resolution_width)
                    ]
                for hook in cfg['SOLVER']['TRAIN_HOOKS']:
                    if hook['NAME'] == 'CheckpointHook':
                        hook['INTERVAL'] = save_interval
                        hook['PUSH_TO_HUB'] = push_to_hub
                        hook['HUB_MODEL_ID'] = hub_model_id
                    if hook['NAME'] == 'BackwardHook':
                        hook['ACCUMULATE_STEP'] = int(accumulate_step)
                if 'EVAL_HOOKS' in cfg['SOLVER']:
                    for hook in cfg['SOLVER']['EVAL_HOOKS']:
                        if hook['NAME'] == 'ProbeDataHook':
                            hook['PROB_INTERVAL'] = save_interval

                with open(cfg_file, 'w') as f_out:
                    yaml.dump(cfg,
                              f_out,
                              encoding='utf-8',
                              allow_unicode=True,
                              default_flow_style=False)
                return cfg_file

            self.trainer_ins.set_gpus(gpus)
            before_kill_inference = self.trainer_ins.check_memory()
            if hasattr(manager, 'inference'):
                for k, v in manager.inference.pipe_manager.pipeline_level_modules.items(
                ):
                    if hasattr(v, 'dynamic_unload'):
                        v.dynamic_unload(name='all')
            if (hasattr(manager, 'preprocess') and hasattr(
                    manager.preprocess.dataset_gallery.processors_manager,
                    'dynamic_unload')):
                manager.preprocess.dataset_gallery.processors_manager.dynamic_unload(
                )
            after_kill_inference = self.trainer_ins.check_memory()
            message = f'GPU info: {before_kill_inference}. \n\n'
            message += f'After unloading inference models, the GPU info: {after_kill_inference}. \n\n'
            _ = prepare_train_config()
            self.trainer_ins.start_task(work_name)
            message += self.trainer_ins.get_log(work_name)
            if user_name not in inference_ui.user_level_model_list:
                inference_ui.user_level_model_list[user_name] = []
            if work_name not in inference_ui.user_level_model_list[user_name]:
                inference_ui.user_level_model_list[user_name].append(work_name)
            gr.Info('Start Training!' + message)
            return gr.Dropdown(
                choices=inference_ui.user_level_model_list[user_name],
                value=work_name)

        self.training_button.click(
            run_train,
            inputs=[
                self.work_name, self.data_source, self.data_type,
                self.ori_data_name, self.ms_data_space, self.ms_data_name,
                self.ms_data_subname, self.base_model,
                self.base_model_revision, self.tuner_name,
                self.resolution_height, self.resolution_width,
                self.train_epoch, self.learning_rate, self.save_interval,
                self.train_batch_size, self.prompt_prefix,
                self.replace_keywords, self.push_to_hub, self.eval_prompts,
                self.eval_image, self.lora_alpha, self.lora_rank,
                self.text_lora_alpha, self.text_lora_rank, self.sce_ratio,
                self.enable_resolution_bucket, self.min_bucket_resolution,
                self.max_bucket_resolution, self.bucket_resolution_steps,
                self.bucket_no_upscale, self.accumulate_step, self.gpus,
                manager.user_name
            ],
            outputs=[inference_ui.output_model_name],
            queue=True)
