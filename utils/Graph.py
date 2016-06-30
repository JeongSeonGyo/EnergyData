# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import FileIO
import os
from GlobalParameter import *


###############################################################################
# Show Graph

class Show:
    def __init__(self):
        pass

    @staticmethod
    def dictionary2graph(dictionary):
        """

        :param dictionary:
        :return:
        """

        plt.figure(figsize=(12, 9))
        plt.title(dictionary['file_name'])
        try:
            plt.scatter(x=dictionary['ts'], y=dictionary['value'], color='b', marker='o')
        except ValueError:
            plt.scatter(x=dictionary['ts'][:, 0], y=dictionary['value'], color='b', marker='o')
        plt.show()
        plt.close()

    @staticmethod
    def raw_data2graph(binary_file):
        """
        -
        :param binary_file:
            energy data에 해당하는 bainary file
        :return:
            NA
        """
        data = FileIO.Load.unpickling(binary_file)
        data['ts'] = data['ts'][:, 0]
        Show.dictionary2graph(data)

    @staticmethod
    def refined_data2graph(binary_file):
        """

        :param binary_file:
        :return:
        """
        Show.dictionary2graph(FileIO.Load.unpickling(binary_file))


class Save:
    def __init__(self):
        pass

    @staticmethod
    def raw_data2graph(directory=RepositoryPath):
        """
        - directory 에 있는 raw sensor data 를 graph 로 그려 graph-figure 저장

        :param directory:
            raw sensor data repository directory
        :return:

        """
        print 'data graph'

        save_path = os.path.join(RepositoryPath, GraphPath)
        FileIO.Save.assure_path_exist(save_path)

        for binary_file in FileIO.Load.binary_file_list(os.path.join(directory, RawDataPath)):
            # load data
            dictionary = FileIO.Load.unpickling(binary_file)

            print'\t',
            print 'drawing : ' + dictionary['file_name']

            # make a plot
            plt.figure(figsize=(12, 9))
            plt.title(dictionary['file_name'])
            plt.scatter(x=dictionary['ts'][:, 0], y=dictionary['value'], color='b', marker='o')

            # save it in png formats
            graph_figure_path = os.path.join(save_path, dictionary['file_name'] + '.png')
            plt.savefig(graph_figure_path, format='png')
            plt.close()

        return save_path
