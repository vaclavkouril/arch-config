-- Luasnip configuration & loading of custom snippets

local ok, ls = pcall(require, 'luasnip')
if not ok then
  return
end

-- VSCode-style snippets (friendly-snippets, etc.)
require('luasnip.loaders.from_vscode').lazy_load()

-- Lua snippets from ~/.config/nvim/snippets/*.lua
local snippets_path = vim.fn.stdpath('config') .. '/snippets'
require('luasnip.loaders.from_lua').load({ paths = snippets_path })

ls.config.set_config({
  history = true,
  updateevents = 'TextChanged,TextChangedI',
  enable_autosnippets = true,
})
