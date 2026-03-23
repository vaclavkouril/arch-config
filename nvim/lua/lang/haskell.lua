-- Haskell language configuration
-- Plugin: mrcjkb/haskell-tools.nvim handles most setup

local ok, ht = pcall(require, 'haskell-tools')
if not ok then
  return
end

-- Example: simple keymap for Haskell repl
vim.keymap.set('n', '<leader>hr', ht.repl.toggle, { desc = 'Haskell REPL' })
