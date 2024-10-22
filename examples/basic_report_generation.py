# ============================================================================================
# EXAMPLE: Basic Report Generation
# ============================================================================================

from tool_reporter_lib import ReportHTML

# --------------------------------------------------------------------------------------------
# Define a basic example function to create a report
# --------------------------------------------------------------------------------------------

def generate_basic_report():
    """
    Generate a basic HTML report using the ReportHTML class.
    This function demonstrates adding titles, text, and saving the report.
    """
    
    # Create a ReportHTML object
    report = ReportHTML(
        title                = "Basic Report Example",  # Report Title
        # - ! You may disable any of parameters, and defult will be used. ! - #
        # sub_title            = "Generated with Tool Reporter Library",  # Subtitle of the report
        file_name            = "basic_report",  # Output file name
        use_title_background = True,  # Use a background image for the title
        open_saved_file      = True  # Automatically open the report in a browser after saving
    )
    
    # Alternatively, can be used with just a few, or none of the parameters    
    # >>> report = ReportHTML("Simple Report Example")
    
    # Add content to the report
    report.add_title("Welcome to the Basic Report")
    report.add_text("This is a simple example of generating an HTML report using the tool_reporter_lib package.")
    
    # Adding a subtitle
    report.add_title("Report Sections", h_level = 1, use_center = True)    
    report.add_text("You can add multiple sections with different heading levels and text content.")

    # Add some more text and a horizontal line to separate sections
    report.add_text("Below is an example of a horizontal line separating two sections.")
    report.add_horizontal_line()

    # Add another section
    report.add_title("End of the Report", h_level = 2)
    report.add_text("This is the end of the basic report example.")
    
    # Save the report to an HTML file
    report.save()
    
    print(f"Report saved as: {report._file_path}")

# --------------------------------------------------------------------------------------------
# Run the example if the script is executed
# --------------------------------------------------------------------------------------------

if __name__ == "__main__":
    generate_basic_report()
