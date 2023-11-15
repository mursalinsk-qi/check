import os
import logging
from bs4 import BeautifulSoup

import send_message

logging.basicConfig(level='DEBUG')

INCREASED = "increased"
DECREASED = "decreased"
NOT_UPDATED = "not changed"
commit_flag = False
data = []


def get_report_file_path(file_name):
    directory = 'coverage_report'
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            logging.error(f"Error creating directory: {e}")
            return ''
    return os.path.join(directory, file_name)


def fetch_coverage_data_from_html(html_file_path):
    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            option_elements = soup.find_all('option')
            return option_elements
    except FileNotFoundError:
        logging.warning(f"Error: File '{html_file_path}' not found.")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return None


def generate_coverage_report(html_file_path):
    coverage_report = {}
    coverage_data = fetch_coverage_data_from_html(html_file_path)
    if coverage_data is None:
        return coverage_report
    for data in coverage_data:
        info = data.text
        index = info.find(' ')
        filename = info[:index]
        value = info[index + 2:-2]
        coverage_report[filename] = float(value)
    return coverage_report


def commit_file(coverage_file, new_coverage_file):
    logging.info("commit flag", commit_flag)
    if commit_flag:
        if os.path.exists(coverage_file):
            os.remove(coverage_file)
        os.rename(new_coverage_file, coverage_file)
    else:
        os.remove(new_coverage_file)


def check_coverage():
    # getting previous coverage report
    coverage_file = get_report_file_path('coverage.html')
    previous_coverage = generate_coverage_report(coverage_file)
    logging.info(previous_coverage)

    # generating new coverage report
    new_coverage_file = get_report_file_path('new.html')
    os.system("go test -v -coverprofile cover.out ./...")
    os.system(f"go tool cover -html cover.out -o {new_coverage_file}")
    new_coverage_data = generate_coverage_report(new_coverage_file)

    for file_name in new_coverage_data:
        old_coverage = previous_coverage.get(file_name, 0.0)
        new_coverage = new_coverage_data.get(file_name, 0.0)
        if new_coverage > old_coverage:
            data.append(
                {'file': file_name, 'old_coverage': old_coverage, 'new_coverage': new_coverage, 'status': INCREASED})
            global commit_flag
            commit_flag = True
            logging.info("Test Coverage value of file %s increased from: %.2f to %.2f" % (
                file_name, old_coverage, new_coverage))
        elif old_coverage == new_coverage:
            data.append(
                {'file': file_name, 'old_coverage': old_coverage, 'new_coverage': new_coverage, 'status': NOT_UPDATED})
        else:
            data.append(
                {'file': file_name, 'old_coverage': old_coverage, 'new_coverage': new_coverage, 'status': DECREASED})
            logging.warning("Test Coverage value of file %s reduced from: %.2f to %.2f" % (
                file_name, old_coverage, new_coverage))

    commit_file(coverage_file, new_coverage_file)


check_coverage()

# send_message.send_message_to_teams(data)
