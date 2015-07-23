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
  export PS1="\[\033[38;5;37m\][\A]\[\033[38;5;15m\] \[\033[38;5;160m\]\u\[\033[38;5;37m\]@\[\033[38;5;160m\]\h\[\033[38;5;15m\] \[\033[38;5;64m\]\W\[\033[38;5;136m\]\$(__git_ps1 \" (%s)\")\[\033[38;5;245m\] \\$\[\033[00m\] "
else
  #green and $ prompt
  export PS1="\[\033[38;5;37m\][\A]\[\033[38;5;15m\] \[\033[38;5;33m\]\u\[\033[38;5;37m\]@\[\033[38;5;33m\]\h\[\033[38;5;15m\] \[\033[38;5;64m\]\W\[\033[38;5;136m\]\$(__git_ps1 \" (%s)\")\[\033[38;5;245m\] \\$\[\033[00m\] "
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

# LS colours
LS_COLORS='no=00:fi=00:di=36:ln=35:pi=30;44:so=35;44:do=35;44:bd=33;44:cd=37;44:or=05;37;41:mi=05;37;41:ex=01;31:*.cmd=01;31:*.exe=01;31:*.com=01;31:*.bat=01;31:*.reg=01;31:*.app=01;31:*.txt=32:*.org=32:*.md=32:*.mkd=32:*.h=32:*.c=32:*.C=32:*.cc=32:*.cpp=32:*.cxx=32:*.objc=32:*.sh=32:*.csh=32:*.zsh=32:*.el=32:*.vim=32:*.java=32:*.pl=32:*.pm=32:*.py=32:*.rb=32:*.hs=32:*.php=32:*.htm=32:*.html=32:*.shtml=32:*.erb=32:*.haml=32:*.xml=32:*.rdf=32:*.css=32:*.sass=32:*.scss=32:*.less=32:*.js=32:*.coffee=32:*.man=32:*.0=32:*.1=32:*.2=32:*.3=32:*.4=32:*.5=32:*.6=32:*.7=32:*.8=32:*.9=32:*.l=32:*.n=32:*.p=32:*.pod=32:*.tex=32:*.go=32:*.bmp=33:*.cgm=33:*.dl=33:*.dvi=33:*.emf=33:*.eps=33:*.gif=33:*.jpeg=33:*.jpg=33:*.JPG=33:*.mng=33:*.pbm=33:*.pcx=33:*.pdf=33:*.pgm=33:*.png=33:*.PNG=33:*.ppm=33:*.pps=33:*.ppsx=33:*.ps=33:*.svg=33:*.svgz=33:*.tga=33:*.tif=33:*.tiff=33:*.xbm=33:*.xcf=33:*.xpm=33:*.xwd=33:*.xwd=33:*.yuv=33:*.aac=33:*.au=33:*.flac=33:*.m4a=33:*.mid=33:*.midi=33:*.mka=33:*.mp3=33:*.mpa=33:*.mpeg=33:*.mpg=33:*.ogg=33:*.ra=33:*.wav=33:*.anx=33:*.asf=33:*.avi=33:*.axv=33:*.flc=33:*.fli=33:*.flv=33:*.gl=33:*.m2v=33:*.m4v=33:*.mkv=33:*.mov=33:*.MOV=33:*.mp4=33:*.mp4v=33:*.mpeg=33:*.mpg=33:*.nuv=33:*.ogm=33:*.ogv=33:*.ogx=33:*.qt=33:*.rm=33:*.rmvb=33:*.swf=33:*.vob=33:*.webm=33:*.wmv=33:*.doc=31:*.docx=31:*.rtf=31:*.dot=31:*.dotx=31:*.xls=31:*.xlsx=31:*.ppt=31:*.pptx=31:*.fla=31:*.psd=31:*.7z=0;35:*.apk=0;35:*.arj=0;35:*.bin=0;35:*.bz=0;35:*.bz2=0;35:*.cab=0;35:*.deb=0;35:*.dmg=0;35:*.gem=0;35:*.gz=0;35:*.iso=0;35:*.jar=0;35:*.msi=0;35:*.rar=0;35:*.rpm=0;35:*.tar=0;35:*.tbz=0;35:*.tbz2=0;35:*.tgz=0;35:*.tx=0;35:*.war=0;35:*.xpi=0;35:*.xz=0;35:*.z=0;35:*.Z=0;35:*.zip=0;35:*.ANSI-30-black=30:*.ANSI-00;30-brblack=00;30:*.ANSI-31-red=31:*.ANSI-00;31-brred=00;31:*.ANSI-32-green=32:*.ANSI-00;32-brgreen=00;32:*.ANSI-33-yellow=33:*.ANSI-00;33-bryellow=00;33:*.ANSI-34-blue=34:*.ANSI-00;34-brblue=00;34:*.ANSI-35-magenta=35:*.ANSI-00;35-brmagenta=00;35:*.ANSI-36-cyan=36:*.ANSI-00;36-brcyan=00;36:*.ANSI-37-white=37:*.ANSI-00;37-brwhite=00;37:*.log=00;32:*~=00;32:*#=00;32:*.bak=00;36:*.BAK=00;36:*.old=00;36:*.OLD=00;36:*.org_archive=00;36:*.off=00;36:*.OFF=00;36:*.dist=00;36:*.DIST=00;36:*.orig=00;36:*.ORIG=00;36:*.swp=00;36:*.swo=00;36:*,v=00;36:*.gpg=34:*.gpg=34:*.pgp=34:*.asc=34:*.3des=34:*.aes=34:*.enc=34:*.sqlite=34:';
export LS_COLORS

