-- General Neovim options

-- Highlight search results
vim.o.hlsearch = true

-- Line numbers
vim.wo.number = true
vim.wo.relativenumber = true

-- Mouse support
vim.o.mouse = 'a'

-- Clipboard sync with system
vim.o.clipboard = 'unnamedplus'

-- Indent & tabs
vim.o.breakindent = true
vim.o.tabstop = 4
vim.o.softtabstop = 4
vim.o.shiftwidth = 4
vim.o.expandtab = true

-- Undo history
vim.o.undofile = true

-- Case insensitive search (smart when using capitals)
vim.o.ignorecase = true
vim.o.smartcase = true

-- Always show signcolumn
vim.wo.signcolumn = 'yes'

-- Responsiveness
vim.o.updatetime = 250
vim.o.timeoutlen = 300

-- Completion menu behavior
vim.o.completeopt = 'menuone,noselect'

-- True color
vim.o.termguicolors = true

-- Filetype tweaks
vim.filetype.add({
  extension = {
    pl = 'prolog',
  },
})
