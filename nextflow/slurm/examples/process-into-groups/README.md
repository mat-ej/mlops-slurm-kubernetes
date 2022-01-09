# Process outputs into groups 

## Problem 

You need to process in the same batch all files that have a matching key in the file name.

## Solution 

Use the https://www.nextflow.io/docs/latest/operator.html#map[map] operator to associate with each file
a key extracted from the file name. Then chain the resulting channel with the https://www.nextflow.io/docs/latest/operator.html#grouptuple[groupTuple] operator to group together all files that have a matching key. Finally use the resulting channel as input for the process.

## Code

        Channel
            .fromPath('reads/*')  
            .map { file -> 
                def key = file.name.toString().tokenize('_').get(0)
                return tuple(key, file)
             }
            .groupTuple()
            .set{ groups_ch }


        process foo {
          input:
          set key, file(samples) from groups_ch

          script:
          """
          echo your_command --batch $key --input $samples 
          """
        } 


## Run it 


    nextflow run patterns/process-into-groups.nf
