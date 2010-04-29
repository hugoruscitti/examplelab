" Syntax highlighting for snippet files (used for snipMate.vim)
" Hopefully this should make snippets a bit nicer to write!
syn match tlComment '^#.*'
syn match  tlListItem  "^\s*[☐_]\s\+" 
syn match  tlDone "^\s*[☑☒✗]\s.*"


hi link tlComment        Comment
hi link tlListItem       Identifier
hi link tlDone           Tag
