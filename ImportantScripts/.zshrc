# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/hafeez/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
#####
# If there are any issues with the font, make sure that you have selected Meslo font chosen in shell preferences
#####
ZSH_THEME="agnoster"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Advanced Tab completion
autoload -U compinit
compinit


# Advanced directory navigation: Does not required cd
# http://zsh.sourceforge.net/Doc/Release/Options.html#Changing-Directories
# Use the shorthand ~/Downloads for cd ~/Downloads.
setopt auto_cd
# Keep a directory stack of all the directories you cd to in a session.
setopt auto_pushd
unsetopt pushd_ignore_dups
# Use Git-like -N instead of the default +N (e.g. cd -2 as opposed to cd +2).
setopt pushdminus # Completion

# Completion options
# http://zsh.sourceforge.net/Doc/Release/Options.html#Completion
# HISTSIZE: Number of commands to save
HISTSIZE=50000

# SaveHist: History is trimmed when its length exceeds by 20%
SAVEHIST=10000

# Extended_History: Timestamp the history and more
setopt extended_history

# HIST_EXPIRE_DUPS_FIRST: Trim duplicated commands from the history before tirmming unique
setopt hist_expire_dups_first

# HIST_IGNORE_DUPS: If you run same command two times, only add it to history once
setopt hist_ignore_dups

# HIST_IGNORE_SPACE: Prefix 
setopt hist_ignore_space

# INC_APPEND_HISTORY: Add commands to the history as soon as they run 
setopt inc_append_history

# SHARE_HISTORY: Timestamp the history, and more
setopt share_history # Changing directories


# TAB⇥ to show a menu of all completion suggestions. TAB⇥ a second time to enter the menu. TAB⇥ again to circulate through the list, or use the arrow keys. ENTER to accept a completion from the menu.
setopt auto_menu

# Move the cursor to the end of the word after accepting a completion
setopt always_to_end

# Disable the use of ⌃S to stop terminal output and the use of ⌃Q to resume it.
setopt complete_in_word
unsetopt flow_control

# If set, this option prevents the completion menu from showing even if AUTO_MENU is set.
unsetopt menu_complete
zstyle ':completion:*:*:*:*:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z-_}={A-Za-z_-}' 'r:|=*' 'l:|=* r:|=*'
zstyle ':completion::complete:*' use-cache 1
zstyle ':completion::complete:*' cache-path $ZSH_CACHE_DIR
zstyle ':completion:*' list-colors ''
zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#) ([0-9a-z-]#)*=01;34=0=01' # Other
# Adds support for command substitution.
# http://zsh.sourceforge.net/Doc/Release/Options.html#Prompting
setopt prompt_subst

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  docker
  npm
  zsh-syntax-highlighting
  zsh-autosuggestions
  web-search
  zsh-history-substring-search
  zsh-completions
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh`="mate ~/.oh-my-zsh"
alias activate='source venv/bin/activate'
alias ls='ls --color=tty'
alias grep='grep --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn}'
