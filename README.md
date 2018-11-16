# Python example using Unix pipes

Need to build your own command line tools? 
Make them utilize the Unix pipes. 
Don't read directly from files, 
there are other tools that can do that better.

If you make your tool read from Unix pipes, 
you can compose it with other command line tools.

## Example usage

List all files in your home folder, 
process them with your tool and sort the output

`ls ~ | python example/example.py | sort`
