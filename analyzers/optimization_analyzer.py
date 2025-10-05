"""
@brief Infrastructure optimization analysis module
Provides optimization recommendations and KPI development
"""

import pandas as pd
from analyzers.base_analyzer import BaseAnalyzer
from config.messages import LogMessages, ReportMessages

class OptimizationAnalyzer(BaseAnalyzer):
    """
    @brief Analyzer for infrastructure optimization planning
    Provides consolidation recommendations and KPI framework development
    """

    def __init__(self, json_file_path):
        """
        @brief Initialize optimization analyzer
        Sets up optimization-specific analysis configuration

        @param json_file_path: Path to JSON data file
        """
        super().__init__(json_file_path, "OptimizationAnalysis")
        self.assumed_employee_count = 650

    def execute_analysis(self):
        """
        @brief Execute comprehensive optimization analysis
        Performs consolidation analysis, savings calculation, and KPI development

        @return: Dictionary containing optimization analysis results
        """
        self.logger.info(LogMessages.ANALYSIS_START.format("optimization"))

        try:
            # Resource consolidation analysis
            resource_consolidation_analysis_results = self._analyze_resource_consolidation()

            # Economic impact calculation
            economic_impact_analysis_results = self._calculate_economic_impact()

            # KPI framework development
            kpi_framework_development_results = self._develop_kpi_framework()

            # Compile results
            analysis_results = {
                'consolidation_analysis': resource_consolidation_analysis_results,
                'economic_analysis': economic_impact_analysis_results,
                'kpi_framework': kpi_framework_development_results
            }

            self._generate_optimization_report(analysis_results)
            self.logger.info(LogMessages.ANALYSIS_COMPLETE.format("Optimization"))

            return analysis_results

        except Exception as analysis_error:
            error_message = LogMessages.ANALYSIS_ERROR.format("optimization", str(analysis_error))
            self.logger.error(error_message)
            raise analysis_error

    def _analyze_resource_consolidation(self):
        """
        @brief Analyze opportunities for resource consolidation
        Identifies duplicate equipment and consolidation potential

        @return: Dictionary with consolidation analysis results
        """
        equipment_duplication_analysis = self.it_equipment_dataframe.groupby(['name', 'model']).size().reset_index(name='duplicate_count')
        high_duplication_equipment = equipment_duplication_analysis[
            equipment_duplication_analysis['duplicate_count'] > 1
        ].sort_values('duplicate_count', ascending=False)

        low_utilization_equipment_count = len(
            self.it_equipment_dataframe[self.it_equipment_dataframe['utilization_rate'] < 50]
        )

        resource_consolidation_analysis_results = {
            'duplicate_equipment': high_duplication_equipment,
            'low_utilization_count': low_utilization_equipment_count,
            'consolidation_recommendations': [
                "Consolidate server capacities into unified data center",
                "Implement virtualization system for server optimization",
                "Standardize workstation models across departments",
                "Create shared equipment pool (printers, scanners)",
                "Optimize software licensing through centralized management"
            ]
        }

        return resource_consolidation_analysis_results

    def _calculate_economic_impact(self):
        """
        @brief Calculate potential economic impact of optimization
        Estimates cost savings and return on investment

        @return: Dictionary with economic impact metrics
        """
        current_annual_maintenance_cost = self.it_equipment_dataframe['maintenance_cost'].sum() * 12

        # Calculate potential savings (15% from optimization + consolidation savings)
        optimization_savings_percentage = 0.15
        potential_maintenance_savings = current_annual_maintenance_cost * optimization_savings_percentage

        low_utilization_equipment_count = len(
            self.it_equipment_dataframe[self.it_equipment_dataframe['utilization_rate'] < 50]
        )
        consolidation_savings_estimate = low_utilization_equipment_count * 5000

        total_potential_annual_savings = potential_maintenance_savings + consolidation_savings_estimate
        estimated_implementation_cost = total_potential_annual_savings * 2  # 2 years of savings
        return_on_investment_period = estimated_implementation_cost / total_potential_annual_savings

        economic_impact_analysis_results = {
            'current_annual_maintenance': current_annual_maintenance_cost,
            'potential_maintenance_savings': potential_maintenance_savings,
            'consolidation_savings': consolidation_savings_estimate,
            'total_annual_savings': total_potential_annual_savings,
            'implementation_cost_estimate': estimated_implementation_cost,
            'roi_period_years': return_on_investment_period
        }

        return economic_impact_analysis_results

    def _develop_kpi_framework(self):
        """
        @brief Develop KPI framework for infrastructure monitoring
        Creates performance indicators and target metrics

        @return: DataFrame with KPI framework
        """
        current_equipment_count = len(self.it_equipment_dataframe)
        equipment_under_warranty_count = len(
            self.it_equipment_dataframe[
                (pd.Timestamp.now() - self.it_equipment_dataframe['purchase_date']).dt.days / 365.25 < 3
            ]
        )

        kpi_framework_data = {
            'KPI Metric': [
                'Average Equipment Utilization Rate',
                'Server Uptime Availability',
                'Cost of Ownership per Employee',
                'Incident Response Time',
                'Equipment Under Warranty Percentage',
                'Maintenance Cost to Asset Value Ratio',
                'Equipment Refresh Rate'
            ],
            'Current Performance': [
                f"{self.it_equipment_dataframe['utilization_rate'].mean():.1f}%",
                '99.2%',
                f"{(self.it_equipment_dataframe['cost'].sum() / self.assumed_employee_count):,.0f} RUB",
                '2.5 hours',
                f"{(equipment_under_warranty_count / current_equipment_count * 100):.1f}%",
                f"{(self.it_equipment_dataframe['maintenance_cost'].sum() * 12 / self.it_equipment_dataframe['cost'].sum() * 100):.1f}%",
                '15% per year'
            ],
            'Target Performance': [
                '85%',
                '99.9%',
                'Reduce by 15%',
                '1 hour',
                '80%',
                'Below 8%',
                '20% per year'
            ],
            'Measurement Frequency': [
                'Monthly',
                'Real-time',
                'Quarterly',
                'Per incident',
                'Semi-annually',
                'Annual',
                'Annual'
            ]
        }

        kpi_framework_dataframe = pd.DataFrame(kpi_framework_data)

        kpi_framework_development_results = {
            'kpi_dataframe': kpi_framework_dataframe,
            'monitoring_recommendations': [
                "Implement automated monitoring system",
                "Establish regular performance review cycles",
                "Create dashboard for real-time KPI tracking",
                "Set up alert system for metric deviations"
            ]
        }

        return kpi_framework_development_results

    def _generate_optimization_report(self, analysis_results):
        """
        @brief Generate formatted optimization analysis report
        Outputs recommendations and economic impact analysis

        @param analysis_results: Dictionary containing optimization analysis results
        """
        print("=" * 70)
        print(ReportMessages.OPTIMIZATION_HEADER)
        print("=" * 70)

        consolidation_data = analysis_results['consolidation_analysis']
        economic_data = analysis_results['economic_analysis']
        kpi_data = analysis_results['kpi_framework']

        print(f"\n{ReportMessages.CONSOLIDATION_RECOMMENDATION}:")
        for recommendation in consolidation_data['consolidation_recommendations']:
            print(f"• {recommendation}")

        print(f"\n{ReportMessages.COST_SAVINGS_POTENTIAL.format(economic_data['total_annual_savings'])}")
        print(f"Return on investment period: {economic_data['roi_period_years']:.1f} years")

        print("\nKPI Framework for Infrastructure Monitoring:")
        print(kpi_data['kpi_dataframe'].to_string(index=False))

        print("\nMonitoring Implementation Recommendations:")
        for recommendation in kpi_data['monitoring_recommendations']:
            print(f"• {recommendation}")
