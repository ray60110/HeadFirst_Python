#A function for printing words and words in a list.
import sys

def print_lol(the_list, indent=False, level=0, fh=sys.stdout):

# let's define a function that could print every item in a list.
# there are four arguments, the target, indent, space, systemout.

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
# to print nested list and give it the indent and level we had assigned.

        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='', file=fh)
            print(each_item, file=fh)
        
