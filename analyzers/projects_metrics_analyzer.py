"""
@brief Project Profit analysis module
Calculates the profit and roi of all projects where the commercial department was involved
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class ProjectsMetricsAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for project profit and roi for commercial department
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize project profit analyzer
        Sets up specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "ProjectProfit")

    def execute_analysis(self):
        """
        @brief Analysis of all projects with the participation
        of the commercial department and calculation of profits

        @return: dictionary with profit sum and ROI
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("projects_profit"))

        try:
            project_analysis_results = self._profit_analysis()

            # Compile results
            analysis_results = {
                'total_profit': project_analysis_results.get('total_profit'),
                'average_roi': project_analysis_results.get('average_roi'),
            }

            self._generate_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("projects_profit"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("projects_profit", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _profit_analysis(self):
        """
        @brief Profit analysis of commercial department
        Calculates sum profit and ROI all projects where the commercial department was involved

        @return: Dictionary with sum profit and ROI
        """
        self.logger.info(LogMessages.PROJECT_PROFIT_CALCULATION)

        total_profit = 0
        average_roi = 0
        for metric in self.data.get('kpi_metrics'):
            if metric['department_id'] == self.department_id:
                total_profit = metric['project_metrics']['total_profit']
                average_roi = metric['project_metrics']['average_roi']
                break

        projects_analysis_results = {
            'total_profit': total_profit,
            'average_roi': average_roi,
        }

        return projects_analysis_results

    def _generate_report(self, analysis_results):
        """
        @brief Generate formatted project analysis report
        Outputs analysis results to console and log

        @param analysis_results: Dictionary containing analysis results
        """
        print("=" * 70)
        print(ReportMessages.PROJECT_PROFIT_HEADER)
        print("=" * 70)

        print("Total project profit: {}".format(analysis_results.get('total_profit')))
        print("Average roi: {}".format(analysis_results.get('average_roi')))
