# NextFlow-on-SLURM
A repository with insturctions on how to boot NextFlow examples using SLURM with the examples and their explanations.

# Requirements:

To use RCI cluster you'll have to:
  - 1)Request access for it , use this page:
https://login.rci.cvut.cz/wiki/doku.php
  - 2)Install an SSH client to be able connect to RCI cluster:
 The SSH client is required to connect RCI cluster. For interactive work with GUI applications, X11 server is required. SSH client is almost in all Linux or Mac OS X distributions. You can use PuTTy SSH client in Windows. X11 server is part of all Linux distributions. Use XQuartz for Mac OS X. Use MobaXterm in Windows - which includes also SSH client, so PuTTy is nod needed, when using MobaXterm.
MobaXterm and Linux options worked best for me.
  - 3)Once you’ve been granted the access to SLURM, you can log in to via SSH client:
  
Address of the access node is: login.rci.cvut.cz (for older Intel nodes n01-n33) or login3.rci.cvut.cz (for newer AMD nodes a01-a16,g01-g12). So in Linux and Mac OS X run from terminal:
  
    ssh username@login.rci.cvut.cz
  
for command line access or

    ssh -X username@login.rci.cvut.cz

for X11 forwarding. MobaXterm automatically uses X11 forwarding when connecting to SSH host.

# Nextflow Installation
To install Nextflow enter this command in your terminal:

    curl -s https://get.nextflow.io | bash
    
You can install specific Nextflow version exporting NXF_VER environment variable before running the install command, e.g.:

    export NXF_VER=20.10.0
    curl -s https://get.nextflow.io | bash
    
# Running NextFlow on SLURM
After downloading NextFlow you should open nextflow.config or create it if it doesn't exit:

    vim nextflow.config
    
You should make shure that process executor is set to 'slurm':
 
    process {
      executor='slurm'
    }

Also you might want to add nextflow to  $PATH  variable to avoid typing full path to it while running commands.

# Running test example(hello.nf) in NextFlow using SLURM:
This is a simple example printing out "Hello world!" in different languages(alternatively you can type whatever text you like in the greetings.txt

First you should create greetings.txt and paste the text in it(or whatever text you'd like):
    
    Hello world!
    Hallo world!
    Ciao world!
    Salut world!
    Bongiorno world!
    Servus world!
    Gruess Gott world!
    Na was los world!
    Gruetzi world!
    Hello world!
    Come va world!
    Ca va world!
    Hi world!
    Good bye world!
    
After that run the example:
    
    nextflow run hello.nf

Alternatively you should point the directory in which you've installed NextFlow if you didn't add it to the $PATH variable:

    path/nextflow run hello.nf

If everything was done correctly you should see output like this:

    COME VA WORLD!
    GOOD BYE WORLD!
    SERVUS WORLD!
    CA VA WORLD!
    BONGIORNO WORLD!
    SALUT WORLD!
    HALLO WORLD!
    NA WAS LOS WORLD!
    HI WORLD!
    GRUESS GOTT WORLD!
    CIAO WORLD!
    HELLO WORLD!
    HELLO WORLD!
    GRUETZI WORLD!

Outputted text won't necessary duplicate the one you've entered in greetings.txt, because every line of text is submitted to SLURM as an individual job and those jobs are not synchronized, so the that's finished first will print out text first.
