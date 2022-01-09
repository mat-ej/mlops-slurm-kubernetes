# Channel duplication   

## Problem 

You need to you use the same channel as input in two or more processes.

## Solution

Use the https://www.nextflow.io/docs/latest/operator.html#into[into] operator to create two (or more) copies of the source channel. Then, use the new channels as input for the processes. 

## Code 


    Channel
        .fromPath('prots/*_?.fa')
        .into { prot1_ch; prot2_ch }

    process foo {
    input: file x from prot1_ch
    script: 
    """
        echo your_command --input $x
    """
    }    

    process bar {
    input: file x from prot2_ch
    script: 
    """
        your_command --input $x
    """
    }    

## Run it

Use the the following command to execute the example:

    nextflow run patterns/channel-duplication.nf
