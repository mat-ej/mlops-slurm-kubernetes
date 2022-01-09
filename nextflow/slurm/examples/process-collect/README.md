# Process all outputs altogether  

## Problem 

You need to process all the outputs of an upstream task altogether. 

## Solution

Use the https://www.nextflow.io/docs/latest/operator.html#collect[collect] operator to gather 
all the outputs produced by the upstream task and emit them as a sole output. 
Then use the resulting channel as input input for the process.

## Code 

    Channel.fromPath('reads/*_1.fq.gz').set { samples_ch }

    process foo {
      input:
      file x from samples_ch
      output:
      file 'file.fq' into unzipped_ch
      script:
      """
      < $x zcat > file.fq
      """
    }

    process bar {
      echo true   
      input:
      file '*.fq' from unzipped_ch.collect()
      """
      cat *.fq
      """
    }


## Run it

Use the the following command to execute the example:


    nextflow run patterns/process-collect.nf

