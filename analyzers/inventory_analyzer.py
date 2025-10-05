"""
@brief Equipment inventory analysis module
Performs comprehensive inventory analysis of IT equipment
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages

class InventoryAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for IT equipment inventory assessment
    Provides equipment counting, valuation, and distribution analysis
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize inventory analyzer
        Sets up specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "InventoryAnalysis")

    def execute_analysis(self):
        """
        @brief Execute comprehensive inventory analysis
        Performs equipment counting, cost calculation, and distribution analysis

        @return: Dictionary containing inventory analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("inventory"))

        try:
            # Equipment type distribution
            equipment_type_distribution = self._analyze_equipment_types()

            # Financial valuation
            financial_analysis_results = self._perform_financial_analysis()

            # Department distribution
            department_distribution_analysis = self._analyze_department_distribution()

            # Compile results
            analysis_results = {
                'equipment_type_distribution': equipment_type_distribution,
                'financial_analysis': financial_analysis_results,
                'department_distribution': department_distribution_analysis,
                'total_equipment_count': len(self.it_equipment_dataframe)
            }

            self._generate_inventory_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Inventory"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("inventory", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _analyze_equipment_types(self):
        """
        @brief Analyze distribution of equipment by type
        Calculates counts and percentages for each equipment type

        @return: DataFrame with equipment type distribution
        """
        equipment_type_distribution = self.it_equipment_dataframe['type'].value_counts().reset_index()
        equipment_type_distribution.columns = ['Equipment Type', 'Count']
        equipment_type_distribution['Percentage'] = (
            equipment_type_distribution['Count'] / len(self.it_equipment_dataframe) * 100
        ).round(2)

        return equipment_type_distribution

    def _perform_financial_analysis(self):
        """
        @brief Perform financial analysis of IT equipment
        Calculates total cost, average cost, and value distribution

        @return: Dictionary with financial metrics
        """
        self.logger.info(LogMessages.EQUIPMENT_COST_CALCULATION)

        total_equipment_cost = self.it_equipment_dataframe['cost'].sum()
        average_equipment_cost = self.it_equipment_dataframe['cost'].mean()
        maximum_equipment_cost = self.it_equipment_dataframe['cost'].max()
        minimum_equipment_cost = self.it_equipment_dataframe['cost'].min()

        financial_analysis_results = {
            'total_cost': total_equipment_cost,
            'average_cost': average_equipment_cost,
            'maximum_cost': maximum_equipment_cost,
            'minimum_cost': minimum_equipment_cost
        }

        return financial_analysis_results

    def _analyze_department_distribution(self):
        """
        @brief Analyze equipment distribution across departments
        Calculates equipment count and value per department

        @return: DataFrame with department distribution analysis
        """
        department_distribution_analysis = self.it_equipment_dataframe.groupby('department_name').agg({
            'equipment_id': 'count',
            'cost': 'sum',
            'utilization_rate': 'mean'
        }).round(2).reset_index()

        department_distribution_analysis.columns = [
            'Department Name',
            'Equipment Count',
            'Total Cost',
            'Average Utilization Rate'
        ]

        department_distribution_analysis = department_distribution_analysis.sort_values(
            'Total Cost',
            ascending=False
        )

        return department_distribution_analysis

    def _generate_inventory_report(self, analysis_results):
        """
        @brief Generate formatted inventory analysis report
        Outputs analysis results to console and log

        @param analysis_results: Dictionary containing analysis results
        """
        print("=" * 70)
        print(ReportMessages.INVENTORY_HEADER)
        print("=" * 70)

        total_equipment_count = analysis_results['total_equipment_count']
        total_equipment_cost = analysis_results['financial_analysis']['total_cost']

        print(f"\n{ReportMessages.TOTAL_EQUIPMENT_COUNT.format(total_equipment_count)}")
        print(f"{ReportMessages.TOTAL_EQUIPMENT_COST.format(total_equipment_cost)}")

        print("\nEquipment Type Distribution:")
        print(analysis_results['equipment_type_distribution'].to_string(index=False))

        print("\nDepartment Distribution (Top 10 by Cost):")
        department_data = analysis_results['department_distribution'].head(10)
        print(department_data.to_string(index=False))
