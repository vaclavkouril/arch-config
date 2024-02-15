#
# ~/.bashrc
#
eval "$(ssh-agent -s)"
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ll='ls --color=auto -l'
alias l.='ls .*'

# Git aliasses
alias g='git'
alias gs='g status'
alias ga='g add'
alias gc='g commit -m'
alias gl='g pull'
alias gp='g push'
alias gb='g branch'
alias gg='g log --all --decorate --oneline --graph'

prompt_git () {
        branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"

        if [[ -z $branch ]]; then 
                return 
        else
              printf "(%s) " "$branch"
        fi

}

prompt_exit () {
        local ec=$?
        [ "$ec" -ne 0 ] && printf "%d " "$ec" 
}
PS1=' $( prompt_exit ) \n\[\033[01;32m\]$( date )\[\033[0m\]\n\[\033[01;34m\]\u\[\033[0m\] $( prompt_git )\[\033[01;35m\]\w\[\033[0m\]$ '
