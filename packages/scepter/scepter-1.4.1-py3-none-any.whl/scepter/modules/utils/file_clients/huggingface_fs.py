# -*- coding: utf-8 -*-
# Copyright (c) Alibaba, Inc. and its affiliates.
import os
import os.path as osp
import urllib.parse as parse
import urllib.request
from typing import Optional, Union

from scepter.modules.utils.file_clients.base_fs import BaseFs
from scepter.modules.utils.file_clients.registry import FILE_SYSTEMS


@FILE_SYSTEMS.register_class()
class HuggingfaceFs(BaseFs):
    para_dict = {
        'RETRY_TIMES': {
            'value': 10,
            'description': 'Retry get object times.'
        }
    }
    para_dict.update(BaseFs.para_dict)

    def __init__(self, cfg, logger):
        super(HuggingfaceFs, self).__init__(cfg, logger=logger)
        retry_times = cfg.get('RETRY_TIMES', 10)
        self._retry_times = retry_times

    def get_prefix(self) -> str:
        return 'hf://'

    def support_write(self) -> bool:
        return False

    def support_link(self) -> bool:
        return False

    def basename(self, target_path) -> str:
        url = parse.unquote(target_path)
        url = url.split('?')[0]
        return osp.basename(url)

    def get_object_to_local_file(self,
                                 target_path,
                                 local_path=None,
                                 wait_finish=False) -> Optional[str]:
        from huggingface_hub import hf_hub_download

        key = osp.relpath(target_path, self.get_prefix())
        key, file_path = key.split('@', 1)

        if ':' in key:
            key, revision = key.split(':', 1)
        else:
            revision = None

        if local_path is None:
            local_path, is_tmp = self.map_to_local(key)
        else:
            is_tmp = False

        if revision is not None:
            local_path = local_path + '_' + str(revision)

        retry = 0
        while retry < self._retry_times:
            try:
                local_path = hf_hub_download(repo_id=key,
                                             revision=revision,
                                             filename=file_path,
                                             cache_dir=local_path)
                if osp.exists(local_path):
                    break
            except Exception:
                retry += 1

        if retry >= self._retry_times:
            return None

        if is_tmp:
            self.add_temp_file(local_path)
        return local_path

    def get_dir_to_local_dir(self,
                             target_path,
                             local_path=None,
                             wait_finish=False,
                             multi_thread=False,
                             timeout=3600,
                             sign_key=None,
                             worker_id=-1) -> Optional[str]:
        from huggingface_hub import snapshot_download
        assert target_path.startswith(self.get_prefix())

        key = osp.relpath(target_path, self.get_prefix())
        if '@' not in key:
            key, ret_folder = key.split('@', 1)[0], ''
        else:
            at_level_folder = key.split('@')
            if len(at_level_folder) > 2:
                raise f'Target path should include only one @, but you give {len(at_level_folder)} @.'
            key, ret_folder = at_level_folder

        if ':' in key:
            key, revision = key.split(':', 1)
        else:
            revision = None

        if local_path is None:
            local_path, is_tmp = self.map_to_local(key)
        else:
            is_tmp = False

        if revision is not None:
            local_path = local_path + '_' + str(revision)

        retry = 0
        while retry < self._retry_times:
            try:
                local_path = snapshot_download(repo_id=key,
                                               revision=revision,
                                               cache_dir=local_path)
                if osp.exists(local_path):
                    break
            except Exception:
                retry += 1

        if retry >= self._retry_times:
            return None

        if is_tmp:
            self.add_temp_file(local_path)
        if not ret_folder == '':
            local_path = os.path.join(local_path, ret_folder)
        return local_path

    def get_object(self, target_path):
        try:
            local_data = open(self.get_object_to_local_file(target_path),
                              'rb').read()
        except Exception as e:
            self.logger.error(f'Read {target_path} error {e}')
            local_data = None
        return local_data

    def put_object(self, local_data, target_path):
        raise NotImplementedError

    def put_object_from_local_file(self, local_path, target_path) -> bool:
        raise NotImplementedError

    def make_link(self, target_link_path, target_path) -> bool:
        raise NotImplementedError

    def make_dir(self, target_dir) -> bool:
        raise NotImplementedError

    def remove(self, target_path) -> bool:
        raise NotImplementedError

    def get_logging_handler(self, target_logging_path):
        raise NotImplementedError

    def walk_dir(self, file_dir, recurse=True):
        raise NotImplementedError

    def put_dir_from_local_dir(self, local_dir, target_dir) -> bool:
        raise NotImplementedError

    def size(self, target_path) -> Optional[int]:
        raise NotImplementedError

    def get_object_chunk_list(self,
                              target_path,
                              chunk_num=1,
                              delimiter=None) -> Optional[list]:
        raise NotImplementedError

    def get_object_stream(
            self,
            target_path,
            start,
            size=10000,
            delimiter=None) -> (Union[bytes, str, None], Optional[int]):
        raise NotImplementedError

    def get_url(self,
                target_path,
                set_public=False,
                skip_check=False,
                lifecycle=3600 * 100):
        return target_path

    def exists(self, target_path) -> bool:
        req = urllib.request.Request(target_path)
        req.get_method = lambda: 'HEAD'

        try:
            urllib.request.urlopen(req)
            return True
        except Exception:
            return False

    def isfile(self, target_path) -> bool:
        # Well for a http url, it should only be a file.
        return True

    def isdir(self, target_path) -> bool:
        return False
