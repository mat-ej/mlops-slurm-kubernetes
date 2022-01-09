# Process per file path  

## Problem 

You need to execute a task for each file that matches a glob pattern. 

## Solution

Use the https://www.nextflow.io/docs/latest/channel.html#frompath[Channel.fromPath] method to create a channel emitting all files matching the glob pattern. Then, use the channel as input of the process implementing your task. 


## Code 

    Channel.fromPath('reads/*_1.fq.gz').set{ samples_ch }

    process foo {
      input:
      file x from samples_ch
  
      script:
      """
      your_command --input $x
      """
    }



## Run it 

Use the the following command to execute the example:

    nextflow run patterns/process-per-file-path.nf

