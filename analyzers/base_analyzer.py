"""
@brief Base analyzer class for Commercial Departments analysis
Provides common functionality and interface for all analyzers
"""

import pandas as pd
import json
from utils.logger import analysis_logger
from config.messages import LogMessages


class BaseAnalyzer:
    """
    @brief Base class for all commercial analyzers
    Implements common data loading and processing functionality
    """

    def __init__(self, json_file_path, analysis_name):
        """
        @brief Initialize base analyzer with data source
        Sets up data loading and logger configuration

        @param json_file_path: Path to JSON data file
        @param analysis_name: Name of the analysis for logging
        """
        self.json_file_path = json_file_path
        self.analysis_name = analysis_name
        self.logger = analysis_logger.get_analysis_logger(analysis_name)
        self.data = None
        self.projects = None

        self.logger.info(LogMessages.SYSTEM_START)
        self.department_id = 17
        self.person_count = 0
        self._load_data()
        self._setup_dataframes()

    def _load_data(self):
        """
        @brief Load JSON data from specified file path
        Handles file reading and JSON parsing with error handling
        """
        self.logger.info(LogMessages.DATA_LOAD_START)
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
                self.data = json.load(json_file)
            self.logger.info(LogMessages.DATA_LOAD_SUCCESS.format(self.json_file_path))
        except Exception as loading_error:
            error_message = LogMessages.DATA_LOAD_ERROR.format(
                self.json_file_path, str(loading_error)
            )
            self.logger.error(error_message)
            raise loading_error

    def _setup_dataframes(self):
        """
        @brief Create pandas DataFrames from loaded JSON data
        Processes equipment, departments, and employees data
        """
        self.logger.info(LogMessages.DATA_PROCESSING_START.format(self.analysis_name))

        if not self.data:
            return

        # Create projects DataFrame
        project_records = []
        for project in self.data.get('projects', []):
            for department in project.get('participating_departments', []):
                if department.get('department_id') == self.department_id:
                    project_record = {
                        'project_id': project['project_id'],
                        'name': project['name'],
                        'description': project['description'],
                        'status': project['status'],
                        'start_date': project['timeline']['start_date'],
                        'end_date': project['timeline']['end_date'],
                        'duration_days': project['timeline']['duration_days'],
                        'budget': project['financials']['budget'],
                        'actual_cost': project['financials']['actual_cost'],
                        'profit': project['financials']['profit'],
                        'roi_percentage': project['financials']['roi_percentage'],
                        'completion_percentage': project['metrics']['completion_percentage'],
                        'risk_level': project['metrics']['risk_level'],
                        'priority': project['metrics']['priority'],
                    }
                    project_records.append(project_record)
                    break

        project_dataframe = pd.DataFrame(project_records)

        # Convert date columns to datetime
        project_dataframe['start_date'] = pd.to_datetime(project_dataframe['start_date'])
        project_dataframe['end_date'] = pd.to_datetime(project_dataframe['end_date'])

        self.projects = project_dataframe
        self.logger.info(LogMessages.PROJECT_COUNT.format(len(self.projects)))

        person_count = 0
        for employee in self.data.get('employees', []):
            if employee.get('work_info')['department_id'] == self.department_id:
                person_count += 1

        self.logger.info(LogMessages.PERSONAL_COUNT.format(person_count))
        self.person_count = person_count

    def execute_analysis(self):
        """
        @brief Execute the analysis (to be implemented by subclasses)
        Template method for analysis execution
        """
        raise NotImplementedError("Subclasses must implement execute_analysis method")
