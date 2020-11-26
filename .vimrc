call plug#begin()
Plug 'nanotech/jellybeans.vim'
Plug 'scrooloose/nerdtree'
Plug 'vim-airline/vim-airline' " vim status bar
Plug 'vim-airline/vim-airline-themes'
Plug 'blueyed/vim-diminactive'
"Plug 'scrooloose/syntastic'
Plug 'klange/nyancat'
call plug#end()

set term=screen-256color

" for vim-airline

let g:airline#extensions#tabline#enabled = 1 " turn on buffer list
let g:airline_theme='hybrid'
set laststatus=2 " turn on bottom bar
let mapleader = ","
nnoremap <leader>q :bp<CR>
nnoremap <leader>w :bn<CR>

" for blueyed/vim-diminactive

let g:diminactive_enable_focus = 1
syntax enable
filetype indent on
highlight Comment term=bold cterm=bold ctermfg=4

if !filereadable(expand("%:p:h")."/Makefile")
	setlocal makeprg=gcc\ -o\ %<\ %\ -lm
endif

"map <C-c> :w<CR> :make!<CR> :cw<CR>
"map <C-x> :!./%:r<CR>
map <C-p> :w<CR>: !python3 %<CR>

set number
set ts=4
set sw=4
set sts=4
set cindent
set smartindent


colorscheme jellybeans
