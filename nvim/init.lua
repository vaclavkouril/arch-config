-- Leader keys
vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

-- Bootstrap lazy.nvim
local lazypath = vim.fn.stdpath('data') .. '/lazy/lazy.nvim'
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    'git',
    'clone',
    '--filter=blob:none',
    'https://github.com/folke/lazy.nvim.git',
    '--branch=stable',
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- Core settings (options, keymaps, autocmds)
require('config.options')
require('config.keymaps')
require('config.autocmds')

-- Setup plugins from lua/plugins/*
require('lazy').setup('plugins', {
  change_detection = { notify = false },
})

-- Language specific tweaks
require('lang.prolog')
require('lang.haskell')
require('lang.latex')

-- Luasnip & custom snippets (after plugins)
require('config.snippets')

-- vim: ts=2 sts=2 sw=2 et
