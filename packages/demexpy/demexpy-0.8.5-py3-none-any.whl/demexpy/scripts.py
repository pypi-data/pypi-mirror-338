from .nodes import Node
import argparse


def new_demex_node():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", help="Specify the file name.")
    parser.add_argument('-n', "--name", help="Specify the name of the node.")
    parser.add_argument("-mb", "--mailbox", help="Specify the file to save the mailbox in.")

    args = parser.parse_args()
    
    if args.file is None:
        print("Please specify a file name with -f. Run demexpy -h for details.")
        return

    if args.name is None:
        print("Please specify a node name with -n. Run demexpy -h for details.")
        return


    n = Node()
    n.set_data_file(args.file)
    n.set_data("name", args.name)
    n.generate_uuid()
    n.generate_keys()

    if args.mailbox is not None:
        n.save_mailbox(args.mailbox)
