"""
@brief Language analysis module
Calculates the distribution of language skills, needs for upgrade language skills nad find
employs, who know english and germany for commercial department
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages
from config.helper_const import Language


class LanguageSkillsAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for language skills for commercial department
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize language skills analyzer
        Sets up specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "LanguageSkillsAnalyzer")

    def execute_analysis(self):
        """
        @brief Analysis distribution of language skills, needs for upgrade language skills nad find
        employs, who know english and germany for commercial department
        if people dont know english and russian for then need upgrade language skills

        @return: dictionary with distribution, needs(bool) and persons, who know english and germany
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("language skills"))

        try:
            language_analysis_result = self._language_analysis()

            # Compile results
            analysis_results = {
                'distribution': language_analysis_result.get('distribution'),
                'needs': language_analysis_result.get('needs'),
                'persons-who-know': language_analysis_result.get('persons-who-know'),
            }

            self._generate_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("language skills"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("language skills", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _language_analysis(self):
        """
        @brief Language analysis of commercial department
        Calculates distribution of language skills, needs for upgrade language skills nad find
        employs, who know english and germany

        @return: dictionary with distribution, needs and persons, who know english and germany
        """
        self.logger.info(LogMessages.LANGUAGE_ANALYSIS)

        needs = []
        persons_who_know = []
        distribution = {}
        for employee in self.data.get('employees', []):
            if employee.get('work_info')['department_id'] == self.department_id:
                know_russian = False
                know_english = False
                know_germany = False
                for language in employee.get('additional_info').get('language_skills', []):
                    if language == Language.ENGLISH:
                        know_english = True
                    if language == Language.RUSSIAN:
                        know_russian = True
                    if language == Language.GERMANY:
                        know_germany = True
                    curr = distribution.get(language, 0)
                    distribution[language] = curr + 1
                fio = ''
                if not know_english or not know_russian:
                    fio = employee.get('personal_info')['full_name']
                    fio = fio + '. '
                    if not know_english:
                        fio = fio + 'Need upgrade english. '
                    if not know_russian:
                        fio = fio + 'Need upgrade russian. '
                if fio != '':
                    needs.append(fio.strip())
                if know_english and know_germany:
                    fio = employee.get('personal_info')['full_name']
                    persons_who_know.append(fio)

        language_analysis_results = {
            'distribution': distribution,
            'needs': needs,
            'persons-who-know': persons_who_know,
        }
        return language_analysis_results

    def _generate_report(self, analysis_results):
        """
        @brief Generate formatted language skills analysis report
        Outputs analysis results to console and log

        @param analysis_results: Dictionary containing analysis results
        """
        print("=" * 70)
        print(ReportMessages.LANGUAGE_HEADER)
        print("=" * 70)

        print("language distribution: {}".format(analysis_results.get('distribution')))
        print("Need upgrade skills: {}".format(analysis_results.get('needs')))
        print("Persons who know english and germany: {}".format(analysis_results.get('persons-who-know')))
