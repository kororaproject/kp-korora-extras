# Source for git information in prompt
if [ -f /usr/share/doc/git/contrib/completion/git-prompt.sh ]; then
  source /usr/share/doc/git/contrib/completion/git-prompt.sh
else
  __git_ps1
  {
    : # Git is not installed so stub out function
  }
fi

#Turn off annoying blinking if interactive
tty -s && [ $TERM != "xterm" ] && setterm --blength 0 2>/dev/null

#Set aliases
alias cp='cp -i'
alias grep='grep --color=auto'
alias grpe='grep --color=auto'
alias l.='ls -d .* --color=auto'
alias ll='ls -l --color=auto'
alias ls='ls --color=auto'
alias la='ls -a --color=auto'
alias lla='ls -la --color=auto'
alias mv='mv -i'
alias rm='rm -i'
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'

#Set terminal colours
if [ ${EUID} -eq 0 ] ; then
  #red and # prompt
  export PS1="\[\033[38;5;37m\][\A]\[\033[38;5;15m\] \[\033[38;5;160m\]\u\[\033[38;5;37m\]@\[\033[38;5;160m\]\h\[\033[38;5;15m\] \[\033[38;5;64m\]\W\[\033[38;5;136m\]\$(__git_ps1 \" (%s)\")\[\033[38;5;245m\] \\$\[\033[38;5;245m\] "
else
  #green and $ prompt
  export PS1="\[\033[38;5;37m\][\A]\[\033[38;5;15m\] \[\033[38;5;33m\]\u\[\033[38;5;37m\]@\[\033[38;5;33m\]\h\[\033[38;5;15m\] \[\033[38;5;64m\]\W\[\033[38;5;136m\]\$(__git_ps1 \" (%s)\")\[\033[38;5;245m\] \\$\[\033[38;5;245m\] "
fi

HAVE_LESS=$(command -v less)
if [ -n "$HAVE_LESS" -a -z "${MANPAGER}" ] ; then
  man() {
      env LESS_TERMCAP_mb=$(printf "\e[1;31m") \
      LESS_TERMCAP_md=$(printf "\e[38;5;33m") \
      LESS_TERMCAP_me=$(printf "\e[0m") \
      LESS_TERMCAP_se=$(printf "\e[0m") \
      LESS_TERMCAP_so=$(printf "\e[1;44;33m") \
      LESS_TERMCAP_ue=$(printf "\e[0m") \
      LESS_TERMCAP_us=$(printf "\e[38;5;136;4m") \
      GROFF_NO_SGR=yes \
      man "$@"
  }
fi
