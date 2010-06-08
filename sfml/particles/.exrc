if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
imap <S-Tab> 
inoremap <C-Tab> 	
imap <F7> <F7>
imap <F4> <F4>
imap <F3> <F3>
imap <F2> <F2>
map d :call RopeShowDoc()
map f :call RopeFindOccurrences()
map g :call RopeGotoDefinition()
map ru :call RopeUseFunction()
map rad :call RopeShowDoc()
map rac :call RopeShowCalltip()
map rx :call RopeRestructure()
map r1r :call RopeRenameCurrentModule()
map rr :call RopeRename()
map ro :call RopeOrganizeImports()
map r1v :call RopeMoveCurrentModule()
map rv :call RopeMove()
map r1p :call RopeModuleToPackage()
map ra? :call RopeLuckyAssist()
map raj :call RopeJumpToGlobal()
map rf :call RopeIntroduceFactory()
map ri :call RopeInline()
map rag :call RopeGotoDefinition()
map rnv :call RopeGenerateVariable()
map rnp :call RopeGeneratePackage()
map rnm :call RopeGenerateModule()
map rnf :call RopeGenerateFunction()
map rnc :call RopeGenerateClass()
map raf :call RopeFindOccurrences()
map rai :call RopeFindImplementations()
map rl :call RopeExtractVariable()
map rm :call RopeExtractMethod()
map ra/ :call RopeCodeAssist()
map rs :call RopeChangeSignature()
map pu :call RopeUndo()
map pr :call RopeRedo()
map pc :call RopeProjectConfig()
map po :call RopeOpenProject()
map p4f :call RopeFindFileOtherWindow()
map pf :call RopeFindFile()
map pnp :call RopeCreatePackage()
map pnm :call RopeCreateModule()
map pnf :call RopeCreateFile()
map pnd :call RopeCreateDirectory()
map pk :call RopeCloseProject()
map ,,rs :r !cat % | grep =====
map ,,c 0I<code><Down></code>
map ,,1 0I====== A ======j
map ,,2 0I===== A =====j
map ,,3 0I==== A ====j
map ,,4 0I=== A ===j
map ,,d {o/*}i*/
imap ¿ =RopeLuckyAssistInsertMode()
imap ¯ =RopeCodeAssistInsertMode()
nmap gx <Plug>NetrwBrowseX
map <F2> :w:make
map <F3> :w:make; ./test
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
map <F12> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .
map <F9> :e $HOME/.vimrc
map <F7> :vimgrep <cword> *.c 
map <F6> :cnext 
map <F5> :cprevious 
inoremap <silent> o =VST_Ornaments()
imap 	 
inoremap <expr>  omni#cpp#maycomplete#Complete()
imap  =CtrlXPP()
inoremap <expr> . omni#cpp#maycomplete#Dot()
inoremap <expr> : omni#cpp#maycomplete#Scope()
inoremap <expr> > omni#cpp#maycomplete#Arrow()
map ¿ :call RopeLuckyAssist()
map ¯ :call RopeCodeAssist()
imap ^- kyyp :s/./-/go
imap ^= kyyp :s/./=/go
imap ^_ kyyp :s/./_/go
let &cpo=s:cpo_save
unlet s:cpo_save
set paste
set background=dark
set backspace=indent,eol,start
set completeopt=preview,menuone
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=es
set incsearch
set mouse=a
set omnifunc=omni#cpp#complete#Main
set printoptions=paper:a4
set runtimepath=~/.vim,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim72,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/after
set shiftwidth=4
set smarttab
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set wildmenu
" vim: set ft=vim :
