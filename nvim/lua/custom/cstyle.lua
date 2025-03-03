vim.cmd([[
" Define a callback for parsing cstyle.pl output
function! s:ParseCstyle(output, bufnr) abort  
  echom "Spouštím ParseCstyle"
  let l:lines = split(a:output, "\n")
  let l:result = []
  for l:line in l:lines
    " Expect format: file: line: error message
    if l:line =~ '^.\+:\s*\d\+:\s\+.\+$'
      let l:match = matchlist(l:line, '^\(.\+\):\s*\(\d\+\):\s\+\(.*\)$')
      if !empty(l:match)
        call add(l:result, {
              \ 'lnum': str2nr(l:match[2]),
              \ 'text': l:match[3],
              \ 'type': 'E'
              \ })
      endif
    endif
  endfor
  return l:result
endfunction

" Ensure ALE uses our custom linter "cstyle" for C files
if exists('g:ale_linters')
  let g:ale_linters.c = ['cstyle']
endif

" Set the absolute path to your cstyle.pl script
let g:ale_cstyle_executable = expand('~/.config/nvim/lua/custom/cstyle.pl')
let g:ale_cstyle_options = ''

" Register the custom linter with ALE
if exists('*ale#linter#Define')
  call ale#linter#Define('c', {
        \ 'name': 'cstyle',
        \ 'executable': g:ale_cstyle_executable,
        \ 'command': g:ale_cstyle_executable . ' %s',
        \ 'callback': function('s:ParseCstyle'),
        \ 'lint_file': 1,
        \ })
endif
]])
