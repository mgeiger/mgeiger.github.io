Title: Interesting Linux Command Line Tricks
Date: 2020-06-05 14:55
Category: Linux
Tags: programming, linux, bash
Summary: A collection of tools, tips, and tricks that I use in my daily live working the command line

## Shortcuts

Go to the beginning of a line:
`ctrl-a`
Search for your prior commands:
`ctrl-r`

## Aliases

Quick `history` information:

`alias h='history'`
`alias hg='history | grep --color=auto'`

Keep an eye on your local network:

`alias LAN='nmap -sn 192.168.1.* | grep report'`

Monitor your system logs:

`alias LOG='tail -f /var/log/*log /var/log/*/*log'`

## History

Add to your `~/.bashrc` `HISTFILESIZE=` some number to increase that


## Prior Commands

If you forget to run a command with `sudo`, just type `sudo !!` and you will rerun that prior command with `sudo`.

You can also do this with a quick alias:

`alias please='sudo $(history -p \!\!)'`


## Web Server

If you have python3 installed on your system, you can quickly make a simple webserver that you can access via http.

`python3 -m http.server`

It gets servered to http://localhost:8000, so keep that in mind.

## SSH Configuration

Edit the `~/.ssh/config` to save information about some of the hosts that you typically connect to.

```
Host tasker
   HostName someserver.example.com
   Port 7000
   UserName admin
```

Then you can just ssh into that machine with `ssh tasker`, instead of `ssh admin@someserver.example.com -p 7000`. 

You can repeat with all your hosts that you can connect to.

## Creating Files

To create a few files with the same/similar names, you can use the following:

```
touch output{0,1,2,}.txt
```

This will create the following files
* output0.txt
* output1.txt
* output2.txt
* output.txt

The last one is because I left the trailing `,` in the curly braces.

### Creating a backup file

This one is very similar to above.
If you have a file that you just want to put a `.bak` extention on:

```
cp file.txt{,.bak}
```

This will keep the original `file.txt` and create a quick backup as `file.txt.bak`.
