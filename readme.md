# Crescent-1: A Data Analyzer

![Main Picture](mainpic.png)

## Introduction
This program demonstrates how to analyze data by talking to the database via SQL queries. It is capable of visualizing trends from historical data, which is useful for studying long-term performance. It also utilizes Linear Regression Machine Learning to predict, for example, the profit numbers for the next year.

## Data Model
![EER Diagram](EER.png)

## Installation
This project requires matplotlib and sql-connector-python to be installed. It also requires you to setup a local MySQL database.<br>
`> pip3 sql-connector-python`<br>
`> pip3 matplotlib`<br>
pip is usually shipped with python, so install python if you don't have it.

## Usage
This program is used for data analysis. For now, this program demonstrates its usage with mock data for a building company. This program can show data trends like how many houses were built between 2014 and 2024, or what is highest price a house was sold for, etc. This program can also predict future scenarios using the Linear Regression Machine Learning algorithm that is trained on historical data. For example, we can use it to predict the profits for the following year.
