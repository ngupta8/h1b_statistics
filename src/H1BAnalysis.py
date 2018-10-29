"""
    Date 10/28/2018
    author Neha Gupta

    As a data engineer, you are asked to create a mechanism to analyze past years data,
    specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

    https://github.com/InsightDataScience/h1b_statistics
"""

import csv
import sys

from collections import defaultdict


class H1BAnalysis(object):

    def __init__(self, input_file, top_10_occupation_file, top_10_state_file):
        """
        Initializing the analysis class with input file location and locations for results files
        :param input_file: String
        :param top_10_occupation_file: String
        :param top_10_state_file: String
        """

        self.total_certified_applications = 0
        self.certified_applications_by_soc = defaultdict(int) # Counting the certified applications by SOC_NAME
        self.certified_applications_by_state = defaultdict(int) # Counting the certified applications by STATE

        self._process_file(input_file)

        # Uncomment below as needed
        # self._debug_data(self.certified_applications_by_soc, 10, self.total_certified_applications)
        # self._debug_data(self.certified_applications_by_state, 10, self.total_certified_applications)

        headers = 'TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'
        self._write_top_n_elements_to_file(top_10_occupation_file, headers, self.certified_applications_by_soc, 10,
                                          self.total_certified_applications)

        headers = 'TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'
        self._write_top_n_elements_to_file(top_10_state_file, headers, self.certified_applications_by_state, 10,
                                          self.total_certified_applications)

    def _process_file(self, filepath):
        """
        Processing the input file to read the contents, and prepare for reading as per requirements.
        Which is search for required columns in the headers
        :param filepath: String
        :return:
        """
        with open(filepath) as f:
            data = csv.reader(f, delimiter=';')
            headers = next(data)
            try:
                soc_name_idx = self.get_index_of_soc_name(headers)
                case_status_idx = self.get_index_of_status(headers)
                loc_idx = self.get_index_of_work_loc(headers)
            except ValueError as e:
                sys.stderr.write("ERROR: Required Column Missing: " + e.message +"\n")
                return 1
            for data_item in data:
                self._build_mappings(data_item, soc_name_idx, case_status_idx, loc_idx)

    def _build_mappings(self, data_item, soc_name_idx, case_status_idx, loc_idx):
        """
        Processing single row of data for hydrating the data objects when the application is certified.
         1. Updating total application numbers
         2. Updating the counts of application by SOC_NAME
         3. Updating the counts of applications by work_state
        :param data_item: List(String)
        :param soc_name_idx: int
        :param case_status_idx: int
        :param loc_idx: int
        :return:
        """
        status = self._clean_element(data_item[case_status_idx])
        soc_name = self._clean_element(data_item[soc_name_idx])
        work_state = self._clean_element(data_item[loc_idx])
        if status == 'CERTIFIED':
            self.certified_applications_by_soc[soc_name] += 1
            self.total_certified_applications += 1
            self.certified_applications_by_state[work_state] += 1

    def _clean_element(self, element):
        """
        Cleaning up elements where string itself includes quotes. This can corrupt the counts when two keys are same
        other than that of one being quoted and other is not
        :param element: String
        :return: String
        """
        return element.replace('"', '')

    def get_index_of_soc_name(self, headers):
        """
        Finding the required column SOC_NAME in the file headers and returns the respective index
        :param headers: List
        :return:
        """
        return headers.index('LCA_CASE_SOC_NAME') if 'LCA_CASE_SOC_NAME' in headers else headers.index('SOC_NAME')

    def get_index_of_status(self, headers):
        """
        Finding the required column STATUS in the file headers and returns the respective index
        :param headers: List
        :return:
        """
        return headers.index('STATUS') if 'STATUS' in headers else headers.index('CASE_STATUS')

    def get_index_of_work_loc(self, headers):
        """
        Finding the required column WORKSITE_STATE in the file headers and returns the respective index
        :param headers:  List
        :return:
        """
        return headers.index('LCA_CASE_WORKLOC1_STATE') if 'LCA_CASE_WORKLOC1_STATE' in headers else headers.index(
            'WORKSITE_STATE')

    def _debug_data(self, data, top_n, total_application):
        """
        Helper function to debug the data and print the results on the stdout.
        :param data: defaultdict(<type 'int'>, {})
        :param top_n: int
        :param total_application: int
        :return:
        """
        for key, num_application in sorted(data.iteritems(), key=lambda(k, v): (-v, k))[:top_n]:
            perc = (float(num_application) / total_application) * 100
            print(';'.join([key, str(num_application), "{0:.1f}%".format(perc)]))

    def _write_top_n_elements_to_file(self, filepath, headers, data, top_n, total_application):
        """
        Writing the results to the specified file along with the needed headers.
        :param filepath: String
        :param headers: String
        :param data: defaultdict(<type 'int'>, {})
        :param top_n: int
        :param total_application: int
        :return:
        """
        with open(filepath, 'w') as f:
            f.write(headers + '\n')
            for key, num_application in sorted(data.iteritems(), key=lambda(k, v): (-v, k))[:top_n]:
                perc = (float(num_application) / total_application) * 100
                f.write(';'.join([key, str(num_application), "{0:.1f}%".format(perc)]) + '\n')
