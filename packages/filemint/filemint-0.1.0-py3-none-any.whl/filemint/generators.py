"""File generation utilities for creating test files in various formats."""

import os
import csv
import random
import string


def random_text(length=100):
    """Generate random text with the specified length.
    
    Args:
        length: The length of the random text to generate
        
    Returns:
        A string of random ASCII letters and whitespace
    """
    # Use only letters and spaces, avoiding newlines and other special whitespace
    return ''.join(random.choices(string.ascii_letters + ' ', k=length))


def generate_csv(output_dir, filename, num_rows=10):
    """Generate a structured CSV file.
    
    Args:
        output_dir: Directory where the file will be saved
        filename: Name of the file to create
        num_rows: Number of data rows to generate
        
    Returns:
        The full path to the created file
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    headers = ['ID', 'Name', 'Value']
    with open(filepath, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for i in range(1, num_rows + 1):
            # Random name and a random numeric value
            name = ''.join(random.choices(string.ascii_letters, k=8))
            value = round(random.uniform(0, 100), 2)
            writer.writerow([i, name, value])
    
    return filepath


def generate_txt(output_dir, filename, num_lines=40):
    """Generate an unstructured TXT file with random text.
    
    Args:
        output_dir: Directory where the file will be saved
        filename: Name of the file to create
        num_lines: Number of lines of random text to generate
        
    Returns:
        The full path to the created file
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, mode='w') as txtfile:
        for _ in range(num_lines):
            # Generate each line separately to ensure exact line count
            txtfile.write(random_text(80) + "\n")
    
    return filepath


def generate_binary(output_dir, filename, size_in_kb=100):
    """Generate a binary file with random bytes.
    
    Args:
        output_dir: Directory where the file will be saved
        filename: Name of the file to create
        size_in_kb: Size of the file in kilobytes
        
    Returns:
        The full path to the created file
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    size = size_in_kb * 1024
    with open(filepath, mode='wb') as binfile:
        binfile.write(os.urandom(size))
    
    return filepath


def generate_invalid_csv(output_dir, filename, num_rows=40):
    """Generate a CSV file with inconsistent columns for testing error handling.
    
    Args:
        output_dir: Directory where the file will be saved
        filename: Name of the file to create
        num_rows: Number of data rows to generate
        
    Returns:
        The full path to the created file
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    headers = ['ID', 'Name', 'Value']
    with open(filepath, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for i in range(1, num_rows + 1):
            # On purpose, sometimes omit the "Value" column
            if random.choice([True, False]):
                writer.writerow([i, ''.join(random.choices(string.ascii_letters, k=8))])
            else:
                writer.writerow(
                    [i, ''.join(random.choices(string.ascii_letters, k=8)), round(random.uniform(0, 100), 2)])
    
    return filepath


def generate_test_files(output_dir, num_csv=10, num_txt=10, num_binary=10, num_invalid=10):
    """Generate multiple test files of each type.
    
    Args:
        output_dir: Directory where files will be saved
        num_csv: Number of CSV files to generate
        num_txt: Number of TXT files to generate
        num_binary: Number of binary files to generate
        num_invalid: Number of invalid CSV files to generate
        
    Returns:
        A list of paths to all created files
    """
    os.makedirs(output_dir, exist_ok=True)
    generated_files = []
    
    for i in range(1, max(num_csv, num_txt, num_binary, num_invalid) + 1):
        # Generate CSV files
        if i <= num_csv:
            filepath = generate_csv(
                output_dir, 
                f"data_{i}.csv", 
                num_rows=random.randint(5, 20)
            )
            generated_files.append(filepath)
        
        # Generate TXT files
        if i <= num_txt:
            filepath = generate_txt(
                output_dir, 
                f"notes_{i}.txt", 
                num_lines=random.randint(5, 15)
            )
            generated_files.append(filepath)
        
        # Generate binary files
        if i <= num_binary:
            filepath = generate_binary(
                output_dir, 
                f"random_{i}.bin", 
                size_in_kb=random.randint(50, 200)
            )
            generated_files.append(filepath)
        
        # Generate invalid CSV files
        if i <= num_invalid:
            filepath = generate_invalid_csv(
                output_dir, 
                f"bad_data_{i}.csv", 
                num_rows=random.randint(5, 20)
            )
            generated_files.append(filepath)
    
    return generated_files 