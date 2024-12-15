import streamlit as st
import json, os
import pandas as pd
import numpy as np
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def load_json_file(filename: str) -> dict:
    """Load and validate JSON data from file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        st.error(f"File {filename} does not exist.")
        return {}

def json_to_table(data: dict) -> pd.DataFrame:
    """Convert JSON data to pandas DataFrame with enhanced formatting."""
    table_data = []
    
    for date, rolls in data.items():
        for roll in rolls:
            # Check if roll is in the new [sides, value] format
            if isinstance(roll, list) and len(roll) == 2:
                sides, value = roll
                table_data.append({
                    'Date': datetime.strptime(date, '%Y-%m-%d').date(),
                    'Sides': sides,
                    'Roll': value,
                    'Percentage': (value / sides) * 100  # How high the roll was relative to max
                })
            else:
                # Handle legacy format (just the roll value)
                table_data.append({
                    'Date': datetime.strptime(date, '%Y-%m-%d').date(),
                    'Roll': roll,
                    'Sides': 20,  # Assume d20 for legacy data
                    'Percentage': (roll / 20) * 100
                })
    
    return pd.DataFrame(table_data)

def analyze_rolls(df: pd.DataFrame) -> dict:
    """Perform statistical analysis on roll data."""
    stats = {}
    
    # Overall statistics
    stats['total_rolls'] = len(df)
    stats['unique_dates'] = df['Date'].nunique()
    stats['dice_types'] = df['Sides'].unique().tolist()
    
    # Analysis per die type
    for sides in stats['dice_types']:
        die_stats = {}
        die_df = df[df['Sides'] == sides]
        
        die_stats['count'] = len(die_df)
        die_stats['mean'] = die_df['Roll'].mean()
        die_stats['median'] = die_df['Roll'].median()
        die_stats['mode'] = die_df['Roll'].mode().iloc[0]
        die_stats['min'] = die_df['Roll'].min()
        die_stats['max'] = die_df['Roll'].max()
        die_stats['std'] = die_df['Roll'].std()
        
        # Calculate how "fair" the die seems (chi-square test)
        expected = len(die_df) / sides  # Expected count for each number
        observed = die_df['Roll'].value_counts()
        chi_square = sum(((observed - expected) ** 2) / expected)
        die_stats['fairness_score'] = 1 / (1 + chi_square)  # Normalized between 0 and 1
        
        stats[f'd{sides}'] = die_stats
    
    return stats

def plot_roll_distribution(df: pd.DataFrame):
    """Create visualizations for roll distributions."""
    # Distribution plot for each die type
    for sides in df['Sides'].unique():
        die_df = df[df['Sides'] == sides]
        
        fig = px.histogram(
            die_df, 
            x='Roll',
            title=f'Distribution of d{sides} Rolls',
            nbins=int(sides),  # Convert numpy.int64 to Python int
            labels={'Roll': 'Roll Value', 'count': 'Frequency'},
            color_discrete_sequence=['#1f77b4']
        )
        
        # Add expected distribution line
        expected_freq = len(die_df) / sides
        fig.add_hline(y=expected_freq, line_dash="dash", line_color="red",
                     annotation_text="Expected Frequency")
        
        st.plotly_chart(fig)

def plot_roll_trends(df: pd.DataFrame):
    """Plot trends in rolling patterns over time."""
    if len(df) > 0:
        # Create figure
        fig = go.Figure()
        
        # Add traces for each die type
        for sides in sorted(df['Sides'].unique()):
            die_df = df[df['Sides'] == sides]
            
            fig.add_trace(go.Scatter(
                x=die_df['Date'],
                y=die_df['Percentage'],
                mode='markers+lines',
                name=f'd{sides}',
                hovertemplate='Date: %{x}<br>Roll: %{text}<br>Percentage: %{y:.1f}%',
                text=die_df['Roll']
            ))
        
        # Update layout
        fig.update_layout(
            title='Roll Percentages Over Time',
            xaxis_title='Date',
            yaxis_title='Roll Percentage',
            hovermode='x unified',
            showlegend=True
        )
        
        st.plotly_chart(fig)
    else:
        st.write("No data available for trend analysis")

def main():
    st.title("Dice Roll Analysis")
    
    # File name of the JSON file
    filename = 'rolls.json'
    
    # Load the JSON data
    data = load_json_file(filename)
    
    if data:
        # Convert JSON data to a table format
        df = json_to_table(data)
        
        # Sidebar for filtering
        st.sidebar.header("Filters")
        selected_dice = st.sidebar.multiselect(
            "Select Dice Types",
            options=sorted(df['Sides'].unique()),
            default=sorted(df['Sides'].unique())
        )
        
        # Filter data based on selection
        filtered_df = df[df['Sides'].isin(selected_dice)]
        
        # Display statistics
        st.header("Statistical Analysis")
        stats = analyze_rolls(filtered_df)
        
        # Overall stats
        st.subheader("Overall Statistics")
        st.write(f"Total Rolls: {stats['total_rolls']}")
        st.write(f"Unique Sessions (Dates): {stats['unique_dates']}")
        
        # Per-die statistics
        for sides in selected_dice:
            die_key = f'd{sides}'
            if die_key in stats:
                st.subheader(f"d{sides} Statistics")
                die_stats = stats[die_key]
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"Count: {die_stats['count']}")
                    st.write(f"Mean: {die_stats['mean']:.2f}")
                    st.write(f"Median: {die_stats['median']}")
                    st.write(f"Mode: {die_stats['mode']}")
                
                with col2:
                    st.write(f"Min: {die_stats['min']}")
                    st.write(f"Max: {die_stats['max']}")
                    st.write(f"Std Dev: {die_stats['std']:.2f}")
                    st.write(f"Fairness Score: {die_stats['fairness_score']:.2%}")
        
        # Visualizations
        st.header("Visualizations")
        
        # Distribution plots
        st.subheader("Roll Distributions")
        plot_roll_distribution(filtered_df)
        
        # Trend analysis
        st.subheader("Rolling Patterns Over Time")
        plot_roll_trends(filtered_df)
        
        # Raw data table
        st.header("Raw Data")
        st.dataframe(filtered_df.sort_values('Date', ascending=False))

if __name__ == '__main__':
    main()
