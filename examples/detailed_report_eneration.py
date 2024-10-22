# ============================================================================================
# EXAMPLE: Detailed Report Generation
# ============================================================================================

# --- IMPORTS --------------------------------------------------------------------------------

from tool_reporter_lib import ReportHTML
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- INFO: ----------------------------------------------------------------------------------

# The result report will be a single HTML file.
# It's made it easy to share by email, or messenger.
# It's also a good tool for documenting mid-process test results,
# by changing parameters and storing the results report files.

# --- Make report object ---------------------------------------------------------------------

report: ReportHTML = ReportHTML(
    title                = 'My Report',      
    # sub_title            = 'Detailed report subtitle',  
    # file_name            = 'my_report',                 
    use_title_background = True, 
    open_saved_file      = True,  )

# if title not set will be used default title.

# if sub_title not set will be used report generation date time.

# if file_name not set will be made from title. 
#       If filename already exists, will be added a number to the end.
#         e.g. 'my_report', 'my_report_1', 'my_report_2', etc.

# if use_title_background not set will be used default value: True.

# if open_saved_file not set will be used default value: True.

# --- Add content to the report --------------------------------------------------------------

report.add_title('Welcome Title',
                    h_level    = 1,      # H tipe. 1 - Largest, .. 3 - Smallest.
                    use_center = True, ) # Cneter, or Left side.

# --- Add text to the report -----------------------------------------------------------------

small_text: str = 'Hello, this is a small text.'

report.add_text(small_text)

big_text: str = '''
Big chunk of text with many lines.
Line 1
Line 2
...
Line N
'''

report.add_text(big_text)

# --- Add a horizontal line ------------------------------------------------------------------

report.add_horizontal_line()

# --- Add a subtitle ------------------------------------------------------------------------
# Add a subtitle with a different heading level and centered text.

report.add_title('Subtitle', h_level = 2) # Just used H_level 2, or 3.

# --- Add a code block -----------------------------------------------------------------------
# Usefull if working with code, where you adjust some parameters, or tweak the code.
# The code block will be Logged by reporter, just by passing function name, or code block.

# making a custom function:
def custom_function_plot_chart(lines_count: int = 100) -> plt.Figure:
    '''
    Custom function to plot a chart with multiple lines.
    '''
    
    fig, axs = plt.subplots(2, 1, 
                            figsize      = (11.7, 6),   # If will be pasted to report, 
                                                        #   with NOT full width, 
                                                        #   recommended width <= 1170px.
                            dpi          = 100,
                            sharex       = True, 
                            tight_layout = True, )
    
    ax_1: plt.Axes = axs[0]
    ax_2: plt.Axes = axs[1]
    
    # plot_1:
    
    x_arr: np.ndarray[np.double] = np.linspace(0, 10, 200, dtype = np.double)
    y_one: np.ndarray[np.double] = np.sin(x_arr)
    y_two: np.ndarray[np.double] = np.cos(x_arr)
    y_thr: np.ndarray[np.double] = y_one * y_two
    
    ax_1.plot(        x_arr, y_one, color = f'#383', alpha = 0.7, linewidth = 0.5, )
    ax_1.fill_between(x_arr, y_one, color = f'#383', alpha = 0.1, label = 'sin(x)' )
    ax_1.plot(        x_arr, y_two, color = f'#338', alpha = 0.7, linewidth = 0.5, )
    ax_1.fill_between(x_arr, y_two, color = f'#338', alpha = 0.1, label = 'cos(x)' )
    ax_1.plot(        x_arr, y_thr, color = f'#833', alpha = 0.7, linewidth = 0.5, )
    ax_1.fill_between(x_arr, y_thr, color = f'#833', alpha = 0.1, label = 'sin(x) * cos(x)' )
    
    ax_1.legend()
    
    ax_1.grid(True)
    ax_1.set_title('Plot 1')
    ax_1.set_xlabel('X')
    ax_1.set_ylabel('Y')
    
    ax_1.spines['top'].set_color('#fff')
    ax_1.spines['right'].set_color('#fff')
    ax_1.spines['bottom'].set_color('#999')
    ax_1.spines['left'].set_color('#999')
    
    # plot_2:
    
    x: np.ndarray[np.double] = np.linspace(0, 10, 100, dtype = np.double)
    
    alpha_temp: float = 0.4 * 5 / lines_count
    alpha_temp        = max(0.05, min(0.3, alpha_temp))
    
    for _ in range(lines_count):

        y_arr: np.ndarray[np.double] = np.sin(x)
        y_arr                       += np.random.normal(0, 0.2, size = y_arr.shape)
        
        ax_2.plot(x, y_arr, alpha = alpha_temp, linewidth = 2.0, color = f'#363')
        pass
    
    ax_2.grid(False)
    ax_2.set_title('Plot 2')
    
    ax_2.spines['top'].set_color('#fff')
    ax_2.spines['right'].set_color('#fff')
    
    return fig

# --- Add code block to the report ----------------------------------------------------------

report.add_code(custom_function_plot_chart, 
                # title = 'My Custom Function',   # if not set will be used function name.
                        )

# --- Add Plot to the report -----------------------------------------------------------------

# Create a plot with custom function:
fig: plt.Figure = custom_function_plot_chart()

# Add the plot to the report:
report.add_plot(plt, 
                use_fullwidth = False, # if not set will be used default value: True.
                # height = 400,          # if not set will be used default from plot.
                # width  = 800,          # if not set will be used default from plot.
                )

# (Optional) Clear the figure, to free memory. ⚠️
fig.clear()

# --- Add DataFrame to the report ------------------------------------------------------------

# Create a sample DataFrame
df: pd.DataFrame = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2.5, 3.5, 4.5, 5.5, 6.5],
        })

df.loc[2, 'C'] = float('nan')  # Set a NaN value in column C
df['Names'] = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# add some space:
report.add_space()

# Add DataFrame to the report:
report.add_dataframe_table(df, 
                            highlight_columns = ['C'],  # Can be named several columns, like ['C', 'A', 'B']
                                                        #   or empty, like []. Will be aplied heatmap color to selected columns.
                            round = 1,                  # Round float values to 1 decimal place.
                            # title = 'My DataFrame',   # if not set will be used 'DataFrame'.
                            color_map_name = 'summer' , # Color map name for heatmap. If not set, will be used default.
                            used_part_of_color = 0.4,   # Part of the color map to use. If not set, will be used default 0.4. The greater, the brighter the colors.
                                )

# --- Add Alert Box to the report ------------------------------------------------------------

report.add_alert_box(   'This is an alert box, with some important information.',
                        alert_type = 'n',   # Can be 'i' - info, 'n' - note, 'w' - warning, 'e' - error.
                        emoji = '✅',       # if not set, will be used default emoji. 
                                            # if set '' - will be no emoji.
                            )

# --- Add text with console style ------------------------------------------------------------

text_to_add_console_style: str = '''
This is a text with console style.
It's good to use, for some printing or returning text values of a function.
Like class status of our report object. \n
''' 
text_to_add_console_style += str(report)
report.add_text_console(text_to_add_console_style)

# --- Add Parameters and Values Table to the report -------------------------------------------

params_values: dict = { 
    'Parameter name'              : 'Parameter Value',
    'Param. can be different type': 12345,
    'and so on'                   : 3.1415,
    'and on'                      : 'Some text', 
    }

report.add_param_value_table(params_values)

# --- Add Parameters and Values, with long values ----------------------------------------------

param: dict = { 
    'Number small' : 34,
    'Array of data': [1, 2, 3, 4, 5],
    'Long array'   : np.arange(50), 
    }
report.add_space()
report.add_param_value_table(param)

# --- Add Long list of Parameters and Values ---------------------------------------------------
param_long: dict = { }

for i in range(25):
    param_long[f'Parameter {i}'] = np.random.randint(-1000, 1000)

report.add_param_value_table_big(param_long)

# --- Adding Show/Hide Region ------------------------------------------------------------------

# Open the show/hide region:
report.add_showhide_region_open('Show/Hide Region Title')

# all added to report content will be inside the show/hide region, until close it.

# add title:
report.add_title('Big Table, that we hide.', use_center = True)

# add some Long table:
report.add_param_value_table_big(param_long)

# Close the show/hide region:
report.add_showhide_region_close()


# --- Add Final Text -------------------------------------------------------------------------
# That element will be already outside the show/hide region, cause it was closed.
report.add_title('(👉ﾟヮﾟ)👉 Completed !', use_center = True)

# --- Save the report ------------------------------------------------------------------------
report.save()

# --- DONE :) --------------------------------------------------------------------------------