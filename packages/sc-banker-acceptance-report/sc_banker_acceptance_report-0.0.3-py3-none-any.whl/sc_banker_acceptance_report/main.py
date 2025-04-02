# The MIT License (MIT)
#
# Copyright (c) 2025 Scott Lau
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import logging
import os

import pandas as pd
from sc_config import ConfigUtils
from sc_utilities import Singleton
from sc_utilities import log_init

from sc_banker_acceptance_report import PROJECT_NAME, __version__
from sc_banker_acceptance_report.analyzer.ba_issuance_analyzer import BankerAcceptanceIssuanceAnalyzer
from sc_banker_acceptance_report.summary.branch_summary_analyzer import BranchSummaryAnalyzer
from sc_banker_acceptance_report.summary.manager_summary_analyzer import ManagerSummaryAnalyzer
from sc_banker_acceptance_report.utils.branch_utils import BranchUtils
from sc_banker_acceptance_report.utils.manifest_utils import ManifestUtils

log_init()


class Runner(metaclass=Singleton):

    def __init__(self):
        project_name = PROJECT_NAME
        ConfigUtils.clear(project_name)
        self._config = ConfigUtils.get_config(project_name)
        # 生成的目标Excel文件存放路径
        self._target_directory = self._config.get("corporate.target_directory")
        # 目标文件名称
        self._target_filename = self._config.get("corporate.target_filename")
        # 生成的Excel中按客户经理汇总的Sheet的名称
        self._target_manager_summary_sheet_name = self._config.get("corporate.target_manager_summary_sheet_name")
        # 生成的Excel中按机构汇总的Sheet的名称
        self._target_branch_summary_sheet_name = self._config.get("corporate.target_branch_summary_sheet_name")

    def _load_branch_stuff(self):
        try:
            BranchUtils.set_config(self._config)
            # 加载机构名称对应表
            BranchUtils.load_branch_name_mapping()
            # 加载所有发生业务的机构清单
            BranchUtils.load_all_business_branch_list()
            return 0
        except Exception as error:
            logging.getLogger(__name__).error("加载机构名称对应表失败：{}".format(error), exc_info=error)
            return 1

    def _load_manifest_stuff(self):
        try:
            ManifestUtils.set_config(self._config)
            # 加载花名册
            ManifestUtils.load_manifest()
            return 0
        except Exception as error:
            logging.getLogger(__name__).error("加载花名册相关信息失败：{}".format(error), exc_info=error)
            return 1

    def run(self, *, args):
        logging.getLogger(__name__).info("arguments {}".format(args))
        logging.getLogger(__name__).info("program {} version {}".format(PROJECT_NAME, __version__))
        logging.getLogger(__name__).debug("configurations {}".format(self._config.as_dict()))

        logging.getLogger(__name__).info("开始数据分析...")
        # 加载机构相关配置
        result = self._load_branch_stuff()
        if result != 0:
            return result
        logging.getLogger(__name__).debug(BranchUtils.get_all_business_branch_list())
        logging.getLogger(__name__).debug(BranchUtils.get_branch_name_mapping())

        # 加载花名册相关配置
        result = self._load_manifest_stuff()
        if result != 0:
            return result
        logging.getLogger(__name__).debug(ManifestUtils.get_manifest_df())

        target_filename_full_path: str = os.path.join(self._target_directory, self._target_filename)
        # 如果文件已经存在，则删除
        if os.path.exists(target_filename_full_path):
            logging.getLogger(__name__).info("删除输出文件：{} ".format(target_filename_full_path))
            try:
                os.remove(target_filename_full_path)
            except Exception as e:
                logging.getLogger(__name__).error("删除文件 {} 失败：{} ".format(target_filename_full_path, e))
                return 1
        logging.getLogger(__name__).info("输出文件：{} ".format(target_filename_full_path))

        with pd.ExcelWriter(target_filename_full_path) as excel_writer:
            # 分析客户经理汇总
            manager_summary_analyzer_list, manager_summary_result, target_column_list = \
                self._manager_summary_analysis(excel_writer)
            # 分析机构汇总
            branch_summary_analyzer_list = self._branch_summary_analysis(
                excel_writer,
                manager_summary_result,
                target_column_list
            )
            # 输出原Excel数据
            self._write_original_excel_data(branch_summary_analyzer_list, manager_summary_analyzer_list)
        logging.getLogger(__name__).info("结束数据分析")
        return 0

    def _manager_summary_analysis(self, excel_writer):
        manager_summary_analyzer_list = [
            # 基金业认申购明细
            BankerAcceptanceIssuanceAnalyzer(config=self._config, excel_writer=excel_writer),
        ]
        # 按客户经理汇总结果
        manifest_data = ManifestUtils.get_manifest_df().copy()
        manager_summary_result = pd.DataFrame()
        previous_data = pd.DataFrame()
        # 输出列清单列表
        target_column_list = list()
        logging.getLogger(__name__).info("按客户经理分析...")
        for analyzer in manager_summary_analyzer_list:
            try:
                manager_summary_result = analyzer.analysis(
                    manifest_data=manifest_data,
                    previous_data=previous_data,
                )
                previous_data = manager_summary_result
                target_column_list.extend(analyzer.get_target_columns())
            except Exception as e:
                logging.getLogger(__name__).exception("分析 {} 时出错".format(analyzer.get_business_type()), exc_info=e)
        # 客户经理汇总分析，待上述分析完成后，这里做一个总计分析
        analyzer = ManagerSummaryAnalyzer(
            config=self._config,
            excel_writer=excel_writer,
            target_column_list=target_column_list,
        )
        try:
            manager_summary_result = analyzer.analysis(
                manifest_data=manifest_data,
                previous_data=previous_data,
            )
        except Exception as e:
            logging.getLogger(__name__).exception("分析 {} 时出错".format(analyzer.get_business_type()), exc_info=e)
        if not manager_summary_result.empty:
            # 没有业绩的显示0
            manager_summary_result.fillna(0, inplace=True)
            manager_summary_result.to_excel(excel_writer=excel_writer, index=False,
                                            sheet_name=self._target_manager_summary_sheet_name)
        return manager_summary_analyzer_list, manager_summary_result, target_column_list

    def _branch_summary_analysis(self, excel_writer, manager_summary_result, target_column_list):
        branch_summary_analyzer_list = [
            # 机构汇总
            BranchSummaryAnalyzer(
                config=self._config,
                manager_summary=manager_summary_result,
                target_column_list=target_column_list,
                excel_writer=excel_writer,
            ),
        ]
        # 唯一的机构清单
        manifest_data = pd.DataFrame(
            data=set(BranchUtils.get_branch_name_mapping().values()),
            columns=[ManifestUtils.get_branch_column_name()],
            dtype=str
        )
        branch_summary_result = pd.DataFrame()
        logging.getLogger(__name__).info("按机构汇总分析...")
        previous_data = pd.DataFrame()
        # 按机构汇总结果
        for analyzer in branch_summary_analyzer_list:
            try:
                branch_summary_result = analyzer.analysis(
                    manifest_data=manifest_data,
                    previous_data=previous_data,
                )
                previous_data = branch_summary_result
            except Exception as e:
                logging.getLogger(__name__).exception("分析 {} 时出错".format(analyzer.get_business_type()), exc_info=e)
        if not branch_summary_result.empty:
            # 没有业绩的显示0
            branch_summary_result.fillna(0, inplace=True)
            # 添加机构合计行
            branch_summary_result.set_index(ManifestUtils.get_branch_column_name(), inplace=True)
            branch_summary_result.loc["合计"] = branch_summary_result.apply(lambda x: x.sum())
            branch_summary_result.reset_index(inplace=True)
            # 输出到Excel
            branch_summary_result.to_excel(excel_writer=excel_writer, index=False,
                                           sheet_name=self._target_branch_summary_sheet_name)
        return branch_summary_analyzer_list

    @staticmethod
    def _write_original_excel_data(branch_summary_analyzer_list, manager_summary_analyzer_list):
        logging.getLogger(__name__).info("输出源数据到Excel...")
        # 输出源数据到Excel
        for analyzer in manager_summary_analyzer_list + branch_summary_analyzer_list:
            try:
                logging.getLogger(__name__).info(f"输出 {analyzer.get_business_type()}...")
                analyzer.write_origin_data()
            except Exception as e:
                logging.getLogger(__name__).exception(
                    "输出 {} 源数据到Excel时出错".format(analyzer.get_business_type()),
                    exc_info=e)


def main():
    try:
        parser = argparse.ArgumentParser(description='Python project')
        args = parser.parse_args()
        state = Runner().run(args=args)
    except Exception as e:
        logging.getLogger(__name__).exception('An error occurred.', exc_info=e)
        return 1
    else:
        return state
