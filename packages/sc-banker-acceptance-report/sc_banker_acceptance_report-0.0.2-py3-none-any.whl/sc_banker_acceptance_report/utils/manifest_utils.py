#  The MIT License (MIT)
#
#  Copyright (c) 2025  Scott Lau
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import logging

import pandas as pd
from sc_utilities import Singleton, calculate_column_index

from .branch_utils import BranchUtils


class ManifestUtils(metaclass=Singleton):
    """
    花名册相关工具类
    """
    # 名单DataFrame
    _df: pd.DataFrame = None
    # 花名册姓名与所在部门对应关系DataFrame
    _name_branch_df: pd.DataFrame = None
    _name_column_name: str = ""
    _branch_column_name: str = ""
    # 离职人员调整表
    _leave_employee_mapping = dict()
    _config = None

    @classmethod
    def set_config(cls, config):
        cls._config = config

    @classmethod
    def get_name_branch_data_frame(cls) -> pd.DataFrame:
        """
        花名册姓名与所在部门对应关系
        :return:
        """
        return cls._name_branch_df

    @classmethod
    def get_name_column_name(cls) -> str:
        """
        姓名列名
        :return: 姓名列名
        """
        return cls._name_column_name

    @classmethod
    def get_branch_column_name(cls) -> str:
        """
        所属机构列名
        :return: 所属机构列名
        """
        return cls._branch_column_name

    @classmethod
    def load_manifest(cls):
        """
        加载花名册
        :return:
        """
        config = cls._config
        src_file_path = config.get("manifest.source_file_path")
        sheet_name = config.get("manifest.sheet_name")
        header_row = config.get("manifest.sheet_config.header_row")
        # 姓名列索引
        name_column_config = config.get("manifest.sheet_config.name_column")
        try:
            name_column = calculate_column_index(name_column_config)
        except ValueError as e:
            logging.getLogger(__name__).error("name_column configuration is invalid", exc_info=e)
            raise e
        # 所属机构列索引
        branch_column_config = config.get("manifest.sheet_config.branch_column")
        try:
            branch_column = calculate_column_index(branch_column_config)
        except ValueError as e:
            logging.getLogger(__name__).error("branch_column configuration is invalid", exc_info=e)
            raise e
        logging.getLogger(__name__).info("加载花名册：{}".format(src_file_path))
        df = pd.read_excel(src_file_path, sheet_name=sheet_name, header=header_row)
        df = df.iloc[:, [name_column, branch_column]]
        cls._name_column_name = df.columns[0]
        cls._branch_column_name = df.columns[1]

        mapping = BranchUtils.get_branch_name_mapping()
        # 替换机构名称
        df = df.replace({cls._branch_column_name: mapping})
        cls._df = df

    @classmethod
    def merge_with_manifest(
            cls, *,
            manifest_data: pd.DataFrame,
            data: pd.DataFrame,
            how,
            name_column_name: str
    ) -> pd.DataFrame:
        """
        与花名册合并

        :param manifest_data: 花名册数据，左边表
        :param data: 待合并DataFrame，右边表
        :param how: 如何合并，即连接方式，默认使用left连接，即左连接，保证花名册的数据完整
        :param name_column_name: 姓名列名称
        :return: 花名册与目标DataFrame合并后的DataFrame
        """
        if name_column_name is None:
            # ID与名称列全为空，则返回原结果
            return data
        return manifest_data.merge(
            data,
            how=how,
            left_on=[cls._name_column_name],
            right_on=[name_column_name],
        )

    @classmethod
    def get_manifest_df(cls) -> pd.DataFrame:
        return cls._df

    @classmethod
    def get_all_names_in_manifest(cls) -> list:
        return cls._df[cls._name_column_name].to_list()
