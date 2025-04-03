# -*- coding: utf-8 -*-
# Copyright (c) Alibaba, Inc. and its affiliates.
# For dataset manager


class TunerManagerNames():
    def __init__(self, language='en'):
        self.save_symbol = '\U0001F4BE'  # 💾
        self.delete_symbol = '\U0001f5d1'  # 🗑️
        self.refresh_symbol = '\U0001f504'  # 🔄
        self.model_export = '\U0001F517'  # 🔗
        self.model_import = '\U00002795'  # ➕
        self.submit = '\U00002714'  # ✔️
        self.close = '\U00002716'  # ✖️

        if language == 'en':
            self.browser_block_name = 'Tuner Browser  ' \
                                      '(\U0001F4BE: Save; \U0001f504: Refresh; \U0001F517: Export; \U00002795: Import)'
            self.base_models = 'Base Model-Tuner Type'
            self.tuner_models = 'Tuner Name'
            self.info_block_name = 'Tuner Info'
            self.tuner_name = 'Tuner Name'
            self.rename = 'Rename'
            self.tuner_type = 'Tuner Type'
            self.base_model_name = 'Base Model Name'
            self.tuner_desc = 'Tuner Description'
            self.tuner_example = 'Results Example'
            self.tuner_prompt_example = 'Prompt Example'
            self.model_err3 = "Doesn't surpport this base model"
            self.model_err4 = \
                f'Custom model does not exist. Please save{self.save_symbol} model first.'
            self.model_err5 = 'Model name not registered locally.'
            self.go_to_inference = 'Go To Inference'
            self.save = 'save changes'
            self.delete = 'Delete'

            self.ms_sdk = 'ModelScope API Token'
            self.ms_username = 'ModelScope User Name'
            self.ms_model_private = 'ModelScope Model Private'
            self.ms_modelid = 'ModelScope Model ID'
            self.ms_url = 'ModelScope Model Url'

            self.hf_sdk = 'HuggingFace API Token'
            self.hf_username = 'HuggingFace User Name'
            self.hf_model_private = 'HuggingFace Model Private'
            self.hf_modelid = 'HuggingFace Model ID'
            self.hf_url = 'HuggingFace Model Url'

            self.export_file = 'Download Model'
            self.save_start = 'Start export model...'
            self.save_end = 'Export model successfully!'
            self.export_zip_err1 = 'export model failure'
            self.zip_file = 'upload model'
            self.file_url = 'upload model url'
            self.upload_success = 'Upload Successfully'
            self.same_name = 'Upload model name already exists'
            self.upload_file_error = 'Upload without .bin file'
            self.upload_file_error2 = 'Upload file failed'
            self.url_invalid = 'Url is invalid'
            self.files_null = 'Upload files/url Null'
            self.utuner_name = 'Upload Tuner Name'
            self.ubase_model = 'Upload Base Model'
            self.utuner_type = 'Upload Tuner Type'
            self.illegal_data_err1 = 'Upload File Format Error(not .zip)'
            self.download_to_local = 'Download to Local'
            self.export_desc = 'Model Export To **ModelScope/HuggingFace**  (\U00002714: Submit; \U00002716: Close)'
            self.import_desc = (
                'Model Import From **ModelScope/HuggingFace/Local**  '
                '(\U00002714: Submit; \U00002716: Close)')
        elif language == 'zh':
            self.browser_block_name = (
                '微调模型查找  '
                '(\U0001F4BE: 保存; \U0001f504: 刷新; \U0001F517: 导出; \U00002795: 导入)'
            )
            self.base_models = '基模型-微调类型'
            self.tuner_models = '微调模型名称'
            self.info_block_name = '微调模型详情'
            self.tuner_name = '微调模型名称'
            self.rename = '重命名'
            self.tuner_type = '微调模型类型'
            self.base_model_name = '基模型名称'
            self.tuner_desc = '微调模型描述'
            self.tuner_example = '示例结果'
            self.tuner_prompt_example = '示例提示词'
            self.model_err3 = '不支持的基础模型'
            self.model_err4 = f'自定义模型不存在，请先保存{self.save_symbol}模型'
            self.model_err5 = '模型名未本地注册'
            self.go_to_inference = '使用模型'
            self.save = '保存修改'
            self.delete = '删除'

            self.ms_sdk = 'ModelScope API Token'
            self.ms_username = 'ModelScope用户名'
            self.ms_model_private = 'ModelScope模型不公开'
            self.ms_modelid = 'ModelScope模型ID'
            self.ms_url = 'ModelScope模型地址'

            self.hf_sdk = 'HuggingFace API Token'
            self.hf_username = 'HuggingFace 用户名'
            self.hf_model_private = 'HuggingFace 模型不公开'
            self.hf_modelid = 'HuggingFace 模型ID'
            self.hf_url = 'HuggingFace 模型地址'

            self.export_file = '下载数据'
            self.save_start = '开始导出模型...'
            self.save_end = '导出模型成功！'
            self.export_zip_err1 = '导出模型失败'
            self.zip_file = '上传模型'
            self.file_url = '上传模型链接'
            self.upload_success = '上传成功'
            self.same_name = '上传模型名已存在'
            self.upload_file_error = '上传缺少.bin文件'
            self.upload_file_error2 = '上传文件失败'
            self.url_invalid = '链接无效'
            self.files_null = '上传文件为空'
            self.utuner_name = '上传微调模型名称'
            self.ubase_model = '上传基模型类型'
            self.utuner_type = '上传微调模型类型'
            self.illegal_data_err1 = '上传文件格式错误(not .zip)'
            self.download_to_local = '下载至本地'
            self.export_desc = '模型导出至**ModelScope/HuggingFace**  (\U00002714: 提交; \U00002716: 关闭)'
            self.import_desc = '模型从 **ModelScope/HuggingFace/本地** 导入   (\U00002714: 提交; \U00002716: 关闭)'
