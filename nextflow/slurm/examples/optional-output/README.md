# Optional output  

## Problem 

A task in your workflow is expected to not create an output file in some circumstances. 

## Solution

Declare such output as an `optional` file. 

## Code 

    process foo {
      output: 
      file 'foo.txt' optional true into foo_ch 

      script:
      '''
      your_command 
      '''
    }


## Run it

Use the the following command to execute the example:

    nextflow run patterns/optional-output.nf
    
