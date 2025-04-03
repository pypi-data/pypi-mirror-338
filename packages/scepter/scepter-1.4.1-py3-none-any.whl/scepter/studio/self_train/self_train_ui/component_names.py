# -*- coding: utf-8 -*-
# Copyright (c) Alibaba, Inc. and its affiliates.
# For dataset manager
class ModelUIName():
    def __init__(self, language='en'):
        if language == 'en':
            self.output_model_block = 'Model Output'
            self.output_model_name = 'Output Model Name'
            self.output_ckpt_name = 'Output Ckpt Name'
            self.test_prompt = 'Test Prompt'
            self.test_prefix = 'Test Prefix'
            self.test_n_prompt = 'Negative Prompt'
            self.sampler = 'Sampler'
            self.num_inference_steps = 'Sampling Step Length'
            self.inference_num = 'Number of Inferences'
            self.generator_seed = 'Sampling Seed'
            self.tuner_method = 'Tuning Method'
            self.inference_resolution = 'Inference Resolution'
            self.output_image = 'Output Result'
            self.display_button = 'Infer'
            self.extra_model_gtxt = 'Extra Model'
            self.extra_model_gbtn = 'Add Model'
            self.refresh_model_gbtn = 'Refresh Model'
            self.go_to_inference = 'Go to inference'
            self.btn_export_log = 'Export Log'
            self.export_file = 'Log File'
            self.log_block = 'Training Log...'
            self.gallery_block = 'Gallery Log...'
            self.eval_gallery = 'Eval Gallery'
            # Error or Warning
            self.inference_err1 = 'Inference failed, please try again.'
            self.inference_err2 = 'Test prompt is empty.'
            self.model_err3 = "Doesn't surpport this base model"
            self.model_err4 = "This model maybe not finish training, because model doesn't exist."
            self.model_err5 = "Model {} doesn't exist."
            self.training_warn1 = 'No log message util now.'

        elif language == 'zh':
            self.output_model_block = '模型产出'
            self.output_model_name = '产出名称'
            self.output_ckpt_name = '产出检查点名称'
            self.test_prompt = '测试提示词'
            self.test_prefix = '测试前缀'
            self.test_n_prompt = '负向提示词'
            self.sampler = '采样器'
            self.num_inference_steps = '采样步长'
            self.inference_num = '推理数'
            self.generator_seed = '采样种子'
            self.tuner_method = '训练方式'
            self.inference_resolution = '推理分辨率'
            self.output_image = '输出结果'
            self.display_button = '推理'
            self.extra_model_gtxt = '额外模型'
            self.extra_model_gbtn = '添加模型'
            self.refresh_model_gbtn = '刷新模型'
            self.btn_export_log = '导出日志'
            self.export_file = '日志文件'
            self.log_block = '训练日志...'
            self.training_button = '开始训练'
            self.gallery_block = '图像日志...'
            self.eval_gallery = '评测图像'
            # Error or Warning
            self.inference_err1 = '推理失败，请重试。'
            self.inference_err2 = '测试提示词为空。'
            self.model_err3 = '不支持的基础模型'
            self.go_to_inference = '使用模型'
            self.model_err4 = '模型可能没有训练完成或者模型不存在'
            self.model_err5 = '模型{}不存在'
            self.training_warn1 = '暂时没有日志文件；任务启动中或失败！'


class TrainerUIName():
    def __init__(self, language='en'):
        self.task_choices = ['Text2Image', 'Image Editing']
        self.data_task_map = {
            'scepter_txt2img': None,
            'scepter_img2img': 'edit',
            'scepter_txt2vid': 'dit'
        }
        if language == 'en':
            self.user_direction = '''
                ### User Guide
                - Data: Data preparation is done through the Data Manager. (zip example: [3D](https://www.modelscope.cn/api/v1/models/iic/scepter/repo?Revision=master&FilePath=datasets/3D_example_csv.zip), txt example(Support only video data): [txt](https://modelscope.cn/models/iic/scepter/resolve/master/datasets/video_example.txt))
                - Parameters: You can try modifying the related parameters.
                - Training: Click on [Start Training].
                - Testing: After completing the training, click [Go to inference].
                - Note: Timeouts may cause the connection to disconnect (an Error may occur).
                 After waiting for the time when the training is likely to be almost complete,
                 refresh the interface and then click [Refresh Model] at the bottom of the page.
                 The trained model should appear in the [Output Model Name] if training was successful;
                 if not, the training may be incomplete or have failed.
                - For processing and training with large-scale data, it is recommended to use the command line.
            '''  # noqa
            self.data_source_choices = [
                'Dataset zip', 'MaaS Dataset', 'Dataset Management'
            ]
            self.illegal_data_err = (
                'The list supports only "," or "#;#" as delimiters. '
                'The two columns represent video path and description, '
                'respectively.')
            self.data_source_value = 'Dataset zip'
            self.data_source_name = 'Data Source'
            self.data_type_map = {
                'scepter_txt2img': 'Text2Image Generation',
                'scepter_img2img': 'Image Edit Generation',
                'scepter_txt2vid': 'Text2Video Generation'
            }
            self.data_type_choices = list(self.data_type_map.keys())
            self.data_type_value = 'scepter_txt2img'
            self.data_type_value_video = 'scepter_txt2vid'
            self.data_type_name = 'Data Type'
            self.ori_data_name = 'Data Name'
            # Supports MaaS dataset/local/HTTP Zip package
            self.ms_data_name_place_hold = 'Please use Dataset Management.'
            self.ms_data_space = 'ModelScope Space'
            self.ms_data_subname = 'MaaS Dataset - Subset'
            self.task = 'Eval Editing Image'
            self.eval_data = 'Evaluation Data'
            self.train_data = 'Training Data'
            self.eval_prompts = 'Eval Prompts'
            self.eval_image = 'Eval Image'
            self.training_block = '''
                                    ### Training Parameters
                                  '''
            self.model_param = 'Model Parameters'
            self.base_param = 'Base Parameters'
            self.base_model = 'Base Model'
            self.tuner_name = 'Tuner Method'
            self.base_model_revision = 'Model Version Number'
            self.resolution_height = 'Train Image or Video Height'
            self.resolution_width = 'Train Image or Video Width'
            self.resolution_height_max = 'Resolution Height Max'
            self.resolution_width_max = 'Resolution Width Max'
            self.train_epoch = 'Total Training Epochs'
            self.learning_rate = 'Learning Rate'
            self.save_interval = 'Checkpoint Save Interval (Epochs)'
            self.train_batch_size = 'Training Batch Size'
            self.prompt_prefix = 'Prefix'
            self.replace_keywords = 'Trigger Keywords'
            self.work_name = 'Save Model Name (refresh to get a random value)'
            self.push_to_hub = 'Push to hub'
            self.training_button = 'Start Training'
            self.tuner_param = 'Tuner Parameters'
            self.enable_resolution_bucket = 'Enable Resolution Bucket'
            self.enable_resolution_bucket_ins = 'Automatically Pack Multi-Resolution Batches'
            self.resolution_param = 'Resolution Parameters'
            self.min_bucket_resolution = 'Min Bucket Resolution'
            self.max_bucket_resolution = 'Max Bucket Resolution'
            self.bucket_resolution_steps = 'Bucket Resolution Steps'
            self.bucket_no_upscale = 'Bucket No Upscale'
            self.bucket_no_upscale_ins = 'Disable Automatic Image Upscaling'
            self.accumulate_step = 'Accumulate Step'
            self.gpus = 'Select GPUs'
            # Error or Warning
            self.training_err1 = 'CUDA is unavailable.'
            self.training_err2 = 'Currently insufficient VRAM, training failed!'
            self.training_err3 = 'You need to prepare training data.'
            self.training_err4 = 'Save model name already exists or is None, please regenerate this name.'
            self.training_err5 = 'Training failed.'
            self.training_err6 = "Can't process training data"

        elif language == 'zh':
            self.user_direction = '''
                ### 使用说明
                - 数据: 通过数据管理器进行数据的准备（ZIP样例：[3D](https://www.modelscope.cn/api/v1/models/iic/scepter/repo?Revision=master&FilePath=datasets/3D_example_csv.zip)，txt样例（仅支持视频数据）：[txt](https://modelscope.cn/models/iic/scepter/resolve/master/datasets/video_example.txt)）
                - 参数: 可尝试进行相关参数的修改
                - 训练: 点击【开始训练】
                - 测试: 完成训练后点击【使用模型】
                - 注意：超时可能导致连接断开(出现Error)，可以等差不多可能训完后，刷新界面再点击页面最后的[刷新模型]，即可在[产出模型名称中]出现已经完成训练的模型，若不存在则没有完成训练或训练失败
                - 对于大规模数据的处理和训练，建议使用命令行形式
                '''  # noqa
            self.data_source_choices = ['数据集zip', 'MaaS数据集', '数据管理器']
            self.illegal_data_err = '列表只支持,或#;#作为分割符，两列分别为视频路径/描述'
            self.data_source_value = '数据集zip'
            self.data_source_name = '数据集来源'
            self.data_type_map = {
                'scepter_txt2img': '文生图数据',
                'scepter_img2img': '图像编辑（图生图）数据',
                'scepter_txt2vid': '文生视频数据'
            }
            self.data_type_choices = list(self.data_type_map.keys())
            self.data_type_value = 'scepter_txt2img'
            self.data_type_value_video = 'scepter_txt2vid'
            self.data_type_name = '数据类型'
            self.ori_data_name = '数据集名称'
            self.ms_data_name_place_hold = '请使用数据管理器导入'  # '支持MaaS数据集/本地/Http Zip包'
            self.ms_data_space = 'ModelScope 空间'
            self.ms_data_subname = 'MaaS数据集-子集'
            self.task = '任务'
            self.eval_data = '评测数据'
            self.train_data = '训练数据'
            self.eval_prompts = '评测文本'
            self.eval_image = '评测图片'
            self.training_block = '''
                                    ### 训练参数
                                  '''
            self.model_param = '模型参数'
            self.base_param = '基本参数'
            self.base_model = '基础模型'
            self.tuner_name = '微调方法'
            self.base_model_revision = '模型版本号'
            self.resolution_height = '训练图片或视频高度'
            self.resolution_width = '训练图片或视频宽度'
            self.resolution_height_max = '最大训练高度'
            self.resolution_width_max = '最大训练宽度'
            self.train_epoch = '总训练轮数'
            self.learning_rate = '学习率'
            self.save_interval = '中间结果存储间隔（轮数）'
            self.train_batch_size = '每批次数据条数（Batch Size）'
            self.prompt_prefix = '前缀'
            self.replace_keywords = '触发关键词'
            self.work_name = '保存模型名称（刷新获得随机值）'
            self.push_to_hub = '推送魔搭社区'
            self.tuner_param = '微调参数'
            self.enable_resolution_bucket = '开启分辨率分桶'
            self.enable_resolution_bucket_ins = '自动组装多分辨率Batch'
            self.resolution_param = '分辨率参数'
            self.min_bucket_resolution = '最小分桶分辨率'
            self.max_bucket_resolution = '最大分桶分辨率'
            self.bucket_resolution_steps = '分桶分辨率步长'
            self.bucket_no_upscale = '分桶分辨率不做放大'
            self.bucket_no_upscale_ins = '禁止图片分辨率上采样'
            self.accumulate_step = '梯度累积数量'
            self.gpus = '选择GPU'
            # Error or Warning
            self.training_err1 = 'CUDA不可用.'
            self.training_err2 = '目前显存不足，训练失败！'
            self.training_err3 = '您需要准备训练数据'
            self.training_err4 = '保存模型未生成或名称已经存在，请重新生成名称'
            self.training_err5 = '训练失败'
            self.training_err6 = '无法处理的数据'
