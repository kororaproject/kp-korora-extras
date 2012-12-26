#Turn off annoying blinking
setterm -blength 0

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
alias vi='vim'
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'

#Set terminal colours
if [ ${EUID} -eq 0 ] ; then
	#red and # prompt
  export PS1="\[\033[0;34m\][\$(date +%H:%M)] \[\033[0;31m\]\u\[\033[0;36m\]@\[\033[0;31m\]\h\[\033[0;34m\] \W\[\033[0;32m\]\$(parse-git-branch.sh) \[\033[0;34m\]#\[\033[00m\] "
else
	#green and $ prompt
  export PS1="\[\033[0;34m\][\$(date +%H:%M)] \[\033[0;32m\]\u\[\033[0;36m\]@\[\033[0;32m\]\h\[\033[0;34m\] \W\[\033[0;32m\]\$(parse-git-branch.sh) \[\033[0;34m\]$\[\033[00m\] "
fi
