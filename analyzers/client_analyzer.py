"""
@brief Client analysis module
Calculates priorities and risk for projects, ratio high-priority low-priority and projects with
high-risk and high profit
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages
from config.helper_const import Levels


class ClientAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for clients for commercial department
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize clients analyzer
        Sets up specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "ClientAnalyzer")

    def execute_analysis(self):
        """
        @brief Analysis priorities and risk for projects, ratio high-priority low-priority and projects with
        high-risk and high profit for commercial department

        @return: dictionary with priorities-risk, ratio, projects
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("clients"))

        try:
            client_analysis_result = self._clients_analysis()

            # Compile results
            analysis_results = {
                'priorities-risk': client_analysis_result.get('priorities-risk'),
                'ratio': client_analysis_result.get('ratio'),
                'projects': client_analysis_result.get('projects'),
            }

            self._generate_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("clients"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("clients", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _clients_analysis(self):
        """
        @brief Clients analysis of commercial department
        Calculates priorities and risk for projects, ratio high-priority low-priority and projects with
        high-risk and high profit for commercial department. High profit - if profit more 200000

        @return: dictionary with priorities-risk, ratio, projects
        """
        self.logger.info(LogMessages.CLIENT_PROJECT_ANALYSIS)

        high_priority_count = 0
        low_priority_count = 0
        priority_risk = {}
        res_projects = []
        projects = self.projects.to_dict(orient='records')
        for project in projects:
            risk = project['risk_level']
            priority = project['priority']
            total = priority + '/' + risk
            cur = priority_risk.get(total, 0)
            priority_risk[total] = cur + 1
            if priority == Levels.LOW:
                low_priority_count += 1
            if priority == Levels.HIGH or priority == Levels.CRITICAL:
                high_priority_count += 1
            if project['profit'] > 200000 and risk == Levels.HIGH:
                res_projects.append(
                    {'name': project['name'], 'priority': priority, 'risk': risk, 'profit': project['profit']})

        client_analysis_results = {
            'priorities-risk': priority_risk,
            'ratio': high_priority_count / low_priority_count,
            'projects': res_projects,
        }
        return client_analysis_results

    def _generate_report(self, analysis_results):
        """
        @brief Generate formatted clients analysis report
        Outputs analysis results to console and log

        @param analysis_results: Dictionary containing analysis results
        """
        print("=" * 70)
        print(ReportMessages.CLIENT_HEADER)
        print("=" * 70)

        print("Priorities-risk for project: {}".format(analysis_results.get('priorities-risk')))
        print("Ratio high/critical to low priority: {}".format(analysis_results.get('ratio')))
        print("Project with high risk and profit: {}".format(analysis_results.get('projects')))
