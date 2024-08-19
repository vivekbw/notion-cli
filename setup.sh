#!/bin/bash

# A script to setup your local environment to be able to run NotionMail

# Exit immediately if a command exits with a non-zero status
set -e

echo "| NotionMail Setup Script - by Vivek |"
echo ""

# Check if a virtual environment already exists, if not, create a new one called "venv"
if [ ! -d "venv" ]; then
  echo "Creating a virtual environment..."
  python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
echo ""
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# Check if .env file exists, if not create a new templated .env file
if [ ! -f ".env" ]; then
  echo ""
  echo "Creating a .env file..."
  touch .env
  echo "NOTION_TOKEN=your_notion_token_here" >> .env
  echo "PROD_DATABASE_ID=your_prod_database_id_here" >> .env
  echo "TEST_DATABASE_ID=your_test_database_id_here" >> .env
fi

echo "-------------------------------------------"
echo ""
echo "Setup complete. To start using NotionMail,"
echo ""
echo "1. Activate the virtual environment with:"
echo "source venv/bin/activate"
echo ""
echo "2. Run NotionalMail with:"
echo "python menu.py"
echo ""
echo "3. Run the Testing Suite with:"
echo "pytest"

echo "" 
echo "Thanks - vivek bhardwaj!"	