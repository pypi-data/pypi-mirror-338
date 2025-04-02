#  The MIT License (MIT)
#
#  Copyright (c) 2025 Scott Lau
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
from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta
from lib2to3.fixer_util import pats_built
from sc_config import ConfigManager

from sc_banker_acceptance_report.analyzer.base_analyzer import BaseAnalyzer
from sc_banker_acceptance_report.utils.manifest_utils import ManifestUtils


class BankerAcceptanceIssuanceAnalyzer(BaseAnalyzer):
    """
    银行承兑汇票开票量报表分析

    是否过期计算规则：
    20250326号下载的是20250325的数据，数据文件命名为20250325，到期日大于20250325才算没到期

    时期：
    1、如果是2025年的数据，直接取：沉淀存款时期数
    2、如果是2024年的数据，计算是否到期
    2.1 如果未到期，直接取票据金额即可
    2.2 如果到期了，票据金额*在账天数/当年已过天数
    2.3 在账天数=到期日-开始日期(20250101)
    2.4 当年已过天数=数据日期-开始日期(20250101)+1

    时点：
    1. 计算是否到期
    1.1. 如果到期了，时点为0
    1.2. 如果没到期，时点即为票据金额

    需要读取20241231和当天的数据，整合并输出结果
    """

    def __init__(self, *, config: ConfigManager, excel_writer: pd.ExcelWriter):
        super().__init__(config=config, excel_writer=excel_writer)
        self._key_enabled = "corporate.ba_issuance.enabled"
        self._key_business_type = "corporate.ba_issuance.business_type"
        self._key_export_column_list = "corporate.ba_issuance.sheet_config.export_column_list"

    def _read_config(self, *, config: ConfigManager):
        # 生成的目标Excel文件存放路径
        self._target_directory = config.get("corporate.target_directory")
        # 文件路径
        self._src_filepath_format = config.get("corporate.ba_issuance.source_file_path")
        # Sheet名称
        self._sheet_name = config.get("corporate.ba_issuance.sheet_name")
        # Excel中的日期格式
        self._date_format_in_excel = config.get("corporate.ba_issuance.date_format_in_excel")
        # 日期格式
        self._date_format = config.get("corporate.ba_issuance.date_format")
        today = datetime.today()
        yesterday = today - relativedelta(days=1)
        # 今年第一天
        self._year_start_date = datetime(today.year, 1, 1)
        # 去年最后一天
        self._last_year_end_date = datetime(today.year - 1, 12, 31)
        # 去年最后一天的数据文件路径
        self._src_filepath_last_year = self._last_year_end_date.strftime(self._src_filepath_format)
        # 数据日期（默认取昨天）
        self._data_date = yesterday
        data_date = config.get("corporate.ba_issuance.data_date")
        # 如果有配置，则使用配置的日期
        if data_date is not None and data_date != '':
            self._data_date = datetime.strptime(data_date, self._date_format)
        # 数据日期当天的数据文件路径
        self._src_filepath_data_date = self._data_date.strftime(self._src_filepath_format)
        # 表头行索引
        self._header_row = config.get("corporate.ba_issuance.sheet_config.header_row")
        # 员工姓名列索引
        self._name_column = self.calculate_column_index_from_config(
            "corporate.ba_issuance.sheet_config.name_column"
        )
        # 定活期保证金比例列索引
        self._percentage_column = self.calculate_column_index_from_config(
            "corporate.ba_issuance.sheet_config.percentage_column"
        )
        self._percentage_filter_list = list()
        percentage_filter_list = config.get("corporate.ba_issuance.sheet_config.percentage_column_filter")
        if percentage_filter_list is not None and type(percentage_filter_list) is list:
            self._percentage_filter_list.extend(percentage_filter_list)
        self._face_value_column = self.calculate_column_index_from_config(
            "corporate.ba_issuance.sheet_config.face_value_column"
        )
        self._start_date_column = self.calculate_column_index_from_config(
            "corporate.ba_issuance.sheet_config.start_date_column"
        )
        self._end_date_column = self.calculate_column_index_from_config(
            "corporate.ba_issuance.sheet_config.end_date_column"
        )
        self._deposit_column = self.calculate_column_index_from_config(
            "corporate.ba_issuance.sheet_config.deposit_column"
        )
        # 输出的时期数列名
        self._time_period_data_column_name = config.get(
            "corporate.ba_issuance.time_period_data_column_name"
        )
        # 输出的时点数列名
        self._time_point_data_column_name = config.get(
            "corporate.ba_issuance.time_point_data_column_name"
        )

    def _read_src_file(self) -> pd.DataFrame:
        logging.getLogger(__name__).info("读取源文件：{}".format(self._src_filepath_data_date))
        data_date_date = pd.read_excel(
            self._src_filepath_data_date,
            sheet_name=self._sheet_name,
            header=self._header_row,
        )
        logging.getLogger(__name__).info("读取源文件：{}".format(self._src_filepath_last_year))
        data_last_year = pd.read_excel(
            self._src_filepath_last_year,
            sheet_name=self._sheet_name,
            header=self._header_row,
        )

        self._name_column_name = data_date_date.columns[self._name_column]
        self._percentage_column_name = data_date_date.columns[self._percentage_column]
        self._face_value_column_name = data_date_date.columns[self._face_value_column]
        self._start_date_column_name = data_date_date.columns[self._start_date_column]
        self._end_date_column_name = data_date_date.columns[self._end_date_column]
        self._deposit_column_name = data_date_date.columns[self._deposit_column]
        return pd.concat([data_last_year, data_date_date], axis=0)

    def _pre_pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        logging.getLogger(__name__).info("预处理数据...")
        # 转换日期列为datetime类型
        data[self._start_date_column_name] = pd.to_datetime(
            data[self._start_date_column_name],
            format=self._date_format_in_excel
        )
        data[self._end_date_column_name] = pd.to_datetime(
            data[self._end_date_column_name],
            format=self._date_format_in_excel
        )

        criterion = True
        # 过滤票据到期日（到期日要是当年的）
        criterion1 = data[self._end_date_column_name].map(
            lambda end_date: end_date > self._year_start_date
        )
        criterion = criterion & criterion1

        # 过滤定活期保证金比例
        criterion2 = data[self._percentage_column_name].map(
            lambda x: x * 100 in self._percentage_filter_list
        )
        criterion = criterion & criterion2

        # 关键修复点（reset_index(drop=True)）
        # 修复calculate_time_period_value中的loc时报错：
        # ValueError: cannot reindex on an axis with duplicate labels
        data = data[criterion].copy().reset_index(drop=True)
        self._calculate_time_period_value(data)
        self._calculate_time_point_value(data)
        return data

    def _calculate_time_period_value(self, data):
        # 添加时期数列和时点数列
        #     是否过期计算规则：
        #     20250326号下载的是20250325的数据，数据文件命名为20250325，到期日大于20250325才算没到期
        #     时期：
        #     1、如果是2025年的数据，直接取：沉淀存款时期数
        #     2、如果是2024年的数据，计算是否到期
        #     2.1 如果未到期，直接取票据金额即可
        #     2.2 如果到期了，票据金额*在账天数/当年已过天数
        #     2.3 在账天数=到期日-开始日期(20250101)
        #     2.4 当年已过天数=数据日期-开始日期(20250101)+1
        data[self._time_period_data_column_name] = 0.0
        # 判断是否是当年的数据
        is_cur_year_data = (
                (data[self._start_date_column_name] >= self._year_start_date)
                & (data[self._end_date_column_name] > self._year_start_date)
        )
        # 处理当年数据
        data.loc[is_cur_year_data, self._time_period_data_column_name] = data[self._deposit_column_name]
        # 判断是否是往年的数据
        is_past_year_data = (
                (data[self._start_date_column_name] < self._year_start_date)
                & (data[self._end_date_column_name] > self._year_start_date)
        )
        # 未到期票据
        not_expired = data[self._end_date_column_name] > self._data_date
        # 未到期票据直接取面值
        past_year_data_not_expired = is_past_year_data & not_expired
        data.loc[past_year_data_not_expired, self._time_period_data_column_name] = data[self._face_value_column_name]
        # 处理到期票据
        expired_mask = is_past_year_data & ~not_expired
        # 计算在账天数
        days_in_account = (data[self._end_date_column_name] - self._year_start_date).dt.days
        # 计算已过天数
        days_passed = (self._data_date - self._year_start_date).days + 1
        # 应用计算公式：票据金额*在账天数/当年已过天数
        data.loc[expired_mask, self._time_period_data_column_name] = (
                data[self._face_value_column_name] * days_in_account / days_passed
        )

    def _calculate_time_point_value(self, data):
        #     时点：
        #     1. 计算是否到期
        #     1.1. 如果到期了，时点为0
        #     1.2. 如果没到期，时点即为票据金额
        data[self._time_point_data_column_name] = data[self._face_value_column_name].where(
            data[self._end_date_column_name].apply(
                lambda end_date: end_date > self._data_date
            ),
            0
        )

    def _pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        index_columns = [self._name_column_name]
        value_columns = [self._time_period_data_column_name, self._time_point_data_column_name]
        logging.getLogger(__name__).info("按{} 透视数据项：{}".format(
            index_columns,
            value_columns,
        ))
        if data.empty:
            return pd.DataFrame(columns=index_columns + value_columns)
        table = pd.pivot_table(data, values=value_columns,
                               index=index_columns,
                               aggfunc="sum", fill_value=0)
        return table

    def _after_pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        return data.reset_index()

    def _merge_with_manifest(self, *, manifest_data: pd.DataFrame, data: pd.DataFrame) -> pd.DataFrame:
        logging.getLogger(__name__).info("与花名册合并...")
        merge_result = ManifestUtils.merge_with_manifest(
            manifest_data=manifest_data,
            data=data,
            how="left",
            name_column_name=self._name_column_name,
        )
        return merge_result

    def _drop_duplicated_columns(self, *, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop(columns=[self._name_column_name])

    def _add_target_columns(self) -> None:
        self._add_target_column(self._time_period_data_column_name)
        self._add_target_column(self._time_point_data_column_name)
