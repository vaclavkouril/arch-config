local ls = require('luasnip')
local s = ls.snippet
local t = ls.text_node
local i = ls.insert_node

ls.add_snippets('haskell', {
  s('module', {
    t('module '), i(1, 'Main'), t({' where', '', ''}),
    t('main :: IO ()'), t({'', 'main = do', '    '}), i(0, 'putStrLn "Hello, world!"')
  }),
})
