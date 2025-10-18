"""
@brief Main execution script for commercial department Analysis System
Orchestrates all analysis modules and generates comprehensive reports
"""

import os
import sys
from analyzers.projects_metrics_analyzer import ProjectsMetricsAnalyzer
from analyzers.personal_analyzer import PersonalEfficiencyAnalyzer
from analyzers.language_analyzer import LanguageSkillsAnalyzer
from analyzers.client_analyzer import ClientAnalyzer
from analyzers.roi_up_analyzer import ROIUpAnalyzer
from config.messages import LogMessages, ReportMessages


class CommercialDepartmentAnalysisOrchestrator:
    """
    @brief Main orchestrator for commercial departments analysis system
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
        self.projects_metric_module = ProjectsMetricsAnalyzer(json_data_file_path)
        self.person_efficiency_module = PersonalEfficiencyAnalyzer(json_data_file_path)
        self.language_analyzer = LanguageSkillsAnalyzer(json_data_file_path)
        self.clients_analyzer = ClientAnalyzer(json_data_file_path)
        self.roi_up_analyzer = ROIUpAnalyzer(json_data_file_path)

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
        @brief Execute complete commercial department analysis
        Runs all analysis modules and compiles comprehensive results

        @return: Dictionary containing all analysis results
        """
        print("INITIATING COMPREHENSIVE COMMERCIAL DEPARTMENT ANALYSIS")
        print("=" * 70)

        try:
            print("INITIATING PROJECT ANALYSIS")
            profit_analysis_result = self.projects_metric_module.execute_analysis()
            self.analysis_results_collection['profit_analysis_result'] = profit_analysis_result

            print("INITIATING PERSONAL ANALYSIS")
            personal_analysis_result = self.person_efficiency_module.execute_analysis()
            self.analysis_results_collection['personal_analysis_result'] = personal_analysis_result

            print("INITIATING LANGUAGE ANALYSIS")
            language_analysis_result = self.language_analyzer.execute_analysis()
            self.analysis_results_collection['language_analysis_result'] = language_analysis_result

            print("INITIATING CLIENT ANALYSIS")
            client_analysis_result = self.clients_analyzer.execute_analysis()
            self.analysis_results_collection['client_analysis_result'] = client_analysis_result

            print("INITIATING ROI UP ANALYSIS")
            roi_up_analysis_result = self.roi_up_analyzer.execute_analysis()
            self.analysis_results_collection['roi_up_analysis_result'] = roi_up_analysis_result

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
        print("COMPREHENSIVE COMMERCIAL DEPARTMENT ANALYSIS SUMMARY")
        print("=" * 70)

        # Extract key metrics from all analyses
        total_profit = self.analysis_results_collection['profit_analysis_result'].get('total_profit')
        average_roi = self.analysis_results_collection['profit_analysis_result'].get('average_roi')

        revenue_per_employee = self.analysis_results_collection['personal_analysis_result'].get('revenue-per-employee')
        corr = self.analysis_results_collection['personal_analysis_result'].get('correlation')

        lang_distribution = self.analysis_results_collection['language_analysis_result'].get('distribution')
        need_upgrade_language = self.analysis_results_collection['language_analysis_result'].get('needs')
        person_with_two_language = self.analysis_results_collection['language_analysis_result'].get('persons-who-know')

        priority_risk = self.analysis_results_collection['client_analysis_result'].get('priorities-risk')
        ratio = self.analysis_results_collection['client_analysis_result'].get('ratio')
        good_projects = self.analysis_results_collection['client_analysis_result'].get('projects')

        potential_profit = self.analysis_results_collection['roi_up_analysis_result'].get('potential_profit')

        print(f"\nKEY PERFORMANCE INDICATORS:")
        print(f"Total profit: {total_profit}")
        print(f"Average ROI: {average_roi}")

        print(f"Revenue per employee: {revenue_per_employee}")
        print(f"Correlation: {corr}")

        print(f"Language distribution: {lang_distribution}")
        print(f"Need upgrade: {need_upgrade_language}")
        print(f"Person with two language: {person_with_two_language}")

        print(f"Priority risk: {priority_risk}")
        print(f"Ratio high/critical to low priority: {ratio}")
        print(f"Projects with high risk and profit: {good_projects}")

        print(f"If roi up for 5%, potential profit: {potential_profit}")


def main():
    """
    @brief Main execution function for Commercial department Analysis
    Handles command line arguments and orchestrates analysis execution
    """
    # Configuration - update this path to match your JSON file
    company_data_json_file_path = "company.json"  # Changed from company_data_detailed.json

    try:
        # Initialize and execute analysis
        analysis_orchestrator = CommercialDepartmentAnalysisOrchestrator(company_data_json_file_path)
        analysis_orchestrator.execute_comprehensive_analysis()

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
