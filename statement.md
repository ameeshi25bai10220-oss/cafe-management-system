# Cafe Management System - Project Statement

## Problem Statement

Problem: Traditional cafe management methods (e.g., manual order taking, paper-based inventory tracking, and spreadsheet-based sales logging) are inefficient, prone to errors in billing and stock discrepancies, and provide slow, inaccurate sales reporting. This leads to lost revenue, wasted resources, and poor customer experience during peak hours.

Proposed Solution: To develop a Python-based Cafe Management System (CMS) that digitises core operations, providing a centralised platform for order management, real-time inventory tracking, and automated sales analysis.

## Scope of the Project

The project is limited to a Command Line Interface (CLI) application focusing on the backend data logic. The core scope includes the implementation of three major functional modules: Order Managemen, Inventory Control, and Sales Reporting.

Exclusions: The system does not include a Graphical User Interface (GUI), external payment gateway integration, complex user authentication (beyond a simple password check, if implemented), or full supply chain modeling.

## Target Users

1.  Staff: Primary users responsible for order entry and generating bills.
2.  Manager: Users responsible for adding/updating menu items, managing stock levels, and viewing sales reports.

## High-Level Features

1.  Order Processing: Enables staff to build a customer order, calculate the total, and log the final transaction to the database.
2.  Inventory Management: Provides CRUD functionality for ingredients/stock and automatically flags items when stock levels drop below a critical threshold.
3.  Reporting & Analytics: Generates aggregated sales data, including total revenue and itemized sales ranking, to aid management decisions.
