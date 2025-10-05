"""
@brief Equipment replacement planning module
Analyzes equipment lifecycle and generates replacement priorities
"""

import pandas as pd
from datetime import datetime
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages
from config.enums import AnalysisPriority

class ReplacementAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for equipment replacement planning
    Provides warranty analysis, age assessment, and replacement prioritization
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize replacement analyzer
        Sets up replacement-specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "ReplacementAnalysis")
        self.current_reference_date = pd.Timestamp.now()
        self.warranty_expiration_threshold_days = 365
        self.equipment_age_threshold_years = 3

    def execute_analysis(self):
        """
        @brief Execute comprehensive replacement analysis
        Performs warranty analysis, age assessment, and replacement prioritization

        @return: Dictionary containing replacement analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("replacement"))

        try:
            # Warranty expiration analysis
            warranty_expiration_analysis_results = self._analyze_warranty_expiration()

            # Equipment age analysis
            equipment_age_analysis_results = self._analyze_equipment_age()

            # Replacement priority calculation
            replacement_priority_analysis_results = self._calculate_replacement_priorities()

            # Compile results
            analysis_results = {
                'warranty_analysis': warranty_expiration_analysis_results,
                'age_analysis': equipment_age_analysis_results,
                'priority_analysis': replacement_priority_analysis_results
            }

            self._generate_replacement_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Replacement"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("replacement", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _analyze_warranty_expiration(self):
        """
        @brief Analyze equipment with expiring warranties
        Identifies equipment needing warranty renewal or replacement

        @return: Dictionary with warranty expiration analysis
        """
        equipment_dataframe_with_warranty_calculation = self.it_equipment_dataframe.copy()
        equipment_dataframe_with_warranty_calculation['days_until_warranty_expiration'] = (
            equipment_dataframe_with_warranty_calculation['warranty_end_date'] - self.current_reference_date
        ).dt.days

        expiring_warranty_equipment_dataframe = equipment_dataframe_with_warranty_calculation[
            equipment_dataframe_with_warranty_calculation['days_until_warranty_expiration'] <= self.warranty_expiration_threshold_days
        ]

        expiring_warranty_equipment_dataframe = expiring_warranty_equipment_dataframe.sort_values(
            'days_until_warranty_expiration'
        )

        if len(expiring_warranty_equipment_dataframe) > 0:
            warranty_expiration_report = expiring_warranty_equipment_dataframe[[
                'equipment_id', 'name', 'department_name',
                'warranty_end_date', 'days_until_warranty_expiration', 'cost'
            ]]
        else:
            warranty_expiration_report = pd.DataFrame()

        warranty_expiration_analysis_results = {
            'expiring_equipment_list': warranty_expiration_report,
            'expiring_equipment_count': len(expiring_warranty_equipment_dataframe),
            'total_replacement_cost': expiring_warranty_equipment_dataframe['cost'].sum() if len(expiring_warranty_equipment_dataframe) > 0 else 0
        }

        return warranty_expiration_analysis_results

    def _analyze_equipment_age(self):
        """
        @brief Analyze equipment age and identify outdated equipment
        Calculates equipment age and identifies candidates for replacement

        @return: Dictionary with equipment age analysis
        """
        equipment_dataframe_with_age_calculation = self.it_equipment_dataframe.copy()
        equipment_dataframe_with_age_calculation['equipment_age_years'] = (
            self.current_reference_date - equipment_dataframe_with_age_calculation['purchase_date']
        ).dt.days / 365.25

        outdated_equipment_dataframe = equipment_dataframe_with_age_calculation[
            equipment_dataframe_with_age_calculation['equipment_age_years'] >= self.equipment_age_threshold_years
        ]

        replacement_cost_calculation = outdated_equipment_dataframe['cost'].sum()

        equipment_age_analysis_results = {
            'outdated_equipment_count': len(outdated_equipment_dataframe),
            'replacement_cost_estimate': replacement_cost_calculation,
            'average_equipment_age': equipment_dataframe_with_age_calculation['equipment_age_years'].mean(),
            'age_distribution': equipment_dataframe_with_age_calculation['equipment_age_years'].describe()
        }

        return equipment_age_analysis_results

    def _calculate_replacement_priorities(self):
        """
        @brief Calculate replacement priorities using weighted scoring
        Generates prioritized replacement list based on multiple factors

        @return: DataFrame with replacement priority rankings
        """
        equipment_dataframe_with_priority_calculation = self.it_equipment_dataframe.copy()

        # Calculate equipment age
        equipment_dataframe_with_priority_calculation['equipment_age_years'] = (
            self.current_reference_date - equipment_dataframe_with_priority_calculation['purchase_date']
        ).dt.days / 365.25

        # Calculate priority score using weighted factors
        maximum_equipment_age = equipment_dataframe_with_priority_calculation['equipment_age_years'].max()
        maximum_maintenance_cost = equipment_dataframe_with_priority_calculation['maintenance_cost'].max()

        equipment_dataframe_with_priority_calculation['priority_score'] = (
            (equipment_dataframe_with_priority_calculation['equipment_age_years'] / maximum_equipment_age) * 0.3 +
            ((100 - equipment_dataframe_with_priority_calculation['efficiency']) / 100) * 0.3 +
            (equipment_dataframe_with_priority_calculation['maintenance_cost'] / maximum_maintenance_cost) * 0.2 +
            ((100 - equipment_dataframe_with_priority_calculation['utilization_rate']) / 100) * 0.2
        )

        # Select top replacement candidates
        top_replacement_priority_dataframe = equipment_dataframe_with_priority_calculation.nlargest(
            10, 'priority_score'
        )[[
            'equipment_id', 'name', 'department_name', 'equipment_age_years',
            'efficiency', 'utilization_rate', 'cost', 'priority_score'
        ]].round(3)

        top_replacement_priority_dataframe = top_replacement_priority_dataframe.sort_values(
            'priority_score',
            ascending=False
        )

        total_replacement_cost_calculation = top_replacement_priority_dataframe['cost'].sum()

        replacement_priority_analysis_results = {
            'priority_list': top_replacement_priority_dataframe,
            'total_replacement_cost': total_replacement_cost_calculation,
            'scoring_breakdown': {
                'age_weight': 0.3,
                'efficiency_weight': 0.3,
                'maintenance_weight': 0.2,
                'utilization_weight': 0.2
            }
        }

        return replacement_priority_analysis_results

    def _generate_replacement_report(self, analysis_results):
        """
        @brief Generate formatted replacement analysis report
        Outputs replacement priorities and cost estimates

        @param analysis_results: Dictionary containing replacement analysis results
        """
        print("=" * 70)
        print(ReportMessages.REPLACEMENT_HEADER)
        print("=" * 70)

        warranty_data = analysis_results['warranty_analysis']
        age_data = analysis_results['age_analysis']
        priority_data = analysis_results['priority_analysis']

        print(f"\nEquipment with expiring warranty: {warranty_data['expiring_equipment_count']} units")
        print(f"Outdated equipment (> {self.equipment_age_threshold_years} years): {age_data['outdated_equipment_count']} units")
        print(f"Total replacement cost estimate: {age_data['replacement_cost_estimate']:,.0f} RUB")

        if warranty_data['expiring_equipment_count'] > 0:
            print("\nEquipment with Expiring Warranty:")
            print(warranty_data['expiring_equipment_list'].to_string(index=False))

        print(f"\n{ReportMessages.REPLACEMENT_PRIORITY}")
        print(priority_data['priority_list'].to_string(index=False))

        print(f"\nTotal cost for top 10 replacement candidates: {priority_data['total_replacement_cost']:,.0f} RUB")
