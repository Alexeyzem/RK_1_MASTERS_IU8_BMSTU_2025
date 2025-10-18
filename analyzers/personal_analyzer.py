"""
@brief Personal efficiency analysis module
Calculates the revenue-per-employee and correlation between salary and performance_score for commercial department
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages


class PersonalEfficiencyAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for personal efficiency for commercial department
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize personal efficiency analyzer
        Sets up specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "PersonalEfficiencyAnalyzer")

    def execute_analysis(self):
        """
        @brief Analysis revenue-per-employee and correlation between salary
        and performance_score for commercial department

        @return: dictionary with revenue-per-employee and correlation
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("personal efficiency"))

        try:
            personal_analysis_result = self._personal_analysis()

            # Compile results
            analysis_results = {
                'revenue-per-employee': personal_analysis_result.get('revenue-per-employee'),
                'correlation': personal_analysis_result.get('correlation'),
            }

            self._generate_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("personal efficiency"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("personal efficiency", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _personal_analysis(self):
        """
        @brief Personal analysis of commercial department
        Calculates revenue-per-employee and correlation between salary and performance_score for commercial department

        @return: dictionary with revenue-per-employee and correlation
        """
        self.logger.info(LogMessages.PERSONAL_REVENUE_PER_EMPLOYEE)

        total_profit = 0
        for metric in self.data.get('kpi_metrics'):
            if metric['department_id'] == self.department_id:
                total_profit = metric['project_metrics']['total_profit']
                break

        self.logger.info(LogMessages.PERSONAL_CORRELATION)
        salary = []
        performance_score = []
        for employee in self.data.get('employees', []):
            if employee.get('work_info')['department_id'] == self.department_id:
                salary.append(employee.get('work_info')['salary'])
                performance_score.append(employee.get('work_info')['performance_score'])

        df = pd.DataFrame({'salary': salary, 'performance_score': performance_score})
        correlation_matrix = df.corr()
        corr_value = correlation_matrix.loc['salary', 'performance_score']

        personal_analysis_results = {
            'revenue-per-employee': total_profit / self.person_count,
            'correlation': corr_value,
        }

        return personal_analysis_results

    def _generate_report(self, analysis_results):
        """
        @brief Generate formatted person analysis report
        Outputs analysis results to console and log

        @param analysis_results: Dictionary containing analysis results
        """
        print("=" * 70)
        print(ReportMessages.PERSON_HEADER)
        print("=" * 70)

        print("revenue-per-employee: {}".format(analysis_results.get('revenue-per-employee')))
        print("Correlation between salary and performance_score: {}".format(analysis_results.get('correlation')))
