# Process per file chunk  

## Problem 

You need to split one or more input files into chunks and execute a task for each of them.

## Solution

Use the the https://www.nextflow.io/docs/latest/operator.html#splittext[splitText] operator to split a file in chunks of a given size. Then use the resulting channel as input for the process implementing your task. 

Caveat: By default chunks are kept in memory. When splitting big files specify the parameter `file: true` to save the chunks into files. See the https://www.nextflow.io/docs/latest/operator.html#splittext[documentation] for details.

Splitter for specific file formats are available, eg https://www.nextflow.io/docs/latest/operator.html#splitfasta[splitFasta] and https://www.nextflow.io/docs/latest/operator.html#splitfastq[splitFastq].
 

## Code 

    Channel
        .fromPath('poem.txt')
        .splitText(by: 5)
        .set{ chunks_ch }

    process foo {
      echo true
      input: 
      file x from chunks_ch

      script:
      """
      rev $x | rev
      """
    } 


## Run it 

Use the the following command to execute the example:

    nextflow run patterns/process-per-file-chunk.nf

