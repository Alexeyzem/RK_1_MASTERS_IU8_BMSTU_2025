"""
@brief Main execution script for IT Infrastructure Analysis System
Orchestrates all analysis modules and generates comprehensive reports
"""

import os
import sys
from analyzers.inventory_analyzer import InventoryAnalyzer
from analyzers.utilization_analyzer import UtilizationAnalyzer
from analyzers.cost_analyzer import CostAnalyzer
from analyzers.replacement_analyzer import ReplacementAnalyzer
from analyzers.optimization_analyzer import OptimizationAnalyzer
from config.messages import LogMessages, ReportMessages

class ITInfrastructureAnalysisOrchestrator:
    """
    @brief Main orchestrator for IT infrastructure analysis system
    Coordinates execution of all analysis modules and compiles results
    """
    
    def __init__(self, json_data_file_path):
        """
        @brief Initialize analysis orchestrator with data source
        Sets up all analyzer instances and configuration
        
        @param json_data_file_path: Path to company data JSON file
        """
        self.json_data_file_path = json_data_file_path
        self.analysis_results_collection = {}
        
        # Verify file exists before initializing analyzers
        self._verify_data_file_exists()

        # Initialize analyzer instances
        self.inventory_analysis_module = InventoryAnalyzer(json_data_file_path)
        self.utilization_analysis_module = UtilizationAnalyzer(json_data_file_path)
        self.cost_analysis_module = CostAnalyzer(json_data_file_path)
        self.replacement_analysis_module = ReplacementAnalyzer(json_data_file_path)
        self.optimization_analysis_module = OptimizationAnalyzer(json_data_file_path)

    def _verify_data_file_exists(self):
        """
        @brief Verify that the data file exists before analysis
        Provides clear error message if file is not found
        """
        if not os.path.exists(self.json_data_file_path):
            error_message = f"Data file not found: {self.json_data_file_path}"
            print(f"ERROR: {error_message}")
            print("Please ensure the JSON data file exists in the specified path")
            raise FileNotFoundError(error_message)

    def execute_comprehensive_analysis(self):
        """
        @brief Execute complete IT infrastructure analysis
        Runs all analysis modules and compiles comprehensive results

        @return: Dictionary containing all analysis results
        """
        print("INITIATING COMPREHENSIVE IT INFRASTRUCTURE ANALYSIS")
        print("=" * 70)

        try:
            # Execute all analysis modules
            print("\nEXECUTING EQUIPMENT INVENTORY ANALYSIS...")
            inventory_analysis_results = self.inventory_analysis_module.execute_analysis()
            self.analysis_results_collection['inventory'] = inventory_analysis_results

            print("\nEXECUTING UTILIZATION EFFICIENCY ANALYSIS...")
            utilization_analysis_results = self.utilization_analysis_module.execute_analysis()
            self.analysis_results_collection['utilization'] = utilization_analysis_results

            print("\nEXECUTING COST ANALYSIS...")
            cost_analysis_results = self.cost_analysis_module.execute_analysis()
            self.analysis_results_collection['cost'] = cost_analysis_results

            print("\nEXECUTING REPLACEMENT PLANNING ANALYSIS...")
            replacement_analysis_results = self.replacement_analysis_module.execute_analysis()
            self.analysis_results_collection['replacement'] = replacement_analysis_results

            print("\nEXECUTING OPTIMIZATION ANALYSIS...")
            optimization_analysis_results = self.optimization_analysis_module.execute_analysis()
            self.analysis_results_collection['optimization'] = optimization_analysis_results

            # Generate final comprehensive report
            self._generate_comprehensive_summary_report()

            return self.analysis_results_collection

        except Exception as comprehensive_analysis_error:
            print(f"\nCOMPREHENSIVE ANALYSIS FAILED: {str(comprehensive_analysis_error)}")
            raise comprehensive_analysis_error

    def _generate_comprehensive_summary_report(self):
        """
        @brief Generate final comprehensive summary report
        Compiles key findings and recommendations from all analyses
        """
        print("\n" + "=" * 70)
        print("COMPREHENSIVE IT INFRASTRUCTURE ANALYSIS SUMMARY")
        print("=" * 70)

        # Extract key metrics from all analyses
        total_equipment_count = self.analysis_results_collection['inventory']['total_equipment_count']
        total_equipment_cost = self.analysis_results_collection['inventory']['financial_analysis']['total_cost']
        average_utilization_rate = self.analysis_results_collection['utilization']['basic_metrics']['average_utilization']
        annual_maintenance_cost = self.analysis_results_collection['cost']['maintenance_analysis']['annual_total']
        low_utilization_count = self.analysis_results_collection['utilization']['low_utilization_equipment']['count']
        expiring_warranty_count = self.analysis_results_collection['replacement']['warranty_analysis']['expiring_equipment_count']
        potential_annual_savings = self.analysis_results_collection['optimization']['economic_analysis']['total_annual_savings']

        print(f"\nKEY PERFORMANCE INDICATORS:")
        print(f"• Total IT Equipment: {total_equipment_count} units")
        print(f"• Total Asset Value: {total_equipment_cost:,.0f} RUB")
        print(f"• Average Utilization Rate: {average_utilization_rate:.1f}%")
        print(f"• Annual Maintenance Cost: {annual_maintenance_cost:,.0f} RUB")
        print(f"• Underutilized Equipment: {low_utilization_count} units")
        print(f"• Equipment with Expiring Warranty: {expiring_warranty_count} units")
        print(f"• Potential Annual Savings: {potential_annual_savings:,.0f} RUB")

def main():
    """
    @brief Main execution function for IT Infrastructure Analysis
    Handles command line arguments and orchestrates analysis execution
    """
    # Configuration - update this path to match your JSON file
    company_data_json_file_path = "company.json"  # Changed from company_data_detailed.json

    try:
        # Initialize and execute analysis
        analysis_orchestrator = ITInfrastructureAnalysisOrchestrator(company_data_json_file_path)
        comprehensive_analysis_results = analysis_orchestrator.execute_comprehensive_analysis()

        print(f"\nANALYSIS COMPLETED SUCCESSFULLY!")
        print(f"Log files generated in 'logs/' directory")

    except FileNotFoundError as file_error:
        print(f"\nFILE ERROR: {str(file_error)}")
        print("Please check the file path and ensure the JSON file exists")
        sys.exit(1)
    except Exception as main_execution_error:
        print(f"\nCRITICAL ERROR DURING ANALYSIS EXECUTION: {str(main_execution_error)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
