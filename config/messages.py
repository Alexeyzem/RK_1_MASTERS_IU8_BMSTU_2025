"""
@brief Message templates for commercial departments Analysis
Contains all user-facing messages and logging templates
"""


class LogMessages:
    """
    @brief Log message templates for analysis operations
    Standardized messages for different logging levels and operations
    """

    # System initialization messages
    SYSTEM_START = "Commercial Department System initialization started"
    SYSTEM_READY = "Commercial Department System ready"
    DATA_LOAD_START = "Starting data loading process from JSON file"
    DATA_PROCESSING_START = "Starting data processing"
    DATA_LOAD_SUCCESS = "Data successfully loaded from file: {}"
    DATA_LOAD_ERROR = "Error loading data from file: {} - {}"

    # Project analysis messages
    PROJECT_COUNT = 'Total project count: {}'
    PROJECT_PROFIT_CALCULATION = 'Calculating average ROI and profit'

    # Personal analysis messages
    PERSONAL_COUNT = 'Total person count: {}'
    PERSONAL_REVENUE_PER_EMPLOYEE = 'Calculating revenue per employee'
    PERSONAL_CORRELATION = 'Calculating correlation between salary and performance_score'

    # Language Skills
    LANGUAGE_ANALYSIS = 'Language complex analysis'

    # Clients analyses
    CLIENT_PROJECT_ANALYSIS = 'Client project analysis'

    # ROI Up analyses
    ROI_ANALYSIS = 'ROI up analysis'

    # Analysis process messages
    ANALYSIS_START = "Starting {} analysis"
    ANALYSIS_COMPLETE = "{} analysis completed successfully"
    ANALYSIS_ERROR = "Error during {} analysis: {}"


class ReportMessages:
    """
    @brief Report message templates for analysis results
    Standardized output messages for different analysis sections
    """

    # Section headers
    PROJECT_PROFIT_HEADER = "PROFIT ANALYSIS"
    PERSON_HEADER = "PERSON ANALYSIS"
    LANGUAGE_HEADER = "LANGUAGE ANALYSIS"
    CLIENT_HEADER = "CLIENT ANALYSIS"
    ROI_HEADER = "ROI UP ANALYSIS"


class ErrorMessages:
    """
    @brief Error message templates
    Standardized error messages for exception handling
    """

    FILE_NOT_FOUND = "Configuration file not found: {}"
    INVALID_JSON = "Invalid JSON format in file: {}"
    DATA_VALIDATION_ERROR = "Data validation error: {}"
    CALCULATION_ERROR = "Calculation error in {}: {}"
