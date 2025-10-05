"""
@brief Equipment cost analysis module
Analyzes ownership costs, maintenance expenses, and financial metrics
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages

class CostAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for IT equipment cost assessment
    Provides total cost of ownership and maintenance expense analysis
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize cost analyzer
        Sets up cost-specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "CostAnalysis")

    def execute_analysis(self):
        """
        @brief Execute comprehensive cost analysis
        Performs maintenance cost calculation, TCO analysis, and financial ratio assessment

        @return: Dictionary containing cost analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("cost"))

        try:
            # Maintenance cost analysis
            maintenance_cost_analysis_results = self._analyze_maintenance_costs()

            # Cost per unit analysis
            cost_per_unit_analysis_results = self._analyze_cost_per_unit()

            # Purchase vs maintenance ratio analysis
            cost_ratio_analysis_results = self._analyze_cost_ratios()

            # Payback period calculation
            payback_period_calculation_results = self._calculate_payback_period()

            # Compile results
            analysis_results = {
                'maintenance_analysis': maintenance_cost_analysis_results,
                'cost_per_unit_analysis': cost_per_unit_analysis_results,
                'cost_ratio_analysis': cost_ratio_analysis_results,
                'payback_analysis': payback_period_calculation_results
            }

            self._generate_cost_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Cost"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("cost", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _analyze_maintenance_costs(self):
        """
        @brief Analyze maintenance costs and annual expenses
        Calculates total and average maintenance costs

        @return: Dictionary with maintenance cost metrics
        """
        self.logger.info(LogMessages.MAINTENANCE_COST_CALCULATION)

        total_monthly_maintenance_cost = self.it_equipment_dataframe['maintenance_cost'].sum()
        total_annual_maintenance_cost = total_monthly_maintenance_cost * 12
        average_monthly_maintenance_cost = self.it_equipment_dataframe['maintenance_cost'].mean()

        total_equipment_purchase_cost = self.it_equipment_dataframe['cost'].sum()
        maintenance_to_purchase_ratio = (total_annual_maintenance_cost / total_equipment_purchase_cost) * 100

        maintenance_cost_analysis_results = {
            'monthly_total': total_monthly_maintenance_cost,
            'annual_total': total_annual_maintenance_cost,
            'monthly_average': average_monthly_maintenance_cost,
            'maintenance_ratio_percentage': maintenance_to_purchase_ratio
        }

        return maintenance_cost_analysis_results

    def _analyze_cost_per_unit(self):
        """
        @brief Analyze cost per unit by equipment type
        Calculates TCO and ownership costs per equipment category

        @return: DataFrame with cost per unit analysis
        """
        cost_per_unit_analysis = self.it_equipment_dataframe.groupby('type').agg({
            'equipment_id': 'count',
            'cost': ['sum', 'mean'],
            'maintenance_cost': ['sum', 'mean']
        }).round(2)

        cost_per_unit_analysis.columns = [
            'Equipment Count',
            'Total Purchase Cost',
            'Average Purchase Cost',
            'Total Monthly Maintenance',
            'Average Monthly Maintenance'
        ]

        cost_per_unit_analysis['Annual Maintenance Cost'] = cost_per_unit_analysis['Average Monthly Maintenance'] * 12
        cost_per_unit_analysis['TCO Percentage'] = (
            cost_per_unit_analysis['Annual Maintenance Cost'] / cost_per_unit_analysis['Average Purchase Cost'] * 100
        ).round(2)

        return cost_per_unit_analysis.reset_index()

    def _analyze_cost_ratios(self):
        """
        @brief Analyze ratios between purchase and maintenance costs
        Calculates financial ratios for cost optimization

        @return: Dictionary with cost ratio metrics
        """
        total_purchase_cost = self.it_equipment_dataframe['cost'].sum()
        total_annual_maintenance_cost = self.it_equipment_dataframe['maintenance_cost'].sum() * 12

        purchase_to_maintenance_ratio = total_purchase_cost / total_annual_maintenance_cost
        maintenance_to_purchase_ratio = total_annual_maintenance_cost / total_purchase_cost

        cost_ratio_analysis_results = {
            'total_purchase_cost': total_purchase_cost,
            'total_annual_maintenance_cost': total_annual_maintenance_cost,
            'purchase_to_maintenance_ratio': purchase_to_maintenance_ratio,
            'maintenance_to_purchase_ratio': maintenance_to_purchase_ratio
        }

        return cost_ratio_analysis_results

    def _calculate_payback_period(self):
        """
        @brief Calculate equipment payback period
        Estimates return on investment timeframes

        @return: Dictionary with payback period metrics
        """
        total_equipment_cost = self.it_equipment_dataframe['cost'].sum()

        # Assume average daily operational savings from equipment usage
        assumed_daily_operational_savings = 1000
        annual_operational_savings = assumed_daily_operational_savings * 365

        payback_period_years = total_equipment_cost / annual_operational_savings

        payback_period_calculation_results = {
            'total_equipment_cost': total_equipment_cost,
            'assumed_daily_savings': assumed_daily_operational_savings,
            'annual_savings': annual_operational_savings,
            'payback_period_years': payback_period_years
        }

        return payback_period_calculation_results

    def _generate_cost_report(self, analysis_results):
        """
        @brief Generate formatted cost analysis report
        Outputs cost metrics and financial recommendations

        @param analysis_results: Dictionary containing cost analysis results
        """
        print("=" * 70)
        print(ReportMessages.COST_HEADER)
        print("=" * 70)

        maintenance_data = analysis_results['maintenance_analysis']
        cost_ratio_data = analysis_results['cost_ratio_analysis']

        print(f"\n{ReportMessages.ANNUAL_MAINTENANCE_COST.format(maintenance_data['annual_total'])}")
        print(f"Maintenance to purchase cost ratio: {maintenance_data['maintenance_ratio_percentage']:.1f}%")

        print("\nCost Per Unit Analysis by Equipment Type:")
        print(analysis_results['cost_per_unit_analysis'].to_string(index=False))

        print(f"\nTotal equipment purchase cost: {cost_ratio_data['total_purchase_cost']:,.0f} RUB")
        print(f"Purchase to maintenance ratio: 1 : {cost_ratio_data['maintenance_to_purchase_ratio']:.2f}")

        payback_data = analysis_results['payback_analysis']
        print(f"Estimated payback period: {payback_data['payback_period_years']:.1f} years")
