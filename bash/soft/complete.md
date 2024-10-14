# Completion for alias

## Installation

    mkdir ~/.bash_completion.d
    curl https://raw.githubusercontent.com/cykerway/complete-alias/master/complete_alias ~/.bash_completion.d/complete_alias

## Application

    source ~/.bash_completion.d/complete_alias

    alias container=docker\ container
    complete -F _complete_alias container
    container can now be autocompleted by the original _docker() completion handler;

    $ container l`<Tab>`
    logs  ls

    $ container s`<Tab>`
    start  stats  stop
