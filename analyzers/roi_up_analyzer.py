"""
@brief ROI up analysis module
Calculates potential profit if roi up by 5%
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class ROIUpAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for potential profit if roi up by 5% for commercial department
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize roi up analyzer
        Sets up specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "ProjectProfit")

    def execute_analysis(self):
        """
        @brief Analysis potential profit if roi up by 5% for commercial department

        @return: dict with potential profit
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("roi_up_analyzer"))

        try:
            roi_up_analysis_results = self._roi_up_analysis()

            # Compile results
            analysis_results = {
                'potential_profit': roi_up_analysis_results,
            }

            self._generate_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("roi_up_analyzer"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("projects_profit", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _roi_up_analysis(self):
        """
        @brief roi up analysis of commercial department
        Calculates profit if roi up by 5% for commercial department

        @return: potential profit
        """
        self.logger.info(LogMessages.ROI_ANALYSIS)

        total_profit = 0
        average_roi = 0
        actual_cost_sum = 0
        for metric in self.data.get('kpi_metrics'):
            if metric['department_id'] == self.department_id:
                total_profit = metric['project_metrics']['total_profit']
                average_roi = metric['project_metrics']['average_roi']
                break

        projects = self.projects.to_dict(orient='records')
        for project in projects:
            actual_cost_sum += project['actual_cost']

        roi_res = average_roi + 5
        res_profit = actual_cost_sum * roi_res / 100

        return res_profit - total_profit

    def _generate_report(self, analysis_results):
        """
        @brief Generate formatted project analysis report
        Outputs analysis results to console and log

        @param analysis_results: Dictionary containing analysis results
        """
        print("=" * 70)
        print(ReportMessages.ROI_HEADER)
        print("=" * 70)

        print("Total potential profit: {}".format(analysis_results.get('potential_profit')))
