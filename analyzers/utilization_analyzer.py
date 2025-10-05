"""
@brief Equipment utilization analysis module
Analyzes usage efficiency and performance metrics of IT equipment
"""

import pandas as pd
import numpy as np
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages
from config.enums import UtilizationLevel

class UtilizationAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for IT equipment utilization assessment
    Provides utilization rate analysis and efficiency metrics
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize utilization analyzer
        Sets up utilization-specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "UtilizationAnalysis")
        self.low_utilization_threshold = 50

    def execute_analysis(self):
        """
        @brief Execute comprehensive utilization analysis
        Performs utilization rate calculation, department comparison, and inefficiency identification

        @return: Dictionary containing utilization analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("utilization"))

        try:
            # Basic utilization metrics
            basic_utilization_metrics = self._calculate_basic_utilization_metrics()

            # Utilization level distribution
            utilization_distribution_analysis = self._analyze_utilization_distribution()

            # Department performance comparison
            department_performance_comparison = self._compare_department_performance()

            # Low utilization equipment identification
            low_utilization_equipment_analysis = self._identify_low_utilization_equipment()

            # Compile results
            analysis_results = {
                'basic_metrics': basic_utilization_metrics,
                'utilization_distribution': utilization_distribution_analysis,
                'department_comparison': department_performance_comparison,
                'low_utilization_equipment': low_utilization_equipment_analysis
            }

            self._generate_utilization_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Utilization"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("utilization", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _calculate_basic_utilization_metrics(self):
        """
        @brief Calculate basic utilization rate statistics
        Computes mean, median, and distribution metrics

        @return: Dictionary with basic utilization metrics
        """
        self.logger.info(LogMessages.UTILIZATION_CALCULATION)

        average_utilization_rate = self.it_equipment_dataframe['utilization_rate'].mean()
        median_utilization_rate = self.it_equipment_dataframe['utilization_rate'].median()
        standard_deviation_utilization = self.it_equipment_dataframe['utilization_rate'].std()

        basic_utilization_metrics = {
            'average_utilization': average_utilization_rate,
            'median_utilization': median_utilization_rate,
            'standard_deviation': standard_deviation_utilization,
            'maximum_utilization': self.it_equipment_dataframe['utilization_rate'].max(),
            'minimum_utilization': self.it_equipment_dataframe['utilization_rate'].min()
        }

        return basic_utilization_metrics

    def _analyze_utilization_distribution(self):
        """
        @brief Analyze distribution of equipment across utilization levels
        Categorizes equipment by utilization efficiency

        @return: DataFrame with utilization level distribution
        """
        utilization_categories = [0, 30, 60, 80, 101]
        utilization_labels = [
            UtilizationLevel.VERY_LOW.value,
            UtilizationLevel.LOW.value,
            UtilizationLevel.MEDIUM.value,
            UtilizationLevel.HIGH.value,
            UtilizationLevel.VERY_HIGH.value
        ]

        utilization_distribution = pd.cut(
            self.it_equipment_dataframe['utilization_rate'],
            bins=utilization_categories,
            labels=utilization_labels[:-1],
            right=False
        ).value_counts().sort_index()

        utilization_distribution_dataframe = utilization_distribution.reset_index()
        utilization_distribution_dataframe.columns = ['Utilization Level', 'Equipment Count']
        utilization_distribution_dataframe['Percentage'] = (
            utilization_distribution_dataframe['Equipment Count'] / len(self.it_equipment_dataframe) * 100
        ).round(2)

        return utilization_distribution_dataframe

    def _compare_department_performance(self):
        """
        @brief Compare utilization performance across departments
        Identifies departments with best and worst utilization rates

        @return: Dictionary with department performance data
        """
        department_utilization_statistics = self.it_equipment_dataframe.groupby('department_name').agg({
            'utilization_rate': ['mean', 'std', 'count']
        }).round(2)

        department_utilization_statistics.columns = [
            'Average Utilization Rate',
            'Standard Deviation',
            'Equipment Count'
        ]

        best_performing_departments = department_utilization_statistics.nlargest(
            5, 'Average Utilization Rate'
        )
        worst_performing_departments = department_utilization_statistics.nsmallest(
            5, 'Average Utilization Rate'
        )

        department_performance_comparison = {
            'best_performers': best_performing_departments,
            'worst_performers': worst_performing_departments,
            'complete_data': department_utilization_statistics
        }

        return department_performance_comparison

    def _identify_low_utilization_equipment(self):
        """
        @brief Identify equipment with low utilization rates
        Finds underutilized equipment and calculates potential losses

        @return: Dictionary with low utilization analysis results
        """
        low_utilization_equipment_dataframe = self.it_equipment_dataframe[
            self.it_equipment_dataframe['utilization_rate'] < self.low_utilization_threshold
        ]

        if len(low_utilization_equipment_dataframe) > 0:
            low_utilization_equipment_report = low_utilization_equipment_dataframe[[
                'equipment_id', 'name', 'department_name', 'utilization_rate', 'cost'
            ]].sort_values('utilization_rate')

            potential_inefficiency_loss = low_utilization_equipment_dataframe['cost'].sum() * 0.5

            low_utilization_analysis_results = {
                'equipment_list': low_utilization_equipment_report,
                'count': len(low_utilization_equipment_dataframe),
                'potential_loss': potential_inefficiency_loss,
                'average_utilization': low_utilization_equipment_dataframe['utilization_rate'].mean()
            }
        else:
            low_utilization_analysis_results = {
                'equipment_list': pd.DataFrame(),
                'count': 0,
                'potential_loss': 0,
                'average_utilization': 0
            }

        return low_utilization_analysis_results

    def _generate_utilization_report(self, analysis_results):
        """
        @brief Generate formatted utilization analysis report
        Outputs utilization metrics and recommendations

        @param analysis_results: Dictionary containing utilization analysis results
        """
        print("=" * 70)
        print(ReportMessages.UTILIZATION_HEADER)
        print("=" * 70)

        basic_metrics = analysis_results['basic_metrics']
        low_utilization_data = analysis_results['low_utilization_equipment']

        print(f"\n{ReportMessages.AVERAGE_UTILIZATION.format(basic_metrics['average_utilization'])}")
        print(f"Equipment with low utilization (<{self.low_utilization_threshold}%): {low_utilization_data['count']} units")

        print("\nUtilization Distribution:")
        print(analysis_results['utilization_distribution'].to_string(index=False))

        print("\nTop 5 Departments by Utilization Efficiency:")
        print(analysis_results['department_comparison']['best_performers'].to_string())

        if low_utilization_data['count'] > 0:
            print(f"\nPotential losses from inefficient utilization: {low_utilization_data['potential_loss']:,.0f} RUB")
            print("\nLow Utilization Equipment:")
            print(low_utilization_data['equipment_list'].to_string(index=False))
