# Optional input 

## Problem 

One or more processes have an optional input file. 

## Solution 

Use a special file name to mark the absence of the file parameter. 

## Code 

    params.inputs = 'prots/*{1,2,3}.fa'
    params.filter = 'NO_FILE'

    prots_ch = Channel.fromPath(params.inputs)
    opt_file = file(params.filter)

    process foo {
      input:
      file seq from prots_ch
      file opt from opt_file 

      script:
      def filter = opt.name != 'NO_FILE' ? "--filter $opt" : ''
      """
      your_commad --input $seq $filter
      """
    }


## Run it 

Run the script with the following command: 

    nextflow run patterns/optional-input.nf 

Run the same script providing an optional file input:

    nextflow run patterns/optional-input.nf --filter foo.txt

