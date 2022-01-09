# Feedback loop  

## Problem 

You need to repeat the execution of one or more tasks, using the output as the input for a new iteration, until a certain condition is reached. 

## Solution

Use the output of the last process in the iteration loop as the input for the first process. 

To do so, explicitly create the output channel using https://www.nextflow.io/docs/latest/channel.html#create[Channel.create] method. 

Then define the process input as a https://www.nextflow.io/docs/latest/operator.html#mix[mix] of the initial input and the
process output to which is applied the https://www.nextflow.io/docs/latest/operator.html#until[until] operator which defines the termination condition. 

## Code 

        params.input = 'hello.txt'

        condition = { it.readLines().size()>3 }
        feedback_ch = Channel.create()
        input_ch = Channel.fromPath(params.input).mix( feedback_ch.until(condition) )

        process foo {
            input: 
            file x from input_ch
            output: 
            file 'foo.txt' into foo_ch
            script:
            """
            cat $x > foo.txt 
            """
        }

        process bar {
            input:
            file x from foo_ch 
            output:
            file 'bar.txt' into feedback_ch
            file 'bar.txt' into result_ch
            script:
            """
            cat $x > bar.txt
            echo World >> bar.txt 
            """
        }

        result_ch.last().println { "Result:\n${it.text.indent(' ')}" }


## Run it

Use the the following command to execute the example:

    nextflow run patterns/feedback-loop.nf
