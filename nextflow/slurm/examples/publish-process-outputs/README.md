# Store process outputs 

## Problem 

You need to store the outputs of one or more processes into a directory structure of your choice.

## Solution 

Use the https://www.nextflow.io/docs/latest/process.html#publishdir[publishDir] directive
to set a custom directory where the process outputs need to be made available.

## Code 

    params.reads = 'reads/*{1,2}.fq.gz'
    params.outdir = 'my-results'

    Channel.fromFilePairs(params.reads).set{ samples_ch }  

    process foo {
      publishDir "$params.outdir/$sampleId"
      input:
      set sampleId, file(samples) from samples_ch
      output:
      file '*.fq'

      script:
      """
      < ${samples[0]} zcat > sample_1.fq 
      < ${samples[1]} zcat > sample_2.fq 
      """
    }


## Run it 

Run the script with the following command: 


    nextflow run patterns/publish-process-outputs.nf 

