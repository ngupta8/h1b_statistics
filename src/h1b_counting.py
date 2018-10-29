"""
    Date 10/28/2018
    author Neha Gupta

    As a data engineer, you are asked to create a mechanism to analyze past years data,
    specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

    https://github.com/InsightDataScience/h1b_statistics
"""

import os
import sys

from H1BAnalysis import H1BAnalysis


def main(argv):
    """
    Accepts lists of argument and Fail Fast on missing files / directories / improper usage
    Usage: <script path> <input file path> <top occupation file path> <top states file path>
    :param argv: List
    :return:
    """
    if len(argv) != 4:
        sys.stderr.write("Usage: %s <input file path> <top occupation file path> <top states file path>" % (argv[0],))
        return 1

    if not os.path.exists(argv[1]):
        sys.stderr.write("ERROR: Input File %r was not found!" % (argv[1],))
        return 1

    if not (os.path.isdir(os.path.dirname(argv[2])) and os.path.isdir(os.path.dirname(argv[3]))):
        sys.stderr.write("ERROR: Output File Directory was not found!")
        return 1

    H1BAnalysis(argv[1], argv[2], argv[3])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
