# Ignore failing process 

## Problem 

A task is expected to fail in a certain condition. You want to ignore the failure and continue the execution of the remaining tasks in the workflow. 

## Solution

Use the process https://www.nextflow.io/docs/latest/process.html#errorstrategy[directive] `errorStrategy 'ignore'` to ignore the error condition. 


## Code 

    process foo {
      errorStrategy 'ignore'
      script:
      '''
        echo This is going to fail!
        exit 1
      '''
    }  

    process bar {
      script:
      '''
      echo OK
      '''
    }


## Run it 

Run the script with the following command: 

    nextflow run patterns/ignore-failing-process.nf 
