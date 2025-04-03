# -*- coding: utf-8 -*-
# Copyright (c) Alibaba, Inc. and its affiliates.
import copy
import os.path
from io import BytesIO
from numbers import Number

import numpy as np
import torch
from PIL import Image

from scepter.modules.utils.file_system import FS


def check_legal_type(data):
    if isinstance(data, str) or isinstance(data, Number):
        return True
    elif isinstance(data, dict):
        for k, v in data.items():
            if not check_legal_type(v):
                return False
        return True
    elif isinstance(data, list):
        for v in data:
            if not check_legal_type(v):
                return False
        return True
    else:
        return False


def register_data(probe_data: dict, key_prefix=''):
    ret_data = {}
    dist_data = {}
    for k, v in probe_data.items():
        key = f'{key_prefix}_{k}'
        if isinstance(v, torch.Tensor) or isinstance(v, np.ndarray):
            ret_data[key] = ProbeData(v)
        elif isinstance(v, ProbeData):
            ret_data[key] = v
        else:
            if not check_legal_type(v):
                raise f'The datatype of {key} should be included in [array, tensor, number, str] or the dict or ' \
                      f'list of (number, str); if you want register the list of image, please use ProbeData instance.'
            ret_data[key] = ProbeData(v)
        if ret_data[key].view_distribute:
            dist_data[key] = ret_data[key].distribute

    return ret_data, dist_data


def merge_gathered_probe(all_gathered_data):
    '''
     Merge the gathered data on rank_0.
    Returns:
        The merged data.

    '''
    for key, gathered_data in all_gathered_data.items():
        # Must be the list of ProbeData.
        if isinstance(gathered_data, list):
            for v in gathered_data:
                if not isinstance(v, ProbeData):
                    all_gathered_data[key] = gathered_data
            # Must be the gathered data.
            ret_data = gathered_data[0]
            if not isinstance(ret_data.data,
                              list) and (isinstance(ret_data.data, np.ndarray)
                                         or isinstance(ret_data.data, dict)
                                         or check_legal_type(ret_data.data)):
                new_data = [v.data for v in gathered_data]
                if ret_data.build_label is not None:
                    ret_data.build_label = [
                        v.build_label for v in gathered_data
                    ]
                all_gathered_data[key] = ProbeData(
                    new_data,
                    is_image=ret_data.is_image,
                    is_video=ret_data.is_video,
                    build_html=ret_data.build_html,
                    build_label=ret_data.build_label,
                    view_distribute=ret_data.view_distribute,
                    is_presave=ret_data.is_presave)
            elif isinstance(ret_data.data, list):
                if ret_data.build_label is not None:
                    if isinstance(ret_data.build_label, str):
                        ret_data.build_label = [
                            ret_data.build_label for _ in ret_data.data
                        ]
                for v in gathered_data[1:]:
                    ret_data.data += v.data
                    if ret_data.build_label is not None:
                        if isinstance(v.build_label, str):
                            ret_data.build_label.extend(
                                [v.build_label for _ in v.data])
                        ret_data.build_label.extend(v.build_label)
                all_gathered_data[key] = ProbeData(
                    ret_data.data,
                    is_image=ret_data.is_image,
                    is_video=ret_data.is_video,
                    build_html=ret_data.build_html,
                    build_label=ret_data.build_label,
                    view_distribute=ret_data.view_distribute,
                    is_presave=ret_data.is_presave)
        else:
            all_gathered_data[key] = gathered_data
    return all_gathered_data


class MediaHandler():
    def __init__(self, batch_size=10):
        self.file_list = []
        self.target_path_list = []
        self.target_status = {}
        self.batch_size = batch_size

    def append(self, source_file, target_path):
        self.file_list.append(source_file)
        self.target_path_list.append(target_path)
        if len(self.file_list) > 2 * self.batch_size:
            generator = FS.put_batch_objects_to(self.file_list,
                                                self.target_path_list,
                                                batch_size=self.batch_size)
            for local_path, target_path, flg in generator:
                self.target_status[target_path] = flg
            self.file_list.clear()
            self.target_path_list.clear()

    def sync(self):
        if len(self.file_list) > 0:
            if len(self.file_list) > 4 * self.batch_size:
                generator = FS.put_batch_objects_to(self.file_list,
                                                    self.target_path_list,
                                                    batch_size=self.batch_size)
                for local_path, target_path, flg in generator:
                    self.target_status[target_path] = flg
            else:
                for file_, target_path in zip(self.file_list,
                                              self.target_path_list):
                    self.target_status[target_path] = FS.put_object(
                        file_.getvalue(), target_path)
            self.file_list.clear()
            self.target_path_list.clear()

    def clear(self):
        self.file_list.clear()
        self.target_path_list.clear()
        self.target_status.clear()


class ProbeData():
    def __init__(self,
                 data,
                 is_image=False,
                 is_video=False,
                 fps=8,
                 build_html=False,
                 build_label=None,
                 view_distribute=False,
                 is_presave=False):
        ''' Probe Data Initialize.
            We only support basic types such as [torch.Tensor, numpy.ndarray, number, str],
            or [dict, list] of [dict, list,
            number, str], or [dict, list] of [tensor, array]
        '''
        data = copy.deepcopy(data)
        self.basic_type = True
        self._distribute_dict = {}
        if view_distribute:
            is_legal = True
            if isinstance(data, str) or isinstance(data, Number):
                is_legal = True
                if data in self._distribute_dict:
                    self._distribute_dict[data] += 1
                else:
                    self._distribute_dict[data] = 1
            elif isinstance(data, list):
                for v in data:
                    if isinstance(v, str) or isinstance(v, Number):
                        is_legal = True
                        if v in self._distribute_dict:
                            self._distribute_dict[v] += 1
                        else:
                            self._distribute_dict[v] = 1
                    else:
                        is_legal = False
            elif isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(v, str) or isinstance(v, Number):
                        is_legal = True
                        n_k = f'{k}_{v}'
                        if n_k in self._distribute_dict:
                            self._distribute_dict[n_k] += 1
                        else:
                            self._distribute_dict[n_k] = 1
                    else:
                        is_legal = False
            else:
                is_legal = False
            if not is_legal:
                print('Unsurpport data type', data)
                assert is_legal
        self.view_distribute = view_distribute
        if isinstance(data, torch.Tensor):
            self.data = data.detach().cpu().numpy()
        elif isinstance(data, np.ndarray):
            self.data = data
        elif isinstance(data, dict):
            for k, v in data.items():
                if not check_legal_type(v):
                    if isinstance(v, torch.Tensor):
                        data[k] = v.detach().cpu().numpy()
                        self.basic_type = False
                    elif isinstance(v, np.ndarray):
                        data[k] = v
                        self.basic_type = False
                    elif isinstance(v, list):
                        for v_idx, v_v in enumerate(v):
                            if not check_legal_type(v_v):
                                if isinstance(v_v, torch.Tensor):
                                    data[k][v_idx] = v_v.detach().cpu().numpy()
                                    self.basic_type = False
                                elif isinstance(v_v, np.ndarray):
                                    data[k][v_idx] = v_v
                                    self.basic_type = False
                                else:
                                    raise f'Unsupport data type for {v_v}'
                    elif isinstance(v, dict):
                        for k_k, v_v in v.items():
                            if not check_legal_type(v_v):
                                if isinstance(v_v, torch.Tensor):
                                    data[k][k_k] = v_v.detach().cpu().numpy()
                                    self.basic_type = False
                                elif isinstance(v_v, np.ndarray):
                                    data[k][k_k] = v_v
                                    self.basic_type = False
                                else:
                                    raise f'Unsupport data type for {v_v}'
                    else:
                        raise f'Unsupport data type for {v}'
            self.data = data
        elif isinstance(data, list):
            for idx, v in enumerate(data):
                if not check_legal_type(v):
                    if isinstance(v, torch.Tensor):
                        data[idx] = v.detach().cpu().numpy()
                        self.basic_type = False
                    elif isinstance(v, np.ndarray):
                        data[idx] = v
                        self.basic_type = False
                    elif isinstance(v, list):
                        for v_idx, v_v in enumerate(v):
                            if not check_legal_type(v_v):
                                if isinstance(v_v, torch.Tensor):
                                    data[idx][v_idx] = v_v.detach().cpu(
                                    ).numpy()
                                    self.basic_type = False
                                elif isinstance(v_v, np.ndarray):
                                    data[idx][v_idx] = v_v
                                    self.basic_type = False
                                else:
                                    raise f'Unsupport data type for {v_v}'
                    elif isinstance(v, dict):
                        for k, v_v in v.items():
                            if not check_legal_type(v_v):
                                if isinstance(v_v, torch.Tensor):
                                    data[idx][k] = v_v.detach().cpu().numpy()
                                    self.basic_type = False
                                elif isinstance(v_v, np.ndarray):
                                    data[idx][k] = v_v
                                    self.basic_type = False
                                else:
                                    raise f'Unsupport data type for {v_v}'
                    else:
                        raise f'Unsupport data type for {v}'
            self.data = data
        elif check_legal_type(data):
            self.data = data
        else:
            raise f'Unsupport data type for {data}'

        self.is_image = is_image
        self.is_video = is_video
        self.image_postfix = 'jpg'
        self.video_postfix = 'mp4'
        self.fps = fps
        self.build_html = build_html
        self.media_handler = MediaHandler()
        self.is_presave = is_presave

        if self.build_html:
            assert build_label is not None
            if isinstance(self.data, str):
                assert isinstance(build_label, str)
            if isinstance(self.data, list):
                assert isinstance(build_label, str) or isinstance(
                    build_label, list)
            if isinstance(self.data, dict):
                assert isinstance(build_label, str) or isinstance(
                    build_label, dict)
        self.build_label = build_label

    def get_format(self, extension):
        if extension.lower() in ['jpg', 'jpeg']:
            return 'JPEG'
        if extension.lower() in ['png']:
            return 'PNG'
        return 'JPEG'

    def save_one_video(self, file_path, videos, fps=8):
        # write video
        import imageio
        try:
            writer = imageio.get_writer(file_path,
                                        fps=fps,
                                        format='.mp4',
                                        codec='libx264',
                                        quality=8)
            for frame in videos:
                writer.append_data(frame)
            writer.close()
            return True
        except Exception:
            return False

    def save_video(self, file_prefix, videos, video_postfix, fps=8, rank=0):
        if isinstance(videos, list):
            for video in videos:
                if isinstance(video, list):
                    raise 'Only surpport one layer nested list.'
            return [
                self.save_video(file_prefix + f'_{rank}_{idx}', v,
                                video_postfix, fps)
                for idx, v in enumerate(videos)
            ]
        np_shape = videos.shape
        # 4D
        shape_str = '_'.join([str(v) for v in np_shape])
        if len(np_shape) == 5:
            # channel is 1 or 3
            if np_shape[-1] == 1 or np_shape[-1] == 3 or np_shape[-1] == 4:
                if np_shape[-1] == 1:
                    videos = videos.reshape(videos.shape[:-1])
                file_list = []
                for idx in range(np_shape[0]):
                    if videos[idx].shape[0] > 1:
                        file_path = os.path.join(
                            file_prefix,
                            f'probe_{rank}_{idx}_[{shape_str}].{video_postfix}'
                        )
                        byio = BytesIO()
                        is_suc = self.save_one_video(byio, videos[idx], fps)
                        if not is_suc:
                            byio.write(b'')
                    else:
                        file_path = os.path.join(
                            file_prefix,
                            f'probe_{rank}_{idx}_[{shape_str}].{self.image_postfix}'
                        )
                        byio = BytesIO()
                        Image.fromarray(videos[idx][0]).save(
                            byio, self.get_format(self.image_postfix))
                    self.media_handler.append(byio, file_path)
                    file_list.append(file_path)
                return file_list
            else:
                raise f"Ensure your data's dim is BWHC, and channel is 1 or 3 for {file_prefix}"
        elif len(np_shape) == 4:
            if np_shape[-1] == 1 or np_shape[-1] == 3 or np_shape[-1] == 4:
                if np_shape[-1] == 1:
                    videos = videos.reshape(videos.shape[:-1])
                if videos.shape[0] > 1:
                    file_path = file_prefix + f'_probe_{rank}_[{shape_str}].{video_postfix}'
                    byio = BytesIO()
                    is_suc = self.save_one_video(byio, videos, fps)
                    if not is_suc:
                        byio.write(b'')
                else:
                    file_path = file_prefix + f'_probe_{rank}_[{shape_str}].{self.image_postfix}'
                    byio = BytesIO()
                    Image.fromarray(videos[0]).save(
                        byio, self.get_format(self.image_postfix))
                self.media_handler.append(byio, file_path)
                return file_path
            else:
                videos = videos.reshape(list(videos.shape) + [1])
                return self.save_video(file_prefix,
                                       videos,
                                       video_postfix,
                                       fps=fps)
        else:
            raise f"Ensure your data's dim is BFWHC or FWHC, and channel is 1 or 3 for {file_prefix}"

    def save_image(self, file_prefix, images, image_postfix, rank=0):
        if isinstance(images, list):
            for image in images:
                if isinstance(image, list):
                    raise TypeError('Only surpport one layer nested list.')
            return [
                self.save_image(file_prefix + f'_{rank}_{idx}', v,
                                image_postfix) for idx, v in enumerate(images)
            ]
        np_shape = images.shape
        # 4D
        shape_str = '_'.join([str(v) for v in np_shape])
        if len(np_shape) == 4:
            # channel is 1 or 3
            if np_shape[-1] == 1 or np_shape[-1] == 3 or np_shape[-1] == 4:
                if np_shape[-1] == 1:
                    images = images.reshape(images.shape[:-1])
                file_list = []
                for idx in range(np_shape[0]):
                    file_path = os.path.join(
                        file_prefix,
                        f'probe_{rank}_{idx}_[{shape_str}].{image_postfix}')
                    byio = BytesIO()
                    Image.fromarray(images[idx, ...]).save(
                        byio, self.get_format(self.image_postfix))
                    self.media_handler.append(byio, file_path)
                    file_list.append(file_path)
                return file_list
            else:
                raise f"Ensure your data's dim is BWHC, and channel is 1 or 3 for {file_prefix}"
        elif len(np_shape) == 3:
            if np_shape[-1] == 1 or np_shape[-1] == 3 or np_shape[-1] == 4:
                if np_shape[-1] == 1:
                    images = images.reshape(images.shape[:-1])
                file_path = file_prefix + f'_probe_{rank}_[{shape_str}].{image_postfix}'
                byio = BytesIO()
                Image.fromarray(images).save(
                    byio, self.get_format(self.image_postfix))
                self.media_handler.append(byio, file_path)
                return file_path
            else:
                images = images.reshape(list(images.shape) + [1])
                return self.save_image(file_prefix, images, image_postfix)
        elif len(np_shape) == 2:
            file_path = file_prefix + f'_probe_{rank}_[{shape_str}].{image_postfix}'
            byio = BytesIO()
            Image.fromarray(images).save(byio,
                                         self.get_format(self.image_postfix))
            self.media_handler.append(byio, file_path)
            return file_path
        else:
            raise f"Ensure your data's dim is BWHC or WHC or WH, and channel is 1 or 3 for {file_prefix}"

    def save_npy(self, file_prefix, data, rank=0):
        shape_str = '_'.join([str(v) for v in data.shape])
        file_path = file_prefix + f'_{rank}_{shape_str}.npy'
        byio = BytesIO()
        np.save(byio, data)
        self.media_handler.append(byio, file_path)
        return file_path

    def save_html(self, html_prefix, ret_data, ret_label):
        height = 600
        with FS.put_to(html_prefix) as local_path:
            with open(local_path, 'w') as f:
                f.writelines('<meta charset="utf-8">\n')
                f.writelines(
                    '<style>input{height:' + f'{height}px;' +
                    'opacity:1.0;} textarea {font-size: 32px;}</style>\n')
                f.writelines('<br><hr/>\n')
                all_ranks = list()
                is_textarea = False
                for save_id, save_data in enumerate(zip(ret_data, ret_label)):
                    save_path, save_label = save_data
                    one_rank = '<table><tr>'
                    for idx, one_data in enumerate(zip(save_path, save_label)):
                        one_path, one_label = one_data
                        one_label = one_label.replace('<', '&lt;').replace(
                            '>', '&gt;')
                        try:
                            url = FS.get_url(
                                one_path, lifecycle=3600 * 365 * 24).replace(
                                    '.oss-internal.aliyun-inc.',
                                    '.oss.aliyuncs.').replace('-internal', '')
                        except Exception:
                            url = one_path
                        if len(one_label) > 10 and idx == len(save_path) - 1:
                            is_textarea = True
                        if self.is_video and one_path.endswith(
                                self.video_postfix):
                            one_rank += f'<td align="center"><video height="{height}" controls="">'
                            one_rank += f'<source src="{url}" type="video/mp4"></video>'
                            if idx == len(save_path) - 1 and is_textarea:
                                one_rank += f'<br><font size="4"><strong>{save_id}-{idx}<strong></font><br/></td>'
                                one_rank += f'<td align="center"><textarea rows="16" cols="40">{one_label}</textarea><br><font size="4"><strong>{save_id}-{idx}<strong></font><br/></td>'
                            else:
                                one_rank += f'<br><font size="4"><strong>{save_id}-{idx}|{one_label}<strong></font><br/></td>'
                        else:
                            one_rank += f'<td align="center"><input type="image" src="{url}" >'
                            if idx == len(save_path) - 1 and is_textarea:
                                one_rank += f'<br><font size="4"><strong>{save_id}-{idx}<strong></font><br/></td>'
                                one_rank += f'<td align="center"><textarea rows="16" cols="40">{one_label}</textarea><br><font size="4"><strong>{save_id}-{idx}<strong></font><br/></td>'
                            else:
                                one_rank += f'<br><font size="4"><strong>{save_id}-{idx}|{one_label}<strong></font><br/></td>'

                    one_rank += '</tr></table><hr/>'
                    all_ranks.append(one_rank)
                f.writelines('\n'.join(all_ranks))
        return html_prefix

    @property
    def distribute(self):
        return self._distribute_dict

    def save_one_media(self,
                       idx,
                       v,
                       prefix_path,
                       image_postfix,
                       video_postfix,
                       rank=0):
        ret_label = None
        if self.is_image:
            ret_medias = self.save_image(prefix_path,
                                         v,
                                         image_postfix,
                                         rank=rank)
        elif self.is_video:
            ret_medias = self.save_video(prefix_path,
                                         v,
                                         video_postfix,
                                         fps=self.fps,
                                         rank=rank)
        else:
            ret_data = self.save_npy(prefix_path, v, rank=rank)
            return ret_data, ret_label
        ret_data = ret_medias if isinstance(ret_medias, list) else [ret_medias]
        if self.build_html:
            if isinstance(ret_medias, list):
                if isinstance(self.build_label, str):
                    ret_label = [self.build_label for _ in ret_medias]
                elif isinstance(self.build_label[idx], list):
                    assert len(self.build_label[idx]) == len(ret_medias)
                    ret_label = self.build_label[idx]
                else:
                    ret_label = [self.build_label[idx] for _ in ret_medias]
            else:
                if isinstance(self.build_label, str):
                    ret_label = [self.build_label]
                else:
                    ret_label = [self.build_label[idx]]
        return ret_data, ret_label

    def presave(self,
                prefix=None,
                image_postfix='jpg',
                video_postfix='mp4',
                rank=0):
        self.image_postfix = image_postfix
        self.video_postfix = video_postfix
        if isinstance(self.data, np.ndarray):
            if prefix is None:
                raise 'You should provide the save prefix for array sample.'
            # save jpg
            if self.is_image:
                ret_data = self.save_image(prefix,
                                           self.data,
                                           image_postfix,
                                           rank=rank)
            elif self.is_video:
                ret_data = self.save_video(prefix,
                                           self.data,
                                           video_postfix,
                                           fps=self.fps,
                                           rank=rank)
            else:
                ret_data = self.save_npy(prefix, self.data, rank=rank)
            self.media_handler.sync()
            self.media_handler.clear()
            if isinstance(ret_data, list):
                ret_data = [ret_data]
                ret_label = []
                if self.build_html:
                    if isinstance(self.build_label, str):
                        ret_label.append(
                            [self.build_label for _ in ret_data[0]])
                    else:
                        ret_label.append(self.build_label)
                    if not len(ret_data[0]) == len(ret_label[0]):
                        raise f"The {prefix} label's length should be equal with 1st dim {self.data.shape[0]}."
                self.data = {'ret_data': ret_data, 'ret_label': ret_label}
            else:
                self.data = ret_data
            self.is_presave = True
        elif isinstance(self.data, list):
            if not self.basic_type:
                ret_data = []
                ret_label = []
                for idx, v in enumerate(self.data):
                    prefix_path = os.path.join(prefix, f'{idx}')
                    ret_one_data, ret_one_label = self.save_one_media(
                        idx,
                        v,
                        prefix_path,
                        image_postfix,
                        video_postfix,
                        rank=rank)
                    ret_data.append(ret_one_data)
                    ret_label.append(
                        ret_one_label
                    ) if ret_one_label is not None else ret_label
                self.media_handler.sync()
                self.media_handler.clear()
                self.data = {'ret_data': ret_data, 'ret_label': ret_label}
                self.is_presave = True
        elif isinstance(self.data, dict):
            if not self.basic_type:
                ret_data = []
                ret_label = []
                for k, v in self.data.items():
                    prefix_path = os.path.join(prefix, f'{k}_')
                    ret_one_data, ret_one_label = self.save_one_media(
                        k,
                        v,
                        prefix_path,
                        image_postfix,
                        video_postfix,
                        rank=rank)
                    ret_data.append(ret_one_data)
                    ret_label.append(
                        ret_one_label
                    ) if ret_one_label is not None else ret_label
                self.media_handler.sync()
                self.media_handler.clear()
                self.data = {'ret_data': ret_data, 'ret_label': ret_label}
                self.is_presave = True

    def to_log(self,
               prefix=None,
               image_postfix='jpg',
               video_postfix='mp4',
               rank=0):
        if not self.is_presave:
            self.presave(prefix, image_postfix, video_postfix, rank=rank)
        if not self.is_presave:
            return self.data
        if isinstance(self.data, str):
            return self.data
        elif isinstance(self.data, dict):
            ret_data, ret_label = self.data['ret_data'], self.data['ret_label']
            if self.build_html:
                html_prefix = prefix + '_probe.html'
                html_file = self.save_html(html_prefix, ret_data, ret_label)
                return {'ori_file': ret_data, 'html': html_file}
            else:
                return {'ori_file': ret_data}
        elif isinstance(self.data, list):
            ret_data, ret_label = [], []
            for one_data in self.data:
                if isinstance(one_data, dict):
                    one_ret_data, one_ret_label = one_data[
                        'ret_data'], one_data['ret_label']
                    ret_data.extend(one_ret_data)
                    ret_label.extend(one_ret_label)
                elif isinstance(one_data, str):
                    ret_data.append(one_data)
            if (self.is_image or self.is_video) and self.build_html:
                html_prefix = prefix + '_probe.html'
                html_file = self.save_html(html_prefix, ret_data, ret_label)
                return {'ori_file': ret_data, 'html': html_file}
            else:
                return {'ori_file': ret_data}
