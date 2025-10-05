"""
@brief Base analyzer class for IT infrastructure analysis
Provides common functionality and interface for all analyzers
"""

import pandas as pd
import json
from utils.logger import analysis_logger
from config.messages import LogMessages

class BaseAnalyzer:
    """
    @brief Base class for all IT infrastructure analyzers
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
        self.it_equipment_dataframe = None

        self.logger.info(LogMessages.SYSTEM_START)
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

        # Create equipment DataFrame
        equipment_records = []
        for equipment_item in self.data.get('equipment', []):
            equipment_record = {
                'equipment_id': equipment_item['equipment_id'],
                'name': equipment_item['name'],
                'type': equipment_item['type'],
                'department_id': equipment_item['department_id'],
                'department_name': equipment_item['department_name'],
                'model': equipment_item['specifications']['model'],
                'manufacturer': equipment_item['specifications']['manufacturer'],
                'purchase_date': equipment_item['purchase_info']['purchase_date'],
                'cost': equipment_item['purchase_info']['cost'],
                'warranty_end_date': equipment_item['purchase_info']['warranty_end_date'],
                'status': equipment_item['operational_info']['status'],
                'efficiency': equipment_item['operational_info']['efficiency_percentage'],
                'maintenance_cost': equipment_item['operational_info']['maintenance_cost_per_month'],
                'utilization_rate': equipment_item['utilization']['utilization_rate'],
                'hours_used_daily': equipment_item['utilization']['hours_used_daily']
            }
            equipment_records.append(equipment_record)

        equipment_dataframe = pd.DataFrame(equipment_records)

        # Convert date columns to datetime
        equipment_dataframe['purchase_date'] = pd.to_datetime(equipment_dataframe['purchase_date'])
        equipment_dataframe['warranty_end_date'] = pd.to_datetime(equipment_dataframe['warranty_end_date'])

        # Filter IT equipment
        self.logger.info(LogMessages.DATA_FILTERING_START)
        it_equipment_filter_pattern = 'Сервер|Компьютер|Ноутбук|Монитор|Принтер|Сканер|Сетевое'
        self.it_equipment_dataframe = equipment_dataframe[
            equipment_dataframe['type'].str.contains(it_equipment_filter_pattern, na=False)
        ]

        self.logger.info(LogMessages.EQUIPMENT_COUNT.format(len(self.it_equipment_dataframe)))

    def execute_analysis(self):
        """
        @brief Execute the analysis (to be implemented by subclasses)
        Template method for analysis execution
        """
        raise NotImplementedError("Subclasses must implement execute_analysis method")
