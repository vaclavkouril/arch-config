local ls = require('luasnip')
local s = ls.snippet
local t = ls.text_node
local i = ls.insert_node

ls.add_snippets('c', {
  s('main', {
    t({'#include <stdio.h>', '', 'int main(int argc, char **argv) {', '    '}),
    i(0, 'return 0;'),
    t({'', '}'})
  }),
})
