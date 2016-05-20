# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import FileIO


class Show:
    def __init__(self):
        pass

    @staticmethod
    def dic2graph(dictionary):
        x = []
        for ts in dictionary['ts']:
            try:
                x.append(ts[0])
            except TypeError:
                x.append(ts)

        y = dictionary['value']

        plt.title(dictionary['file_name'])
        plt.scatter(x, y, marker='x')
        plt.show()
        plt.close()

    @staticmethod
    def bin2graph(binary_file):
        Show.dic2graph(FileIO.Load.unpickling(binary_file))

    # @staticmethod
    # def bins2graphs(path):
    #     file_list = FileIO.Load.load_filelist(path)
    #     for file in file_list:
    #         Show.bin2graph(file)
    #         print

    @staticmethod
    def vectors2graphs(file):
        vectors = FileIO.Load.unpickling(file)
        for i in xrange(len(vectors['file_name'])):
            name = vectors['file_name'][i].rsplit('/', 1)[1]
            name = name.split('.')[0]

            x = np.linspace(0, 1, len(vectors['vec_data'][i]))
            plt.scatter(x, vectors['vec_data'][i], marker='+')
            plt.title(name)
            plt.show()
            plt.close()
            print


"""

class Save:
    def __init__(self):
        pass

    @staticmethod
    def bin2graph(file):
        x = []
        for line in unpickling(file)['ts']:
            x.append(line[0])
        y = unpickling(file)['value']

        file_name = file.rsplit('/', 1)[-1]
        file_name = file_name.split('.')[0] + '.jpg'

        plt.title(file_name)
        plt.scatter(x, y, marker='x')

    @staticmethod
    def bins2graphs(path, file_list):
        old_path = os.getcwd()

        path = path_checker(path)
        path = os.path.join(path, RESULT_DIRECTORY, 'graph')
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)

        for file in file_list:
            start_time = time.time()

            print 'saving' + file,

            x = []
            for line in unpickling(file)['ts']:
                x.append(line[0])
            y = unpickling(file)['value']

            file_name = file.rsplit('/', 1)[1]
            file_name = file_name.split('.')[0] + '.jpg'

            plt.title(file_name)
            plt.scatter(x, y, marker='x')
            plt.savefig(file_name)
            plt.close()

            end_time = time.time()
            print '\t' + 'run time: ' + str(end_time - start_time)

        os.chdir(old_path)

    @staticmethod
    def vectors2graphs(path, vectors):
        old_path = os.getcwd()

        path = path_checker(path)
        path = os.path.join(path, RESULT_DIRECTORY, 'graph', 'vectorize', str(VEC_DIMENSION))
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)

        for i in xrange(len(vectors['file_name'])):
            start_time = time.time()

            name = vectors['file_name'][i].rsplit('/', 1)[1]

            print 'drawing graph of VECTORIZED ' + name,

            name = name.split('.')[0]
            name = name + '_vec_' + str(VEC_DIMENSION) + '.jpg'

            x = np.linspace(0, 1, len(vectors['vec_data'][i]))
            plt.scatter(x, vectors['vec_data'][i], marker='+')
            plt.title(name)
            plt.savefig(name)
            plt.close()

            end_time = time.time()

            print '\t\t' + 'run time: ' + str(end_time - start_time)

        os.chdir(old_path)

"""
