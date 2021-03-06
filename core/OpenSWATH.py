#!/usr/python
#coding=utf-8


import os
from core import GlobaVar as gl
from core import parameters


class OpenSWATH(object):
    '''
    OpenSWATH Workflow.

    '''

    # init
    #
    # @infile
    # @trfile
    # @trirt
    # @oswfile
    # @threads
    # @mz_window
    # @rt_window
    # @command
    #
    #
    def __init__(self, infile, trfile, trirt, oswfile, threads=20,
                 mz_window = parameters.MZ_WINDOW, rt_window = parameters.RT_WINDOW, command=""):
        self.infile = infile
        self.trfile = trfile
        self.trirt = trirt
        self.oswfile = oswfile
        self.threads = threads
        if self.threads >= 20 :
            self.threads = 20
        self.mz_window = mz_window
        self.rt_window = rt_window
        self.command = command
        if self.command == "":
            self.command = parameters.COMMAND

    def __pase_command(self):
        input_command = ("OpenSwathWorkflow "
                         "-in %s "
                         "-tr %s "
                         "-tr_irt %s "
                         "-out_osw %s "
                         "-threads %s "
                         "-outer_loop_threads 4 " # 20190801 Add
                         "-mz_extraction_window %s "
                         "-rt_extraction_window %s"
                         " %s" # other command
                         % (self.infile,
                            self.trfile,
                            self.trirt,
                            self.oswfile,
                            self.threads,
                            self.mz_window,
                            self.rt_window,
                            self.command
                            ))
        return input_command

    def __docker(self, path, command = ""):

        docker_command = ("docker run --rm -v"
                          "%s %s"
                          ":/data/ openswath"
                          % (command, path))
        return docker_command

    def run(self, path, extra=""):
        run_cmd = ("%s %s"
                   % (self.__docker(path, extra), self.__pase_command()))
        print(run_cmd)
        if gl.get_value("debug"):
            print(run_cmd)
            return_info = "DEBUG: " + run_cmd
            return return_info
        else:
            return_info = os.popen(run_cmd)
            return_info= "Guomics Lab: " + '\n'.join(return_info.readlines())

            return return_info


if __name__ == "__main__":
    pass