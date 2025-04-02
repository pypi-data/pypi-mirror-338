import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import re
import json
import numpy as np
import matplotlib.ticker as mticker
import textwrap




###################-------------plots----------------------------##############
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import textwrap
import datetime
from dateutil import parser

def format_large_number(value, pos=None):
    """Format large numbers with currency symbols and appropriate suffixes."""
    if value >= 1e9:
        return f'${value/1e9:.1f}B'  # Billion
    elif value >= 1e6:
        return f'${value/1e6:.1f}M'  # Million
    elif value >= 1e3:
        return f'${value/1e3:.1f}K'  # Thousand
    else:
        return f'${int(value)}'  # Small values show as whole dollars
        
def format_axis_based_on_type(ax, chart_props, axis='x'):
    """
    Format axis based on its type (categorical, datetime, numeric)
    
    Parameters:
    ax: Matplotlib axis
    chart_props: Chart properties containing axis type info
    axis: Which axis to format ('x' or 'y')
    
    Returns:
    A tuple of (formatted_data, formatter) for the specified axis
    """
    axis_type_key = f'{axis}AxisType'
    axis_type = chart_props.get(axis_type_key, 'categorical')
    
    # Find the data for this axis
    data = None
    data_key = f'{axis}Data'
    
    for series in chart_props.get('data', []):
        if data_key in series:
            data = series[data_key]
            break

    if not data:
        return None, None

    if axis_type == 'datetime':
        formatted_data = []
        has_time_granularity = False

        for d in data:
            try:
                if isinstance(d, (int, float)):
                    # Normalize large timestamps (ns/us/ms to s)
                    if d > 1e17:
                        d = d / 1e9  # nanoseconds
                    elif d > 1e14:
                        d = d / 1e6  # microseconds
                    elif d > 1e11:
                        d = d / 1e3  # milliseconds
                    dt = datetime.datetime.fromtimestamp(d)
                elif isinstance(d, str):
                    dt = parser.parse(d)
                else:
                    dt = d
                formatted_data.append(dt)

                # Detect if time granularity exists (hour/min/sec != 0)
                if dt.hour != 0 or dt.minute != 0 or dt.second != 0:
                    has_time_granularity = True

            except Exception:
                formatted_data.append(d)

        # Choose format
        if has_time_granularity:
            formatter = mdates.DateFormatter('%d-%m-%Y %H:%M:%S')
        else:
            formatter = mdates.DateFormatter('%d-%m-%Y')

        locator = mdates.AutoDateLocator()

        if axis == 'x':
            ax.xaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(locator)
            plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        else:
            ax.yaxis.set_major_formatter(formatter)
            ax.yaxis.set_major_locator(locator)

        return formatted_data, formatter

    elif axis_type == 'numeric':
        formatted_data = [float(d) if isinstance(d, (int, float, str)) and str(d).replace('.', '', 1).isdigit() else d for d in data]

        if axis == 'y':
            formatter = mticker.FuncFormatter(format_large_number)
            ax.yaxis.set_major_formatter(formatter)
        else:
            formatter = mticker.ScalarFormatter()

        return formatted_data, formatter

    else:  # categorical
        formatted_data = data
        return formatted_data, None



def populate_chart(ax, chart_data, debug=False):
    """
    Populate a chart with data, using matplotlib's built-in text wrapping
    and layout capabilities for better alignment.

    Parameters:
    ax: Matplotlib axis
    chart_data: Chart data from the structure
    debug: Whether to show debug information
    """
    if debug:
        print(f"Populating chart: {chart_data.get('id')}")

    # Extract chart data
    chart_type = chart_data.get('charts')
   
    chart_props = chart_data.get('chartData', {})
    
    # If chartData is not present, try using the chart_data directly
    # This handles different chart data formats
    if not chart_props:
        chart_props = chart_data
        
    chart_category = chart_props.get('category', '')
    # Check chart position/type
    chart_id = chart_data.get('id', '')
    
    # Analyze chart placement:
    # 1. Is this a parent chart?
    is_parent = 'children' in chart_data and chart_data['children']
    
    # 2. Is this a top row chart? 
    is_top_row = 'row_0' == chart_id or chart_id.startswith('row_0_') 
    
    # 3. Is this a child chart?
    is_child = '_row' in chart_id or '_col' in chart_id
    
    # Set chart title and labels with position-specific adjustments
    title = chart_props.get('title', 'Chart')
    
    # Make titles shorter to avoid overlap between adjacent plots
    # Create a wrapped title that won't extend too far horizontally
    if len(title) > 25:
        # Limit title length and split into multiple lines using textwrap
        wrapped_title = '\n'.join(textwrap.wrap(title, width=25))
        title = wrapped_title
    
    # Balanced title padding with bold font and custom color
    if is_parent:
        ax.set_title(title, fontsize=11, fontweight='bold', wrap=True, pad=8, color='#2F4F4F')  # Dark slate gray
    else:
        ax.set_title(title, fontsize=11, fontweight='bold', wrap=True, pad=8, color='#2F4F4F')  # Dark slate gray

    # Handle x-label placement - balanced approach
    x_label = chart_props.get('xAxisLabel')
    if x_label:
        if is_parent:
            # For parent charts, slightly reduce padding but keep readable
            ax.set_xlabel(x_label, fontsize=10, fontweight='bold', labelpad=3, color='#2F4F4F')  # Dark slate gray
        else:
            # For child charts, standard settings
            ax.set_xlabel(x_label, fontsize=10, fontweight='bold', labelpad=5, color='#2F4F4F')  # Dark slate gray

    y_label = chart_props.get('yAxisLabel')
    if y_label:
        ax.set_ylabel(y_label, fontsize=10, fontweight='bold', labelpad=5, color='#2F4F4F')  # Dark slate gray
    
    # Ensure the grid is active for all charts with consistent appearance
    ax.grid(True, linestyle='--', alpha=0.6, color='#cccccc')
    
    # Make tick labels darker and more readable
    ax.tick_params(axis='both', colors='#555555')
    for tick in ax.get_xticklabels():
        tick.set_fontsize(9)
    for tick in ax.get_yticklabels():
        tick.set_fontsize(9)

    # Adjust margins for better text fitting
    ax.margins(0.1)

    # Apply axis formatting based on axis types
    # Only apply default formatter if no special type is specified
    if chart_props.get('yAxisType') != 'datetime' and chart_props.get('yAxisType') != 'categorical':
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(format_large_number))

    # Add a border around the figure
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_color('#555555')

    # Handle different chart types
    if chart_type == 'bar':
        plot_bar(ax, chart_props, chart_data)
    elif chart_type == 'pie' or (chart_type is None and any(d.get('type') == 'pie' for d in chart_props.get('data', []))):
        plot_pie(ax, chart_props)
    elif chart_type=='box':
      plot_box(ax, chart_props, chart_data)
    elif chart_category=='html':
      plot_html(ax, chart_props, chart_data)
    elif chart_type=='line':
      plot_line(ax, chart_props, chart_data)
    elif chart_category=='histogram':
      plot_histogram(ax, chart_props, chart_data)
    elif chart_type=='scatter':
      plot_line(ax, chart_props, chart_data)
    else:
        # Unsupported chart type
        ax.text(0.5, 0.5, f"Unsupported chart type: {chart_type}",
                ha='center', va='center')

def plot_bar(ax, chart_props, chart_data):
    """
    Plot a bar chart with the given data. Can be vertical (default) or horizontal,
    and supports both regular and stacked bar charts.
    
    Parameters:
    ax: Matplotlib axis
    chart_props: Chart properties from the structure
    chart_data: Full chart data (for positioning info)
    """
    # Check chart type and orientation
    is_horizontal = chart_props.get('title', '').lower().find('horizontal') >= 0 or chart_props.get('chartId', '').find('horizontal') >= 0
    is_stacked = chart_props.get('chartId', '').find('stacked') >= 0 or any(series.get('type', '') == 'stackedBar' for series in chart_props.get('data', []))
    
    data = chart_props.get('data', [])

    if not data:
        ax.text(0.5, 0.5, "No bar data found", ha='center', va='center')
        return

    # Format axes based on types
    if is_horizontal:
        # For horizontal bars, we swap x and y axes
        formatted_y_data, y_formatter = format_axis_based_on_type(ax, chart_props, axis='x')
        formatted_x_data, x_formatter = format_axis_based_on_type(ax, chart_props, axis='y')
        
        if not formatted_y_data:
            ax.text(0.5, 0.5, "No y-axis data found", ha='center', va='center')
            return
    else:
        # For vertical bars (standard)
        formatted_x_data, x_formatter = format_axis_based_on_type(ax, chart_props, axis='x')
        formatted_y_data, y_formatter = format_axis_based_on_type(ax, chart_props, axis='y')
        
        if not formatted_x_data:
            ax.text(0.5, 0.5, "No x-axis data found", ha='center', va='center')
            return

    # Create a beautiful color palette for bars
    color_palette = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC']
    
    # Set up positions based on orientation
    if is_horizontal:
        positions = np.arange(len(formatted_y_data))
    else:
        positions = np.arange(len(formatted_x_data))
    
    # Initialize bottom/left values for stacked bars
    if is_stacked:
        if is_horizontal:
            stack_left = np.zeros(len(positions))
        else:
            stack_bottom = np.zeros(len(positions))
    else:
        # Calculate bar width/height for non-stacked bars
        bar_size = 0.8 / len(data)

    # Plot each series
    for i, series in enumerate(data):
        if 'yData' not in series:
            continue
            
        # Get series properties
        name = series.get('name', f'Series {i+1}')
        color = series.get('color', color_palette[i % len(color_palette)])
        y_values = series['yData']

        if is_stacked:
            # For stacked bars, we use the full width/height and stack on top/side
            if is_horizontal:
                # Horizontal stacked bars
                bars = ax.barh(positions, y_values, height=0.8, left=stack_left,
                           label=name, color=color, edgecolor='white', linewidth=0.8, alpha=0.85)
                
                # Update left positions for next series
                stack_left = stack_left + y_values
                
                # Annotate values on horizontal stacked bars
                for j, (bar, value) in enumerate(zip(bars, y_values)):
                    # Only annotate if bar is wide enough
                    if value > max(y_values) * 0.05:
                        formatted_value = format_large_number(value)
                        # Position label in middle of this segment
                        ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + bar.get_height()/2,
                                formatted_value, ha='center', va='center', 
                                fontsize=9, fontweight='bold', color='white')
            else:
                # Vertical stacked bars
                bars = ax.bar(positions, y_values, width=0.8, bottom=stack_bottom,
                          label=name, color=color, edgecolor='white', linewidth=0.8, alpha=0.85)
                
                # Update bottom positions for next series
                stack_bottom = stack_bottom + y_values
                
                # Annotate values on vertical stacked bars
                for j, (bar, value) in enumerate(zip(bars, y_values)):
                    # Only annotate if bar is tall enough
                    if value > max(y_values) * 0.05:
                        formatted_value = format_large_number(value)
                        # Position label in middle of this segment
                        ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + bar.get_height()/2,
                                formatted_value, ha='center', va='center', 
                                fontsize=9, fontweight='bold', color='white')
        else:
            # Non-stacked bars
            offset = (i - len(data)/2 + 0.5) * bar_size
            
            if is_horizontal:
                # Horizontal bars
                bars = ax.barh(positions + offset, y_values, height=bar_size, 
                            label=name, color=color, edgecolor='white', linewidth=0.8, alpha=0.85)
                            
                # Annotate values on horizontal bars
                max_value = max(y_values) if y_values else 0
                for bar, value in zip(bars, y_values):
                    # Only show value if bar is wide enough
                    if max_value > 0 and bar.get_width() > max_value * 0.05:
                        formatted_value = format_large_number(value)
                        ax.text(bar.get_width() * 0.95, bar.get_y() + bar.get_height()/2,
                                formatted_value, ha='right', va='center', 
                                fontsize=9, fontweight='bold', color='black')
            else:
                # Vertical bars
                bars = ax.bar(positions + offset, y_values, width=bar_size, 
                            label=name, color=color, edgecolor='white', linewidth=0.8, alpha=0.85)
                            
                # Annotate values on vertical bars
                max_value = max(y_values) if y_values else 0
                for bar, value in zip(bars, y_values):
                    # Only show value if bar is tall enough
                    if max_value > 0 and bar.get_height() > max_value * 0.05:
                        formatted_value = format_large_number(value)
                        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 0.95,
                                formatted_value, ha='center', va='top', 
                                fontsize=9, fontweight='bold', color='black')

    # Set axis ticks and labels
    if is_horizontal:
        # Set y-ticks for horizontal bars (categories on y-axis)
        ax.set_yticks(positions)
        
        # Handle y-axis labels for horizontal bars
        y_axis_type = chart_props.get('xAxisType', 'categorical')  # We use xAxisType for y-axis in horizontal
        
        if y_axis_type != 'datetime':
            y_display_labels = [str(y) for y in formatted_y_data]
            ax.set_yticklabels(y_display_labels)
            
        # Reverse y-axis to have first item at top
        ax.invert_yaxis()
    else:
        # Set x-ticks for vertical bars (categories on x-axis)
        ax.set_xticks(positions)
        
        # Handle x-axis labels for vertical bars
        x_axis_type = chart_props.get('xAxisType', 'categorical')
        
        if x_axis_type != 'datetime':
            # Get display labels
            x_display_labels = [str(x) for x in formatted_x_data]
            
            # Dynamically adjust label rotation for better readability
            max_label_len = max([len(str(x)) for x in x_display_labels])
            n_labels = len(x_display_labels)

            # Dynamic calculation of rotation angle
            rotation_angle = min(90, max(0, max_label_len * 2 + n_labels * 3 - 10))

            if rotation_angle > 0:
                # Adjust rotation and placement based on chart position/type
                chart_id = chart_data.get('id', '')
                is_parent = 'children' in chart_data and chart_data['children']
                is_top_row = 'row_0' == chart_id or chart_id.startswith('row_0_')
                
                # For parent charts or top row charts, optimize tick display
                if is_parent or is_top_row:
                    rotation_angle = min(45, rotation_angle)  # Cap rotation at 45 degrees
                    
                    ax.set_xticklabels(x_display_labels, rotation=rotation_angle, 
                                    ha='right' if rotation_angle > 0 else 'center',
                                    fontsize=7)
                    ax.tick_params(axis='x', pad=2)
                else:
                    ax.set_xticklabels(x_display_labels, rotation=rotation_angle, 
                                    ha='right' if rotation_angle < 60 else 'center',
                                    fontsize=7)
                    ax.tick_params(axis='x', pad=4)
            else:
                ax.set_xticklabels(x_display_labels)

    # For stacked bar charts, add a total value at the top/end of each stack
    if is_stacked:
        # Calculate totals for each position
        totals = np.zeros(len(positions))
        for series in data:
            if 'yData' in series:
                for i, val in enumerate(series['yData']):
                    totals[i] += val
        
        # Add total annotations
        for i, total in enumerate(totals):
            if is_horizontal:
                # For horizontal stacked bars
                ax.text(total * 1.02, positions[i], 
                        format_large_number(total),
                        ha='left', va='center', fontsize=10, fontweight='bold')
            else:
                # For vertical stacked bars
                ax.text(positions[i], total * 1.02, 
                        format_large_number(total),
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Determine best legend location
    if is_stacked:
        # For stacked charts, generally best to put legend at bottom
        legend_loc = 'upper center' if is_horizontal else 'upper right'
        ncol = min(3, len(data))  # More columns for stacked legend
    else:
        # For regular bar charts, determine based on data distribution
        y_data_all = [series.get('yData', []) for series in data if 'yData' in series]
        
        if y_data_all:
            all_values = []
            for yd in y_data_all:
                all_values.extend(yd)

            if not all_values:
                legend_loc = 'best'
            else:
                # Find where there's the least data
                max_val = max(all_values) if all_values else 0
                min_val = min(all_values) if all_values else 0
                mid_val = (max_val + min_val) / 2

                # Calculate average values in top/right and bottom/left halves
                high_values = [v for v in all_values if v > mid_val]
                low_values = [v for v in all_values if v <= mid_val]

                high_density = len(high_values) / len(all_values) if all_values else 0.5

                # Choose location based on data density and chart orientation
                if is_horizontal:
                    if high_density > 0.6:  # More data in right half
                        legend_loc = 'upper left'
                    elif high_density < 0.4:  # More data in left half
                        legend_loc = 'upper right'
                    else:
                        legend_loc = 'best'
                else:
                    if high_density > 0.6:  # More data in top half
                        legend_loc = 'lower right'
                    elif high_density < 0.4:  # More data in bottom half
                        legend_loc = 'upper right'
                    else:
                        legend_loc = 'best'
        else:
            legend_loc = 'best'
            
        ncol = min(2, len(data))  # Fewer columns for regular legends

    # Create a clean, modern legend
    legend = ax.legend(loc=legend_loc, fontsize=9, frameon=True, framealpha=0.9, 
                    edgecolor='#dddddd', facecolor='white', 
                    title_fontsize=10, ncol=ncol)
    
    # Add thin borders to improve legend appearance
    legend.get_frame().set_linewidth(0.8)

def plot_pie(ax, chart_props):
    """
    Plot a pie chart with the given data.
    
    Parameters:
    ax: Matplotlib axis
    chart_props: Chart properties from the structure
    """
    # Find pie data
    pie_data = None
    for item in chart_props.get('data', []):
        if item.get('type') == 'pie' and 'data' in item:
            pie_data = item['data']
            break

    if pie_data:
        # Extract non-zero wedges
        labels = []
        sizes = []

        for item in pie_data:
            size = item.get('wedgeSize', 0)
            if size > 0:  # Only include non-zero wedges
                labels.append(item.get('label', ''))
                sizes.append(size)

        if sizes:
            # Create a modern color palette for pie charts
            pie_palette = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', '#FF9DA7']
            
            # Create pie chart with clean, modern styling
            wedges, texts, autotexts = ax.pie(
                sizes,
                labels=labels,
                autopct='%1.1f%%',
                startangle=90,
                colors=pie_palette,
                textprops={'fontsize': 9, 'fontweight': 'bold', 'color': '#2F4F4F'},
                wedgeprops={'edgecolor': 'white', 'linewidth': 1.5, 'antialiased': True},
                shadow=False,  # Cleaner look without shadow
            )

            # Make percentage text bold and white for better visibility
            for autotext in autotexts:
                autotext.set_fontweight('bold')
                autotext.set_color('white')
                autotext.set_fontsize(10)
            
            ax.axis('equal')  # Equal aspect ratio ensures circular pie
            ax.set_xlabel('') # Remove x-axis label.
            ax.set_ylabel('') # Remove y-axis label.
            ax.set_xticks([]) # Remove x-axis ticks.
            ax.set_yticks([]) # Remove y-axis ticks.
        else:
            ax.text(0.5, 0.5, "No non-zero values for pie chart",
                    ha='center', va='center')
    else:
        ax.text(0.5, 0.5, "No pie data found", ha='center', va='center')
        ax.set_xlabel('') # Remove x-axis label.
        ax.set_ylabel('') # Remove y-axis label.
        ax.set_xticks([]) # Remove x-axis ticks.
        ax.set_yticks([]) # Remove y-axis ticks.

def plot_line(ax, chart_props, chart_data):
    """
    Plot a line chart using the given chart properties and data.
    Supports single and multiple line series with customizable styling.
    
    Parameters:
    ax: Matplotlib axis
    chart_props: Chart properties dict
    chart_data: Full chart data, used for context like ID or positioning
    """
    data = chart_props.get('data', [])
    if not data:
        ax.text(0.5, 0.5, "No line data found", ha='center', va='center')
        return

    # Check if this is a multi-line chart
    is_multi_line = len(data) > 1 or chart_props.get('chartId', '').find('multi_line') >= 0

    # Format axes based on types
    formatted_x_data, x_formatter = format_axis_based_on_type(ax, chart_props, axis='x')
    formatted_y_data, y_formatter = format_axis_based_on_type(ax, chart_props, axis='y')

    if not formatted_x_data:
        ax.text(0.5, 0.5, "No x-axis data found", ha='center', va='center')
        return

    # Create enhanced color palette for multi-line charts
    color_palette = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', 
                     '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC']
    
    # Handle x-ticks with improved readability
    x_axis_type = chart_props.get('xAxisType', 'categorical')
    if x_axis_type != 'datetime':
        ax.set_xticks(range(len(formatted_x_data)))
        
        # Get label length to determine rotation
        x_display_labels = [str(x) for x in formatted_x_data]
        max_label_len = max([len(str(x)) for x in x_display_labels])
        n_labels = len(x_display_labels)
        
        # Dynamic rotation angle
        rotation_angle = min(45, max(0, max_label_len * 2 + n_labels * 2 - 8))
        
        # Apply rotation and styling
        ax.set_xticklabels(x_display_labels, 
                         rotation=rotation_angle, 
                         ha='right' if rotation_angle > 0 else 'center', 
                         fontsize=8)

    # Track all y values for marker placement and scaling
    all_y_values = []
    
    # Plot each line series
    for i, series in enumerate(data):
        x_vals = formatted_x_data
        y_vals = series.get('yData', [])
        if not y_vals:
            continue
            
        all_y_values.extend(y_vals)

        # Get line properties with defaults for better visualization
        name = series.get('name', f'Series {i+1}')
        color = series.get('color', color_palette[i % len(color_palette)])
        linestyle = series.get('lineStyle', '-')
        linewidth = series.get('lineWidth', 2.0 if is_multi_line else 2.5)  # Thinner for multi-line
        
        # For non-datetime x-axis, use numeric positions
        if x_axis_type != 'datetime':
            x_vals = range(len(formatted_x_data))

        # Plot the line with enhanced styling
        line = ax.plot(x_vals, y_vals, label=name, color=color,
                linestyle=linestyle, linewidth=linewidth)
        
        # Add markers based on chart type and number of data points
        marker_size = 8 if is_multi_line else 10
        marker_type = 'o'  # Default marker type
        
        # Choose marker frequency based on data density
        if len(y_vals) > 10:
            # For dense data, only mark key points
            local_max_indices = [i for i in range(1, len(y_vals)-1) if y_vals[i] > y_vals[i-1] and y_vals[i] > y_vals[i+1]]
            local_min_indices = [i for i in range(1, len(y_vals)-1) if y_vals[i] < y_vals[i-1] and y_vals[i] < y_vals[i+1]]
            marker_indices = sorted(local_max_indices + local_min_indices + [0, len(y_vals)-1])
            
            # Plot markers only at these points
            marker_x = [x_vals[j] for j in marker_indices]
            marker_y = [y_vals[j] for j in marker_indices]
            ax.scatter(marker_x, marker_y, color=color, s=marker_size, zorder=10, marker=marker_type)
        else:
            # For less dense data, mark all points
            ax.scatter(x_vals, y_vals, color=color, s=marker_size, zorder=10, marker=marker_type)
        
        # For multi-line charts with few points, add value labels
        if is_multi_line and len(y_vals) <= 7:
            for x, y in zip(x_vals, y_vals):
                # Position labels slightly above points
                ax.annotate(format_large_number(y), 
                          (x, y), 
                          textcoords="offset points",
                          xytext=(0, 7),
                          ha='center',
                          fontsize=8,
                          color=color,
                          weight='bold')

    # Determine best legend location based on data distribution
    if all_y_values:
        max_y = max(all_y_values)
        min_y = min(all_y_values)
        mid_y = (max_y + min_y) / 2
        
        top_values = [y for y in all_y_values if y > mid_y]
        top_density = len(top_values) / len(all_y_values)
        
        # Choose legend position based on data density
        if top_density > 0.6:  # More data points in top half
            legend_loc = 'lower right'
        elif top_density < 0.4:  # More data points in bottom half
            legend_loc = 'upper right'
        else:
            # Check left/right distribution for center-heavy data
            x_mid = len(formatted_x_data) // 2
            right_values = []
            for series in data:
                y_data = series.get('yData', [])
                if len(y_data) > x_mid:
                    right_values.extend(y_data[x_mid:])
            
            right_density = len(right_values) / len(all_y_values) if all_y_values else 0.5
            
            if right_density > 0.6:  # More data on right side
                legend_loc = 'upper left'
            else:
                legend_loc = 'upper right'
    else:
        legend_loc = 'best'

    # Determine number of legend columns based on number of lines
    if is_multi_line and len(data) > 3:
        ncol = min(3, len(data))  # More columns for many lines
    else:
        ncol = 1  # Single column for few lines
    
    # Add grid for better readability in multi-line charts
    if is_multi_line:
        ax.grid(True, linestyle='--', alpha=0.7, color='#cccccc')
        
        # Set a slightly expanded y-axis limit for better visualization
        if all_y_values:
            y_range = max(all_y_values) - min(all_y_values)
            ax.set_ylim(min(all_y_values) - y_range * 0.05, max(all_y_values) + y_range * 0.1)

    # Final legend styling
    legend = ax.legend(loc=legend_loc, fontsize=9, frameon=True, framealpha=0.9,
                       edgecolor='#dddddd', facecolor='white',
                       title_fontsize=10, ncol=ncol)
    legend.get_frame().set_linewidth(0.8)

def plot_scatter(ax, chart_props, chart_data):
    """
    Plot a scatter chart using the given chart properties and data.
    
    Parameters:
    ax: Matplotlib axis
    chart_props: Chart properties dict
    chart_data: Full chart data, used for ID and context
    """
    data = chart_props.get('data', [])
    if not data:
        ax.text(0.5, 0.5, "No scatter data found", ha='center', va='center')
        return

    # Format axes based on types
    formatted_x_data, x_formatter = format_axis_based_on_type(ax, chart_props, axis='x')
    formatted_y_data, y_formatter = format_axis_based_on_type(ax, chart_props, axis='y')

    if not formatted_x_data or not formatted_y_data:
        ax.text(0.5, 0.5, "Missing x or y data", ha='center', va='center')
        return

    for series in data:
        x_vals = formatted_x_data
        y_vals = series.get('yData', [])
        if not y_vals:
            continue

        # Scatter style
        color = series.get('color', '#4E79A7')
        marker = series.get('marker', 'o')
        size = series.get('size', 40)
        alpha = series.get('alpha', 0.9)
        name = series.get('name', 'Series')

        # If x isn't datetime, map range instead of values
        x_axis_type = chart_props.get('xAxisType', 'categorical')
        if x_axis_type != 'datetime':
            x_vals = range(len(formatted_x_data))

        # Adjust size to matplotlib's units (square of point size)
        ax.scatter(x_vals, y_vals, label=name, color=color, alpha=alpha,
                   s=size**2, marker=marker, edgecolors='white', linewidths=0.5)

    # Dynamic legend placement
    all_y = [y for series in data for y in series.get('yData', []) if y is not None]
    if all_y:
        mid_y = (max(all_y) + min(all_y)) / 2
        top_density = len([y for y in all_y if y > mid_y]) / len(all_y)
        legend_loc = 'lower right' if top_density > 0.6 else 'upper right' if top_density < 0.4 else 'best'
    else:
        legend_loc = 'best'

    legend = ax.legend(loc=legend_loc, fontsize=9, frameon=True, framealpha=0.9,
                       edgecolor='#dddddd', facecolor='white',
                       title_fontsize=10, ncol=min(2, len(data)))
    legend.get_frame().set_linewidth(0.8)

def plot_box(ax, chart_props, chart_data):
    """
    Plot a box and whisker chart with the given data.
    
    Parameters:
    ax: Matplotlib axis
    chart_props: Chart properties from the structure
    chart_data: Full chart data (for positioning info)
    """
    data = chart_props.get('data', [])
    print("inside box")
    if not data:
        ax.text(0.5, 0.5, "No box plot data found", ha='center', va='center')
        return

    # Get category labels (x-axis)
    x_labels = []
    for series in data:
        if 'xData' in series:
            x_labels = series['xData']
            break
    
    if not x_labels:
        ax.text(0.5, 0.5, "No category labels found", ha='center', va='center')
        return

    # Create a color palette for boxes
    color_palette = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC']
    
    # Collect data for each category
    all_distributions = []
    for series in data:
        if 'yData' not in series:
            continue
            
        # For box plots, yData contains the distribution data for each category
        y_data = series.get('yData', [])
        
        # Extract the actual numeric data from each category
        for category_data in y_data:
            if 'data' in category_data:
                all_distributions.append(category_data['data'])
    
    if not all_distributions:
        ax.text(0.5, 0.5, "No distribution data found", ha='center', va='center')
        return
    
    # Set up positions for the boxes
    positions = range(1, len(all_distributions) + 1)
    
    # Get series properties
    series_props = data[0] if data else {}
    series_color = series_props.get('color', color_palette[0])
    series_name = series_props.get('name', 'Distribution')
    
    # Prepare box plot settings
    box_props = dict(
        boxprops=dict(facecolor=series_color, alpha=0.7, linewidth=1.5),
        medianprops=dict(color='#333333', linewidth=2),
        whiskerprops=dict(linewidth=1.5),
        capprops=dict(linewidth=1.5),
        flierprops=dict(marker='o', markerfacecolor=series_color, markersize=5, 
                        alpha=0.7, markeredgecolor='none'),
        patch_artist=True,
        showmeans=True,
        meanprops=dict(marker='D', markerfacecolor='white', 
                       markeredgecolor=series_color, markersize=7)
    )
    
    # Create the box plot
    bp = ax.boxplot(all_distributions, positions=positions, widths=0.7, 
                   vert=True, **box_props)
    
    # Add a subtle grid for readability
    ax.grid(True, linestyle='--', alpha=0.3, axis='y')
    
    # Set x-ticks and labels
    ax.set_xticks(positions)
    
    # Handle category label rotation based on length
    max_label_len = max([len(str(x)) for x in x_labels])
    rotation_angle = min(45, max(0, max_label_len * 3 - 10))
    
    ax.set_xticklabels(x_labels, rotation=rotation_angle, 
                      ha='right' if rotation_angle > 0 else 'center')
    
    # Calculate and display key statistics for each distribution
    for i, (pos, dist) in enumerate(zip(positions, all_distributions)):
        if not dist:
            continue
            
        # Calculate key statistics
        q1 = np.percentile(dist, 25)
        median = np.percentile(dist, 50)
        q3 = np.percentile(dist, 75)
        mean = np.mean(dist)
        
        # Formatted values
        median_str = f"{median:.1f}"
        mean_str = f"{mean:.1f}"
        
        # Label median at the center of the box
        ax.text(pos, median, median_str, ha='center', va='bottom',
               fontsize=9, fontweight='bold', color='white')
        
        # Label mean with a marker
        text_color = '#333333'
        ax.text(pos + 0.25, mean, mean_str, ha='left', va='center',
               fontsize=8, fontweight='bold', color=text_color)
    
    # Add a light background to the plot for better aesthetics
    ax.set_facecolor('#f8f8f8')
    
    # Calculate appropriate y-axis limits
    all_values = [val for dist in all_distributions for val in dist]
    if all_values:
        min_val = min(all_values)
        max_val = max(all_values)
        range_val = max_val - min_val
        
        # Set y-axis limits with some padding
        ax.set_ylim(min_val - range_val * 0.05, max_val + range_val * 0.05)
    
    # Add a subtle title for the y-axis to explain the values
    y_axis_label = chart_props.get('yAxisLabel', 'Distribution')
    ax.set_ylabel(y_axis_label, fontsize=10)
    
    # Improve x-axis appearance
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add summary statistics as a legend
    # Calculate summary statistics for the legend
    legend_text = ""
    for i, (label, dist) in enumerate(zip(x_labels, all_distributions)):
        if not dist:
            continue
            
        q1 = np.percentile(dist, 25)
        q3 = np.percentile(dist, 75)
        iqr = q3 - q1
        
        # Add to legend text
        if i < len(x_labels) - 1:
            legend_text += f"{label}: IQR={iqr:.1f}, "
        else:
            legend_text += f"{label}: IQR={iqr:.1f}"
    
    # Add a text box with summary statistics if needed
    if len(x_labels) <= 6:  # Only add if we have a reasonable number of categories
        summary_props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9)
        ax.text(0.95, 0.05, legend_text, transform=ax.transAxes, fontsize=8,
               verticalalignment='bottom', horizontalalignment='right',
               bbox=summary_props)
        
def plot_html(ax, chart_props, chart_data):
    """
    Plot HTML content as plain text on a matplotlib axis, stripping HTML tags.
    
    Parameters:
    ax: Matplotlib axis
    chart_props: Chart properties from the structure
    chart_data: Full chart data (for positioning info)
    """
    data = chart_props.get('data', [])

    if not data:
        ax.text(0.5, 0.5, "No HTML data found", ha='center', va='center')
        return
    
    # Extract HTML content
    html_content = ""
    for item in data:
        if item.get('type') == 'html' and 'htmlText' in item:
            html_content = item['htmlText']
            break
    
    if not html_content:
        ax.text(0.5, 0.5, "No HTML text found", ha='center', va='center')
        return
    
    # Extract text content from HTML
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text(separator="\n", strip=True)
    except ImportError:
        # Simple fallback HTML tag removal if BeautifulSoup is not available
        import re
        text_content = re.sub(r'<[^>]*>', ' ', html_content)
        text_content = re.sub(r'\s+', ' ', text_content).strip()
        
        # Split into lines for better readability
        words = text_content.split()
        lines = []
        current_line = []
        line_length = 0
        
        # Create lines with sensible word wrapping
        max_line_length = 50  # Characters per line
        for word in words:
            if line_length + len(word) + 1 > max_line_length:
                lines.append(' '.join(current_line))
                current_line = [word]
                line_length = len(word)
            else:
                current_line.append(word)
                line_length += len(word) + 1
        
        if current_line:
            lines.append(' '.join(current_line))
        
        text_content = '\n'.join(lines)
    
   
    
    # Remove axis elements for cleaner appearance
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Add the title if available
    title = chart_props.get('title', None)
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    
    # Display the extracted text
    ax.text(0.05, 0.95, text_content,
            transform=ax.transAxes,
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='left',
            linespacing=1.5,
            family='sans-serif')


def plot_histogram(ax, chart_props, chart_data):
    """
    Plot a histogram with the given data.
    
    Parameters:
    ax: Matplotlib axis
    chart_props: Chart properties from the structure
    chart_data: Full chart data (for positioning info)
    """
    data = chart_props.get('data', [])

    if not data:
        ax.text(0.5, 0.5, "No histogram data found", ha='center', va='center')
        return

    # For histogram, we expect the data to include values rather than x and y coordinates
    values = []
    bin_width = 10  # Default bin width
    hist_color = '#4E79A7'  # Default color
    
    for series in data:
        # Histogram may store values in different ways
        if 'yData' in series:
            if isinstance(series['yData'], list):
                values = series['yData']
            
        # Or it might be stored directly in 'values'
        if 'values' in series:
            values = series['values']
            
        # Get histogram properties
        if 'binwidth' in series:
            bin_width = series['binwidth']
            
        if 'color' in series:
            hist_color = series['color']
        elif 'c' in series:
            hist_color = series['c']
    
    if not values:
        ax.text(0.5, 0.5, "No histogram values found", ha='center', va='center')
        return
    
    # Convert values to numpy array if they aren't already
    if not isinstance(values, np.ndarray):
        values = np.array(values)
    
    # Calculate appropriate bins based on bin width
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    
    # If bin width is specified, use it to determine number of bins
    if bin_width:
        num_bins = max(1, int(range_val / bin_width))
        bins = np.linspace(min_val - (min_val % bin_width), 
                          max_val + bin_width - (max_val % bin_width), 
                          num_bins + 1)
    else:
        # Default to Sturges' formula for number of bins
        num_bins = int(np.ceil(np.log2(len(values)) + 1))
        bins = num_bins
    
    # Plot the histogram
    n, bins, patches = ax.hist(values, bins=bins, color=hist_color, 
                              alpha=0.7, edgecolor='white', linewidth=1)
    
    # Calculate and plot a kernel density estimate (KDE) if we have enough data points
    if len(values) >= 20:
        try:
            # Calculate KDE
            from scipy import stats
            kde_x = np.linspace(min_val - 0.1 * range_val, max_val + 0.1 * range_val, 1000)
            kde = stats.gaussian_kde(values)
            kde_y = kde(kde_x)
            
            # Scale the KDE to match histogram height
            scale_factor = max(n) / max(kde_y) if max(kde_y) > 0 else 1
            kde_y_scaled = kde_y * scale_factor
            
            # Plot KDE as a smooth curve
            ax.plot(kde_x, kde_y_scaled, 'r-', linewidth=2, alpha=0.7)
            
            # Add a second y-axis for the density
            ax2 = ax.twinx()
            max_density = max(kde_y)
            ax2.set_ylim(0, max_density * 1.1)
            ax2.set_ylabel('Density', color='r')
            ax2.tick_params(axis='y', colors='r')
        except:
            # If KDE fails, just continue without it
            pass
    
    # Add grid for readability
    ax.grid(True, linestyle='--', alpha=0.3, axis='y')
    
    # Calculate and display summary statistics
    mean_val = np.mean(values)
    median_val = np.median(values)
    std_val = np.std(values)
    
    # Add a vertical line for the mean
    ax.axvline(mean_val, color='#E15759', linestyle='-', linewidth=2, alpha=0.7)
    ax.text(mean_val, max(n) * 0.95, f'Mean: {mean_val:.1f}',
           ha='center', va='top', fontsize=9, fontweight='bold',
           bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.3'))
    
    # Add a vertical line for the median if it's meaningfully different from mean
    if abs(median_val - mean_val) > range_val * 0.01:
        ax.axvline(median_val, color='#59A14F', linestyle='--', linewidth=2, alpha=0.7)
        ax.text(median_val, max(n) * 0.85, f'Median: {median_val:.1f}',
               ha='center', va='top', fontsize=9, fontweight='bold',
               bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.3'))
    
    # Improve the appearance of the histogram
    ax.set_xlabel(chart_props.get('xAxisLabel', 'Values'))
    ax.set_ylabel(chart_props.get('yAxisLabel', 'Frequency'))
    
    # Set x-axis limits with a bit of padding
    pad = range_val * 0.05
    ax.set_xlim(min_val - pad, max_val + pad)
    
    # Add a light background
    ax.set_facecolor('#f8f8f8')
    
    # Enhance spines
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add a text box with distribution statistics
    stats_text = (f"n = {len(values)}\n"
                 f"Mean = {mean_val:.1f}\n"
                 f"Std Dev = {std_val:.1f}\n"
                 f"Min = {min(values):.1f}\n"
                 f"Max = {max(values):.1f}")
                 
    stats_props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9)
    ax.text(0.95, 0.95, stats_text, transform=ax.transAxes, fontsize=8,
           verticalalignment='top', horizontalalignment='right',
           bbox=stats_props)

######################################################################################################
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import re
import json
import numpy as np
import matplotlib.ticker as mticker
import textwrap


def create_grid_from_structure(structure, debug=False):
    """
    Creates a matplotlib grid based on the nested structure.
    Layout is determined intelligently based on the element type and child ID patterns.

    IMPORTANT:
    - Rows in the output are plotted horizontally (side by side)
    - Columns in the output are plotted vertically (stacked)
    """
    if debug:
        print("Creating grid from structure...")

    # Create the figure with explicit figsize to control proportions
    # Using a taller figure helps separate the charts vertically
    fig = plt.figure(figsize=(16, 14))  # Made taller to provide more vertical space
    
    # Set a clean, modern style
    plt.style.use('ggplot')
    
    # Override some style elements for a cleaner look
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
    plt.rcParams['axes.facecolor'] = '#f9f9f9'
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['grid.color'] = '#dddddd'
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.edgecolor'] = '#cccccc'
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['xtick.color'] = '#555555'
    plt.rcParams['ytick.color'] = '#555555'
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.linewidth'] = 0.8
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False

    # Calculate the number of rows and columns in the main grid
    has_rows = 'rows' in structure and 'children' in structure['rows']
    has_columns = 'columns' in structure and 'children' in structure['columns']

    if debug:
        print(f"Has rows: {has_rows}, Has columns: {has_columns}")

    # Initialize the axes dictionary
    axes_dict = {}

    # Get the main ratio for splitting the figure
    main_ratios = structure.get('main', {}).get('ratio', [1, 1])
    
    # Create the gridspec with proper spacing
    # Using a larger wspace value to separate adjacent plots horizontally
    fig.subplots_adjust(wspace=0.4, hspace=0.6)

    # For a grid layout, split the figure into top/bottom and left/right based on main ratio
    if has_rows and has_columns:
        # Create a 2x1 grid for the main split (rows on top, columns on bottom)
        # Add very large space between main sections to prevent overlap
        main_gs = gridspec.GridSpec(2, 1, height_ratios=[0.45, 0.55], figure=fig, hspace=0.6)

        # Process rows in the top section
        if debug:
            print(f"Processing rows with ratios: {structure['rows']['ratio']}")

        row_ratios = structure['rows']['ratio']
        # MODIFIED: Main level rows are horizontal (side by side)
        rows_gs = gridspec.GridSpecFromSubplotSpec(1, len(row_ratios),
                                                subplot_spec=main_gs[0, 0],
                                                width_ratios=row_ratios,
                                                wspace=0.25)  # Added wspace

        # Process each row child - now horizontally
        for i, child in enumerate(structure['rows']['children']):
            process_element(fig, child, rows_gs[0, i], axes_dict, debug=debug)

        # Process columns in the bottom section
        if debug:
            print(f"Processing columns with ratios: {structure['columns']['ratio']}")

        col_ratios = structure['columns']['ratio']
        # MODIFIED: Main level columns are vertical (stacked)
        cols_gs = gridspec.GridSpecFromSubplotSpec(len(col_ratios), 1,
                                                subplot_spec=main_gs[1, 0],
                                                height_ratios=col_ratios,
                                                hspace=0.6)  # Added hspace

        # Process each column child - now vertically
        for i, child in enumerate(structure['columns']['children']):
            process_element(fig, child, cols_gs[i, 0], axes_dict, debug=debug)

    # Handle rows-only layout
    elif has_rows:
        if debug:
            print(f"Processing rows-only layout with ratios: {structure['rows']['ratio']}")

        # Process row children recursively
        ratios = structure['rows']['ratio']
        # MODIFIED: Main level rows are horizontal (side by side)
        gs = gridspec.GridSpec(1, len(ratios), width_ratios=ratios, figure=fig, wspace=0.25)

        for i, child in enumerate(structure['rows']['children']):
            process_element(fig, child, gs[0, i], axes_dict, debug=debug)

    # Handle columns-only layout
    elif has_columns:
        if debug:
            print(f"Processing columns-only layout with ratios: {structure['columns']['ratio']}")

        # Process column children recursively
        ratios = structure['columns']['ratio']
        # MODIFIED: Main level columns are vertical (stacked)
        gs = gridspec.GridSpec(len(ratios), 1, height_ratios=ratios, figure=fig, hspace=0.4)

        for i, child in enumerate(structure['columns']['children']):
            process_element(fig, child, gs[i, 0], axes_dict, debug=debug)

    # Add a default axis if no charts were found
    if not axes_dict:
        ax = fig.add_subplot(111)
        ax.text(0.5, 0.5, "No charts found in structure", ha='center', va='center', fontsize=14)
        ax.axis('off')

    # Don't use tight_layout as requested
    # Apply targeted axis adjustments based on the chart structure
    for ax in fig.get_axes():
        # Get the position of the axes in figure coordinates
        pos = ax.get_position()
        
        # Check chart ID and type for specific adjustments
        chart_id = ax.get_title()
        
        # Check if this is a parent chart at the top
        if 'row_0' == str(chart_id) or 'row_0 ' in str(chart_id):
            # For parent charts, make them slightly shorter to create space below
            # but not too extreme to avoid excessive spacing
            ax.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
            
            # For parent chart, we can also modify tick parameters
            ax.tick_params(axis='x', labelsize=7, pad=2)
            
        # For row charts that are children of the parent
        elif '_row' in str(chart_id):
            row_number = 0
            try:
                # Extract row number from ID (e.g., "row_0_row1" → 1)
                parts = str(chart_id).split('_row')
                if len(parts) > 1 and parts[1].isdigit():
                    row_number = int(parts[1])
            except:
                pass
                
            if row_number == 0:
                # First row under parent - subtle adjustment
                ax.set_position([pos.x0, pos.y0 + 0.01, pos.width, pos.height])
            elif row_number == 1:
                # Middle row - no special adjustment needed
                pass
            elif row_number == 2:
                # Last row - normal position
                pass

    return fig, axes_dict

def determine_layout_orientation(element, children, debug=False):
    """
    Determine the layout orientation based on element type and children IDs.
    IMPORTANT: For this specific application:
    - Rows in the output should be plotted as columns in matplotlib (stacked vertically)
    - Columns in the output should be plotted as rows in matplotlib (side by side horizontally)

    Returns:
        str: Either "horizontal" or "vertical"
    """
    element_id = element.get('id', '')
    element_type = element.get('type', '')

    # Check if we have child IDs that can give us a hint
    row_pattern = re.compile(r'_row\d+$')
    col_pattern = re.compile(r'_col\d+$')

    row_children = [c for c in children if row_pattern.search(c.get('id', ''))]
    col_children = [c for c in children if col_pattern.search(c.get('id', ''))]

    if debug:
        print(f"  Element {element_id} has {len(row_children)} row children and {len(col_children)} col children")

    # Look at the container name for hints
    container_is_row = "row" in element_id.lower() and "col" not in element_id.lower()
    container_is_col = "col" in element_id.lower() and "row" not in element_id.lower()

    # CHANGED LOGIC: If children have row in their IDs, they should be horizontal (side by side)
    # but if the parent is a "row" type, we want to stack them vertically
    if row_children and not col_children:
        if debug:
            print(f"  Children have row IDs, using horizontal layout")
        return "horizontal"

    # If children have col in their IDs, they should be vertical (stacked)
    elif col_children and not row_children:
        if debug:
            print(f"  Children have col IDs, using vertical layout")
        return "vertical"

    # MODIFIED: If it's explicitly a row container, use vertical layout for children
    # This is the key change - rows in output should be plotted as columns in matplotlib
    elif element_type == 'row':
        if debug:
            print(f"  Element is row type, using vertical layout instead of horizontal")
        return "vertical"  # Changed from "horizontal" to "vertical"

    # If it's explicitly a column container, use horizontal layout for children
    elif element_type == 'col':
        if debug:
            print(f"  Element is col type, using horizontal layout")
        return "horizontal"  # Changed from "vertical" to "horizontal"

    # Last resort: look at container name
    elif container_is_row:
        if debug:
            print(f"  Container name suggests row, using vertical layout")
        return "vertical"  # Changed from "horizontal" to "vertical"

    elif container_is_col:
        if debug:
            print(f"  Container name suggests column, using horizontal layout")
        return "horizontal"  # Changed from "vertical" to "horizontal"

    # Default fallback
    if debug:
        print(f"  No clear pattern, defaulting to horizontal layout")
    return "horizontal"

def process_element(fig, element, subplot_spec, axes_dict, level=0, debug=False):
    """
    Process an element in the structure (row, column, or chart).

    Parameters:
    fig: Matplotlib figure
    element: The element to process
    subplot_spec: Subplot specification for this element
    axes_dict: Dictionary to store chart axes
    level: Current nesting level
    debug: Whether to show debug information
    """
    if not element or 'type' not in element:
        return

    indent = "  " * level
    element_id = element.get('id', f"unknown_{level}")
    element_type = element.get('type')

    if debug:
        print(f"{indent}Processing {element_type}: {element_id} at level {level}")
        
    # Detect whether this is the specific row_0 chart (parent chart with nested children)
    is_parent_chart = element_id == 'row_0' and element_type == 'chart' and 'children' in element
    has_row_children = 'children' in element and any('_row' in child.get('id', '') for child in element['children'])

    # Check if this is a chart without children (leaf chart)
    if element_type == 'chart' and ('children' not in element or not element['children']):
        # For charts without children, create an axis in the specified subplot position
        if debug:
            print(f"{indent}Creating chart axis for: {element_id}")

        ax = fig.add_subplot(subplot_spec)
        axes_dict[element_id] = ax

        # Add debug info if needed
        if debug:
            ax.set_title(f"{element_id}\n{element_type}", pad=15)
            ax.grid(True)

        return

    # For chart containers (charts with children), handle differently
    if element_type == 'chart' and 'children' in element and element['children']:
        if debug:
            print(f"{indent}Processing chart container: {element_id} with {len(element['children'])} children")

        # Create a composite layout that includes the parent chart at the top
        # Parent gets 30% height, children get 70% height
        # Use moderate spacing between parent and children charts
        parent_height_ratio = 0.3  # Back to standard ratio
        children_height_ratio = 0.7
        composite_gs = gridspec.GridSpecFromSubplotSpec(2, 1,
                                                        subplot_spec=subplot_spec,
                                                        height_ratios=[parent_height_ratio, children_height_ratio],
                                                        hspace=0.35)  # Moderate hspace

        # Create an axis for the parent chart at the top
        parent_ax = fig.add_subplot(composite_gs[0, 0])
        axes_dict[element_id] = parent_ax

        if debug:
            print(f"{indent}Created parent chart axis: {element_id}")

        # Check for the presence of both rowRatio and colRatio
        has_row_ratio = 'rowRatio' in element
        has_col_ratio = 'colRatio' in element

        # Create a grid in the lower section for all the children
        children_gs = composite_gs[1, 0]

        if has_row_ratio and has_col_ratio:
            # This chart container has both row and column children
            if debug:
                print(f"{indent}Chart container has both row and column children")
                print(f"{indent}Row ratios: {element['rowRatio']}")
                print(f"{indent}Column ratios: {element['colRatio']}")

            # Sort children by their ID to ensure proper ordering
            sorted_children = sorted(element['children'], key=lambda x: x['id'])

            # Group children by type (row or col prefix in ID)
            row_children = [child for child in sorted_children if '_row' in child['id']]
            col_children = [child for child in sorted_children if '_col' in child['id']]

            if debug:
                print(f"{indent}Found {len(row_children)} row children and {len(col_children)} column children")

            # Create a complex grid with both rows and columns
            # First, create a 2-row grid to separate rows and columns
            children_composite_gs = gridspec.GridSpecFromSubplotSpec(2, 1,
                                                                    subplot_spec=children_gs,
                                                                    height_ratios=[0.7, 0.3],
                                                                    hspace=0.3)  # Added hspace

            # Create row grid in the top section
            if row_children:
                row_ratios = element['rowRatio']
                row_orientation = determine_layout_orientation(element, row_children, debug)

                if row_orientation == "horizontal":
                    # Row children side by side - increased spacing
                    row_gs = gridspec.GridSpecFromSubplotSpec(1, len(row_ratios),
                                                            subplot_spec=children_composite_gs[0, 0],
                                                            width_ratios=row_ratios,
                                                            wspace=0.4)  # Increased spacing

                    # Process row children horizontally
                    for i, child in enumerate(row_children):
                        if i < len(row_ratios):
                            process_element(fig, child, row_gs[0, i], axes_dict, level+1, debug)
                else:
                    # Row children stacked
                    row_gs = gridspec.GridSpecFromSubplotSpec(len(row_ratios), 1,
                                                            subplot_spec=children_composite_gs[0, 0],
                                                            height_ratios=row_ratios,
                                                            hspace=0.4)  # Added hspace

                    # Process row children vertically
                    for i, child in enumerate(row_children):
                        if i < len(row_ratios):
                            process_element(fig, child, row_gs[i, 0], axes_dict, level+1, debug)

            # Create column grid in the bottom section
            if col_children:
                col_ratios = element['colRatio']
                col_orientation = determine_layout_orientation(element, col_children, debug)

                if col_orientation == "horizontal":
                    # Column children side by side - increased spacing
                    col_gs = gridspec.GridSpecFromSubplotSpec(1, len(col_ratios),
                                                            subplot_spec=children_composite_gs[1, 0],
                                                            width_ratios=col_ratios,
                                                            wspace=0.4)  # Increased spacing

                    # Process column children horizontally
                    for i, child in enumerate(col_children):
                        if i < len(col_ratios):
                            process_element(fig, child, col_gs[0, i], axes_dict, level+1, debug)
                else:
                    # Column children stacked
                    col_gs = gridspec.GridSpecFromSubplotSpec(len(col_ratios), 1,
                                                            subplot_spec=children_composite_gs[1, 0],
                                                            height_ratios=col_ratios,
                                                            hspace=0.4)  # Added hspace

                    # Process column children vertically
                    for i, child in enumerate(col_children):
                        if i < len(col_ratios):
                            process_element(fig, child, col_gs[i, 0], axes_dict, level+1, debug)

        # Handle row children only
        elif has_row_ratio:
            ratios = element['rowRatio']
            # Sort row children by ID for proper ordering
            row_children = sorted(
                [child for child in element['children'] if '_row' in child['id']],
                key=lambda x: x['id']
            )

            # Determine orientation based on child IDs and container type
            orientation = determine_layout_orientation(element, row_children, debug)

            if debug:
                print(f"{indent}Using {orientation} layout for row children with ratios: {ratios}")

            if orientation == "horizontal":
                # Row children side by side - increased spacing
                gs = gridspec.GridSpecFromSubplotSpec(1, len(ratios),
                                                    subplot_spec=children_gs,
                                                    width_ratios=ratios,
                                                    wspace=0.4)  # Increased spacing

                # Process children horizontally
                for i, child in enumerate(row_children):
                    if i < len(ratios):
                        process_element(fig, child, gs[0, i], axes_dict, level+1, debug)
            else:
                # Row children stacked
                gs = gridspec.GridSpecFromSubplotSpec(len(ratios), 1,
                                                    subplot_spec=children_gs,
                                                    height_ratios=ratios,
                                                    hspace=0.4)  # Added hspace

                # Process children vertically
                for i, child in enumerate(row_children):
                    if i < len(ratios):
                        process_element(fig, child, gs[i, 0], axes_dict, level+1, debug)

        # Handle column children only
        elif has_col_ratio:
            ratios = element['colRatio']
            # Sort column children by ID for proper ordering
            col_children = sorted(
                [child for child in element['children'] if '_col' in child['id']],
                key=lambda x: x['id']
            )

            # Determine orientation based on child IDs and container type
            orientation = determine_layout_orientation(element, col_children, debug)

            if debug:
                print(f"{indent}Using {orientation} layout for column children with ratios: {ratios}")

            if orientation == "horizontal":
                # Column children side by side - increased spacing
                gs = gridspec.GridSpecFromSubplotSpec(1, len(ratios),
                                                    subplot_spec=children_gs,
                                                    width_ratios=ratios,
                                                    wspace=0.4)  # Increased spacing

                # Process children horizontally
                for i, child in enumerate(col_children):
                    if i < len(ratios):
                        process_element(fig, child, gs[0, i], axes_dict, level+1, debug)
            else:
                # Column children stacked
                gs = gridspec.GridSpecFromSubplotSpec(len(ratios), 1,
                                                    subplot_spec=children_gs,
                                                    height_ratios=ratios,
                                                    hspace=0.4)  # Added hspace

                # Process children vertically
                for i, child in enumerate(col_children):
                    if i < len(ratios):
                        process_element(fig, child, gs[i, 0], axes_dict, level+1, debug)

        # If no ratios available, use a grid layout
        else:
            # Sort all children by ID for proper ordering
            sorted_children = sorted(element['children'], key=lambda x: x['id'])
            num_children = len(sorted_children)

            # Determine a reasonable grid shape
            n_cols = int(np.ceil(np.sqrt(num_children)))
            n_rows = int(np.ceil(num_children / n_cols))

            if debug:
                print(f"{indent}Using grid layout {n_rows}x{n_cols} for chart container")

            gs = gridspec.GridSpecFromSubplotSpec(n_rows, n_cols, 
                                                subplot_spec=children_gs,
                                                wspace=0.4, hspace=0.4)  # Increased spacing

            # Process children in grid layout
            for i, child in enumerate(sorted_children):
                if i < n_rows * n_cols:
                    row = i // n_cols
                    col = i % n_cols
                    process_element(fig, child, gs[row, col], axes_dict, level+1, debug)

        return

    # For other containers (row/col), create nested grid
    if 'children' not in element or not element['children']:
        if debug:
            print(f"{indent}Element {element_id} has no children, skipping")
        return

    # Get ratios for this level (default to equal if not specified)
    ratios = element.get('ratio', [1] * len(element['children']))

    if debug:
        print(f"{indent}Creating grid for {element_type} with ratios: {ratios}")

    # Sort children by ID for proper ordering
    sorted_children = sorted(element['children'], key=lambda x: x['id'])

    # Determine orientation based on child IDs and container type
    orientation = determine_layout_orientation(element, sorted_children, debug)

    if debug:
        print(f"{indent}Using {orientation} layout for children")

    # For horizontal layouts (side-by-side charts), add extra wspace
    if orientation == "horizontal":
        # Children side by side
        n_cols = len(ratios)
        n_rows = 1
        gs = gridspec.GridSpecFromSubplotSpec(n_rows, n_cols,
                                            subplot_spec=subplot_spec,
                                            width_ratios=ratios,
                                            wspace=0.4)  # Increased wspace for side-by-side plots

        # Process children
        for i, child in enumerate(sorted_children):
            if i < len(ratios):
                # Place children horizontally
                process_element(fig, child, gs[0, i], axes_dict, level+1, debug)

    else:  # vertical
        # Children stacked
        n_rows = len(ratios)
        n_cols = 1
        gs = gridspec.GridSpecFromSubplotSpec(n_rows, n_cols,
                                            subplot_spec=subplot_spec,
                                            height_ratios=ratios,
                                            hspace=0.4)  # Added hspace

        # Process children
        for i, child in enumerate(sorted_children):
            if i < len(ratios):
                # Place children vertically
                process_element(fig, child, gs[i, 0], axes_dict, level+1, debug)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import textwrap

def format_large_number(value, pos=None):
    """Format large numbers with currency symbols and appropriate suffixes."""
    if value >= 1e9:
        return f'${value/1e9:.1f}B'  # Billion
    elif value >= 1e6:
        return f'${value/1e6:.1f}M'  # Million
    elif value >= 1e3:
        return f'${value/1e3:.1f}K'  # Thousand
    else:
        return f'${int(value)}'  # Small values show as whole dollars



def find_charts(structure):
    """
    Find all charts in the structure, including those that are also containers.

    Returns:
    list: List of (chart_id, chart_data) tuples
    """
    charts = []

    def traverse(node):
        if not node or not isinstance(node, dict):
            return

        # If this is a chart, add it to the list
        if node.get('type') == 'chart':
            charts.append((node['id'], node))

            # IMPORTANT: Even if it's a chart, also check if it has children
            # This handles the case where a chart is also a container

        # Traverse children (whether or not this node is a chart)
        if 'children' in node and node['children']:
            for child in node['children']:
                traverse(child)

    # Start with rows container
    if 'rows' in structure and 'children' in structure['rows']:
        for row in structure['rows']['children']:
            traverse(row)

    # Also check columns container
    if 'columns' in structure and 'children' in structure['columns']:
        for col in structure['columns']['children']:
            traverse(col)

    # Sort charts by ID to ensure consistent ordering
    return sorted(charts, key=lambda x: x[0])

def visualize_data_structure(structure_json, output_file=None, debug=False):
    """
    Visualize a dashboard structure.

    Parameters:
    structure_json: JSON string or dictionary with structure
    output_file: Optional path to save the visualization
    debug: Whether to show debug information

    Returns:
    tuple: (fig, axes_dict) with the figure and axes dictionary
    """
    # Parse the JSON if it's a string
    if isinstance(structure_json, str):
        try:
            structure = json.loads(structure_json)
        except:
            # Try to load from file
            with open(structure_json, 'r') as f:
                structure = json.load(f)
    else:
        structure = structure_json

    # Create the grid
    fig, axes_dict = create_grid_from_structure(structure, debug)

    if debug:
        print(f"Created grid with {len(axes_dict)} axes")

    # Find and populate chart nodes
    charts = find_charts(structure)

    if debug:
        print(f"Found {len(charts)} charts in structure")
        for chart_id, _ in charts:
            print(f"  - Chart ID: {chart_id}")

    # Populate each chart
    for chart_id, chart_data in charts:
        if chart_id in axes_dict:
            try:
                populate_chart(axes_dict[chart_id], chart_data, debug)
                if debug:
                    print(f"Populated chart: {chart_id}")
            except Exception as e:
                if debug:
                    print(f"Error populating chart {chart_id}: {e}")
                # Add error message to chart
                axes_dict[chart_id].text(0.5, 0.5, f"Error: {e}",
                                    ha='center', va='center')
        elif debug:
            print(f"Chart {chart_id} not found in axes_dict")

    # Don't use tight_layout as requested
    # Instead use explicit subplot adjustments only
    fig.subplots_adjust(hspace=0.6, wspace=0.3)

    # Save the figure if requested
    if output_file:
        plt.savefig(output_file, bbox_inches='tight')
        if debug:
            print(f"Saved visualization to {output_file}")

    return fig, axes_dict