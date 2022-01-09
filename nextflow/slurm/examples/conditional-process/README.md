# Conditional process executions 

## Problem 

Two different tasks need to be executed in a mutually exclusive manner, 
then a third task should post-process the results of the previous execution.

## Solution

Use a https://www.nextflow.io/docs/latest/process.html#when[when] statement to conditionally 
execute two different processes. Each process declares its own output channel.

Then use the https://www.nextflow.io/docs/latest/operator.html#mix[mix] operator to create 
a new channel that will emit the outputs produced by the two processes and use it as the input
for the third process.

## Code 

    params.flag = false 

    process foo {
      output: 
      file 'x.txt' into foo_ch
      when:
      !params.flag

      script:
      '''
      echo foo > x.txt
      '''
    }

    process bar {
      output: 
      file 'x.txt' into bar_ch
      when:
      params.flag

      script:
      '''
      echo bar > x.txt
      '''
    }

    process omega {
      echo true
      input:
      file x from foo_ch.mix(bar_ch)

      script:
      """
      cat $x 
      """
    }


## Run it

Use the the following command to execute the example:

    nextflow run patterns/conditional-process.nf

The processes `foo` and `omega` are executed. Run the same command 
with the `--flag` command line option. 

    nextflow run patterns/conditional-process.nf --flag 

This time the processes `bar` and `omega` are executed.


## Alternative solution

Conditionally create the input channels normally (with data) or as 
https://www.nextflow.io/docs/latest/channel.html#empty[empty] channels. 
The process consuming the individual input channels will only execute if 
the channel is populated. Each process still declares its own output channel.

Then use the https://www.nextflow.io/docs/latest/operator.html#mix[mix] operator to create 
a new channel that will emit the outputs produced by the two processes and use it as the input
for the third process.

## Code 

    params.flag = false

    (foo_inch, bar_inch) = ( params.flag
                         ? [ Channel.empty(), Channel.from(1,2,3) ]
                         : [ Channel.from(4,5,6), Channel.empty() ] )   

    process foo {

      input:
      val(f) from foo_inch

      output:
      file 'x.txt' into foo_ch

      script:
      """
      echo $f > x.txt
      """
    }

    process bar {
      input:
      val(b) from bar_inch

      output:
      file 'x.txt' into bar_ch

      script:
      """
      echo $b > x.txt
      """
    }

    process omega {
      echo true
      input:
      file x from foo_ch.mix(bar_ch)

      script:
      """
      cat $x
      """
    }


## Run it 


    nextflow run patterns/conditional-process2.nf

