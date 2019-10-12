import argparse
import textwrap
import os
import socket
from subprocess import PIPE,Popen
import sys
from os import path

class Utilities:

    def __init__(self):
        pass

    def create_empty_file(self,fname):
        with open(fname,"w") as f:
            f.write("")
            f.close()

    def get_file_content(self,fname):
        """
        Read file content and return a list

        :param fname:
        :return:
        """
        content=list()
        with open(fname) as f:
            content=f.readlines()
        return content


    def get_command_statements(self,command,arraylist):

        content = list()
        commandLine = command

        if not arraylist:
            content.append(commandLine)
        else:
            for line in arraylist:
                #if not line.strip('\n').strip(" ").__len__() ==0:
                    content.append(commandLine + '"{}"'.format(line.strip('\n')))
                # else:
                #     content.append(commandLine + (line.strip('\n')))
        return (content)

    def set_command_file(self,connection,command,fileName,arraylist):

        """
        Read input file conents in a list, create full command set and write to file
        Return the file created
        :param connection:
        :param command:
        :param fileName:
        :return:
        """

        outfile=fileName
        with open(outfile, "w") as f:
            f.write(connection)
            for e in self.get_command_statements(command,arraylist):
                f.write(e)
            f.write("close")
            f.close()
        return outfile

    def add_job_extention(self,arraylist,postfix):

        tlist=list()
        for e in arraylist:
            tlist.append(str(e.strip('\n'))+".{}".format(postfix))
        return tlist


class System:

    def execute_cli(self,cmdfile):
        p=list()
        p = Popen([os.path.join(os.getcwd(),"cli.cmd")," --cmdfile {}".format("dataflowlist.out")], stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        exitcode=p.returncode
        print("-----------------------------------------")
        #print(output)
        #print(err.decode("utf-8"))
        t=list(err.decode("utf-8"))
        print(t)
        #print("ERROR: {}".format(err.decode("utf-8")))
        print(" process exit code is : {}".format(exitcode))
        print("-----------------------------------------")


class Connection:

    def __init__(self,hostname=socket.gethostname(),port="8080",username="admin",password="admin"):
        self.hostname=str(hostname)
        self.port=str(port)
        self.username=str(username)
        self.password=str(password)

    def get_connection_string(self):
        return "connect --h {}:{} --u {} --p {}".format(self.hostname,self.port,self.username,self.password)

    def set_hostname(self,hostname):
        self.hostname=hostname

    def set_portname(self,portname):
        self.port=portname

    def set_username(self,username):
        self.username=username

    def set_password(self,password):
        self.password=password

    @staticmethod
    def close_connection(self):
        return "close"


class CommandHandler:

    def __init__(self):

        self.utility=Utilities()
        self.run=System()

    def dataflow_list(self,connection):

        command="dataflow list"
        tfile = self.utility.set_command_file(connection,command,"dataflowlist.out",list())
        print(tfile)
        self.run.execute_cli(tfile)

    def dataflow_export(self,connection,fileName):

        command="dataflow export  --e True --o exports --d "
        tfile=self.utility.set_command_file(connection,command,"dataflowexport.out",self.utility.get_file_content(fileName))
        self.run.execute_cli(tfile)
        print(tfile)

    def dataflow_import(self,connection,fileName):

        command = "dataflow import --u True --p exports --f "
        dflist=self.utility.add_job_extention(self.utility.get_file_content(fileName),"df")
        tfile = self.utility.set_command_file(connection, command,"dataflowimport.out",dflist)
        #self.run.execute_cli(tfile)
        print(tfile)


class ArgumentHandler:

    def __init__(self,arglist):
        self.args=arglist
        self.commandList=('dataflow export', 'processflow export', 'dataflow list')

    def run(self):
        self.validate_arguments()

    def validate_arguments(self):
        print(self.args)
        if not self.args.command:
            print("Command missing.. use: {} -h for help ".format(path.basename(sys.argv[0])))
            exit(1)
        else:
            if self.args.command not in self.commandList:
                print("Supported commands are:")
                for e in self.commandList:
                    print(e)
                exit(1)



def main():
    # cmd=Commands()
    # c=Connection()
    # c.set_portname("9090")
    # print(c.get_connection_string())
    # cmd.dataflow_list(c.get_connection_string())
    # cmd.dataflow_export(c.get_connection_string(),"dataflowexport.txt")
    # cmd.dataflow_import(c.get_connection_string(), "dataflowexport.txt")
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--command", help=textwrap.dedent("""Usage: Spectrum command name
                                               eg: "dataflow list"
                        """), type=str)
    parser.add_argument("-s", "--serverName", help="Host name of machine where to execute command")
    parser.add_argument("-f", "--fileName",
                        help="File name having names of [dataflows] OR [processflows] OR [subflows]")

    args = parser.parse_args()



    arginst=ArgumentHandler(parser.parse_args())
    arginst.run()


if __name__ == '__main__':
    main()



#

# #
# # if args.serverName:
# #     print(args.serverName)
#
#
#
#
#
# def create_command_file(command,fname="cmdfile"):
#     fname="D:\\spectrum-cli-12.1\\{}".format(fname)
#     with open(fname, "w") as f:
#         print(Connection.get_connection_string(), file=f)
#         for e in read_command_file(command):
#             print(e, file=f)
#         print(Connection.close_connection(), file=f)
#     return fname
#
#
#
#
#
# def read_command_file(command,fname="default"):
#     if fname.__eq__("default"):
#         with open(fname,"w") as f:
#             print(file=f)
#
#     content = list()
#     commandLine=command
#     with open(fname) as f:
#         for line in f:
#             content.append(commandLine+line.strip('\n'))
#     return (content)
#
# def export_data_flows():
#
#     if not args.serverName:
#         print("ServerName required")
#         print('Usage: -c "dataflow export" -s "serverName" -f "fileName"')
#     elif not args.fileName:
#             print("FileName required")
#             print('Usage: -c "dataflow export" -s "serverName" -f "fileName"')
#     else:
#         """
#             1. For each record in file, create corresponding export command, Write to a temporary file
#             2. Send commands to CLI
#         """
#         command=args.command + " --o "+ args.directory + " --d "
#
#
# def dataflowlist():
#     create_command_file(args.command)
#
# #export_data_flows()
# dataflowlist()
#


